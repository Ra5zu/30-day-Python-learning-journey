num_list = ""

for i in range(1, 11):
    num_list += ("\n")
    for j in range(1, 11):
        num_list += str((i*j)) + " "
print(num_list)