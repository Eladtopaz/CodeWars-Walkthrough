public class Solution {
    public static Object[] longestRepetition(String s) {
      
        String c = "";
        int l = 0;
        for(int i = 0; i < s.length(); i++){
          
          String temp_c = String.valueOf(s.charAt(i));
          int temp_l = 0;
          
          for(int j = i; j <s.length(); j++){
            if(temp_c.equals(String.valueOf(s.charAt(j)))){
                temp_l++;
            }else{
              break;
            }
          }
          if(temp_l > l){
            l = temp_l;
            c = temp_c;
          }
        }
        return new Object[]{c, l};
    }
}
