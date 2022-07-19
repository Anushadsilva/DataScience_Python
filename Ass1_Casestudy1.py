#1.Write a program which will find factors of given number and find whether the factor is even or odd.Hint:
#use Loop with if-else statements


if __name__ == '__main__':

    x = int(input("Enter the number to find the factor"))
    for i in range(1, x+1):
        if x%i == 0:
            print( "{}".format(i))
            if i%2 ==0:
                print("The number is even")
            else:
                print("The number is odd")