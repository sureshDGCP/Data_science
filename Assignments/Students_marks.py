'''

Question 6: Take marks from students it could from 0  to 100, if the student scores 0 to 30 its avg, if 30 - 65 its above avg,
65 - 75 its good, and above 75 its best and print the results accordingly

'''

'''
marks = int(input("Please enter your percentage :"))

if (marks >0) and (marks <=30):
    print("Your Grade is Average")
else:
    if (marks >30) and (marks <= 65):
        print("Your Grade is Above Average")
    else:
        if (marks > 65) and (marks <= 75):
            print("Your grade is Good")
        else:
            print("Your Grade is Best!")

'''
# the above example is nested if else example, you can use below for more simplified version


# marks = int(input("Please enter your percentage :"))
#
# if (marks > 0) and (marks <= 30):
#     print("Your Grade is Average")
# elif (marks > 30) and (marks <= 65):
#     print("Your Grade is Above Average")
# elif (marks > 65) and (marks <= 75):
#     print("Your grade is Good")
# else:
#     print("Your Grade is Best!")


marks = int(input("Please enter your percentage :"))

if (marks > 0) and (marks <= 30):
    print("Your Grade is Average")
elif (marks > 30) and (marks <= 65):
    print("Your Grade is Above Average")
elif (marks > 65) and (marks <= 75):
    print("Your grade is Good")
elif (marks > 75) and (marks <= 100):
    print("Your Grade is Best!")
