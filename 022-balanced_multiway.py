"""
022-balanced_multiway.py
Esquema simplificado de Balanced Multiway Merging: mezclar k runs a la vez.
"""
def multiway_merge(runs):
    import heapq
    heap = []
    for i, run in enumerate(runs):
        if run:
            heap.append((run[0], i, 0))
    heapq.heapify(heap)
    out = []
    while heap:
        val, i, idx = heapq.heappop(heap)
        out.append(val)
        if idx+1 < len(runs[i]):
            heapq.heappush(heap, (runs[i][idx+1], i, idx+1))
    return out

def main():
    runs = [[1,4,7],[2,5,8],[3,6,9]]
    print("Runs:", runs)
    print("Merged:", multiway_merge(runs))