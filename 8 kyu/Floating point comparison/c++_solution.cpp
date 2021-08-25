#include <cmath>
using namespace std;

bool approx_equals(double a, double b) {
  return abs(a - b) < 0.001;
}
