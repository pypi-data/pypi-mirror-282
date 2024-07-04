import networkx as nx
import igraph as ig


class GraphPipeline:
    def __init__(self):
        self.ig_graph = None
        self.G = None

    def create_network_igraph(self, df, source: str, target: str, edge_attr: list):
        """Create network from dataframe"""
        self.G = nx.from_pandas_edgelist(
            df,
            source,
            target,
            edge_attr
        )
        self.ig_graph = ig.Graph.from_networkx(self.G)
        print(
            f"Vertix: {self.ig_graph.vertex_attributes()}"
            f"Edges: {self.ig_graph.edge_attributes()}"
        )
        return self.ig_graph

    def create_graph_from_similarity_matrix(self, similarity_matrix, threshold: int = 0.5):
        """
        Create network from similarity matrix
        cosine_similarity_matrix = np.array([
            [1.0, 0.8, 0.2],
            [0.8, 1.0, 0.5],
            [0.2, 0.5, 1.0]
        ])
        """
        self.G = nx.Graph()
        num_nodes = similarity_matrix.shape[0]

        # Add nodes
        for i in range(num_nodes):
            self.G.add_node(i)

        # Add edges based on the similarity threshold
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if similarity_matrix[i, j] >= threshold:
                    self.G.add_edge(i, j, weight=similarity_matrix[i, j])

        return self.G

    def plot(
            self,
            visual_style: dict = None,
            file_name: str = 'graph_plot.png',
    ):
        layout = self.ig_graph.layout("kk")  # Kamada-Kawai layout

        if not visual_style:
            visual_style = {
                'layout': layout,
                'bbox': (2000, 1000),
                'margin': 20
            }
        ig.plot(self.ig_graph, file_name, **visual_style)
