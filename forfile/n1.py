# import os
#
#
# def juft_toq(filename):
#     toq = []
#     juft = []
#
#     with open(filename, 'r') as file:
#         for line in file:
#             nums = line.split()
#             for i in nums:
#                 if int(i) % 2 == 0:
#                     juft.append(int(i))
#                 else:
#                     toq.append(int(i))
#     return juft, toq
#
# filename = 'test'
# juft, toq = juft_toq(filename)
#
# print(f"Juft: {juft}")
# print(f"Toq: {toq}")


# def delete_first_num(filename):
#     with open(filename, 'r+') as file:
#         lines = file.readlines()
#         file.seek(0)
#         for line in lines:
#             x = line.split()
#             for j in x:
#                 try:
#                     float(j)
#                 except ValueError:
#                     line = line.replace(x, "")
#
#             file.write(line)
#         file.truncate()
#
# file = 'test'
# delete_first_num(file)

# with open('test', 'r') as file:
#     lines = file.readlines()
#
# processed_lines = []
# for line in lines:
#     first_space_index = line.find(' ')
#     if first_space_index != -1:
#         processed_line = line[first_space_index+1:]
#     else:
#         processed_line = line
#     processed_lines.append(processed_line)
#
# with open('output.txt', 'w') as file:
#     file.writelines(processed_lines)
