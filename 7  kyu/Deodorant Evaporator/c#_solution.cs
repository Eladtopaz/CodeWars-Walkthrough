public class Evaporator { 
  
  public static int evaporator(double content, double evap_per_day, double threshold) {
    int i = 0;
    double restrict = (threshold / 100) * content;
    while(content > restrict)
    {
        content = content - (content * (evap_per_day / 100));
        i += 1;
    }
    return i;
  }
}
