package TTT;
import TTT.classes.*;
import java.util.*; 


public class Game {
  private char [][] board = new char [3][3];
  public void printBoard() {
    int counter = 1;
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        if (board[i][j] == 'X' || board[i][j] == 'O') {
          System.out.print(" ");
          System.out.print(board[i][j]);
          System.out.print(" ");
        }
        else {
          System.out.print("   ");
        }
        if (j < 2) {
          System.out.print("|");
        }
      }
      System.out.println();
      if (i < 2) {
        System.out.println("---+---+---");
      }
    }
  }

  // returns 1 if user wins
  // returns 2 if computer wins
  // returns 3 if draw
  public int hasEnded() {
    int xCounter;
    int yCounter;
    
    
    // checking diagonal
    if (board[1][1] == 'X' || board[1][1] == 'O') {
      if (board[0][0] == board[1][1] && board[2][2] == board[1][1]) {
        if (board[1][1] == 'X') {
          return 1;
        }
        else {
          return 2;
        }
      }
      if (board[0][2] == board[1][1] && board[2][0] == board[1][1]) {
        if (board[1][1] == 'X') {
          return 1;
        }
        else {
          return 2;
        }
      }
    }
    for (int i = 0; i < 3; i++) {
      xCounter = 0;
      yCounter = 0;
      
      for (int j = 0; j < 3; j++) {
        if ((board[i][j] == 'X' || board[i][j] == 'O') && j == 0) {
          xCounter++;
          yCounter++;
        }
        else {
          // checks the row
          if ((board[i][j] == 'X' || board[i][j] == 'O') && board[i][j] == board[i][0]) {
            xCounter++;
          }
          // checks the column
          if ((board[j][i] == 'X' || board[j][i] == 'O') && board[j][i] == board[0][i]) {
            yCounter++;
          }
        }
        if ((xCounter == 3 || yCounter == 3)) {
          int r;
          int c;
          if (xCounter == 3) {
            r = i;
            c = j;
          }
          else {
            r = j;
            c = i;
          }
          if (board[r][c] == 'X') {
            return 1;
          }
          else {
            return 2;
          }
          
        }
      }
      
    }
    boolean isFull = true;
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        if (!(board[i][j] == 'X' || board[i][j] == 'O')) {
          isFull = false;
        }
      }
    }
    if (isFull) {
      return 3;
    }
    return 0;
  }
  public void run(Player p1, Player p2) {
    Set<Integer> taken = new HashSet<Integer>();
    int p1Spot;
    int p2Spot;
    int r;
    int c;
    while (hasEnded() == 0) {
      p1Spot = p1.play(taken);
      taken.add(p1Spot);
      r = (p1Spot-1) / 3;
      c = (p1Spot-1) % 3;
      this.board[r][c] = 'X';
      if (hasEnded() == 0) {
        p2Spot = p2.play(taken);
        taken.add(p2Spot);
        r = (p2Spot-1) / 3;
        c = (p2Spot-1) % 3;
        this.board[r][c] = 'O';
      }
      this.printBoard();
    }
  }
  public static void main(String[] args) {
      Game game = new Game();
      Player user1 = new UserPlayer();
      Player user2 = new ComputerPlayer();
      game.run(user1, user2);
      if (game.hasEnded() == 1) {
        System.out.println("Player 1 has won!");
      }
      else if (game.hasEnded() == 2) {
        System.out.println("Computer has won!");
      }
      else if (game.hasEnded() == 3) {
        System.out.println("Draw!");
      }
  }
}




