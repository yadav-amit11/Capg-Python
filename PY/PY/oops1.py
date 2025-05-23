class InstagramProfile:
    def __init__(self, user_name, password, mail_id):
        self.user_name = user_name          # public (username is usually okay)
        self.__password = password          # private
        self.__mail_id = mail_id            # private
        self.__following = 0                # private
        self.__followers = 0                # private

    # ----------------- Getter Methods -----------------
    def get_following(self):
        return self.__following

    def get_followers(self):
        return self.__followers

    def get_mail_id(self):
        return self.__mail_id

    def get_password(self):
        return "******"  

    # ----------------- Setter Methods -----------------
    def set_password(self, new_password):
        self.__password = new_password

    def set_mail_id(self, new_mail):
        self.__mail_id = new_mail

    # ----------------- Follow Method -----------------
    def follow(self, other_user):
        if self == other_user:
            print("Same user cannot follow themselves")
        elif self.user_name == other_user.user_name:
            print("Username should be different")
        else:
            self.__following += 1
            other_user.__followers += 1  # Accessing private inside class is allowed

    # ----------------- Unfollow Method -----------------
    def unfollow(self, other_user):
        if self == other_user:
            print("Same user cannot unfollow themselves")
        elif self.user_name == other_user.user_name:
            print("Username should be different")
        else:
            if self.__following > 0 and other_user.__followers > 0:
                self.__following -= 1
                other_user.__followers -= 1
            else:
                print("Unable to unfollow")

    # ----------------- Display Info Method -----------------
    def displayinfo(self):
        print(f'Username: {self.user_name}')
        print(f'Password: {self.get_password()}')
        print(f'Mail ID: {self.get_mail_id()}')
        print(f'Followers: {self.get_followers()}')
        print(f'Following: {self.get_following()}')

# ----------------- Example Execution -----------------
user1 = InstagramProfile("User1", "User_123", "user1@gmail.com")
user2 = InstagramProfile("User2", "1234", "user2@gmail.com")
user3 = InstagramProfile("User3", "1234", "user3@gmail.com")

print("Follow")
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user3.follow(user1)

print("\nStart..")
user1.displayinfo()
print("---------------------------------------")
user2.displayinfo()
print("---------------------------------------")
user3.displayinfo()

