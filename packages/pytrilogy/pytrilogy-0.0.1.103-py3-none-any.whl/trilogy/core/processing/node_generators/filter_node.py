from typing import List


from trilogy.core.enums import JoinType
from trilogy.core.models import (
    Concept,
    Environment,
)
from trilogy.core.processing.nodes import FilterNode, MergeNode, NodeJoin, History
from trilogy.core.processing.node_generators.common import (
    resolve_filter_parent_concepts,
)
from trilogy.constants import logger
from trilogy.core.processing.utility import padding
from trilogy.core.processing.node_generators.common import concept_to_relevant_joins

LOGGER_PREFIX = "[GEN_FILTER_NODE]"


def gen_filter_node(
    concept: Concept,
    local_optional: List[Concept],
    environment: Environment,
    g,
    depth: int,
    source_concepts,
    history: History | None = None,
) -> MergeNode | FilterNode | None:
    immediate_parent, parent_concepts = resolve_filter_parent_concepts(concept)

    logger.info(f"{padding(depth)}{LOGGER_PREFIX} fetching filter node parents")
    parent = source_concepts(
        mandatory_list=parent_concepts,
        environment=environment,
        g=g,
        depth=depth + 1,
        history=history,
    )
    if not parent:
        return None
    filter_node = FilterNode(
        input_concepts=[immediate_parent] + parent_concepts,
        output_concepts=[concept, immediate_parent] + parent_concepts,
        environment=environment,
        g=g,
        parents=[parent],
    )
    if not local_optional:
        return filter_node
    enrich_node = source_concepts(  # this fetches the parent + join keys
        # to then connect to the rest of the query
        mandatory_list=[immediate_parent] + parent_concepts + local_optional,
        environment=environment,
        g=g,
        depth=depth + 1,
        history=history,
    )
    x = MergeNode(
        input_concepts=[concept, immediate_parent] + local_optional,
        output_concepts=[
            concept,
        ]
        + local_optional,
        environment=environment,
        g=g,
        parents=[
            # this node fetches only what we need to filter
            filter_node,
            enrich_node,
        ],
        node_joins=[
            NodeJoin(
                left_node=enrich_node,
                right_node=filter_node,
                concepts=concept_to_relevant_joins(
                    [immediate_parent] + parent_concepts
                ),
                join_type=JoinType.LEFT_OUTER,
                filter_to_mutual=False,
            )
        ],
    )
    return x
