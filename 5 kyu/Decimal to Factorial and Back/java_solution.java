import com.google.common.primitives.Ints;
import java.util.Arrays;
import java.util.*;

public class Dec2Fact {
  
  public static int in_array(String[] arr, char st){
    
    
    for(int i = 0; i < arr.length; i++){
      if(arr[i].equals(String.valueOf(st))){
        return i;
      }
    }
    return -1;
  }
	
  public static long Factorial(long nb){
    
    if (nb < 1){
        return 0;
    }
    long res = 1;
    while (nb > 1){
      res = res * nb;
      nb -= 1;
    }
    return res;
  }
  
	public static String dec2FactString(long nb) {
    
    int[] numbers = { 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35 };
    String[] letters = { "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" };

    String st = "0";
    long x = 2;
    while (nb > 0){
      int new_num = (int)(nb % x);
      String new_digit = String.valueOf(new_num);
      int index = Ints.indexOf(numbers, new_num);
      if (index != -1){
          new_digit = letters[index];
      }
      st += new_digit;
      nb = nb / x;
      x += 1;
    }
    StringBuffer str = new StringBuffer(st);
    str.reverse();
    st = new String(str);
    return st;
	}
	public static long factString2Dec(String str) {

    int[] numbers = { 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35 };
    String[] letters = { "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" };
    long result = 0;
    int x = 0;
      
    StringBuffer st = new StringBuffer(str);
    st.reverse();
    str = new String(st);
    for (int i = 0; i < str.length(); i++){
      
      if (in_array(letters, str.charAt(i)) != -1){
        int pos = in_array(letters, str.charAt(i));
        result += numbers[pos] * Factorial(x);
      }
      else
      {
        result += Factorial(x) * Integer.parseInt(String.valueOf(str.charAt(i)));
      }
      x += 1;
    }
    System.out.println(result);
    return result;
	}
}
