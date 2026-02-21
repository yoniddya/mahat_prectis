# q1

# counter = 0
# list_of_nums = []
# while counter < 6 :
#     numbers = int(input("enter first number :"))
#     number2 = int(input("enter second number :"))
#     list_of_nums.append(str(numbers))
#     list_of_nums.append(str(number2))
#     counter += 1
# sum_of_too_digit = 0
# count_too_digit = 0
# for i in range(len(list_of_nums)):
#     if len(list_of_nums[i]) == 2 :
#         count_too_digit += 1
#         sum_of_too_digit += int(list_of_nums[i])
# print (f"sum of too digit numbers is : {sum_of_too_digit}")
# print(f" amount of too digit numbers is : {count_too_digit}")


# q2

# lengh_of_str = 0
# list_of_words = []
# while lengh_of_str % 2 == 0:
#     word = input("enter your word :")
#     list_of_words.append(word)
#     if len(word) % 2 != 0 :
#         lengh_of_str = len(word)
#     if "z" in word:
#         print("their is z in the word")
# print(list_of_words)
# counter = 0
#
# for i in range(len(list_of_words)):
#     s = list_of_words[i][0]
#     l = list_of_words[i][-1]
#     for j in range(i + 1, len(list_of_words)):
#         if list_of_words[j].startswith(s) and list_of_words[j].endswith(l):
#             counter += 1
#
# print(f"count of similar start and end chars: {counter}")


# q3

# import  random
#
#
# numbers = []
# while len(numbers) < 40:
#     number = random.randint(10, 100)
#     numbers.append(number)
# print(numbers)
# max_num = 0
# number_of_timse = 0
# for i in range(len(numbers)):
#     current_num = numbers[i]
#     counter = 0
#     for j in range(i + 1 ,len(numbers)):
#         if numbers[j] == current_num:
#             counter += 1
#             if counter >= number_of_timse:
#                 max_num = current_num
#                 number_of_timse = counter
# print(f"max num is : {max_num} \nnumber of tims : {number_of_timse}")

# q4

