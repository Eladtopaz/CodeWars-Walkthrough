public class Number
{
  public int DigitalRoot(long n)
  {
    long sum = 0;
    while(n > 0){
      sum += n % 10;
      n = n / 10;
    }
    if(sum <= 9)
      return (int)sum;
    return DigitalRoot(sum);
  }
}
