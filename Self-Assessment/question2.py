def dfs_traversal(graph, initial_node):
    viewed_stack = []
    viewed_stack.append(initial_node)
    curr_stack = []
    curr_stack.append(initial_node)

    dfs_result = []

    while len(curr_stack) > 0:
        curr_node = curr_stack.pop(-1)
        dfs_result.append(curr_node)
        
        # add the right node before the left node to get the correct order
        temp = list(graph[curr_node])
        temp.reverse()
        for neighbor in temp:
            if neighbor not in viewed_stack:
                viewed_stack.append(neighbor)
                curr_stack.append(neighbor) 
    print(dfs_result)
    return dfs_result

if __name__== '__main__':
    dict1 = {"+": ["*",3], "*":[2,7], 2:[],7:[],3:[]}
    start1 = "+"
    dfs_traversal(dict1, start1)
    dict2 = {0: [1,3], 1:[2,3], 2:[3,1], 3:[0,1]}
    start2 = 0
    dfs_traversal(dict2, start2)
