def bfs_traversal(graph, initial_node):
    viewed_queue = []
    viewed_queue.append(initial_node)
    curr_queue = []
    curr_queue.append(initial_node)

    bfs_result = []

    while len(curr_queue) > 0:
        curr_node = curr_queue.pop(0)
        bfs_result.append(curr_node)
        
        for neighbor in graph[curr_node]:
            if neighbor not in viewed_queue:
                viewed_queue.append(neighbor)
                curr_queue.append(neighbor)
    print(bfs_result)
    return bfs_result




if __name__== '__main__':
    dict1 = {"+": ["*",3], "*":[2,7], 2:[],7:[],3:[]}
    start1 = "+"
    bfs_traversal(dict1, start1)
    dict2 = {0: [1,3], 1:[2,3], 2:[3,1], 3:[0,1]}
    start2 = 0
    bfs_traversal(dict2, start2)

