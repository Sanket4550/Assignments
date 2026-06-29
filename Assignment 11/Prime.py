def is_prime(n):
    if n <= 1:  
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    No = int(input("Enter number : "))
    
    Ret = is_prime(No)

    if Ret:
        print("Prime")
    else:
        print("Non prime")

if __name__ == "__main__":
    main()