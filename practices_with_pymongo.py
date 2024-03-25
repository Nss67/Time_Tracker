import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")

db_list = my_client.list_database_names()
# print(db_list)

my_db = my_client["my_shop"]
my_col = my_db["customers"]

col_list = my_db.list_collection_names()
# print(col_list)

my_dict = {"name": "John", "address": "Highway 37"}

# x = my_col.insert_one(my_dict)
# print(x.inserted_id)

my_second_dict = mylist = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"}
]

# y = my_col.insert_many(my_second_dict)

# count = 0
# for i in y.inserted_ids:
#     count += 1
#     print(count, "", i)

# Drop a collection
my_col.drop()

my_third_dict = [
    {"_id": 1, "name": "John", "address": "Highway 37"},
    {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    {"_id": 3, "name": "Amy", "address": "Apple st 652"},
    {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
    {"_id": 5, "name": "Michael", "address": "Valley 345"},
    {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
    {"_id": 8, "name": "Richard", "address": "Sky st 331"},
    {"_id": 9, "name": "Susan", "address": "One way 98"},
    {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
    {"_id": 12, "name": "William", "address": "Central st 954"},
    {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
    {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

z = my_col.insert_many(my_third_dict)

# print(z.inserted_ids)

# x = my_col.find_one({"_id": 3})
# print(x)

# x = my_col.find()
# for i in x:
    # print(i)

# x = my_col.find({}, {"_id": 0, "name": 1, "address": 1})
# for i in x:
#     print(i)

# query = {"address": {"$gt": "S"}}
# projection = {"_id": 0, "name": 1, "address": 1}
# x = my_col.find(query, projection)
# for i in x:
#     print(i)

# query = {"address": {"$regex": "^S"}}
# projection = {"_id": 0, "name": 1, "address": 1}
# x = my_col.find(query, projection)
# for i in x:
#     print(i)

# sorting
# x = my_col.find().sort("name")
# for i in x:
#     print(i)

# x = my_col.find().sort("name", -1)  # Sort Descending
# for i in x:
#     print(i)

# x = my_col.find().sort("name", 1)  # sort ascending
# for i in x:
#     print(i)

# delete a document
# query = {"address": "Mountain 21"}
# my_col.delete_one(query)
# x = my_col.find()
# for i in x:
#     print(i)

# delete many documents
# query = {"address": {"$regex": "^S"}}
# my_col.delete_many(query)
# x = my_col.find()
# for i in x:
#     print(i)

# delete all documents
# query = {}
# x = my_col.delete_many({})
# print(x.deleted_count, "documents deleted")

#  update a document
# query = {"address": "Valley 345"}
# newValue = {"$set": {"address": "Canyon 123"}}
# x = my_col.find_one(query)
# my_col.update_one(query, newValue)
# y = my_col.find_one({"address": "Canyon 123"})
# print(x, "\n", y)

# update many documents
# query = {"address": {"$regex": "^S"}}
# newValue = {"$set": {"name": "Mania"}}
# x = my_col.find(query)
# print(75 * "=")
# for i in x:
#     print(i)
# z = my_col.update_many(query, newValue)
# y = my_col.find({"name": "Mania"})
# print("\n", z.modified_count, "documents updated", "\n")
# for i in y:
#     print(i)
# print(75 * "=")

# limit
# x = my_col.find().limit(5)
# for i in x:
    # print(i)

