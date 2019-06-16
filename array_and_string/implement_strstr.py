# TODO: Implement using KMP.
def str_str(haystack: str, needle: str) -> int:
    h_len = len(haystack)
    n_len = len(needle)
    # When needle length greater than the string to be searched return -1
    if n_len > h_len:
        return -1
    elif n_len == 0:
        return 0
    for i in range(h_len):
        # If no of characters remaining to be searched in haystack less than
        # needle length, no need to search further, return -1
        if (h_len - i) < n_len:
            return -1
        for j in range(n_len):
            if (i + j) >= h_len:
                return -1
            elif haystack[i + j] == needle[j]:
                if j == (n_len - 1):
                    return i
            else:
                break
    return -1