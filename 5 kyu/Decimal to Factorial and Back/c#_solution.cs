using System;
using System.Linq;

    public class Dec2Fact
    {


        public static long Factorial(long nb)
        {
            if (nb < 1)
            {
                return 0;
            }
            long res = 1;
            while (nb > 1)
            {
                res = res * nb;
                nb -= 1;
            }
            return res;
        }
        public static string dec2FactString(long nb)
        {

            string[] numbers = { "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35" };
            string[] letters = { "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" };

            string st = "0";
            long x = 2;
            while (nb > 0)
            {
                string new_digit = (nb % x).ToString();
                if (Array.IndexOf(numbers, new_digit) != -1)
                    new_digit = letters[Array.IndexOf(numbers, new_digit)];
                st += new_digit;
                nb = nb / x;
                x += 1;
            }
            char[] charArray = st.ToCharArray();
            Array.Reverse(charArray);
            st = new string(charArray);
            return st;
        }
        public static long factString2Dec(string str)
        {

            string[] numbers = { "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35" };
            string[] letters = { "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" };
            long result = 0;
            int x = 0;
            char[] charArray = str.ToCharArray();
            Array.Reverse(charArray);
            str = new string(charArray);

            for (int i = 0; i < str.Length; i++)
            {

                if (Array.IndexOf(letters, str[i].ToString()) != -1)
                {
                    int pos = Array.IndexOf(letters, str[i].ToString());
                    result += Int16.Parse(numbers[pos]) * Factorial(x);
                }
                else
                {
                    result += Factorial(x) * int.Parse(str[i].ToString());
                }
                x += 1;
            }
            return result;
        }
    }
