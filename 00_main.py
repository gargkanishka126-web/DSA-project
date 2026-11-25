import json
from pathlib import Path

from benchmark import benchmark_shortest_paths
from graph import DeliveryGraph
from scheduler import DeliveryScheduler
from visualization import display_route, plot_route


PROJECT_DIR = Path(__file__).parent
MAP_FILE = PROJECT_DIR / "data" / "sample_map.json"
DELIVERIES_FILE = PROJECT_DIR / "data" / "sample_deliveries.json"


def load_data():
    """Load the sample map and delivery orders from JSON files."""
    with MAP_FILE.open(encoding="utf-8") as file:
        map_data = json.load(file)

    with DELIVERIES_FILE.open(encoding="utf-8") as file:
        delivery_data = json.load(file)

    graph = DeliveryGraph()

    for location in map_data["locations"]:
        graph.add_location(location)

    for location_a, location_b, distance in map_data["roads"]:
        graph.add_road(location_a, location_b, distance)

    return graph, delivery_data


def main():
    graph, delivery_data = load_data()
    depot = delivery_data["depot"]
    deliveries = delivery_data["deliveries"]
    scheduler = DeliveryScheduler(graph)

    while True:
        print("\n=== Delivery Route Optimization System ===")
        print("1. Show locations and roads")
        print("2. Find a shortest path")
        print("3. Create a delivery schedule")
        print("4. Display route map")
        print("5. Benchmark shortest paths")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            for location, neighbors in graph.adjacency.items():
                print(f"{location}: {neighbors}")

        elif choice == "2":
            start = input("Enter starting location: ").strip()
            destination = input("Enter destination: ").strip()

            try:
                distances, previous = graph.shortest_paths(start)
                distance = distances.get(destination, float("inf"))

                if distance == float("inf"):
                    print("No route exists between those locations.")
                else:
                    path = graph.build_path(previous, destination)
                    print("Shortest path:", " -> ".join(path))
                    print(f"Distance: {distance:.2f} km")
            except ValueError as error:
                print(error)

        elif choice == "3":
            schedule = scheduler.create_schedule(depot, deliveries)
            display_route(schedule)

        elif choice == "4":
            schedule = scheduler.create_schedule(depot, deliveries)
            plot_route(graph, schedule)

        elif choice == "5":
            try:
                benchmark_shortest_paths(graph, depot)
            except ValueError as error:
                print(error)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from the menu.")


if __name__ == "__main__":
    main()