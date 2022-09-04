def tree_to_text(tree, root_node):
    temp = []
    ans = []
    curr = root_node
    while len(ans) != len(tree.keys()):
        # go all the way down the left side of the tree
        while len(tree[curr]) > 0:
            temp.append(curr)
            curr = tree[curr][0]
        if len(ans) < len(tree.keys()):
            ans.append(curr)
        # once there is no more to the left, pop elements, try the right
        try:
            curr2 = temp.pop(-1)
            if len(ans) < len(tree.keys()):
                ans.append(curr2)
        except:
            pass
        curr = tree[curr2][1]
    ans = ''.join(ans)
    print(ans)
    return ans

def parse_tree_input(input, root):
     # parsing the tree and root node to numberical/symbolic values
    new_dict = {}
    for key, elems in input.items():
        i = key.index('_')
        new_dict[key[i+1]] = []
        for elem in elems:
            j = elem.index('_')
            new_dict[key[i+1]].append(elem[j+1])
    root_i = root.index('_')
    root = root[root_i+1]
    return new_dict, root



if __name__ == '__main__':
    dict1 = {"n1_+": ["n2_*","n3_3"], "n2_*":["n4_2","n5_7"], "n4_2":[],"n5_7":[],"n3_3":[]}
    start1 = "n1_+"
    new_in1 = parse_tree_input(dict1, start1)
    tree_to_text(new_in1[0], new_in1[1])
    dict2 ={'n1_+': ['n2_3', 'n3_*'], 'n3_*': ['n4_/', "n5_2"], 'n4_/': ["n6_10", "n7_5"], "n6_10": [], "n7_5": [], "n5_2": [], 'n2_3': []}
    start2 = "n1_+" 
    new_in2 = parse_tree_input(dict2, start2)
    tree_to_text(new_in2[0], new_in2[1])
