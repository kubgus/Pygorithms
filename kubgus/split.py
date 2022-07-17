def split(s: str, p: str):
    temp = ""
    final = []
    for c in s:
        if c == p:
            final.append(temp)
            temp = ""
        else:
            temp += c
    final.append(temp)
    return final


print(split("stormtrooper/4/5/abc", "/"))
