#Author-Udana Indumini
#Date-20/11/2022
#Purpose-Grade calculator(SD CW)-Part TWO

progress=0 #Used to calculate the no of students who progressed
trailer=0  #Used to calculate the no of students who recieved "Progress(module trailer)"
retreive=0 #Used to calculate the no of students who are module retreivers
exclude=0 #Used to calculate the no of students who got excluded
students=0 #variable to count the no of students
total=0  #Variable used to check whther the total credits is eqaul to 120
reesult='' #Progression outcome will be stored in this varibale and will be used to store in the list2
list2=[]  #Nested list to store the marks and progression outcome
colon=":"
switch="yes" #Used to end the while loop once the user enters q

    
def marks_input(message): #Function used for the validation of the marks
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
    print("-"*40)

def decision():
    while True:
        option=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:").lower()
        if option=='y':
            break
        elif option=='q':
            dash()
            print("Histogram")
            histogram("Progress",progress)
            histogram("Trailer",trailer)
            histogram("Retriever",retreive)            
            histogram("Excluded",exclude)
            print(students,"outcome(s) in total.")
            dash()
            return option
            break
        else:
            print("Invalid input,please select 'y' or 'q'")
            continue
            
def histogram(grade,count):         #Function used to print the histogram
    print(f'{grade:9} {count:3} {colon:3}',end='')
    print('*'*count)

while switch=="yes":
    pc=marks_input("\nPlease enter your credits at PASS:" ) #pc-pass credits
    dc=marks_input("Please enter your credits at DEFER:" ) #dc-defer credits
    fc=marks_input("Please enter your credits at FAIL:" ) #fc-fail credits
    total=pc+dc+fc
    if total!=120 :
        print("Total incorrect")
        option2=decision()
        continue
    elif pc==120:
        print("Progress")
        result="Progress"
        progress+=1
    elif pc==100:
        print("Progress (module trailer)")
        result="Progress (module trailer)"
        trailer+=1
    elif pc>40 or (pc==40 and dc!=0) or (pc==20 and dc>20) or (pc==0 and dc>=60) :
        print("Do not Progress – module retriever ")
        result="Module retriever"
        retreive+=1
    else:
        print("Exclude")
        result="Exclude"
        exclude+=1
    students+=1    
    list2.append([result,pc,dc,fc])
    option2=decision()

    while option2=='q':
        print("Part Two(Lists):")
        for item in list2:
            print (item[0],"-",str(item[1])+","+str(item[2])+","+str(item[3]))
        dash()
        switch='no'
        break
    
        
       

           
