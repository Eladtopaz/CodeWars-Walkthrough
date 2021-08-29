namespace Solution
{
  using System;
  public static class Kata
  {
      public static Tuple<char?, int> LongestRepetition(string input)
      {
          
          char c = '\0';
          int l = 0;
          for(int i = 0; i<input.Length; i++)
          {
            char temp_c = input[i];
            int temp_l = 0;
            for(int j = i; j<input.Length;j++)
            {
              if(temp_c == input[j])
              {
                temp_l++;
              }
              else
              {
                break;
              }
            }
            if(temp_l > l)
            {
              l = temp_l;
              c = temp_c;
            }
          }
        
          if(c != '\0')
            return new Tuple<char?, int>(c, l);
          return new Tuple<char?, int>(null, 0);

      }
  }
}
