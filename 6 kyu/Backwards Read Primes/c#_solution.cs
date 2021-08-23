using System;
using System.Linq;

public class BackWardsPrime {
  
  
	public static bool is_prime(long n){
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
	public static string backwardsPrime(long start, long end) {
		
    string prime_list = "";
    
    for(long i = start;i <= end; i ++){
      
        string st = i.ToString();
        
        char[] charArray = st.ToCharArray();
        Array.Reverse(charArray);
        
        st = new string(charArray);
      
        if(is_prime(i))
          if(is_prime(Convert.ToInt64(st)))
             if(i != Convert.ToInt64(st))
                prime_list = prime_list + i + " ";
              
    }
    
    if (prime_list.Length != 0)
      return prime_list.Substring(0, prime_list.Length - 1);
    return "";
  }
}
