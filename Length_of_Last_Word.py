class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Initializing length to 0 to keep the count of the length of the word encountered
        length = 0
        # Removing the leading and trailing white spaces
        x = s.strip()
        # Looping through the length of the string
        for i in range(len(x)):
            # Whenever a space is encountered we reset the length to 0
            if x[i] == " ":
                length = 0
            # Whenever a character is encountered we increment the length by 1
            else:
                length += 1
        return length