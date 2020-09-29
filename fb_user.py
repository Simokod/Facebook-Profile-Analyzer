class FBUser:
    def __init__(self, url, age, total_friends, mutual_friends, posts):
        self.url = url
        self.age = age
        # self.friendship_duration = friendship_duration
        self.total_friends = total_friends
        self.mutual_friends = mutual_friends
        self.posts = posts
