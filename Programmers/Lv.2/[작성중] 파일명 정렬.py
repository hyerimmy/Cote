import re
def solution(files):
    answer = []

    f_head = []
    f_num = []
    for f in files:
        head = ""
        num = ""
        for ff in f:
            if 65 <= ord(ff) <= 90 or 97 <= ord(ff) <= 122:
                head += ff
            if 48 <= ord(ff) <= 57:
                num += ff


    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

print(ord("0"))
print(ord("9"))
