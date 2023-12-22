class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        for i in s:
            if self.isVowel(i):
                stack.append(i)

        # Now, replace.
        for (i, item) in enumerate(s):
            if self.isVowel(item):
                new_char = stack.pop()
                s = s[:i] + new_char + s[i+1:]

        return s


    def isVowel(self, c) -> bool:
        if c.lower() == 'a':
            return True
        elif c.lower() == 'e':
            return True
        elif c.lower() == 'i':
            return True
        elif c.lower() == 'o':
            return True
        elif c.lower() == 'u':
            return True

        return False
