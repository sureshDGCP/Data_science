'''
Question 1 :
take an input from user and try to generate the output in given format:
also take the repetition number from user
e.g. input = Python, repetition no = 3
output should be like:

    ***Python***
'''

input_text = input("Please provide your text:")
#print(input_text)
reps_no = input("Please provide Number of '*' :")
#print(reps_no)

astricks = "*"*int(reps_no)
#print(astricks)

print(f"{astricks}{input_text}{astricks}")


'''

Question 2:
Take input from user and print no of characters present in string

'''
input_string = input("Enter your string or sentence:")
print(len(input_string))


'''

Question 3:
take an input from user which contains 11 characters, print 2 lines first will be all the characters present in even indices
like 0, 2, 4, 6, 8, 10 and 2nd print should contain all the odd characters from input string.

12345678910
135790
24681

'''
input_string = input("Enter your string or sentence:")
print(len(input_string))

#print(input_string[0]+input_string[2]+input_string[4]+input_string[6]+input_string[8]+input_string[10])
#print(input_string[1]+input_string[3]+input_string[5]+input_string[7]+input_string[9])


print(input_string[::2])  # Even indices: 0, 2, 4, .... "2" in the [::2] is used to set the how many letters you want to skip
print(input_string[1::2])
# for ::2 what happens is start = 0 and then 0+2 = 2 , 2+2= 4, and so on ....
# for 1::2 what happens here is start is 1 then 1+2=3, 3+2=5, and so on.....

s = "aeronautical"
print(s[3::3])      # 3, 3+3=6, 6+3=9, 9+3=12  ouc
print(s[0:7:2] )   # 0, 0+2=2,2+2=4, 4+2=6 arnu
print(s[0::5])      # 0, 0+5=5, 5+5=10    aaa
