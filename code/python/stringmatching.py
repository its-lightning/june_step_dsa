def n2_patternmatching(text,pattern):
    n = len(pattern)

    for i in range(len(text) - n + 1):
        match = True
        for j in range(n):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i

    return -1

# def patternmatching(text,pattern):

#     pattern_hash = [(ord(pattern[0])-96) for i in range(0,len(pattern))]

#     print(pattern_hash)

#     for i in range(len(text) - len(pattern) + 1):
#         text[i:len(pattern)]
        


if __name__ == "__main__":
    txt = "abababc"
    pat = "ababc"

    print(n2_patternmatching(txt,pat))
    # print(patternmatching(txt,pat))    



