__author__ = 'Topper121'

def selection_sort(list):
    """ Sort a list using the selection sort """

    # Loop through the entire array
    for cur_pos in range(len(list)):
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos

        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(list)):

            # Is this position smallest?
            if list[scan_pos] < list[min_pos]:

                # It is, mark this position as the smallest
                print(scan_pos)
                min_pos = scan_pos

        # Swap the two values
        temp = list[min_pos]
        list[min_pos] = list[cur_pos]
        list[cur_pos] = temp
        print(list)

list = [15,57,14,33,72,79,26,56,42,40]

selection_sort(list)

print(list)