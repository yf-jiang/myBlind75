def wordBreak(s, wordDict):
    dpArr = [False] * len(s) + [True]

    for i in range(len(s)-1, -1, -1):
        for word in wordDict:
            if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                dpArr[i] = dpArr[i + len(word)]

            if dpArr[i]:
                break

    return dpArr[0]


s1 = "leetcode"
wordDict1 = ["leet", "code"]
s2 = "applepenapple"
wordDict2 = ["apple", "pen"]
s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s1, wordDict1))
print(wordBreak(s2, wordDict2))
print(wordBreak(s3, wordDict3))
