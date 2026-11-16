# @leetcode slug=decode-string id=394 qid=394
# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        ansStr = []

        for i in range(len(s)):
            if s[i] == "]":
                tempStr = []

                while ansStr[-1] != "[":
                    tempStr.append(ansStr.pop())

                tempStr = tempStr[::-1]

                ansStr.pop()
                
                #pop untill number to to get k. 
                k = []

                while ansStr and ansStr[-1].isdigit():
                    k.append(ansStr.pop()) 

                k = k[::-1]


                answerString = tempStr * int("".join(k))
                print(answerString)
                ansStr.extend(answerString)
            else:
                ansStr.append(s[i])

        return "".join(ansStr)