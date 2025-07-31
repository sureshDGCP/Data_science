# ================================== Nested Loops =======================================
"""
They are loop inside loop
e.g.

"""

# for i in range(5):      # 0,1,2,3,4
#     print("This is outer loop")
#     print(f"This is {i}")
#     for j in range(10):     # 0 1, .... 9
#         print("This is inner loop")
#         print(f"{i}*{j} = {i*j}")
#

# ============================================ Control statements =====================

"""
They are "break" and "continue"

break exits the loop and continue skips the iteration. 
"""


num = int(input("PLease enter start no: "))

# for no in range(num):
#     print(no)


#
# for no in range(num):
#     if no != 3:
#         print(no)
#     else:
#         break

for no in range(num):
    if no == 3:
        break
    print(no)


for no in range(num):
    if no == 3:
        continue            # skips the specific condition value but runs for all the rest iterations
    print(no)


for no in range(num):
    if no == 3:
        print(no)
    else:
        pass                # this opposite of continue. 

