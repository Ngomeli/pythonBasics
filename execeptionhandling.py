
try:
    num1 = 39
    num2 = 0
    print(num1 / num2)
except ZeroDivisionError:
    print("ZeroDivisionError has occurred")
finally:
    print("Success")