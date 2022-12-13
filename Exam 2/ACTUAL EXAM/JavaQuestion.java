public class JavaQuestion{
    public int id;
    public JavaQuestion() {}
    public static void main (String [] args) {
        int [] ex1 = {0, 1, 2, 241, 241, 0, 0, 241, 241, 241};
        JavaQuestion ex1q = new JavaQuestion();
        System.out.println(ex1q.findMaxConsecutiveNumbers(ex1));
        int [] ex2 = {0, 241, 241, 241, 241, 0, 0, 241, 241, 241};
        JavaQuestion ex2q = new JavaQuestion();
        System.out.println(ex2q.findMaxConsecutiveNumbers(ex2));
    }
	public int findMaxConsecutiveNumbers(int[] nums) {
	    /* your solution goes here */
        int target = 241;
        int maxOccurrences = 0;
        int tempCount = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                tempCount += 1;
                if (tempCount > maxOccurrences) {
                    maxOccurrences = tempCount;
                }
            }
            else {
                tempCount = 0;
            }

        }
        return maxOccurrences;

	}
}