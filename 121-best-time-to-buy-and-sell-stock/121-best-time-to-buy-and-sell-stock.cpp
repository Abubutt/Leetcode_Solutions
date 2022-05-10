class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int start = 0;
        int end = 1;
        int size = prices.size();
        int maxProfit = 0;
        int currProfit = 0;
            
        while(end < size){
            if(prices[start] > prices[end]){
                start = end;
            }
            else{
                currProfit = prices[end] - prices[start];
                maxProfit = max(maxProfit, currProfit);
            }
            end++;
        }
        return maxProfit;
            
        
    }
};