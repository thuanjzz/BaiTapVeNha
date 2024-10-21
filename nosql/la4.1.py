
from pymongo import MongoClient
from datetime import datetime


# Buoc 1: Ket noi den MongoDB
client = MongoClient("mongodb://LocalHost:27017/")
db = client['facebookData01']
# Xoa database
client.drop_database("facebookData01")

# Buoc 2 Tao collections
users_collection = db["users"]
posts_collection = db["posts"]
comments_collection = db["comments"]

# Buoc 3 Them du lieu vao users_collection
users_data = [
    { 'user_id': 1, 'name': "Nguyen Van A", 'email': "a@gmail.com", 'age': 25 },
    { 'user_id': 2, 'name': "Tran Thi B", 'email': "b@gmail.com", 'age': 30 },
    { 'user_id': 3, 'name': "Le Van C", 'email': "c@gmail.com", 'age': 22 }
]
users_collection.insert_many(users_data)

# Them du lieu posts_collection
posts_data = [
    { "comment_id": 1, "post_id": 1, "user_id": 2, "content": "Thật tuyệt vời!", "created_at": datetime(2024,10,1) },
    { "comment_id": 2, "post_id": 2, "user_id": 3, "content": "Mình cũng muốn xem bộ phim này!", "created_at": datetime(2024,10,2) },
    { "comment_id": 3, "post_id": 3, "user_id": 1, "content": "Cảm ơn bạn!", "created_at": datetime(2024,10,3) }
]
posts_collection.insert_many(posts_data)

# Them du lieu cho comments_collection
comments_data = [
    { 'comment_id': 1, 'post_id': 1, 'user_id': 2, 'content': 'Thật tuyệt vời!', 'created_at': datetime(2024,10,1) },
    { 'comment_id': 2, 'post_id': 2, 'user_id': 3, 'content': 'Mình cũng muốn xem bộ phim này!', 'created_at': datetime(2024,10,2) },
    { 'comment_id': 3, 'post_id': 3, 'user_id': 1, 'content': 'Cảm ơn bạn!', 'created_at': datetime(2024,10,3) }
]

comments_collection.insert_many(comments_data)
# Buoc 5 Truy van du lieu

#5.1 Xem tat ca noi dung nguoi dung
print("Tat ca nguoi dung")
#for user in users_collection.find():
#    print(user)

# 5.2 Xem tat ca bai dang cua nguoi dung vs user_id =1
print("Bai dang cua user_id = 1")
# user_id = users_collection.find({"user_id":1})
# for user in user_id:
#     print(user)

# 5.3Xem tat ca binh luan cho bai dang posy_id = 1
print("Binh luan cho bai dang voi post_id =1")
# post_id = comments_collection.find({"post_id":1})
# for user in post_id:
#     print(user)


# 5.4 Truy van co do tuoi tren 25
print("Nguoi co do tuoi tren 25")
# ages = users_collection.find({"age":{"$gt":25}})
# for age in ages:
#     print(age)

# 5.5 Truy van tat ca bai dang tao trong thang 10
print("Bai dang trong thang 10")
# create_posts =  posts_collection.find(
#     {"created_at":{'$gt': datetime(2024,10,1),'$lt':datetime(2024,11,1)}}
#     )
# for post in create_posts:
#     print(post)

# 5.6 Cap nhat va xoa du lieu
# Cap nhat noi dung cua bai dang cua nguoi dung cos post_id =1
print("Cap nhat user co post_id = 1")
# updated_user = posts_collection.update_one({"post_id":1}, {"$set":{"content":"Hôm nay thời tiết thật đẹp!"}})
# for post in posts_collection.find():
#     print(post)

# 5.7Xoa binh luan voi comment_id =2
print("Xoa")
# delete_comments = comments_collection.delete_one({'comment_id':2})
# for delete in comments_collection.find():
#     print(delete)

posts_collection.find()
print(posts_collection)
comments_collection.find()
print(comments_collection)