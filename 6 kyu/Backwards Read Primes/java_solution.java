import java.lang.*;

public class BackWardsPrime {
	
  public static boolean is_prime(long n){
    if(n <= 1){
      return false;
    }
    if(n == 2 || n % 2 == 0){
      return false;
    }
    for(int i=3; i < n; i = i + 2){
      if(n % i == 0){
        return false;
      }
    }
    return true;
    
  }
	public static String backwardsPrime(long start, long end) {
    
    String prime_list = "";
    
    for(long i = start;i <= end; i ++){
      
        String st = String.valueOf(i);
        StringBuilder st2 = new StringBuilder();
        st2.append(st);
        st2.reverse();
        st = st2.toString();
      
        if(is_prime(i))
          if(is_prime(Long.parseLong(st)))
             if(i != Long.parseLong(st))
                prime_list = prime_list + i + " ";
              
    }
    if (prime_list.length() != 0)
      return prime_list.substring(0, prime_list.length() - 1);
    return "";
	}
}
