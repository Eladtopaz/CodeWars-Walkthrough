using namespace std;
class Evaporator
{

  public:
  static int evaporator(double content, double evap_per_day, double threshold) {
    int i = 0;
    double res = (threshold / 100) * content;
    while(content > res)
    {
        content = content - (content * (evap_per_day / 100));
        i += 1;
    }
    return i;
  }
};
