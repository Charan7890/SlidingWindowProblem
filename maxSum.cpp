
#include <iostream>
#include<climits>

using namespace std;

int maxSum(int a[],int n,int ws){
    int i=0,j=0;
    int max = INT_MIN;
    int sum = 0;
    
    while(j<n){
        //calculation-1
        sum=sum+a[j];
        if(j-i+1<ws){
            j++;
        }
        else if(j-i+1==ws){
        // calculation-2
        if(max<sum){
            max = sum;
        }
        sum = sum - a[i];
            i++;
            j++;
        }
    }
    return max;
}

int main()
{
    int n,ws;
    cin>>n;
    
    int *a = new int[n];
    
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    
    cin>>ws;
    
    int res = maxSum(a,n,ws);
    
    cout<<res;

    return 0;
}

