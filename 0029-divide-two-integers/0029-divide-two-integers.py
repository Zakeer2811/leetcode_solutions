class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=True
        cnt=ans=0
        sign=(dividend<0) ^ (divisor<0)
        numerator=abs(dividend)
        denominator=abs(divisor)
        while(numerator>=denominator):
            cnt=0
            while(denominator<<(cnt+1)<=numerator):
                cnt+=1
            numerator=numerator-(denominator*(1<<cnt))
            ans+=(1<<cnt)
       
        
        if ans>2**31 and sign==False:
            return -2**31
        if ans>2**31 and sign==True:
            return 2**31
        if sign:
            ans=-ans
        return ans