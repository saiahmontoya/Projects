# Saiah Montoya 029177653
import math
import sys
from queue import PriorityQueue
import matplotlib.pyplot as plt

# Haversine formula to calculate distance between two lat/lon points
def haversine(lat1, lon1, lat2, lon2):
    # Earth's radius in miles
    r = 3958.8  
    
    # Convert latitude and longitude from degrees to radians
    phi1, phi2 = math.radians(lat1), math.radians(lat2)  # Latitude in radians
    delta_phi = math.radians(lat2 - lat1)  # Difference in latitude in radians
    delta_lambda = math.radians(lon2 - lon1)  # Difference in longitude in radians
    
    # Apply Haversine formula
    # a: square of half the length between the points
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    
    # c: angular distance in radians
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Distance between two points in miles
    return r * c



# Read coordinates.txt file
def read_coordinates(file_path):
    # Empty dict to store city coordinates
    coordinates = {}
    
    # Read file line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Split city and coords, remove parentheses, split lat/lon
            city, coord = line.strip().split(':')
            lat, lon = coord.strip('()').split(',')
            
            # Store city and its (lat, lon)
            coordinates[city] = (float(lat), float(lon))
    
    # Return city coordinates
    return coordinates

# Read map.txt file
def read_map(file_path):
    # Empty dict to store adjacency list
    map_list = {}
    
    # Read file line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Split city and neighbors
            city, neighbors = line.strip().split('-')
            neighbors = neighbors.split(',')
            
            # Store each neighbor and its distance
            map_list[city] = []
            for neighbor in neighbors:
                neighbor_city, distance = neighbor.split('(')
                distance = float(distance.strip(')'))
                map_list[city].append((neighbor_city, distance))
    
    # Return adjacency list (map)
    return map_list

# For fun I wanted to visualize the best path possible
# Function to plot all possible routes and the optimal route
def plot_route(coordinates, optimal_path):
    latitudes = []
    longitudes = []
    
    # Extract latitudes and longitudes for the optimal path
    for city in optimal_path:
        if city in coordinates:
            lat, lon = coordinates[city]
            latitudes.append(lat)
            longitudes.append(lon)
        else:
            print(f"Warning: Missing coordinates for city {city}")

    if latitudes and longitudes:
        # Plot the optimal route in red
        plt.plot(longitudes, latitudes, color='red', linestyle='-', linewidth=2, zorder=2)

    # Plot the cities (nodes) and label all cities
    for city, (lat, lon) in coordinates.items():
        plt.scatter(lon, lat, color='blue', zorder=3)
        plt.text(lon, lat, city, fontsize=9, ha='right', color='black')

    # Set plot labels and title
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Optimal Route')
    plt.grid(True)
    
    # Display the plot
    plt.show()

# a* algorithm
def a_star(start, goal, coordinates, map_list):
    # priority queue to store (f-cost, g-cost, current city, path)
    pq = PriorityQueue()
    pq.put((0, 0, start, []))  # (f-cost, g-cost, current city, path so far)
    visited = {}
    
    while not pq.empty():
        current_f_cost, current_g_cost, current_city, path = pq.get()

        # If current city has been visited with a smaller cost, skip
        if current_city in visited and visited[current_city] <= current_g_cost:
            continue

        visited[current_city] = current_g_cost

        # Add current city to path
        path = path + [current_city]

        # If we reach the goal return path and cost
        if current_city == goal:
            return path, current_g_cost

        # Iterate through neighbors
        for neighbor, dist in map_list.get(current_city, []):
            if neighbor not in visited or visited[neighbor] > current_g_cost + dist:
                # Calculate heuristic using the Haversine
                lat1, lon1 = coordinates[current_city]
                lat2, lon2 = coordinates[goal]
                h = haversine(lat1, lon1, lat2, lon2)

                # Reduce influence of the heuristic to avoid unnecessary detours
                h = h * 0.1  # Reduce the weight of the heuristic, tried 0.3, 0.5, and none, 0.1 works best

                # g = current cost + actual distance to neighbor
                g = current_g_cost + dist

                # f = g + h (g = actual cost so far, h = heuristic)
                total_cost = g + h

                # Add to priority queue
                pq.put((total_cost, g, neighbor, path))

    # If no path is found
    return None, float('inf')


# Main function to execute the script
def main():
    if len(sys.argv) != 3:
        print("Usage: python a-star.py <start_city> <end_city>")
        sys.exit(1)

    start_city = sys.argv[1]
    end_city = sys.argv[2]

    # read the input files
    coordinates = read_coordinates('coordinates.txt')
    #testing print(coordinates)
    map_list = read_map('map.txt')
    #testing print(map_list)

    # Run A* algorithm
    path, total_distance = a_star(start_city, end_city, coordinates, map_list)

    # Output the result
    if path:
        print(f"From city: {start_city}")
        print(f"To city: {end_city}")
        print("Best Route: " + " - ".join(path))
        print(f"Total distance: {total_distance:.2f} mi")
        plot_route(coordinates, path)
    else:
        print("No route found")

if __name__ == '__main__':
    main()
