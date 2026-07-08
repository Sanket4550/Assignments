def AcceptNumber():
    print("Enter a number")
    No = int(input())
    return No

def Display(Result):
    print("Result is :", Result)

def main():
    Value = AcceptNumber()

    Power = lambda A: A ** 2

    Ans = Power(Value)

    Display(Ans)

if __name__ == "__main__":
    main()