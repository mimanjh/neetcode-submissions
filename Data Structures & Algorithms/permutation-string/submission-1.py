class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        charmap = {}

        for c in s1:
            charmap[c] = charmap.get(c, 0) + 1

        for i in range(len(s2) - n + 1):
            charmapCopy = charmap.copy()

            for j in range(n):
                c = s2[i + j]
                if c not in charmapCopy:
                    break

                charmapCopy[c] -= 1
                
                if charmapCopy[c] == 0:
                    charmapCopy.pop(c)

            if not charmapCopy:
                return True

        return False