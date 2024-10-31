public class Person
{
    private string name; // 私有字段

    // 属性
    public string Name
    {
        get { return name; }
        set { name = value; }
    }
}

public class property 
{
    public static void Main()
    {
        Person person = new Person();
        string name = person.Name = "hemingyang";
        Console.WriteLine(person.Name);
    }
}