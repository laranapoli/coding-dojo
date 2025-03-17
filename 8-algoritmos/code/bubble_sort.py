def bubble_sort(input_list):
    length = len(input_list)

    for i in range(length):
        swap = False

        for j in range(0, length - i - 1):
            if input_list[j] > input_list[j+1]:
                swap = True
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
        
        if not swap:
            break
            


sequence = [4, 6, 7, 8]

bubble_sort(sequence)

print(sequence)