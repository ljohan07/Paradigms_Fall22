package TTT.classes;
import TTT.classes.Player;
import java.util.*;

public abstract class AbstractPlayer implements Player {
   public int play(Set<Integer> taken) {
    int choice = generatePos();
    while (taken.contains(choice)) {
        choice = generatePos();
    }
    return choice;
   }
   public abstract int generatePos();
}
