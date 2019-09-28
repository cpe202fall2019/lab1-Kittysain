def max_list_iter(int_list):  # must use iteration not recursion
    # when the list is none, raise value error
    # when the list is empty, return none
    # assign the index of the maximum number as 0, use a for loop to compare the index of maximum number to each
    # item. if the item is larger than the assigned maximum item, then the index of the maximum number is re-assigned
    # to the item, otherwise, the assigned maximum item will be the maximum the two being compared and thus keep the
    # assigned index.
    # return the maximum as output
    if int_list is None:
        raise ValueError
    elif len(int_list) == 0:
        return None
    else:
        index_max = 0
        for i in range(1, len(int_list)):
            if int_list[i] > int_list[index_max]:
                index_max = i
            elif int_list[i] <= int_list[index_max]:
                continue
        return int_list[index_max]


def reverse_rec(int_list):
    # raise ValueError for list that is none
    # the base case is when there is no item in the list, return empty list
    # the last item is popped out of the list and added to the front

    if int_list is None:
        raise ValueError
    if len(int_list) == 0:
        return []
    else:
        last_item = [int_list.pop()]
        new_list = int_list
        return last_item + reverse_rec(new_list)


def bin_search(target, low, high, int_list):
    # searches for target in int_list[low..high] and returns index if found
    # If target is not found returns None. If list is None, raises ValueError
    if int_list is None:
        raise ValueError
    if (target in int_list) is False:
        return None
    if len(int_list) == 0 or target < int_list[low] or target > int_list[high]:
        return None
    elif target == int_list[low]:
        return low
    elif target == int_list[high]:
        return high

    if int_list[(high + low) // 2] == target:
        return (high + low) // 2
    elif int_list[(high + low) // 2] < target < int_list[high]:
        return bin_search(target, (high + low) // 2, high, int_list)
    elif int_list[(high + low) // 2] > target > int_list[low]:
        return bin_search(target, low, (high + low) // 2, int_list)
