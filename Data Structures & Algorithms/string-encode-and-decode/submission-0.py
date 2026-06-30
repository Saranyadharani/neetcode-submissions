class Solution:
    def encode(self, strs):
        """Encodes list of strings to single string."""
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    
    def decode(self, s):
        """Decodes single string back to list."""
        result = []
        i = 0
        
        while i < len(s):
            # Find where # is
            j = i
            while s[j] != '#':
                j += 1
            
            # Get length (number before #)
            length = int(s[i:j])
            
            # Get the actual string
            string_start = j + 1
            string_end = string_start + length
            result.append(s[string_start:string_end])
            
            # Move to next
            i = string_end
            
        return result