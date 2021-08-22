public class Kata
{
  public static string Repeater(string s, int n)
  {    
    string new_string = "";
    while(n != 0)
    {
      new_string += s;
      n--;
    }
    return new_string;
  }
}
