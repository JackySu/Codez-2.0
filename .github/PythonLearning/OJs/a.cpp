#include <iostream>
using namespace std;

int main()
{
    int m;
    int n;
    int a;
    int b;
    cin >> m;
    cin >> n;
    cin >> a;
    cin >> b;
    int chess[n + 3][m + 3];
    long count[n + 1][m + 1];
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= m; j++)
        {
            chess[i][j] = 0;
            count[i][j] = 0;
        }
    
    chess[a][b] = -1;
    if (a > 1)
    {
        chess[a - 2][b - 1] = -1;
        chess[a - 2][b + 1] = -1;
    }
    chess[a + 2][b - 1] = -1;
    chess[a + 2][b + 1] = -1;
    if (b > 1)
    {
        chess[a - 1][b - 2] = -1;
        chess[a + 1][b - 2] = -1;
    }
    chess[a - 1][b + 2] = -1;
    chess[a + 1][b + 2] = -1;


    for (int i = 0; i <= n; i++)
    {
        count[0][i] = 1;
    }
    for (int i = 0; i <= n; i++)
    {
        count[i][0] = 1;
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            if (chess[i][j] != -1)
            {
                if (chess[i - 1][j] == -1)
                    count[i][j] = count[i][j - 1];
                else if (chess[i][j - 1] == -1)
                    count[i][j] = count[i - 1][j];
                else
                    count[i][j] = count[i - 1][j] + count[i][j - 1];
            }
        }
    }
    cout << count[m][n] << endl;
    system("pause");
}