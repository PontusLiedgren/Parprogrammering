def get_indices(my_list, my_item):
    new_list = []
    offset = -1
    while True:
        try:
            offset = my_list.index(my_item, offset+1)
        except ValueError:
            return new_list
        new_list.append(offset)

print(get_indices([5, 5, 6, 2, 7], 5))