using System;
using System.Windows.Forms;

public class MyForm : Form
{
    private Button button;

    public MyForm()
    {
        button = new Button();
        button.Text = "Click Me!";
        button.Click += new EventHandler(Button_Click);
        Controls.Add(button);
    }

    private void Button_Click(object sender, EventArgs e)
    {
        MessageBox.Show("Hello, Windows Forms!");
    }

    [STAThread]
    public static void Main()
    {
        Application.Run(new MyForm());
    }
}
