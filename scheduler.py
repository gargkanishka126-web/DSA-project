class DeliveryScheduler:

    def __init__(self, graph, average_speed_kmh=30):
        if average_speed_kmh <= 0:
            raise ValueError("Average speed must be greater than zero.")

        self.graph = graph
        self.average_speed_kmh = average_speed_kmh

    def create_schedule(self, depot, deliveries):

        if depot not in self.graph.adjacency:
            raise ValueError(f"Unknown depot: {depot}")

        remaining = list(dict.fromkeys(deliveries))
        route = [depot]
        total_distance = 0
        current = depot
        completed = []

        while remaining:
            distances, previous = self.graph.shortest_paths(current)

            reachable = [
                location for location in remaining
                if location in distances and distances[location] != float("inf")
            ]

            if not reachable:
                break

            next_location = min(reachable, key=lambda location: distances[location])
            path = self.graph.build_path(previous, next_location)
            leg_distance = distances[next_location]

            # Do not repeat the current location when joining route segments.
            route.extend(path[1:])
            total_distance += leg_distance
            completed.append(next_location)
            remaining.remove(next_location)
            current = next_location

        travel_time_hours = total_distance / self.average_speed_kmh

        return {
            "route": route,
            "total_distance_km": total_distance,
            "travel_time_hours": travel_time_hours,
            "completed_deliveries": completed,
            "unreachable_deliveries": remaining,
        }