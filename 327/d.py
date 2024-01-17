from collections import deque


class BipartiteGraph:
    """ 2部グラフ判定クラス

    2部グラフかどうかを判定するクラスです。
    ・つかい方
        graph = BipartiteGraph(N): インスタンス生成
        graph.add_edge(u, v): 2頂点u, v間に無向辺をはる
        graph.draw(): 2部グラフならTrue, そうでないならFalseを返す
        graph.color[v]: (draw()をした後のみ)、頂点vの色(0 or 1) を返す
    """

    def __init__(self, n: int) -> None:
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.color = [None] * n

    def add_edge(self, u: int, v: int) -> None:
        self.graph[u].append(v)
        self.graph[v].append(u)
        return None

    def draw(self) -> bool:
        for v in range(self.n):
            if self.color[v] is not None:
                continue
            self.color[v] = 0
            que = deque()
            que.append(v)
            while que:
                ov = que.popleft()
                for nv in self.graph[ov]:
                    if self.color[nv] is None:
                        self.color[nv] = self.color[ov] ^ 1
                        que.append(nv)
                    elif self.color[nv] == self.color[ov]:
                        return False
        return True


N, M = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
B = list(map(lambda x: int(x) - 1, input().split()))

graph = BipartiteGraph(N)
for a, b in zip(A, B):
    graph.add_edge(a, b)

is_bipartite = graph.draw()
if is_bipartite:
    print("Yes")
else:
    print("No")
