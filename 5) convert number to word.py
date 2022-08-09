numbers={"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
n=input("Enter the number: ")
int_n=int(n)
if(int_n>=1 and int_n<=9):
    print(numbers[n])
else:
    print("please enter a number range 1-9")

