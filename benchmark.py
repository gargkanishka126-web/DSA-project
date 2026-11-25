from time import perf_counter


def benchmark_shortest_paths(graph, start, repeats=100):
    if repeats <= 0:
        raise ValueError("Repeats must be greater than zero.")

    start_time = perf_counter()

    for _ in range(repeats):
        graph.shortest_paths(start)

    elapsed = perf_counter() - start_time
    average_seconds = elapsed / repeats

    print(f"Locations: {len(graph.adjacency)}")
    print(f"Runs: {repeats}")
    print(f"Average shortest-path time: {average_seconds:.8f} seconds")

    return average_seconds