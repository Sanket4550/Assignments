Circle_Area = lambda R, P: P * (R * R)



def main():


    Radius = float(input("Enter radius : "))

    Pi = 3.14


    Ret = Circle_Area(Radius,Pi)
    print("Area of a circle is : ",Ret)
    

if __name__ == "__main__":
    main()