#Break Statement -Exits the entrie loop
'''
num=20
while num <=25:
    print(num)
    if num ==24:
        break
    num += 1
'''
#Continue Statement -Skips a loop
devices=["Laptop", "Phone", "Tablet"]
for i in devices:
    if i == "Phone":
        continue
    print(i)