# #print each cher of str
# s = 'python'
# for ch in s:
#     print(ch)

# #count number of char in a str
# s = 'hello'
# count = 0
# for ch in s:
#     count = count+1
# print(count)

# #count vowels in str
# s = 'hello'
# vowels = "aeiouAEIOU"
# count = 0
# for ch in s:
#     if ch in vowels:
#         count += 1
# print(count)

# #reverse a str
# rev = ""
# for ch in s:
#     rev = ch+rev
# print(rev)

# list1 = input("Enter subjects of 1st student: ").split()
# list2 = input("Enter subjects of 2nd student: ").split()
# common_subjects = []
# for i in list1:
#     if i in list2:
#         common_subjects.append(i)
# print("Common Subjects:", common_subjects)

# list1 = input("Enter 1st list: ").split()
# list2 = input("Enter 2nd list: ").split()
# found = False
# for item in list1:
#     if item in list2:
#         found = True
#         break
# if found:
#     print("common element is exists ")
# else:
#     print("No common element is exists")

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# a = []
# for word in words:
#     if word not in a:
#         a.append(word)
# result = " ".join(a)                                                                                                                  
# print("Sentence after removing duplicates:",result)
