# try:
#     with open("a_file.txt") as file:
#         text = file.read()
# except FileNotFoundError:
#     print("error")
# except FileExistsError:
#     print("another error")
# else:
#     print(text)
# finally: print("COde run")
#
# try:
#     dicta = {"key": "value"}
#     print(dicta["igna"])
# except KeyError as error_message:
#     print(f"{error_message} - Not such error")


try:
    num = 0
    num += 1
except num > 2:
    raise ValueError("Num should be higher")

