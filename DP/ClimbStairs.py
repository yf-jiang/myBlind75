def climbStairs(n):
    if n == 1:
        return 1

    else:
        arr = []

        for i in range(n+1):
            arr.append(None)

        arr[n] = 0
        arr[n-1] = 1
        arr[n-2] = 2

        for i in range(n-3, -1, -1):
            arr[i] = arr[i+1] + arr[i+2]

        return arr[0]


n1 = 2
n2 = 3
n3 = 5
print(climbStairs(n1))
print(climbStairs(n2))
print(climbStairs(n3))
