from tqdm import tqdm
from collections import defaultdict


class PageRank():
    def __init__(self, filepath):
        self.filepath = filepath
        self.graph = {}
        self.nodes = []
        self.node_idx = {}
        self.n = 0
        self.adjacency_matrix = defaultdict(float)  # Sparse adjacency matrix
        self.G_sparse = defaultdict(float)  # Final Google matrix
        self.beta = 0.85
        self.c = 50
        self.epsilon = 1e-6
        self.dangling_nodes = set()
        self.out_degrees = defaultdict(int)  # Track out-degrees for each node

    def build_graph(self):
        """Build graph, calculate out-degrees and identify dangling nodes"""
        with open(self.filepath, 'r') as lines:
            for line in tqdm(lines.readlines()[4:]):
                from_node, to_node = map(int, line.strip().split())

                if from_node not in self.graph:
                    self.graph[from_node] = []
                self.graph[from_node].append(to_node)
                self.out_degrees[from_node] += 1  # Count out-degrees

        # Get all nodes and create node index mapping
        all_nodes = set(self.graph.keys()) | {to_node for neighbors in self.graph.values() for to_node in neighbors}
        self.nodes = sorted(all_nodes)
        self.node_idx = {node: idx for idx, node in enumerate(self.nodes)}
        self.n = len(self.nodes)

        # Identify dangling nodes (nodes with no outlinks)
        self.dangling_nodes = {self.node_idx[node] for node in all_nodes if node not in self.graph}
        print(f"Total nodes: {self.n}, Dangling nodes: {len(self.dangling_nodes)}")

    def build_adjacency_matrix(self):
        """Build sparse adjacency matrix"""
        for from_node, neighbors in tqdm(self.graph.items(), desc="Building adjacency matrix"):
            i = self.node_idx[from_node]
            for to_node in neighbors:
                j = self.node_idx[to_node]
                # Set 1 for each edge in adjacency matrix
                self.adjacency_matrix[(j, i)] = 1.0

    def calculate_G_matrix(self):
        """
        Calculate sparse representation of Google matrix G
        G = βM + (1-β)E, where:
        M = D^(-1)A (D is diagonal matrix of out-degrees, A is adjacency matrix)
        """
        # First multiply adjacency matrix with inverse out-degrees
        for (j, i), value in tqdm(self.adjacency_matrix.items(), desc="Calculating G matrix"):
            from_node = self.nodes[i]
            d_inv = 1.0 / self.out_degrees[from_node]
            # Multiply adjacency matrix element by d_inv and damping factor
            self.G_sparse[(j, i)] = self.beta * d_inv * value

        # Handle dangling nodes - their probability mass is distributed uniformly
        self.dangling_factor = (1 - self.beta) / self.n

    def power_iteration(self):
        """
        Run power iteration method to compute PageRank
        r^(t+1) = G * r^(t)
        """
        # Initialize rank vector uniformly
        self.r_t = [1.0 / self.n for _ in range(self.n)]

        for t in tqdm(range(self.c), desc="Power iteration"):
            r_next = [0.0] * self.n

            # Handle non-dangling nodes multiplication
            for (j, i), prob in self.G_sparse.items():
                r_next[j] += prob * self.r_t[i]

            # Handle dangling nodes
            dangling_sum = sum(self.r_t[i] for i in self.dangling_nodes)
            dangling_contrib = self.dangling_factor * dangling_sum

            # Add uniform teleportation factor and dangling nodes contribution
            uniform_factor = (1.0 - self.beta) / self.n
            for i in range(self.n):
                r_next[i] += dangling_contrib + uniform_factor

            # Normalize to ensure sum equals 1
            total = sum(r_next)
            r_next = [x / total for x in r_next]

            # Check convergence
            diff = max(abs(r_next[i] - self.r_t[i]) for i in range(self.n))
            if diff < self.epsilon:
                print(f'Converged at iteration {t + 1}')
                break

            self.r_t = r_next

    def save_results(self, output_file):
        """Save PageRank scores sorted in descending order"""
        with open(output_file, 'w') as f:
            sorted_nodes = sorted(zip(self.nodes, self.r_t), key=lambda x: (-x[1], x[0]))
            for node, score in sorted_nodes:
                f.write(f'{node}\t{score:.6f}\n')

    def run(self):
        print("Starting PageRank calculation...")
        self.build_graph()
        print('[done] graph building!')
        self.build_adjacency_matrix()
        print('[done] adjacency matrix building!')
        self.calculate_G_matrix()
        print('[done] G matrix calculation!')
        self.power_iteration()
        print('[done] power iteration!')


if __name__ == '__main__':
    filepath = './web-Google.txt'
    output_file = '202110065_output.txt'

    pagerank = PageRank(filepath)
    pagerank.run()
    pagerank.save_results(output_file)