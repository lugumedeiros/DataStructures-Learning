from collections import deque

def bfs_search_bad(graph, start_search, item_search):
    # Tried to do my own just from concepts, not so bad I think
    invalid_graph = []
    search_graph = graph[start_search]
    degree = 1
    
    while len(search_graph) > 0:
        if item_search in search_graph:
            print(f"item found!, {degree} items distant from start")
            break
        else:
            temp_graph = search_graph.copy()
            for key in search_graph:
                invalid_graph.append(key)
                temp_graph += graph[key]
            new_graph = []
            for key in temp_graph:
                if not key in invalid_graph:
                    new_graph.append(key)
        search_graph = new_graph
        degree += 1

def bfs_search(graph, start_search, item_search):
    # This one I applied FIFO, first time I used this...
    degree = 0
    fifo = deque([(start_search, degree)]) # List of tuples
    invalid_keys = set([start_search])

    while len(fifo) > 0:
        key, degree = fifo[0]
        if key == item_search:
            print(f"item found!, {degree} items distant from start")
            return
        else:
            fifo.popleft()
            for subkey in graph[key]:
                if not subkey in invalid_keys:
                    fifo.append((subkey, degree + 1))