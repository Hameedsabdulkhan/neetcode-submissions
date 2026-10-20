class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stk=[]
        ans=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stk and stk[-1][0]<t:
                stk_k,stk_i=stk.pop()
                ans[stk_i]=i-stk_i
            stk.append((t,i))
        return ans