public class Repeater{
  public static String repeat(String string,long n){
    
    String new_string = "";
    while(n != 0)
    {
      new_string += string;
      n--;
    }
    return new_string;
  }
}
