'''
class(blueprint)
attributes/properties
1.states/variables
class,instance variables

2.Methods
    i. class methods
    ii. instance method
            i. normal instance methods
            ii. special/magic methdos (default 29 magic methods are created when creating a class)

3.static method
'''
#class creation
# class KIIT:
#     pass
# obj=KIIT()
# print(dir(obj))

#class creation with values:
# class new:
#     def __init__(self,a): # init is used to initialize the instance variable, self stores the address of the object
#         self.a=a
# obj=new()  
# class myclass:
#     def __init__(self,a):
#         print(self,a)
# obj=myclass(10)
# obj2=myclass()

# class new:
#     var_c="new class"
#     def __init__(self,a):
#         self.a=a
# obj1=new(10)
# print(obj1.a)

# class new:
#     var1="new class"
#     def __init__(self,a):
#         self.a=a
#         print(self.a)
#         # print(a,self.a) # not possible
# obj=new(10)
# obj1=new(11)
# print(obj.a)

# class stud_detail:
#     name="Student details"
#     def init(self,name,regno):
#         self.name=name
#         self.regno=regno
#     def get_details(self):
#         print(f"name : {self.name}\nRegno :{self.regno}")
#     def update(self,name):
#         self.name=name
# obj=stud_detail("Jarvis",111222)
# obj.get_details()
# obj=stud_detail("Vipul",333555)
# obj.get_details()

# #class instagram
# initialize 
# three instance methods:follow
# unfollow,details

# step1:you have to create an account with username,acc_pwd of three users.and after creating this you have to do the instance method
# where 1->follows 2
# display the followers count and following count for 1.
# follow request from 1-3
# dispaly the followers count and following count for 1.
# request from 3-1
# same for unfollow
#again dispaly the details of the three accounts.
#use access specifiers 
class Instagram:
    def __init__(self, username, acc_pwd):
        self.username = username                     
        self.__password = acc_pwd                    
        self._followers = set()                      
        self._following = set()                      

    def follow(self, other):
        if self.username not in other._followers:
            other._followers.add(self.username)
            self._following.add(other.username)
            print(f"{self.username} followed {other.username}")
        else:
            print(f"{self.username} already follows {other.username}")

    def unfollow(self, other):
        if self.username in other._followers:
            other._followers.remove(self.username)
            self._following.remove(other.username)
            print(f"{self.username} unfollowed {other.username}")
        else:
            print(f"{self.username} is not following {other.username}")

    def get_details(self):
        print(f"\nUsername: {self.username}")
        print(f"Followers count: {len(self._followers)}")
        print(f"Following count: {len(self._following)}")

# Step 1: Create three accounts
acc1 = Instagram("user1", "pass1")
acc2 = Instagram("user2", "pass2")
acc3 = Instagram("user3", "pass3")

# Step 2: user1 follows user2
acc1.follow(acc2)

# Display followers and following for user1
print("\n--- Details after user1 follows user2 ---")
acc1.get_details()

# Step 3: user1 follows user3
acc1.follow(acc3)

# Display followers and following for user1 again
print("\n--- Details after user1 follows user3 ---")
acc1.get_details()

# Step 4: user3 follows user1
acc3.follow(acc1)

# Step 5: Unfollow steps
acc1.unfollow(acc2)
acc3.unfollow(acc1)

# Step 6: Display details of all users
print("\n--- Final Account Details ---")
acc1.get_details()
acc2.get_details()
acc3.get_details()
