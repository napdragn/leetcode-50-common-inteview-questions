def two_sum_sorted_array(numbers: list, target: int) -> tuple:
    start_ind, end_ind = 0, len(numbers) - 1
    while start_ind != end_ind:
        wanted_num = target - numbers[start_ind]
        if numbers[end_ind] == wanted_num:
            return (start_ind + 1, end_ind + 1)
        elif numbers[end_ind] > wanted_num:
            end_ind -= 1
            continue
        else:
            start_ind += 1
    return (-1, -1)