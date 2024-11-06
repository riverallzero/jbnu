from tqdm import tqdm

# https://github.com/yuhc/web-dataset/blob/master/web-Google/web-Google.txt
filepath = '/Users/dayoung/Code/jbnu/data-mining/A2/web-Google.txt'

"""
graph[Dict]
- key: 'from_node'
- value: 'from_node'에서 연결된 모든 'to_node'
"""
graph = {}
with open(filepath, 'r') as lines:
    for line in tqdm(lines.readlines()[4:]):
        from_node, to_node = map(int, line.strip().split())

        if from_node not in graph:
            graph[from_node] = []
        graph[from_node].append(to_node)

# graph dictionary의 key를 오름차순으로 정렬
nodes = sorted(graph.keys() | {to_node for neighbors in graph.values() for to_node in neighbors})
node_idx = {node: idx for idx, node in enumerate(nodes)}
n = len(nodes)

"""
D^(-1): out degree의 역수 matrix
"""
D_inverse_matrix = [[0] * n for _ in range(n)]

for from_node, neighbors in graph.items():
    i = node_idx[from_node]

    if len(neighbors) == 0:
        D_inverse_matrix[i][i] = 0
    else:
        D_inverse_matrix[i][i] = 1/len(neighbors)

print('=> [done] calculation: D Matrix')

"""
A: adjacency matrix
"""
A_matrix = [[0] * n for _ in range(n)]

for from_node, neighbors in graph.items():
    for to_node in neighbors:
        i = node_idx[from_node]
        j = node_idx[to_node]
        A_matrix[i][j] = 1
        
print('=> [done] calculation: A Matrix')

"""
Ã: D^(-1) * A
"""
A_tilde_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        A_tilde_matrix[i][j] = sum(D_inverse_matrix[i][k] * A_matrix[k][j] for k in range(n))

print('=> [done] calculation: Ã Matrix')

"""
B̃: Ã를 column stochastic하게 수정한 matrix 
- column 값의 합이 1이 아닌 경우, 1/n으로 값을 채워넣음
"""
for j in range(n):  
    col_sum = sum(A_tilde_matrix[j][i] for i in range(n))
    if col_sum != 1: 
        for i in range(n):
            A_tilde_matrix[j][i] = 1 / n

B_tilde_matrix = A_tilde_matrix

beta = 0.85

B_tilde_transpose_matrix = [[B_tilde_matrix[j][i] for j in range(len(B_tilde_matrix))] for i in range(len(B_tilde_matrix[0]))]

print('=> [done] calculation: B̃ Matrix')

"""
G: beta * B̃^T + (1-beta)[1/n]_(nxn)
"""
G_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        G_matrix[i][j] = beta * B_tilde_transpose_matrix[i][j] + (1-beta)/n

print('=> [done] calculation: G Matrix')

"""
Power Iteration
"""
for t in tqdm(range(50)):
    if t == 0:
        r_t = [1/n for _ in range(n)]
    else:
        r_t = [0 for _ in range(n)]

        for i in range(n):
            r_t[i] = sum(G_matrix[i][k] * r_t[k] for k in range(n))

with open('202110065_output.txt', 'w') as f:
    for i in range(n):
        f.write(f'{nodes[i]}\t{r_t[i]}')
f.close()