def longestCommonSubsequence(text1, text2):
    dpArr = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(1, len(text1)+1):
        for j in range(1, len(text2)+1):
            if text1[i-1] == text2[j-1]:
                dpArr[i][j] = 1 + dpArr[i-1][j-1]

            else:
                dpArr[i][j] = max(dpArr[i-1][j], dpArr[i][j-1])

    return dpArr[-1][-1]


text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1, text2))
text1 = "abc"
text2 = "abc"
print(longestCommonSubsequence(text1, text2))
text1 = "abc"
text2 = "def"
print(longestCommonSubsequence(text1, text2))