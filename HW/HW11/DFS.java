import java.util.*; 
public class DFS {
    public static void main(String[] args) {
        DFS dfs1 = new DFS();
        String root = "a";
        Map<String, List<String>> graph = new HashMap<>();
        graph.put("a", Arrays.asList("b", "e"));
        graph.put("b", Arrays.asList("c", "d"));
        graph.put("c", Arrays.asList("e"));
        graph.put("d", Arrays.asList("b"));
        graph.put("e", Arrays.asList("a", "f"));
        graph.put("f", Arrays.asList());
        List<String> ans1 = new ArrayList<String>();
        ans1 = dfs1.traverse(root, graph);
        System.out.println(ans1);
        System.out.println(graph);
    }
    public List<String> traverse(String root, Map<String,List<String>> graph){
        Stack<String> stk= new Stack<String>(); 
        List<String> ans = new ArrayList<String>();

        stk.push(root);

        while (!stk.empty()) {
            String top = stk.peek();
            stk.pop();

            if (ans.contains(top)) {
                continue;
            }
            ans.add(top);

            for (int i = graph.get(top).size() - 1; i >=0; i--) {
                stk.push(graph.get(top).get(i));
            }

        }
        return ans;

    }    

    
}
