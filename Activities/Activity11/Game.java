public class Game{
    public Board board;
    public Player player;
    public int id;
    
    public Game(Player player, Board board) {
        this.board = board;
        this.player = player;
        this.id = 0;
    }

    public void newspot();
}