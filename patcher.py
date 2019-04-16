# coding=utf-8
import sys

special_chars = [
    'Ȁ', # up left
    'Ȃ', # down left
    'Ȅ', # up right
    'Ȇ', # down right
    'Ȉ', # vertical
    'Ȋ'  # horizontal
]


if len(sys.argv) < 4:
    print("Usage: python patcher.py commands box outputfile")
    exit(0)

commandsfile = sys.argv[1]
boxfile = sys.argv[2]
output = sys.argv[3]

with open(commandsfile, 'r', encoding="utf-8") as cmdf:
    with open(boxfile, 'r', encoding="utf-8") as boxf:
        boxes = boxf.readline().split(" ")
        with open(output, 'w', encoding="utf-8") as out:
            lines = "".join(cmdf.readlines())
            
            for i in range(len(special_chars)):
                print(special_chars[i])
                print(boxes[i])
                lines = lines.replace(special_chars[i], boxes[i])

            out.write(lines)

