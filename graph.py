import heapq


class DeliveryGraph:

    def __init__(self):
        self.adjacency = {}

    def add_location(self, name):
        if not name or not name.strip():
            raise ValueError("Location name cannot be empty.")

        self.adjacency.setdefault(name, {})

    def add_road(self, location_a, location_b, distance):
        if distance < 0:
            raise ValueError("Road distance cannot be negative.")

        if location_a not in self.adjacency:
            self.add_location(location_a)
        if location_b not in self.adjacency:
            self.add_location(location_b)

        self.adjacency[location_a][location_b] = distance
        self.adjacency[location_b][location_a] = distance

    def shortest_paths(self, start):
        if start not in self.adjacency:
            raise ValueError(f"Unknown starting location: {start}")

        distances = {location: float("inf") for location in self.adjacency}
        previous = {location: None for location in self.adjacency}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current = heapq.heappop(priority_queue)

            if current_distance != distances[current]:
                continue

            for neighbor, road_distance in self.adjacency[current].items():
                new_distance = current_distance + road_distance

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current
                    heapq.heappush(
                        priority_queue,
                        (new_distance, neighbor)
                    )

        return distances, previous

    @staticmethod
    def build_path(previous, destination):
        if destination not in previous:
            return []

        path = []
        current = destination

        while current is not None:
            path.append(current)
            current = previous[current]

        return list(reversed(path))