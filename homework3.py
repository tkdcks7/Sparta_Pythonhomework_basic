class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
    def display(self):
        print("사용자명: ", self.name, " ID: ", self.username)
    

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


user1 = Member('뽀로로', '펭귄맨', 1111)
user2 = Member('크롱', '둘리', 2222)
user3 = Member('루피', '군침이', 3333)
user4 = Member('에디','티벳여우',4444)

members = []
members.append(user1)
print(members[0].name)