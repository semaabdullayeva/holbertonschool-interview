# Wild Compare

## Description

The function `wildcmp` compares two strings and returns 1 if the strings can be considered identical, otherwise return 0.

## Prototype

```c
int wildcmp(char *s1, char *s2);
```

## Usage

```c

#include "wildcmp.h"

int main(void)
{
    char *s1 = "main.c";
    char *s2 = "*.c";

    printf("%d\n", wildcmp(s1, s2)); /* 1 */

    return (0);
}
```
