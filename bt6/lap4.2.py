from pymongo import MongoClient
from datetime import datetime


# Buoc 1: Ket noi den MongoDB
client = MongoClient("mongodb://LocalHost:27017/")
db = client['driveManagement01']
# Xoa database
client.drop_database("driveManagement01")

files_collection = db["files"]

# // Bước 2: Tạo bộ sưu tập để lưu trữ thông tin tệp
# // Tạo bộ sưu tập 'files' để quản lý các tệp trên Google Drive
files_data = [
     { 'file_id': 1, 'name': "Report.pdf", 'size': 2048, 'owner': "Nguyen Van A", 'created_at': datetime(2024,1,10), 'shared': 'false' },
    { 'file_id': 2, 'name': "Presentation.pptx", 'size': 5120, 'owner': "Tran Thi B", 'created_at': datetime(2024,1,15), 'shared': 'true' },
    { 'file_id': 3, 'name': "Image.png", 'size': 1024, 'owner': "Le Van C", 'created_at': datetime(2024,1,20), 'shared': 'false' },
    { 'file_id': 4, 'name': "Spreadsheet.xlsx", 'size': 3072, 'owner': "Pham Van D", 'created_at': datetime(2024,1,25), 'shared': 'true' },
    { 'file_id': 5, 'name': "Notes.txt", 'size': 512, 'owner': "Nguyen Thi E", 'created_at': datetime(2024,1,30), 'shared': 'false' }
]
files_collection.insert_many(files_data)

# Tim tep co size lon hon 2000
print("Tep co size lon hon 2000")
# sizes = files_collection.find({'size':{'$gt':2000}})
# for size in sizes:
#     print(size)

# 3.3 Tim tat ca cac tep duoc chia se
print("Dem so file ")
# count_files = files_collection.find().countDocuments()
# print(count_files)

print("Tim tep duoc chia se")
# share_files = files_collection.find({"shared":"true"})
# for shared in share_files:
#     print(shared)

# 3.5Thong ke luong tep
print("Thong ke so luong tep theo chu so huu")
# owners = files_collection.aggregate(
#     [{'$group':{'_id':'owner', 'count':{'$sum':1}}}]
# )
# for owner in owners:
#     print(owner)

# Cap nhat va xoa thong tin
update =files_collection.update_one({ 'file_id': 1 }, { '$set': { 'shared': 'true' } })

print(update)