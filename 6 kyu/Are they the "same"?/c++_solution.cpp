#include <stdbool.h>
#include <stdlib.h>

bool comp(const int *a, const int *b, size_t n)
{
    int* new_b = b;
    if(n == 0)
    {
      return false;
    }
    for(int i = 0;i < n; i++)
    {
      int new_number = a[i] * a[i];
      bool ok = false;
      for(int j = 0;j < n;j++)
      {
        if(new_b[j] == new_number)
        {
          ok = true;
          new_b[j] = -1;
          break;
        }
      }
      if(!ok)
      {

        return false;
      }
    }
    return true;
}
