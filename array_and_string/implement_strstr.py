# TODO: Implement using KMP.
def str_str(haystack: str, needle: str) -> int:
    h_len = len(haystack)
    n_len = len(needle)
    # When needle length greater than the string to be searched return -1
    if n_len > h_len:
        return -1
    elif n_len == 0:
        return n_len
    for i in range(h_len):
        # If no of characters remaining to be searched in haystack less than
        # needle length, no need to search further, return -1
        if (h_len - i) < n_len:
            return -1
        temp_i = i
        for j in range(n_len):
            if temp_i >= h_len:
                return -1
            elif haystack[temp_i] == needle[j]:
                if j == (n_len - 1):
                    return i
                temp_i += 1
            else:
                break
    return -1