class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a,b):
            return a+b
        def sub(a,b):
            return a-b
        def mul(a,b):
            return a * b
        def div(a,b):
            return int(a/b)
        new_sum=0
        stk=[]
        hash_map={
            '+':add,
            '-':sub,
            '*':mul,
            '/':div
        }
        for token in tokens:
            if token in hash_map and stk:
                first_pop=stk.pop()
                second_pop=stk.pop()
                new_sum = hash_map[token](second_pop, first_pop)
                stk.append(new_sum)
            else:
                stk.append(int(token))
        return stk[-1]
             


        