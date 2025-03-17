class Solution {
public:
    bool divideArray(vector<int>& nums) {
        unordered_map<int, int> freq;
        int n = nums.size();
        int p = n / 2, ispair = 0;

        for (int num : nums) {
            freq[num]++;
        }

        for (auto& pair : freq) {
            if (pair.second % 2 == 0) {
                ispair += pair.second / 2;
            }
        }

        return ispair == p;
    }
};
