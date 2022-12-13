package TTT.classes;
import TTT.classes.AbstractPlayer;
import java.util.Scanner;  // Import the Scanner class


public class UserPlayer extends AbstractPlayer {
   public int generatePos() {
    Scanner myObj = new Scanner(System.in);  // Create a Scanner object
    System.out.println("Enter valid position: ");

    String pos = myObj.nextLine();  // Read user input
    int position = Integer.parseInt(pos);
    return position;
   }
}