# 1768. Merge Strings Alternately
"""
You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, 
append the additional letters onto the end of the merged string. Return the merged string.
"""
 
"""
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

"""


class Solution(object):
    def mergeAlternately(self, word1, word2):
        result= ""
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1,n2)
        for i in range(n):
            result += word1[i] + word2[i]
            print(result)
        if n1 == n2 :
            return result 
        elif n1 > n2:
            return result + word1[n:]
        return result + word2[n:]

s1 = Solution()
print(s1.mergeAlternately('abc','pqr')) #Output := apbqcr