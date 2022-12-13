public class Homework10{
    public static void main(String [] args) {
        System.out.println("Hello world");
        char [][] correctPositions = new char[][] 
        {{ 'W', '*', 'R'}, { 'W', '*' }, { 'S', '*', 'G', '*', 'R'}, {}, { '*', '*', '*', '*', '*'}};
        String [] words = {"WoRdle", "wordle", "SUGAR", "", "PARADIGMS"}; 

        Homework10 hw10 = new Homework10();
        boolean checker;
        for (int i = 0; i < correctPositions.length; i++) {
            checker = hw10.check(correctPositions[i], words[i]);
            if (checker) {
                System.out.println("true");
            } else {
                System.out.println("false");
        }
        }
        
    }
    public boolean check(char[] correctPositions, String word) {
        /* your solution goes here */
        for (int i = 0; i < correctPositions.length; i++) {
            if (correctPositions[i] != '*') {
                if (correctPositions[i] != word.charAt(i)) {
                    return false;
                }
            }
        }
        return true;
    }
}
