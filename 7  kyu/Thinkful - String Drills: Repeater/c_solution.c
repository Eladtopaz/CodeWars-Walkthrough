#include <stdlib.h>
#include <string.h>

char* repeater(const char* strin, int n) {

    char* new_string = (char *) calloc ((strlen(strin) * n) + 1, sizeof(char));

    strcpy(new_string, strin);
    while(n != 1)
    {
      strcat(new_string, strin);
      n--;
    }
    return new_string;
}
