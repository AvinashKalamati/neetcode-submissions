class Solution:
    def isValid(self, s: str) -> bool:
        valid_map={
            '}':'{',
            ']':'[',
            ')':'('}
        stk =[]
        for c in s:
            if c not in valid_map:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped=stk.pop()
                    if popped!=valid_map[c]:
                        return False
        return not stk 
                    