def valid_palindrome(s: str) -> bool:
    start_ind, end_ind = 0, len(s) - 1
    while start_ind <= end_ind:
        if s[start_ind].isalnum() and s[end_ind].isalnum():
            if s[start_ind] == s[end_ind]:
                start_ind += 1
                end_ind -= 1
                continue
            else:
                return False
        elif not s[start_ind].isalnum():
            start_ind += 1
            continue
        elif not s[end_ind].isalnum():
            end_ind -= 1
    return True