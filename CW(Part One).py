#Author-Udana Indumini
#Date-20/11/2022
#Purpose-Grade calculator(SD CW)-Part One
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20221179/w1954023
# Date: 14/12/2022


progress=0 #Used to calculate the no of students who progressed
trailer=0  #Used to calculate the no of students who recieved "Progress(module trailer)"
retreive=0 #Used to calculate the no of students who are module retreivers
exclude=0 #Used to calculate the no of students who got excluded
students=0 #variable to count the no of students
total=0  #Variable used to check whther the total credits is eqaul to 120
colon=":"
switch="y" #Main while loop will run until it changes its value,when the user presses q
    
def marks_input(message):         #Function used for the validation of the marks
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
def dash():   #function used to divide he parts of the program
    print("-"*60)

def decision():
    dash()
    print("Histogram")
    histogram("Progress",progress)
    histogram("Trailer",trailer)
    histogram("Retriever",retreive)            
    histogram("Excluded",exclude)
    print(students,"outcome(s) in total.")
    dash()

def histogram(grade,count):         #Function used to print the histogram
    print(f'{grade:9} {count:3} {colon:2}',end='')
    print('*'*count)

while switch=='y':
    pc=marks_input("\nPlease enter your credits at PASS:" ) #pc-pass credits
    dc=marks_input("Please enter your credits at DEFER:" ) #dc-defer credits
    fc=marks_input("Please enter your credits at FAIL:" ) #fc-fail credits
    total=pc+dc+fc
    if total!=120 :
        print("Total incorrect")
        continue
    elif pc==120:
        print("Progress")
        progress+=1
    elif pc==100:
        print("Progress (module trailer)")        
        trailer+=1
    elif pc>40 or (pc==40 and dc!=0) or (pc==20 and dc>20) or (pc==0 and dc>=60) :
        print("Do not Progress – module retriever ")       
        retreive+=1
    else:
        print("Exclude")        
        exclude+=1
    students+=1
    while True:
        option=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:").lower()
        if option=='y':
            break
        elif option=='q':
            decision()
            switch='n'
            break
        else:
            print("Invalid input,please select 'y' or 'q'")
            continue
            
            
    
