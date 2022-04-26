class Solution {
public:
    int maxArea(vector<int>& height) {
        int start = 0;
        int end = height.size() - 1;
        int ans = 0;
        int length = 0;
        int width = 0;
        int curr = 0;
            
        while(start < end){
            length = min(height[start], height[end]);
            width = end - start;
            curr = length * width;
            ans = max(ans, curr);
            if(height[start] > height[end]){
                end--;
            }
            else{
                start++;
            }
        }
        return ans;
    }
};