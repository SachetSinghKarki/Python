# # dict={
# #     "luna":34,
# # "leo":35,
# #     2:67,
# #     3:8
# # }

# # print(dict["luna"])

# # print(dict.get(1, "Sorry not found"))


# keys={"ram", "hari", "shyam"}
# values = [34,64,87]

# dict = dict(zip(keys,values))
# print(dict)
# print(type(dict))

data = {
    "js": "vs-code",
    "python": ["pycharm", "vs-code"],
    "java": {"core": "vs-code", "spring": "iij"},
}


print(data)
print(data["python"])
print(data["java"]["spring"])