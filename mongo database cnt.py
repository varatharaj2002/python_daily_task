import pymongo

connect=pymongo.MongoClient("mongodb://localhost:27017")

db=connect.python_learning_12_1
col=db.database_mongo_db

# create
student={
    "name":"sudharani",
    "age":21,
    "course":"python"
}

# res=col.insert_one(student)
# print(res.inserted_id)

students=[
    {
    "name":"vardharaj",
    "age":20,
    "course":"Java"
},
{
    "name":"shanmathi",
    "age":22,
    "course":"C"
},
{
    "name":"Rajeswari",
    "age":21,
    "course":"python"
}
]

res=col.insert_many(students)
print(res.inserted_ids)

# read

# res=col.find_one ()
# print(res)

# res=col.find()
# print(res)
# for i in res:
    # print(i)

# update

# previous_data={"age":20}

# present_data={"$set":{"age":21}}

# res=col.update_one(previous_data,present_data)


# previous_data={"course":"Java"}
# present_data={"$set":{"course":"python"}}
# res=col.update_many(previous_data,present_data)

# delete
# res=col.delete_one({"age":22})
# print(res.deleted_count)

# query
# query={"name":"sudharani"}

# res=col.find(query)
# for i in res:
    # print(i)


# limit

# res=col.find().limit(2)
# for i in res:
#     print(i)