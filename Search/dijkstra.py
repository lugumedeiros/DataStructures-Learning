from collections import deque
import heapq

def dijkstra_bad2(graph, start):
    """I tried to make my own code for the dijkstra algorithm but it ended like a bfs search with distance mapping
    The main problem is that it will watse time because the order of searching is decided by the graph input,
    and not about the shortest path first, but in the end works and it has the complexity of a bfs lol.
    """

    # Create a FIFO and visited blacklist set
    fifo = deque([(start)])
    visited = set([])
    
    # Create distance map with invalid dist.
    distance = {node:float('inf') for node in graph}
    distance[start] = 0

    while len(fifo):
        node = fifo.popleft()
        visited.add(node)
        curr_dist = distance[node]
        for key, dist in graph[node]:
            dist += curr_dist
            # Test if current node was visited already
            if key in visited:
                pass
            else:
                fifo.append(key)
                # Test if current declared distance is greater than new one
                if distance[key] > dist:
                    distance[key] = dist
                else:
                    pass
    return distance  

def dijkstra_bad(graph, start):
    """ I never user heapq before, so this was my poor implementation of "correct" dijkstra, chapgpt is screaming tho...
    In the end this was potentially slower than my bfs version.
    """
    def get_smaller_value(map, blacklist):
        smll_v = float('inf')
        smll_k = None
        for key, value in map.items():
            if not (key in blacklist) and (value < smll_v):
                smll_v = value
                smll_k = key
        if smll_k == None:
            pass
        return smll_k

    set_visited = set([]) # List with all searched nodes
    map_dist = {node:float('inf') for node in graph} # List with the updated distances from start
    map_dist[start] = 0

    while len(set_visited) < len(map_dist):
        node = get_smaller_value(map_dist, set_visited)
        if node is None: break
        set_visited.add(node)
        current_dist = map_dist[node]

        for sub_node, sub_dist in graph[node]:
            sub_dist += current_dist
            if sub_node in set_visited:
                pass
            else:
                if sub_dist < map_dist[sub_node]:
                    map_dist[sub_node] = sub_dist

    return map_dist
                    
def dijkstra(graph, start):
    """This is the correct python code for "dijksjktsra" i think... I used heapq this time, as adviced by chatgpt."""
    map_dist = {node:float('inf') for node in graph}
    map_dist[start] = 0
    to_visit = [(0, start)]

    while len(to_visit) > 0:
        current_dist, node = heapq.heappop(to_visit)

        for sub_node, sub_dist in graph[node]:
            sub_dist += current_dist

            if sub_dist < map_dist[sub_node]:
                map_dist[sub_node] = sub_dist
                heapq.heappush(to_visit, (sub_dist, sub_node))

    return map_dist