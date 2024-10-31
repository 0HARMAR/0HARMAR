// father class
class Animal {
    public void eat() {
        System.out.println("This animal eats food.");
    }
}

// child class
class Dogs extends Animal {
    public void bark() {
        System.out.println("The dog barks.");
    }

    @Override
    public void eat() {
        // TODO Auto-generated method stub
        super.eat();
    }
}


public class extend {
    public static void main(String arg[])
    {
        System.out.println("hello");
        Dogs dog = new Dogs();
        dog.bark();
        dog.eat(); // inherit fathers method
    }
}

