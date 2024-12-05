import heapq
import sys
input = sys.stdin.readline

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 1
    pq = [(1, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_node == end:
            return current_distance

        for neighbor, weight in graph[current_node].items():
            distance = current_distance * weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances[end]

def main():
    (n, m) = map(int, input().split())
    graph = {i: {} for i in range(1, n+1)}

    for _ in range(m):
        (u, v, p) = map(int, input().split())
        graph[u][v] = 1 - p / 100
        graph[v][u] = 1 - p / 100

    (A, B) = map(int, input().split())
    distance = dijkstra(graph, A, B)

    required_units = 100 / distance
    print(f"{required_units:.8f}")

main()
