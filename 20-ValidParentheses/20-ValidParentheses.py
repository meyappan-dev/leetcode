class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if(char == '('):
                stack.append(')')
            elif(char == '{'):
                stack.append('}')
            elif(char == '['):
                stack.append(']')
            
            elif len(stack)>0:
                if(char == stack[-1]):
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append('')
        if stack == []:
            return True
        else:
            return False
            