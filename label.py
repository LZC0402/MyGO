import os

import cv2
def trans(name,mask_0):
    im=cv2.imread("./label/"+name)
    print("./label/"+name)
    im=im[57:425,143:513]
    a,b,c=im.shape
    #im2=cv2.imread("./label/"+name)
    im3=cv2.imread("./label/"+name)
    #im2=im2[57:513,143:425]
    im3=im3[57:425,143:513]#143,57 513 425
    #cv2.imwrite("./our_data/0/"+name,im)
    #cv2.imwrite("./mask/0/"+name,im2)
    cv2.imwrite("./mask/0/"+name,im3)
    print("./img/"+name.split("_")[0]+"_"+name.split("_")[1]+"_t2w_"+name.split("_")[2]) #10000_1000000_t2w_0.png
    #input()
    im4=cv2.imread("./images/"+name.split("_")[0]+"_"+name.split("_")[1]+"_t2w_"+name.split("_")[2])
    im4 = im4[57:425,143:513]
    cv2.imwrite("./img/"+name.split("_")[0]+"_"+name.split("_")[1]+"_t2w_"+name.split("_")[2],im4)

for i in os.listdir("./label/"):
    if (i[0] == "."): continue



    trans(i,i)