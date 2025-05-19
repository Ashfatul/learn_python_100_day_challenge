# memo = []
# def fib(n, memo):
#     if n in memo:
#         return memo[n]
#     if n == 1 or n == 2:
#         result = 1
#     else:
#         result = fib(n - 1, memo) + fib(n - 2, memo)
#     memo[n] = result
#     return result

# print(fib(1, memo))


# Memoization
# dictionary = {}

# def fib(n, dictionary):
#     if n in dictionary:
#         return dictionary[n]
#     elif n == 1 or n == 2:
#         result = 1
#     else:
#         result = fib(n-1, dictionary) + fib(n-2,dictionary)
#     return result


# print(fib(10, dictionary))

# Recursion only
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
    
# print(fib(3))


# Tabulation



def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    table = [0] * (n + 1)
    
    table[1] = 1
    table[2] = 1
    
    for t in range(3,n+1):
        table[t] = table[t - 1] + table[t - 2]
    
    return table[n]
print(fib(5))