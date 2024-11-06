from tqdm import tqdm

class PageRank():
    def __init__(self, filepath):
        self.filepath = filepath
        self.graph = {}
        self.nodes = []
        self.node_idx = {}
        self.n = 0
        self.D_inverse_matrix = []
        self.A_matrix = []
        self.A_tilde_matrix = []
        self.B_tilde_matrix = []
        self.B_tilde_transpose_matrix = []
        self.G_matrix = []
        self.beta = 0.85
        self.c = 50

        """
        graph: dict
            - 'from_node'를 key로, 'from_node'에서부터 출발하는 모든 'to_node'를 value로 설정
        node: list
            - graph에서 key를 기준으로 정렬한 node
        node_idx: dict
            - node를 key로, graph에서 node의 index를 value로 설정
        D_inverse_matrix: list
            - D^(-1): out degree의 역수 matrix
        A_matrix: list
            - A: adjacency matrix
        A_tilde_matrix: list
            - Ã: D^(-1) * A
        B_tilde_matrix: list
            - B̃: Ã를 column stochastic하게 수정한 matrix 
            - column 값의 합이 1이 아닌 경우, 1/n으로 값을 채워넣음
        G_matrix: list
            - G: beta * B̃^T + (1-beta)[1/n]_(nxn)
        beta: float
            - 0.8 ~ 0.9 사이값
            - 0.85로 흔히 사용
        c: int
            - convergence threshold
        """

    def build_graph(self):
        with open(self.filepath, 'r') as lines:
            for line in tqdm(lines.readlines()[4:]):
                from_node, to_node = map(int, line.strip().split())

                if from_node not in self.graph:
                    self.graph[from_node] = []
                self.graph[from_node].append(to_node)

        self.nodes = sorted(self.graph.keys() | {to_node for neighbors in self.graph.values() for to_node in neighbors})
        self.node_idx = {node: idx for idx, node in enumerate(self.nodes)}
        self.n = len(self.nodes)

    def calculate_matrices(self):
        self.calculate_D_inverse_matrix()
        self.calculate_A_matrix()
        self.calculate_A_tilde_matrix()
        self.calculate_B_tilde_matrix()
        self.calculate_G_matrix()

    def calculate_D_inverse_matrix(self):
        self.D_inverse_matrix = [[0] * self.n for _ in range(self.n)]

        for from_node, neighbors in self.graph.items():
            i = self.node_idx[from_node]

            if len(neighbors) == 0:
                self.D_inverse_matrix[i][i] = 0
            else:
                self.D_inverse_matrix[i][i] = 1/len(neighbors)

        print('=> [done] calculation: D Matrix')

    def calculate_A_matrix(self):
        self.A_matrix = [[0] * self.n for _ in range(self.n)]

        for from_node, neighbors in self.graph.items():
            for to_node in neighbors:
                i = self.node_idx[from_node]
                j = self.node_idx[to_node]
                self.A_matrix[i][j] = 1

        print('=> [done] calculation: A Matrix')

    def calculate_A_tilde_matrix(self):
        self.A_tilde_matrix = [[0] * self.n for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.n):
                self.A_tilde_matrix[i][j] = sum(self.D_inverse_matrix[i][k] * self.A_matrix[k][j] for k in range(self.n))

        print('=> [done] calculation: Ã Matrix')

    def calculate_B_tilde_matrix(self):
        self.B_tilde_matrix = self.A_tilde_matrix.copy()

        for j in range(self.n):  
            col_sum = sum(self.B_tilde_matrix[j][i] for i in range(self.n))
            if col_sum != 1: 
                for i in range(self.n):
                    self.B_tilde_matrix[j][i] = 1 / self.n

        self.B_tilde_transpose_matrix = [[self.B_tilde_matrix[j][i] for j in range(len(self.B_tilde_matrix))] for i in range(len(self.B_tilde_matrix[0]))]

        print('=> [done] calculation: B̃ Matrix')

    def calculate_G_matrix(self):
        self.G_matrix = [[0] * self.n for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.n):
                self.G_matrix[i][j] = self.beta * self.B_tilde_transpose_matrix[i][j] + (1-self.beta)/self.n

        print('=> [done] calculation: G Matrix')

    def run_power_iteration(self):
        for t in tqdm(range(self.c)):
            if t == 0:
                self.r_t = [1/self.n for _ in range(self.n)]
            else:
                self.r_t = [0 for _ in range(self.n)]

                for i in range(self.n):
                    self.r_t[i] = sum(self.G_matrix[i][k] * self.r_t[k] for k in range(self.n))

    def save_results(self, output_file):
        with open(output_file, 'w') as f:
            sorted_nodes = sorted(zip(self.nodes, self.r_t), key=lambda x: x[1], reverse=True)
            for node, score in sorted_nodes:
                f.write(f'{node}\t{score}\n')
        f.close()

if __name__ == '__main__':
    # https://github.com/yuhc/web-dataset/blob/master/web-Google/web-Google.txt
    filepath = '/Users/dayoung/Code/jbnu/data-mining/A2/web-Google.txt'
    output_file = '202110065_output.txt'

    pagerank = PageRank(filepath)
    pagerank.build_graph()
    pagerank.calculate_matrices()
    pagerank.run_power_iteration()
    pagerank.save_results(output_file)
