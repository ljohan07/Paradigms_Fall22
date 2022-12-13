import java.lang.Math;
public class Point {
    private int x;
    private int y;

    public static void main(String[] args) {
        Point a = new Point(1,1);
        Point b = new Point(-1, -1);
        Point c = new Point(3, 4);

        if (a.equals(b))
            System.out.println(a.toString() + " == " + b.toString());
        else 
            System.out.println(a.toString() + " != " + b.toString());

        if (a.equals(c))
            System.out.println(a.toString() + " == " + c.toString());
        else 
            System.out.println(a.toString() + " != " + c.toString());

        if (b.equals(c))
            System.out.println(b.toString() + " == " + c.toString());
        else 
            System.out.println(b.toString() + " != " + c.toString());
        
        if (b.equals(null))
            System.out.println(b.toString() + " == null");
        else 
            System.out.println(b.toString() + " != null");
    }
    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }



    // the equals method is based on the distance 
    // from each point to the origin (0,0). It returns true if obj is equally 
    // closer to the origin (0,0) compared to “this”. False otherwise.
    @Override
    public boolean equals(Object other){
        if (other == null)
            return false;
        if(getClass() != other.getClass())
            return false;

        Point point = (Point) other;
        double dist_other = distance(point.x, point.y);
        double dist_this = distance(this.x, this.y);

        return dist_other == dist_this;
    }

    public double distance(int x, int y) {
        return Math.sqrt(Math.pow(x, 2) + Math.pow(y,2));
    }


    @Override
    public int hashCode(){
        int varCodeX = x;
        int varCodeY = y;
        // inits hash with the var code for one of the fields
        int hash = varCodeX;
        //  hash = <prime number> * hash + var_code;
        hash = 41 * hash + varCodeY;
        return hash;
    }

    @Override
    public String toString() {
        return "[" + x + ", " + y + "]";
    }

}