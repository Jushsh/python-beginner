print("welcme to calculator")
print("+, -, *, /")

while True:
  operation_option = input("Choose operation (+, -, *, /) or type 'quit': ")

  if operation_option == "quit":
    print("Goodbye")
    break

  elif operation_option == "+":
    try:
      num1 = float(input("Enter your first number: "))
      num2 = float(input("Enter your second number: "))
      result_add = num1 + num2 
      print(f"the result is {result_add}")
    except Exception as e:
      print("enter only number please!")
  elif operation_option == "-":
    try:
      num3 = float(input("Enter your first number: "))
      num4 = float(input("Enter your second number: "))
      result_sub = num3 - num4
      print(f"the result is {result_sub}")
    except Exception as e:
      print("enter only number please!")
  elif operation_option == "*":
    try:
      num5 = float(input("Enter your first number: "))
      num6 = float(input("Enter your second number: "))
      result_mul = num5 * num6
      print(f"the result is {result_mul}")
    except Exception as e:
      print("enter only number please!")
  elif operation_option == "/":
    try:
      num7 = float(input("Enter your first number: "))
      num8 = float(input("Enter your second number: "))
      result_div = num7 / num8
      print(f"the result is {result_div}")
    except Exception as e:
      print("enter only number please!")
  