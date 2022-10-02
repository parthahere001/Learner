#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        ll n;
        cin>>n;
        ll sum=0;
        ll cz=0;
        for (ll i=0;i<n-1;i++)
        {
            ll j;
            cin>>j;
            sum+=j;
            if(j==0)
            cz++;

        }
        int l;
        cin>>l;
        if(sum==0)
        {
            cout<<"0\n";
        }
        else
        cout<<sum+cz<<"\n";
    }
  
 return 0;
}