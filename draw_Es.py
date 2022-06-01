import cv2
import numpy as np
import random
def drawE(img,x,y,size,face,color):#0Right,1Up,2Left,3Down
    if face==0 or face==2:
        cv2.rectangle(img,(x,y),(x+5*size-1,y+size-1),color,-1)
        cv2.rectangle(img,(x,y+2*size),(x+5*size-1,y+3*size-1),color,-1)
        cv2.rectangle(img,(x,y+4*size),(x+5*size-1,y+5*size-1),color,-1)
        if face==0:
            cv2.rectangle(img,(x,y),(x+size-1,y+5*size-1),color,-1)
        else:
            cv2.rectangle(img,(x+4*size,y),(x+5*size-1,y+5*size-1),color,-1)
    else:
        cv2.rectangle(img,(x,y),(x+size-1,y+5*size-1),color,-1)
        cv2.rectangle(img,(x+2*size,y),(x+3*size-1,y+5*size-1),color,-1)
        cv2.rectangle(img,(x+4*size,y),(x+5*size-1,y+5*size-1),color,-1)
        if face==1:
            cv2.rectangle(img,(x,y+4*size),(x+5*size-1,y+5*size-1),color,-1)
        else:
            cv2.rectangle(img,(x,y),(x+5*size-1,y+size-1),color,-1)
if __name__=='__main__':
    background=(255,255,255)
    color=(0,0,0)
    img=np.zeros((1080,1080,3),np.uint8)
    cv2.rectangle(img,(0,0),(img.shape[1],img.shape[0]),background,-1)
    for n in range(1,13):
        for x in range(n+1):
            for y in range(n+1):
                if x==0 or y==0 or x==n or y==n:
                    drawE(img,int(540-n**2-5*(n+1)*n/2)+7*x*n,int(540-n**2-5*(n+1)*n/2)+7*y*n,n,random.randint(0,3),color)
    cv2.imwrite('eye.png',img)
