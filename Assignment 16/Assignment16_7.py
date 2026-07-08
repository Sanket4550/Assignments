def ChkDiv(no):
    if no%5 == 0:
        return True 
    else:
        False
def main():
    num = int(input("Enter a number."))
    print(ChkDiv(num))
    if __name__ == "__main__":
        main()

