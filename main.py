def calculate():
    number = int(input("введи 5-ти значное число "))
    ten_thousands = number // 10000
    thousands = (number // 1000) % 10
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    units = number % 10
    result = (tens ** units) * hundreds / (ten_thousands - thousands)
    print(f"result {result}")
calculate()