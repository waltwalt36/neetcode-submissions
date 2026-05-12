# Understand:
#   - Encode a list of strings to a single string
#   - Decode the string back into the list of strings
#   - strs[i] contains any possible characters out of 256 ASCII characters

# Plan:
#   - Encode a character(s) that represent the start of a new string
#   - Encode chars using its ASCII value for simplicity
#   - Encode a special character that represents a seperate string
#   - Initialize encoded: string, which will contain encoded string
#   - Traverse strs and encode each string into encoded
#   - Return string, encoded
#   - Decode takes encoded and decodes back into regular characters
#   - Decode should also identify special character
#   - Return list of decoded strings

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        if not strs:
            return ""

        for i in range(len(strs[0])):
            encoded += str(ord(strs[0][i]))
            encoded += ","
        encoded += "|"

        for i in range(1, len(strs)):
            for j in range(len(strs[i])):
                encoded += str(ord(strs[i][j]))
                encoded += ","
            encoded += "|"

        return encoded

    def decode(self, s: str) -> List[str]:
        current = ""
        string = ""
        result = []

        if s == "":
            return []
        for c in s:
            if c != "," and c != "|":
                current += c
            elif c == ",":
                string += chr(int(current))
                current = ""
            elif c == "|":
                result.append(string)
                string = ""
                
        return result
