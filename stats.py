def get_num_words(content: str) -> int:
    return len(content.split(None))

def get_char_count(content: str) -> dict[str, int]:
    retdict = {}
    for char in content:
        lowerchar = char.lower()
        if lowerchar.isalnum:
            if lowerchar not in retdict:
                retdict[lowerchar] = 1
            else:
                retdict[lowerchar] += 1
    return retdict