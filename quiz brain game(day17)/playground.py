class User:
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1




        
        

user_1 = User("009","kirti")
user_2 = User("007","singh")
# user_1.id = "009"
# user_1.user_name = "kirti"

# print(user_1.name)
# print(user_1.id)
# print(user_2.name)
# print(user_2.id)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
# user_2 = User()
# user_2.id = "007"
# user_2.user_name = "singh"