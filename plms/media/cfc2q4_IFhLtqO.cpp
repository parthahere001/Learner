#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,c,q;
        cin>>n>>c>>q;
        string s;
        cin>>s;
        for (int i=0;i<c;i++)
        { int a,b;
        cin>>a>>b;
            s=s+s.substr((a-1),(b-a+1));

        }
        for(int i=0;i<q;i++)
        {
            int k;cin>>k;
            cout<<s[(k-1)]<<"\n";
        }
    }
    
  
 return 0;
}