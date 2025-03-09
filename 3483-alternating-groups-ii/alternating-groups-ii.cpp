class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int maxLen=1,ans=0,n=colors.size();
        for(int i=0;i<n-1+k-1;i++){
            if(colors[i%n] != colors[(i-1+n)%n]){
                maxLen++;
            }
            else{
                maxLen=1;
            }
            if (maxLen>=k){
                ans++;
            }
        }
        return ans;
    }
};