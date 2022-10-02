#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{ int t;
cin>>t;
while(t--)
{
    ll n;
    
    cin>>n;
    if (n%2==0)
    { ll arr[n];
    cin>>arr[0];
    cin>>arr[1];
    ll count1=0;
    ll counta1=0;
    ll counta2=0;
    ll count2=0;
    
    for (int i=2;i<n;i++)
    {
        cin>>arr[i];
        if ((i-1)%2!=0)
            {
                int maxi = max(arr[i-2],arr[i]);
                if (arr[i-1]<=maxi)
                count1+=(maxi-arr[i-1]+1);
                else
                counta1++;
                
            }
        else
        {

            int maxi = max(arr[i-2],arr[i]);
                if (arr[i-1]<=maxi)
                count2+=(maxi-arr[i-1]+1);
                else
                counta2++;

        }
        


    }
    //cout<<"#"<<counta1<<" "<<counta2<<endl;
    int k;
    if (n-2 == 1)
    k=1;
    else k=(n-2)/2;
    if (counta1 + counta2 >= k)
      cout<<"0\n";
    
    else
    cout<<min(count1,count2)<<"\n";
  










    }
    else
    { ll arr[n];
    cin>>arr[0];
    cin>>arr[1];
    ll count=0;
        for (int i=2;i<n;i++)
        {
            cin>>arr[i];
            if ((i-1)%2!=0)
            {
                int maxi = max(arr[i-2],arr[i]);
                if (arr[i-1]<=maxi)
                count+=(maxi-arr[i-1]+1);
                
            }
        }
        cout<<count<<"\n";

    }

}
  
 return 0;
}