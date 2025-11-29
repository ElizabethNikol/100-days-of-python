# Problem 1: Python If-Else
def if_else_solution(n):
    if n % 2 == 1:
        print("Weird")
    elif n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")

# Problem 2: Arithmetic Operators
def arithmetic_operators(a, b):
    print(a + b)
    print(a - b)
    print(a * b)

# Problem 3: Division
def division(a, b):
    print(a // b)
    print(a / b)


# Problem 4: Loops

for i in range(0, n):
    print(i**2)

# Problem 5: Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    first_max = -100
    for i in range(n):
        if arr[i] > first_max:
            first_max = arr[i]
    
    second_max = -100
    for i in range(n):
        if arr[i] > second_max and arr[i] < first_max:
            second_max = arr[i]
    
    print(second_max)
