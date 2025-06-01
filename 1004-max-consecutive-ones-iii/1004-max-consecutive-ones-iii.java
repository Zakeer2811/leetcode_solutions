class Solution {
    public int longestOnes(int[] nums, int k) {
        int cnt=0;
        int len=0,maxlen=0;
        int l=0,r=0;
        while(r<nums.length){
            if(nums[r]==0){
                cnt++;
            }
            if(cnt>k){
                if(nums[l]==0){
                    cnt--;
                }
                l++;
            }
            if(cnt<=k){
                len=r-l+1;
                maxlen=Math.max(len,maxlen);
            }
            r++;
        }
        return maxlen;
        
    }
}