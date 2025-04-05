class Solution {
    // Modify the method to accept int[] instead of List<Integer>
    public boolean isPossible(int[] bloomDay, int mid, int m, int k) {
        int cnt = 0; // Count of consecutive flowers that have bloomed by day 'mid'
        int no_of_boq = 0; // Number of bouquets we can make

        // Iterate over the bloomDay array to check each flower's blooming day
        for (int i = 0; i < bloomDay.length; i++) {
            if (bloomDay[i] <= mid) { // Flower has bloomed by 'mid' day
                cnt++; // Increment count of consecutive blooming flowers
            } else {
                no_of_boq += (cnt / k); // Form bouquets with groups of 'k' flowers
                cnt = 0; // Reset count for the next group of flowers
            }
        }
        
        // Add bouquets formed from the last group of consecutive flowers
        no_of_boq += (cnt / k);
        
        // Check if we can form at least 'm' bouquets
        return no_of_boq >= m;
    }

    // Modify this method to accept an int[] as the first argument
    public int minDays(int[] bloomDay, int m, int k) {
        // If the total number of flowers needed for m bouquets is more than the available flowers, return -1
        if ((double)m * k > bloomDay.length) {
            return -1;
        }

        // Binary search for the minimum day 'mid' where we can make 'm' bouquets
        int low = Integer.MAX_VALUE; // Initialize low as the minimum possible day
        int high = Integer.MIN_VALUE; // Initialize high as the maximum possible day

        // Find the minimum and maximum blooming days in the array
        for (int day : bloomDay) {
            low = Math.min(low, day); // Minimum day
            high = Math.max(high, day); // Maximum day
        }

        // Binary search for the minimum possible day that can allow making m bouquets
        while (low <= high) {
            int mid = low + (high - low) / 2; // Find the middle day

            if (isPossible(bloomDay, mid, m, k)) { // If we can form m bouquets by 'mid' day
                high = mid - 1; // Try to find an earlier day (lower day)
            } else {
                low = mid + 1; // If not, try a later day (higher day)
            }
        }

        // The answer will be the first day where we can form at least 'm' bouquets
        return low;
    }
}
