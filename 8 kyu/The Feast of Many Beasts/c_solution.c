#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool feast(const char* beast, const char* dish) {

  return beast[0] == dish[0] && beast[strlen(beast)-1] == dish[strlen(dish)-1];

}
