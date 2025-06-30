import java.util.HashMap;

class Solution {
    public int findLHS(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int ans = 0;
        
        // First loop to populate the HashMap
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        // Second loop to find the longest harmonious subsequence
        for (int num : map.keySet()) {
            if (map.containsKey(num + 1)) {
                ans = Math.max(ans, map.get(num) + map.get(num + 1));
            }
        }
        
        return ans;
    }
}
