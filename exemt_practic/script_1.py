# for i in range(5,-5,-1):
#     try:
#         print(3/i)
#     except:
#         pass

# for i in range(5,-5,-1):
#     try:
#         print(3/i)
#     except:
#         print("x --> inf")


# class RuntimeError(Exception):
#         pass
#
# while True:
#      try:
#              x = int(input("Please enter a number: "))
#              break
#      except ValueError:
#          print("Oops! That was no valid number. Try again...")
#
#      except RuntimeError:
#          pass

# x = int(input("enter a number: "))
# y = int(input("enter a divider: "))
#
# assert y != 0, "divider cannot be zero"
# assert y >= 1, "divider must be at least 1"
#
# print(x / y)


# items = [2,7,3]
# def double(arg):
#     return arg*2
#
# y = map(double, items)
# print(list(y))

# def desc(colour):
#     return lambda obj : print("“The “" + obj + "“ is “" + colour)
# green = desc("“green”")
# green("“table”")
# blue = desc("“blue”")
# blue("“chair”")


# a = [i for i in range(10)]
# print(a)

# y = [double(item) for item in items ]
# print(y)



