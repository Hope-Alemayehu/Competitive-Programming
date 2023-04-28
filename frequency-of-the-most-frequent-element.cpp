class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
       sort(nums.begin(), nums.end());
       const int n = nums.size();
       long long sum = 0;
       int left = 0, ans = 1;

       for (int right = 1; right < n; right++) {
           sum += (long long)(right - left) * (nums[right] - nums[right - 1]);
           while (sum > k) {
               sum -= nums[right] - nums[left];
               left++;
           }
           ans = max(ans, right - left + 1);
       }
       return ans;
    }
};
