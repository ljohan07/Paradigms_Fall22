function tree_to_text(tree, root_node){
    // your implementation here
    // your function will return a string!
    ans = ''
    let ans_arr = []
    let track_queue = []
    let node = root_node
    while (Object.keys(tree).length != ans_arr.length) {
        while (tree[node] && tree[node][0]) {
            track_queue.push(node)
            node = tree[node][0]
        }
        let left = node
        let curr = track_queue.pop()
        if (left) {
            ans_arr.push(left)
        }
        if (curr) {
            ans_arr.push(curr)
        }
        
        if (tree[curr] && tree[curr][1]) {
            node = tree[curr][1]
        }
        
    }
    ans_str = ""
    let i = 0
    for (i = 0; i < ans_arr.length; i++) {
        let text_arr = ans_arr[i].split("_")
        ans_str += text_arr[1]
    }
    
    return ans_str
}

let tree1 = {
    'n1_+': ['n2_3', 'n3_*'], 
    'n3_*': ['n4_/', "n5_2"], 
    'n4_/': ["n6_10", "n7_5"], 
    "n6_10": [], 
    "n7_5": [], 
    "n5_2": [], 
    'n2_3': []
  }
let root_node1 = "n1_+" 
tree2 =  {
    "n1_+": ["n2_*","n3_3"], 
    "n2_*":["n4_2","n5_7"], 
    "n4_2":[],
    "n5_7":[],
    "n3_3":[]
  }
  root_node2 = "n1_+" 

console.log(tree_to_text(tree1, root_node1))
console.log(tree_to_text(tree2, root_node2))