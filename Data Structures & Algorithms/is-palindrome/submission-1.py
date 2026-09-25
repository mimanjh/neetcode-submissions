class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated = [char.lower() for char in s if char.isalnum()]
        
        end = -1
        for c in updated:
            if c != updated[end]:
                return False
            end -= 1
        return True