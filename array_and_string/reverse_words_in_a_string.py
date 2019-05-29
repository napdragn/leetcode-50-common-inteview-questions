def reverseWords(s: str) -> str:
    temp_word, rev_sent = "", ""
    for char in s:
        if char != " ":
            temp_word += char
        elif temp_word:
            if not rev_sent:
                rev_sent = temp_word
            else:
                rev_sent = "".join((temp_word, " ", rev_sent))
            temp_word = ""
    if not rev_sent:
        rev_sent = temp_word
    elif temp_word:
        rev_sent = "".join((temp_word, " ", rev_sent))
    return rev_sent