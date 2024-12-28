class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for string in path:
            if string == '' or string == '.':
                continue
            if stack and string == '..':
                _ = stack.pop()
            elif string != '..':
                stack.append(string)
                
        pathString = "/".join(stack)
        
        return f"/{pathString}"
                
            
                
                
        
        
        