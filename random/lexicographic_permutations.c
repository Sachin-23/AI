#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void swap(char **s, int i, int j)  {
  char *temp = s[i];
  s[i] = s[j];
  s[j] = temp;
}

void reverse(char **s, int start, int end)  {
  while (start < end)  {
    swap(s, start++, end--);
  }
}

void lexi(char **a, int n)  {
  int k = -1, I = -1;

  for (int i = 0; i < 3; i++)  {
    printf("%s ", a[i]);
  }

  printf("\n");

  for (int i = 0; i < n - 1; i++)  {
    if (strcmp(a[i + 1], a[i]) > 0)  {
      k = i;
    }
  }

  if (k == -1)  {
    printf("Done");
    exit(0);
  }

  for (int i = 0; i < n; i++)  {
    if (strcmp(a[i], a[k]) > 0)  {
      I = i;
    }
  }

//  printf("k = %d, I = %d\n", k, I);

  swap(a, k, I);

  reverse(a, k + 1, n - 1);

  lexi(a, n);
  sleep(1);
}

int main()  {
  char *a[] = {"a", "bc", "bc"}; 
  lexi(a, 3);
  return 0;
}
