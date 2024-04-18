#Author-Udana Indumini
#Date-20/11/2022
#Purpose-Grade calculator(SD CW)-Part Four
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20221179/w1954023
# Date: 14/12/2022

total=0 #Variable used to check whther the total credits is eqaul to 120
result='' #Progression outcome will be stored in this variable and will be used to store in the list2
marks={}
switch=0 #Main while loop will run until switch changes its value 

def marks_input(message):         #Function used for the valdation of the marks
    while True:
        try:
            no=int(input(message))
        except ValueError:
            print("\nInvalid input,an integer is required...Please try again")
        else:
            if no%20==0 and (no<121 and no>=0):
                return no
            else:
                print("Out of range")
                continue
def dash():
    print('-'*60)
while switch==0:
    ID=input("Please enter your student ID:")
    if ID=='':
        print("Incorrect ID,please enter your ID again")
        continue
    else:
        pc=marks_input("\nPlease enter your credits at PASS:" ) #pc-pass credits
        dc=marks_input("Please enter your credits at DEFER:" ) #dc-defer credits
        fc=marks_input("Please enter your credits at FAIL:" ) #fc-fail credits
        total=pc+dc+fc
        if total!=120 :
            print("Total incorrect")
            continue        
        elif pc==120:
            print ("Progress")
            result="Progress"
        elif pc==100:
            print("Progress (module trailer)")
            result="Progress (module trailer)"
        elif pc>40 or (pc==40 and dc!=0) or (pc==20 and dc>20) or (pc==0 and dc>=60) :
            print("Do not Progress – module retriever ")
            result="Module retriever"
        else:
            print("Exclude")
            result="Exclude"
        marks[ID]=result,pc,dc,fc
        ID=''
    while switch==0:
        option=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:").lower()    
        if option=='y':
            break
        elif option=='q':
            dash()
            print ("Part Four:\n")
            for key in marks:
                print (f'{key}:{marks[key][0]}-{marks[key][1]},{marks[key][2]},{marks[key][3]}')
                switch=1
        else:
            print("Invalid input,please select 'y' or 'q'")
            continue

            
    
