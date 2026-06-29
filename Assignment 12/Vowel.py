def Is_Vowel(C):

    Vowels = ["a", "e", "i", "o", "u"]

    if (C in Vowels):
        print("character is vowel")
    else:
        print("Not a vowel")

def main():

    Char = input("Enter your character : ")

    Ret = Is_Vowel(Char)
    

if __name__ == "__main__":
    main()