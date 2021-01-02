# for i in range(1,11):
#     print(":) " * i)

# x = 1
# while x<11:
#     print(":) " * x)
#     x+=1

# # without string multiplication
# for num in range(1,11):
#     count = 1
#     smileys = ""
#     while count <= num:
#         smileys += ":) "
#         count += 1
#     print(smileys)

space = 8
for i in range(1,11,2):
    print( space * " " + "* " * i)
    space -=2