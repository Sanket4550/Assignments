from functools import reduce

def operations():
    n = int(input("Enter number of elements: "))

    lst = []
    for i in range(n):
        lst.append(int(input()))

    filtered = list(filter(lambda x: x % 2 == 0, lst))
    mapped = list(map(lambda x: x ** 2, filtered))
    result = reduce(lambda x, y: x + y, mapped)

    print("List after filter =", filtered)
    print("List after map =", mapped)
    print("Output of reduce =", result)

operations()
