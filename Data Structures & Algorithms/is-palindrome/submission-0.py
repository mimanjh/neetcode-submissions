class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated = [char.lower() for char in s if char.isalnum()]
        return updated == updated[::-1]