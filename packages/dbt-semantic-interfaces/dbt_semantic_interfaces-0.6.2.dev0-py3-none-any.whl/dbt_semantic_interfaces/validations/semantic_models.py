import logging
from typing import Generic, List, Sequence

from dbt_semantic_interfaces.protocols import SemanticManifestT, SemanticModel
from dbt_semantic_interfaces.references import SemanticModelReference
from dbt_semantic_interfaces.type_enums import EntityType
from dbt_semantic_interfaces.validations.validator_helpers import (
    FileContext,
    SemanticManifestValidationRule,
    SemanticModelContext,
    SemanticModelValidationHelpers,
    ValidationError,
    ValidationIssue,
    validate_safely,
)

logger = logging.getLogger(__name__)


class SemanticModelValidityWindowRule(SemanticManifestValidationRule[SemanticManifestT], Generic[SemanticManifestT]):
    """Checks validity windows in semantic models to ensure they comply with runtime requirements."""

    @staticmethod
    @validate_safely(whats_being_done="checking correctness of the time dimension validity parameters in the model")
    def validate_manifest(semantic_manifest: SemanticManifestT) -> Sequence[ValidationIssue]:
        """Checks the validity param definitions in every semantic model in the model."""
        issues: List[ValidationIssue] = []

        for semantic_model in semantic_manifest.semantic_models:
            issues.extend(SemanticModelValidityWindowRule._validate_semantic_model(semantic_model=semantic_model))

        return issues

    @staticmethod
    @validate_safely(
        whats_being_done="checking the semantic model's validity parameters for compatibility with "
        "runtime requirements"
    )
    def _validate_semantic_model(semantic_model: SemanticModel) -> List[ValidationIssue]:
        """Runs assertions on semantic models with validity parameters set on one or more time dimensions."""
        issues: List[ValidationIssue] = []

        validity_param_dims = [dim for dim in semantic_model.dimensions if dim.validity_params is not None]

        if not validity_param_dims:
            return issues

        context = SemanticModelContext(
            file_context=FileContext.from_metadata(metadata=semantic_model.metadata),
            semantic_model=SemanticModelReference(semantic_model_name=semantic_model.name),
        )
        requirements = (
            "Semantic models using dimension validity params to define a validity window must have exactly two time "
            "dimensions with validity params specified - one marked `is_start` and the other marked `is_end`."
        )
        validity_param_dimension_names = [dim.name for dim in validity_param_dims]
        start_dim_names = [
            dim.name for dim in validity_param_dims if dim.validity_params and dim.validity_params.is_start
        ]
        end_dim_names = [dim.name for dim in validity_param_dims if dim.validity_params and dim.validity_params.is_end]
        num_start_dims = len(start_dim_names)
        num_end_dims = len(end_dim_names)

        if len(validity_param_dims) == 1 and num_start_dims == 1 and num_end_dims == 1:
            # Defining a single point window, such as one might find in a daily snapshot table keyed on date,
            # is not currently supported.
            error = ValidationError(
                context=context,
                message=(
                    f"Semantic model {semantic_model.name} has a single validity param dimension that defines its "
                    f"window: `{validity_param_dimension_names[0]}`. This is not a currently supported configuration! "
                    f"{requirements} If you have one column defining a window, as in a daily snapshot table, you can "
                    f"define a separate dimension and increment the time value in the `expr` field as a work-around."
                ),
            )
            issues.append(error)
        elif len(validity_param_dims) != 2:
            error = ValidationError(
                context=context,
                message=(
                    f"Semantic model {semantic_model.name} has {len(validity_param_dims)} dimensions defined with "
                    f"validity params. They are: {validity_param_dimension_names}. There must be either zero or two! "
                    f"If you wish to define a validity window for this semantic model, please follow these "
                    f"requirements: {requirements}"
                ),
            )
            issues.append(error)
        elif num_start_dims != 1 or num_end_dims != 1:
            # Validity windows must define both a start and an end, and there should be exactly one
            start_dim_names = []
            error = ValidationError(
                context=context,
                message=(
                    f"Semantic model {semantic_model.name} has two validity param dimensions defined, but does not "
                    f"have exactly one each marked with is_start and is_end! Dimensions: "
                    f"{validity_param_dimension_names}. is_start dimensions: {start_dim_names}. is_end dimensions: "
                    f"{end_dim_names}. {requirements}"
                ),
            )
            issues.append(error)

        primary_or_unique_entities = [
            entity for entity in semantic_model.entities if entity.type in (EntityType.PRIMARY, EntityType.UNIQUE)
        ]
        if not any([entity.type is EntityType.NATURAL for entity in semantic_model.entities]):
            error = ValidationError(
                context=context,
                message=(
                    f"Semantic model {semantic_model.name} has validity param dimensions defined, but does not have "
                    f"an entity with type `natural` set. The natural key for this semantic model is what we use to "
                    f"process a validity window join. Primary or unique entities, if any, might be suitable for "
                    f"use as natural keys: ({[entity.name for entity in primary_or_unique_entities]})."
                ),
            )
            issues.append(error)

        if primary_or_unique_entities:
            error = ValidationError(
                context=context,
                message=(
                    f"Semantic model {semantic_model.name} has validity param dimensions defined and also has one or "
                    f"more entities designated as `primary` or `unique`. This is not yet supported, as we do not "
                    f"currently process joins against these key types for semantic models with validity windows "
                    f"specified."
                ),
            )
            issues.append(error)

        if semantic_model.measures:
            # Temporarily block measure definitions in semantic models with validity windows set
            measure_names = [measure.name for measure in semantic_model.measures]
            error = ValidationError(
                context=context,
                message=(
                    f"Semantic model {semantic_model.name} has both measures and validity param dimensions defined. "
                    f"This is not currently supported! Please remove either the measures or the validity params. "
                    f"Measure names: {measure_names}. Validity param dimension names: "
                    f"{validity_param_dimension_names}."
                ),
            )
            issues.append(error)

        return issues


class SemanticModelDefaultsRule(SemanticManifestValidationRule[SemanticManifestT], Generic[SemanticManifestT]):
    """Checks defaults in semantic models."""

    @staticmethod
    @validate_safely(whats_being_done="running model validation ensuring the defaults are valid")
    def validate_manifest(semantic_manifest: SemanticManifestT) -> Sequence[ValidationIssue]:  # noqa: D
        issues: List[ValidationIssue] = []

        for semantic_model in semantic_manifest.semantic_models:
            issues.extend(SemanticModelDefaultsRule._validate_default_agg_time_dimension(semantic_model=semantic_model))
        return issues

    @staticmethod
    @validate_safely(whats_being_done="checking validity of the semantic model's default agg_time_dimension")
    def _validate_default_agg_time_dimension(semantic_model: SemanticModel) -> List[ValidationIssue]:
        issues: List[ValidationIssue] = []

        if semantic_model.defaults is None or semantic_model.defaults.agg_time_dimension is None:
            return []

        default_agg_time_dimension = semantic_model.defaults.agg_time_dimension

        if not SemanticModelValidationHelpers.time_dimension_in_model(
            time_dimension_name=default_agg_time_dimension, semantic_model=semantic_model
        ):
            issues.append(
                ValidationError(
                    context=SemanticModelContext(
                        file_context=FileContext.from_metadata(metadata=semantic_model.metadata),
                        semantic_model=SemanticModelReference(semantic_model_name=semantic_model.name),
                    ),
                    message=f"Default aggregation time dimension was specified as '{default_agg_time_dimension}' which "
                    f"doesn't exist as a time dimension in semantic model named '{semantic_model.name}'.",
                )
            )

        return issues
