class Solution {
public:
    int hIndex(std::vector<int>& citations) {
        int n = citations.size();
        
        // Step 1: Sort citations in descending order
        std::sort(citations.begin(), citations.end(), std::greater<int>());

        int h_index = 0;
        
        // Step 2: Find the maximum h such that citations[h] >= h + 1
        for (int i = 0; i < n; i++) {
            if (citations[i] >= i + 1) {
                h_index = i + 1;
            } else {
                break;
            }
        }
        
        return h_index;
    }
};