#include <stdio.h>
#define MAX 10 
#define INT_MAX 65535


int count(int arr[], int n)  {
  int count = 0;
  for (int i = 0; i < n; i++)  {
    if (arr[i] != INT_MAX && arr[i] != -1)  {
      count++; 
    }
  }
  return count;
}

int extract_min(int arr[], int n)  {
  int min = INT_MAX, pos;
  for (int i = 0; i < n; i++)  {
    if (arr[i] < min && arr[i] != -1)  {
      min = arr[i];
      pos = i;
    }
  }
  arr[pos] = -1;
  return pos;
}

void update(int arr[], int i, int key)  {
  arr[i] = key;
}


void dijkstra(int g[MAX][MAX], int n, int u)  {
  int d[MAX], pred[MAX], pq[MAX];
  for (int i = 0; i < n; i++)  {
    d[i] = INT_MAX;
    pq[i] = INT_MAX;
  }
  d[u] = 0;
  pq[u] = 0;
  while (count(pq, n))  {
    u = extract_min(pq, n);
    for (int i = 0; i < n; i++)  {
      if (g[u][i] != 0)  {
        if (d[u] + g[u][i] < d[i])  {
          d[i] = d[u] + g[u][i];
          update(pq, i, d[i]);
          pred[i] = u;
        }
      }
    }
  }
  printf("cost from source to v:  ");
  for (int i = 0; i < n; i++)  {
    printf("%d ", d[i]);
  }
  printf("\n");
  printf("pq: ");
  for (int i = 0; i < n; i++)  {
    printf("%d ", pq[i]);
  }
}

int main()  {
  int i, j, u, n = 5; 
  int g[MAX][MAX] = {  // weighted-graph 
    {0, 2, 7, 0, 0},
    {0, 0, 3, 8, 5},
    {0, 2, 0, 1, 0},
    {0, 0, 0, 0, 4},
    {0, 0, 0, 5, 0}
  };
  /*int g[MAX][MAX] = {  // weighted-graph 
    {0, 1, 0, 3, 10},
    {1, 0, 5, 0, 0},
    {0, 5, 0, 2, 1},
    {3, 0, 2, 0, 6},
    {10, 0, 1, 6, 0}
  };*/
  u = 0; // source node
 
  /*
  for (int i = 0; i < n; i++)  {
    for (int j = 0; j < n; j++)  {
      printf("%d ", g[i][j]);
    }
    printf("\n");
  }
  */

  dijkstra(g, n, u); 

  return 0;
}
