public class Board{
    private int [][] board;
    private int[] available;
    public Board() {
        this.board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]];
        this.available = [1,2,3,4,5,6,7,8,9];
    }
    public boolean place(int row, int col, int player_type);
    public boolean determine_win(int player);
}
