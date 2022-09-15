def numDecodings(s):
    dp = {len(s): 1}

    for i in range(len(s)-1, -1, -1):

        if s[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

        if (i + 1 < len(s) and (s[i] == '1' or
                                (s[i] == '2' and s[i + 1] in '0123456'))):
            dp[i] = dp[i] + dp[i + 2]
        print(dp)

    return dp[0]


def forwardNumDecodings(s):
    dp = {-1: 1}

    for i in range(len(s)):
        if s[i] == '0':
            dp[i] = 0

        else:
            dp[i] = dp[i - 1]

        if i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] in '0123456')):
            dp[i] = dp[i] + dp[i - 2]
    print(dp)
    return dp[len(s) - 1]


def recurNumDecodings(s):
    dp = {len(s): 1}

    def dfs(i):
        if i in dp:
            return dp[i]

        if s[i] == '0':
            return 0

        res = dfs(i + 1)
        if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
            res += dfs(i + 2)

        return res

    return dfs(0)


s1 = "12"
s2 = "226"
s3 = "06"
error1 = "0"
error2 = "10"
error3 = "2101"
error4 = "1201234"
error5 = "1123"
error6 = "207"
# print(numDecodings(s1))
# print(numDecodings(s2))
# print(numDecodings(s3))
# print(numDecodings(error1))
# print(numDecodings(error2))
# print(numDecodings(error3))
# print(numDecodings(error4))
# print(numDecodings(error5))
# print(numDecodings(error6))

print(forwardNumDecodings(error4))
