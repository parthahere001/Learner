#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        long long arr[n+1];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        sort(arr, arr + n);
        arr[n + 1] = -5;
        int dcount = 0;
        for (int i = 1; i < n; i++)
        {
            if ((arr[i - 1] != arr[i]) && (arr[i + 1] != arr[i]))
                dcount++;
        }

        if (arr[0] != arr[1])
            dcount++;
        if (arr[n - 1] != arr[n] && n != 1)
            dcount++;
        cout << "#" << dcount;
        cout << (dcount + 1) / 2 << "\n";
    }

    return 0;
}