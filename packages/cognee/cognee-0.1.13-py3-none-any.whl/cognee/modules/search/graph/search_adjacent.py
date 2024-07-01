""" This module contains the function to find the neighbours of a given node in the graph"""


from typing import Union, Dict
import networkx as nx
from cognee.shared.data_models import GraphDBType
from cognee.infrastructure.databases.graph.config import get_graph_config

async def search_adjacent(graph: Union[nx.Graph, any], query: str, other_param: dict = None) -> Dict[str, str]:
    """
    Find the neighbours of a given node in the graph and return their descriptions.
    Supports both NetworkX graphs and Neo4j graph databases based on the configuration.

    Parameters:
    - graph (Union[nx.Graph, AsyncSession]): The graph object or Neo4j session.
    - query (str): Unused in this implementation but could be used for future enhancements.
    - other_param (dict, optional): A dictionary that may contain 'node_id' to specify the node.

    Returns:
    - Dict[str, str]: A dictionary containing the unique identifiers and descriptions of the neighbours of the given node.
    """
    node_id = other_param.get('node_id') if other_param else query

    if node_id is None:
        return {}

    graph_config = get_graph_config()

    if graph_config.graph_database_provider == "NETWORKX":
        if node_id not in graph:
            return {}

        neighbors = list(graph.neighbors(node_id))
        neighbor_descriptions = {neighbor: graph.nodes[neighbor].get('description') for neighbor in neighbors}
        return neighbor_descriptions

    elif graph_config.graph_database_provider  == "neo4j":
        cypher_query = """
        MATCH (node {id: $node_id})-[:CONNECTED_TO]->(neighbor)
        RETURN neighbor.id AS neighbor_id, neighbor.description AS description
        """
        results = await graph.run(cypher_query, node_id=node_id)
        neighbor_descriptions = {record["neighbor_id"]: record["description"] for record in await results.list() if "description" in record}
        return neighbor_descriptions

    else:
        raise ValueError("Unsupported graph engine type in the configuration.")