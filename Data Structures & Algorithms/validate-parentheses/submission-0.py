class Solution():
    def isValid(self, s: str):  # Added 'self' parameter
        stack = []
        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Process each character
        for char in s:
            if char in '({[':  # Opening bracket
                stack.append(char)
            else:  # Closing bracket
                # Check if stack is empty
                if not stack:
                    return False
                
                # Check if top matches
                if stack[-1] == matching[char]:
                    stack.pop()
                else:
                    return False
        
        # Final check
        return len(stack) == 0