public class Demo {
    public static void main(String[] args){
        Square square = new Square(10.0);
        System.out.println(square);
    }
}

class Square{
    private double side;
    public Square(){
        side = 1.0;
    }

    public Square(double side){
        this.side = side;
    }

    public double getSide() {
        return side;
    }

    public void setSide(double side) {
        this.side = side;
    }

    public double getArea(){
        return side*side;
    }

    public String toString(){
        return String.format("Square: side=%.1f area=%.1f", side,getArea());
    }
}