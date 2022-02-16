#A program to demonstrate working of Extended Euclidean Algorithm
def find(firstNum, secondNum): 




    if firstNum == 0 :  

        return secondNum, 0, 1

            

    output, n, m = find(secondNum % firstNum, firstNum) 

    

    n1 = m - ( secondNum//firstNum ) * n 

    m1 = n 

    

    return output,n1,m1



#this section accepts input from users so as to check their gcd
firstNum = int(input("Enter the first number: "))

secondNum = int(input("Enter the second number: "))

output, n1, m1 = find(firstNum, secondNum) 

print("The gcd({0},{1}) is {2} ".format(firstNum, secondNum ,output))
