def display_route(schedule):
    """Print a text summary of a delivery schedule."""
    route = schedule["route"]

    print("\nOptimized Delivery Route")
    print("-" * 30)
    print("Route:", " -> ".join(route))
    print(f"Total distance: {schedule['total_distance_km']:.2f} km")
    print(f"Estimated travel time: {schedule['travel_time_hours']:.2f} hours")
    print("Completed deliveries:", schedule["completed_deliveries"])
    print("Unreachable deliveries:", schedule["unreachable_deliveries"])


def plot_route(graph, schedule):
    """Draw the graph and route using matplotlib."""
    try:
        import matplotlib.pyplot as plt
        import networkx as nx
    except ImportError as error:
        print("Map display requires matplotlib and networkx.")
        print("Install them with: pip install matplotlib networkx")
        return

    network = nx.Graph()

    for location, neighbors in graph.adjacency.items():
        network.add_node(location)
        for neighbor, distance in neighbors.items():
            network.add_edge(location, neighbor, weight=distance)

    positions = nx.spring_layout(network, seed=7)
    route = schedule["route"]
    route_edges = list(zip(route, route[1:]))

    nx.draw(
        network,
        positions,
        with_labels=True,
        node_color="lightblue",
        node_size=1800,
        font_size=9,
    )
    nx.draw_networkx_edges(network, positions, edge_color="gray")

    if route_edges:
        nx.draw_networkx_edges(
            network,
            positions,
            edgelist=route_edges,
            edge_color="red",
            width=3,
        )

    edge_labels = nx.get_edge_attributes(network, "weight")
    nx.draw_networkx_edge_labels(network, positions, edge_labels=edge_labels)

    plt.title("Delivery Locations and Optimized Route")
    plt.show()