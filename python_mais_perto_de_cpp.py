import random
value = int(0)
import cv2
from a_cv2_imshow_thread import add_imshow_thread_to_cv2
import numpy as np

def create_id():
    global value;
    value += 1;
    return value;

def colorsearch(
        pic: list[int],
        colors: list[int],
        width: int,
        totallengthpic: int,
        totallengthcolor: int,
        outputx: list[int],
        outputy: list[int],
        lastresult: list[int],

):
    for i in range(0, totallengthcolor // 3 + 1, int(3)):  # parallel
        r = int(i * 3);
        g = int(i * 3 + 1);
        b = int(i * 3 + 2);
        for j in range(int(0), totallengthpic, 3):
            if (colors[r] == pic[j]) & (colors[g] == pic[j + 1]) & (colors[b] == pic[j + 2]):
                dividend = int(j / 3);
                quotient = int(dividend / width);
                remainder = int(dividend % width);
                upcounter = int(create_id());
                outputx[upcounter] = quotient;
                outputy[upcounter] = remainder;
                lastresult[0] = upcounter;


add_imshow_thread_to_cv2()
picture = [[random.choice([[255, 255, 255], [0, 0, 0], [255, 255, 0]]) for q in range(320)] for qq in range(320)]
picturetest = np.array(picture,dtype=np.uint8)
cv2.imshow_thread(picturetest)

colors2check = [[0, 0, 0], [255, 255, 0]]
pic = np.array(picture).flatten().tolist()
colors = np.array(colors2check).flatten().tolist()
width = len(picture)
totallengthpic = len(pic)
totallengthcolor = len(colors)
outputx = [0] * len(pic)
outputy = [0] * len(pic)
lastresult = [0]
colorsearch(
    pic,
    colors,
    width,
    totallengthpic,
    totallengthcolor,
    outputx,
    outputy,
    lastresult,

)
final = [y for y in zip(outputx[:lastresult[0]], outputy[:lastresult[0]])]
print(final)
