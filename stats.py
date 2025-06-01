def get_num_words(content: str) -> int:
    return len(content.split(None))

def get_char_count(content: str) -> dict[str, int]:
    retdict = {}
    for char in content:
        lowerchar = char.lower()
        if lowerchar not in retdict:
            retdict[lowerchar] = 1
        else:
            retdict[lowerchar] += 1
    return retdict

def get_sorted_char_count(chardict: dict[str, int]) -> list[dict[str, int]]:
    retlist = []
    for key,value in chardict.items():
        newkey = {"char": key, "num": value}
        retlist.append(newkey)
    retlist.sort(key=sort_func, reverse=True)
    return retlist

def sort_func(e):
    return e['num']