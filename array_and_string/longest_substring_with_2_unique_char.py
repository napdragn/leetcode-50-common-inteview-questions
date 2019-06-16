def longest_substring_with_k_unique_char(st, k):
    if len(st) <= 1:
        return len(st)
    max_len = start = end = 0
    char_map = dict()
    while end < len(st):
        char_map[st[end]] = (char_map[st[end]] + 1) if st[end] in char_map else 1
        while len(char_map) > k:
            temp_char = st[start]
            char_map[temp_char] -= 1
            if char_map[temp_char] == 0:
                char_map.pop(temp_char)
            start += 1
        max_len = max(max_len, end - start + 1)
        end += 1
    return max_len
