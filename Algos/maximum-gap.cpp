class Solution {
public:
    int maximumGap(vector<int>& nums) {

        sort(nums.begin(), nums.end());
        int max = 0;

        for(int i = 1; i < nums.size(); i++ )
        {
            int diff =  nums[i] - nums[i-1];
            if(diff > max)
                max = diff;
        }
        return max;
    }
};
