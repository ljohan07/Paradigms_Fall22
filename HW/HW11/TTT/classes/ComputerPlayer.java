package TTT.classes;
import TTT.classes.AbstractPlayer;
import java.util.Random;


public class ComputerPlayer extends AbstractPlayer {
   public int generatePos() {
    Random rand = new Random();
  
    // Generate random integers in range 0 to 999
    int randPos = rand.nextInt(8) + 1;
    return randPos;
   }
}