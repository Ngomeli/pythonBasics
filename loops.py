#while loop
#number =10
#increament
'''
while number <=20:
    print(number)
    number+=1
'''
#decrement
'''
count = 105
while count >=100:
    print("Number is :", count)
    count -= 1
    '''
#for loop
'''
for x in range(10):
    print(x)
'''
'''
for num in range(15,20):
    print(num)
    '''
'''
for b in range(1,10,2):
    print(b)
'''
#list
"""languages=["python", "php", "SQL"]
for lang in languages:
    print(lang)"""

fam=[1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam):
    #print(f"Index: {index}, Height: {height}")
    print("index" + str(index) + ":" +str(height))