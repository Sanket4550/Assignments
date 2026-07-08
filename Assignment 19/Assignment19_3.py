from functools import reduce

def operations():
    n = int(input("Enter number of elements: "))

    lst = []
    for i in range(n):
        lst.append(int(input()))

    filtered = list(filter(lambda x: 70 <= x <= 90, lst))
    mapped = list(map(lambda x: x + 10, filtered))
    result = reduce(lambda x, y: x * y, mapped)

    print("List after filter =", filtered)
    print("List after map =", mapped)
    print("Output of reduce =", result)

operations()