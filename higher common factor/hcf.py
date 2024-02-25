#This program prompts a user to enter two
#integers. It works out the higher common factor(HFC)
#of the two numbers and outputs the result

def find_hcf(a, b):
    if a < b:
        #we only need to check for a factor up to half of the number
        for i in range(1,int(b/2+1)):
            if a % i == 0 and b % i == 0: # a and b must be divisible by i
                hcf = i #updates hcf when a bigger common factor is found
    elif a > b:
        for i in range(1,int(a/2+1)):
            if b % i == 0 and a % i == 0:
                hcf = i        
    else:
        hcf = a
        
    return hcf
try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
except ValueError:
    print("Invalid input")
    
print(f"The hcf of {first_number} and {second_number} is {find_hcf(first_number,second_number)}")
