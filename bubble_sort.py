def bubble(sequence):
    for i in range(len(sequence)):
        for j in range(len(sequence)-1):
            if sequence [j] > sequence [j+1]:
                sequence[j],sequence[j+1] = sequence [ j+1], sequence [j]

sequence = [19, 13, 6, 2, 18, 8]
bubble(sequence)
print(sequence)


'''def bubble_sort(our_list):
    # We go through the list as many times as there are elements
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]

our_list = [19, 13, 6, 2, 18, 8]
bubble_sort(our_list)
print(our_list)'''