#Definition of dictionary
#europe = {"Spain":"Madrid", "France":"Paris", "Germany":"Berlin"}
#Additing Italy to europe dictionary
#europe["Italy"] = "Rome"

#Printing the updated dictionary

#print(europe)

world = {"europe":30.55, "Africa":39.21, "Asia": 49.89}
world.update({"europe": 20.55, "Africa": 49.21})
for key, value in world.items():
    print(f"{key}: {value} million people")
