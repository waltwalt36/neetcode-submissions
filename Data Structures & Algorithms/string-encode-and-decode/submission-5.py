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
        encoded = []

        if not strs:
            return ""

        for i in range(len(strs[0])):
            encoded.append(str(ord(strs[0][i])))
            encoded.append(",")
        encoded.append("|")

        for i in range(1, len(strs)):
            for j in range(len(strs[i])):
                encoded.append(str(ord(strs[i][j])))
                encoded.append(",")
            encoded.append("|")

        encoded = "".join(encoded)

        return encoded

    def decode(self, s: str) -> List[str]:
        current = []
        string = []
        result = []

        if s == "":
            return []
            
        for c in s:
            if c != "," and c != "|":
                current.append(c)
            elif c == ",":
                string.append(chr(int("".join(current))))
                current.clear()
            elif c == "|":
                result.append("".join(string))
                string.clear()

        return result
