#include<bits/stdc++.h>
using namespace std;
int fun()
{
     long long int n,x,k;
        cin>>n>>x;
        k=n*2;
        long long int arr[k];
        for (int i=0;i<k;i++)
        {
            cin>>arr[i];
        }

        sort (arr,arr+k);
        int j=n;
        for (int i=0;i<n;i++)
        {
            if ((arr[j]-arr[i])<x)
            {
                cout<<"NO\n";
                return 0;
            }
            j++;
        }
        cout<<"YES\n";
        return 0;

}

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
       fun();
    }
  
 return 0;
}