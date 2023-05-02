class Solution {
public:
     int maxCoins(vector<int>& piles) {
        
   
     sort(piles.begin(),piles.end());
        int n=piles.size();
        int ans=0;
        for(int i=n/3;i<n;i=i+2)
            ans+=piles[i];
        return ans;
    }
int main() 
{ 
 vector<int> arr = { 9,8,7,6,5,1,2,3,4 }; 
 cout<<maxCoins(arr)<<endl; 
 return 0;

}
};
