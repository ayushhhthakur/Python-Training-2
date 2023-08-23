my_list = []

for i in range(10):
    if i == 5:
        my_list.append(5)
    elif i == 8:
        my_list.append(8)
    else:
        my_list.append(None)

print("Initial List:", my_list)

queue = []

for i in range(len(my_list)):
    if my_list[i] == 5:
        break
    queue.append(my_list[i])

for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] == 8:
        break
    queue.append(my_list[i])

print("Queue:", queue)
