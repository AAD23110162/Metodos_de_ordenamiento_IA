"""
024-distribution_initial_runs.py
Distribución de runs iniciales (simulación): dividir entrada en runs y asignar a ficheros/buckets.
"""
def distribute_runs(a, bucket_count):
    runs = []
    curr = []
    for x in a:
        if not curr or x >= curr[-1]:
            curr.append(x)
        else:
            runs.append(curr); curr = [x]
    if curr:
        runs.append(curr)
    # asignar a buckets round-robin (simulado)
    buckets = [[] for _ in range(bucket_count)]
    for i, r in enumerate(runs):
        buckets[i % bucket_count].append(r)
    return buckets

def main():
    a = [1,2,6,3,4,7,5,8,9]
    print("Input:", a)
    print("Buckets:", distribute_runs(a, 3))