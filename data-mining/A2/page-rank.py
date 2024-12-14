from collections import defaultdict

class PageRank():
    def __init__(self, filepath):
        self.filepath = filepath
        self.graph = {}
        self.nodes = []
        self.node_idx = {}
        self.adjacency_matrix = defaultdict(float) 
        self.G_sparse = defaultdict(float)
        self.beta = 0.85
        self.c = 50
        self.epsilon = 1e-6
        self.dangling_nodes = set()
        self.out_degrees = defaultdict(int)

        """
        graph: dict
            - 'from_node'를 key로, 'from_node'에서부터 출발하는 모든 'to_node'를 value로 설정
        nodes: list
            - graph에서 key를 기준으로 정렬한 node
        node_idx: dict
            - node를 key로, graph에서 node의 index를 value로 설정
        adjacency_matrix: dict
            - A: adjacency matrix
        G_sparse: dict
            - G: google matrix
            - beta * B̃^T + (1-beta)[1/n]_(nxn)
        beta: float
            - 0.8 ~ 0.9 사이값
            - 0.85로 흔히 사용
        c: int
            - convergence threshold
            - power iteration 반복 횟수
        epsilon: float
            - convergence threshold
            - r^{t+1}과 r^t의 차이
        """

    def build_graph(self):
        """
        데이터를 이용해 graph를 만들어 out degree를 계산하고, dangling한 node 확인
        """
        with open(self.filepath, 'r') as lines:
            # 데이터 파일 주석 제거
            for line in lines.readlines()[4:]:
                from_node, to_node = map(int, line.strip().split())

                # 그래프에 from_node가 없으면 빈 리스트 추가
                if from_node not in self.graph:
                    self.graph[from_node] = []
                self.graph[from_node].append(to_node)
                # D: out degree matrix
                self.out_degrees[from_node] += 1

        # 모든 노드를 가져와 node 인덱스를 설정 후 정렬
        all_nodes = set(self.graph.keys()) | {to_node for neighbors in self.graph.values() for to_node in neighbors}
        self.nodes = sorted(all_nodes)
        self.node_idx = {node: idx for idx, node in enumerate(self.nodes)}
        self.n = len(self.nodes)

        # out degree가 0인 노드를 dangling node로 설정
        self.dangling_nodes = {self.node_idx[node] for node in all_nodes if node not in self.graph}

    def calculate_G_matrix(self):
        """
        google matrix 계산(D: out degree diagonal matrix, A: adjacency matrix)
            - M = D^(-1)A
            - G = beta * M + (1-beta)[1/n]_(nxn)
        """
        # A: adjacency matrix
        for from_node, neighbors in self.graph.items():
            i = self.node_idx[from_node]
            for to_node in neighbors:
                j = self.node_idx[to_node]
                # 인접 행렬에서 각 엣지에 대해 1을 설정
                self.adjacency_matrix[(j, i)] = 1.0

        # M = D^{-1} * A
        for (j, i), value in self.adjacency_matrix.items():
            from_node = self.nodes[i]
            d_inv = 1.0 / self.out_degrees[from_node]
            # beta * M
            self.G_sparse[(j, i)] = self.beta * d_inv * value

        # (1-beta)[1/n]_(nxn): dangling한 노드의 값은 (1-beta)/n으로 설정
        self.dangling_factor = (1 - self.beta) / self.n

    def power_iteration(self):
        """
        c번 동안 수렴할 때까지 power iteration을 수행
            - |r^{t+1}-r^t|가 epsilon보다 작을때 수렴
            - r^(t+1) = G * r^(t)
        """
        # rank vector 초기화
        self.r_t = [1.0 / self.n for _ in range(self.n)]

        for t in range(self.c):
            r_next = [0.0] * self.n

            # dangling하지 않은 node에 대한 행렬곱 수행
            for (j, i), prob in self.G_sparse.items():
                r_next[j] += prob * self.r_t[i]

            # dangling한 node 처리
            dangling_sum = sum(self.r_t[i] for i in self.dangling_nodes)
            dangling_contrib = self.dangling_factor * dangling_sum

            # dangling한 node에는 (1-beta)/n을 더함
            uniform_factor = (1.0 - self.beta) / self.n
            for i in range(self.n):
                r_next[i] += dangling_contrib + uniform_factor

            # vector 정규화로 총합을 1로 맞춤
            total = sum(r_next)
            r_next = [x / total for x in r_next]

            # 다음 시점과 현재 시점의 rank vector의 차이로 수렴하는지 파악
            diff = max(abs(r_next[i] - self.r_t[i]) for i in range(self.n))
            if diff < self.epsilon:
                print(f'Converged at iteration {t + 1}')
                break

            self.r_t = r_next

    def save_results(self, output_file):
        """
        page rank 결과를 importance가 높은순으로 정렬해 .txt 파일에 저장
        """
        with open(output_file, 'w') as f:
            sorted_nodes = sorted(zip(self.nodes, self.r_t), key=lambda x: (-x[1], x[0]))
            for node, score in sorted_nodes:
                f.write(f'{node}\t{score:.6f}\n')

    def run(self):
        self.build_graph()
        print('[done] graph building!')
        self.calculate_G_matrix()
        print('[done] G matrix calculation!')
        self.power_iteration()
        print('[done] power iteration!')


if __name__ == '__main__':
    filepath = './web-Google.txt'
    output_file = './202110065_output.txt'

    pagerank = PageRank(filepath)
    pagerank.run()
    pagerank.save_results(output_file)
