def func(s):
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
    max_length = 1
    start = 0
    for l in range(2,len(s)+1):
        for i in range(len(s)-l+1):
            end = i+l
            if l==2:
                if s[i] == s[end-1]:
                    dp[i][end-1]=True
                    max_length = l
                    start = i
            else:
                if s[i] == s[end-1] and dp[i+1][end-2]:
                    dp[i][end-1]=True
                    max_length = l
                    start = i
    return s[start:start+max_length]


def main():
    print(func("babad"))
    return


if __name__=="__main__":
    main()
