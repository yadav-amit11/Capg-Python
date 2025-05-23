#modules n packages
"""
module : .py file
package : collection of files and modules

"""
# import random
# #random
# print(random.random())
# print(random.randint(1,100))
# print(random.choice(["stone","paper","rod"]))
# l=[1,2,3,4,900]
# random.shuffle(l)
# print(l)
#-----------------------------------------------------------------------------
import random
user = input("stone, paper or scissor? ").lower()
comp = random.choice(['stone', 'paper', 'scissor'])
print(f"Computer: {comp}")
if user == comp:
    print("Tie")
elif (user == 'stone' and comp == 'scissor') or (user == 'paper' and comp == 'stone') or (user == 'scissor' and comp == 'paper'):
    print("You win")
else:
    print("You lose")
#------------------------------------------------------------------------------
# import random
# user = int(input("Enter a number (1-6): "))
# comp = random.randint(1, 6)
# print(f"Computer: {comp}")
# if user == comp:
#     print("Out!")
# else:
#     print(f"You scored: {user}")

