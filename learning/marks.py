#enter marks of 3 students from user and store them in dictionary. start with empty dictionary and add one by one. use subject as key and marks as value

stud_marks = {}
subject= input("enter subject: ")
#marks= int(input(f"enter marks for {subject}")) # print variable value in input statement
marks= int(input("enter marks for " +str(subject) +": ")) # print variable value in input statement
stud_marks[subject]=marks # stud_marks.update({subject: marks})


subject= input("enter subject: ")
marks= int(input("enter marks for " +str(subject) +": "))
stud_marks[subject]=marks

print(stud_marks)