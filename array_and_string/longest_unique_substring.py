def longest_unique_substring(s: str) -> int:
    s_len = len(s)
    if s_len <= 1:
        return s_len
    longest_len = temp_len = 0
    start = end = 0
    visited = dict()
    while start < s_len and end < s_len:
        while end < s_len and s[end] not in visited:
            temp_len += 1
            visited[s[end]] = end
            end += 1
        longest_len = max(longest_len, temp_len)
        if end == s_len:
            break
        end = start = (visited.pop(s[end]) + 1)
        visited = dict()
        temp_len = 0
    return longest_len
