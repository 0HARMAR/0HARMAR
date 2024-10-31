using System;

namespace HelloWorld
{
    public class GenericClass<T> // def genericity class
{
    private T data;

    public GenericClass(T value)
    {
        data = value;
    }

    public void DisplayData()
    {
        Console.WriteLine("Data: " + data);
    }
}

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!,hmy");

            GenericClass<int> gc = new GenericClass<int>(1); // type is int
            gc.DisplayData();

            GenericClass<String> gc1 = new GenericClass<string>("hello"); // type is string
            gc1.DisplayData();
        }
    }
}
