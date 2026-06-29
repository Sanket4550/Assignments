def Even(No):
    
   for i in range(1,No + 1):
        if (i % 2 == 0):
            print(i, end = " ")
    
      
def main():
    Num = int(input("Enter a number : "))

    Ret = Even(Num)
    

if __name__ == "__main__":
    main()