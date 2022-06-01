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
    size=1
    face=random.randint(0,3)
    times=0
    right=0
    imgsize=(500,500,3)
    x=int(imgsize[1]/2)-int(5/2*size)+7*size*random.randint(-int(imgsize[1]/21/size),int(imgsize[1]/21/size))
    y=int(imgsize[0]/2)-int(5/2*size)+7*size*random.randint(-int(imgsize[1]/21/size),int(imgsize[1]/21/size))
    mouseface=-1
    def mouse_face(event,x,y,flags,param):
        global mouseface,imgsize
        if event==cv2.EVENT_LBUTTONDOWN:
            if y>int((img.shape[0]-12*5)/2) and y<int((img.shape[0]-12*5)/2)+12*5:
                if  x>imgsize[1]-12*5:
                    mouseface=0
                elif x<12*5:
                    mouseface=2
            elif x>int((img.shape[1]-12*5)/2) and x<int((img.shape[1]-12*5)/2)+12*5:
                if  y>imgsize[0]-12*5:
                    mouseface=3
                elif y<12*5:
                    mouseface=1
    cv2.namedWindow('img')
    cv2.setMouseCallback('img',mouse_face)
    while True:
        img=np.zeros(imgsize,np.uint8)
        cv2.rectangle(img,(0,0),(img.shape[1],img.shape[0]),background,-1)
        drawE(img,0,int((img.shape[0]-12*5)/2),12,2,color)
        drawE(img,int((img.shape[1]-12*5)/2),0,12,1,color)
        drawE(img,img.shape[1]-12*5,int((img.shape[0]-12*5)/2),12,0,color)
        drawE(img,int((img.shape[1]-12*5)/2),img.shape[0]-12*5,12,3,color)
        drawE(img,x,y,size,face,color)
        cv2.imshow('img',img)
        key=cv2.waitKey(1)&0xff
        if key==27:
            break
        elif key==ord('w'):
            if face==1:
                right+=1
            times+=1
            face=random.randint(0,3)
            x=int(img.shape[1]/2)-int(5/2*size)+7*size*random.randint(-int(img.shape[1]/21/size),int(img.shape[1]/21/size))
            y=int(img.shape[0]/2)-int(5/2*size)+7*size*random.randint(-int(img.shape[1]/21/size),int(img.shape[1]/21/size))
        elif key==ord('a'):
            if face==2:
                right+=1
            times+=1
            face=random.randint(0,3)
            x=int(img.shape[1]/2)-int(5/2*size)+7*size*random.randint(-int(img.shape[1]/21/size),int(img.shape[1]/21/size))
            y=int(img.shape[0]/2)-int(5/2*size)+7*size*random.randint(-int(img.shape[1]/21/size),int(img.shape[1]/21/size))
        elif key==ord('s'):
            if face==3:
                right+=1
            times+=1
            face=random.randint(0,3)
            x=int(img.shape[1]/2)-int(5/2*size)+7*size*random.randint(-int(img.shape[1]/21/size),int(img.shape[1]/21/size))
            y=int(img.shape[0]/2)-int(5/2*size)+7*size*random.randint(-int(img.shape[1]/21/size),int(img.shape[1]/21/size))
        elif key==ord('d'):
            if face==0:
                right+=1
            times+=1
            face=random.randint(0,3)
            x=int(img.shape[1]/2)-int(5/2*size)+7*size*random.randint(-int(img.shape[1]/21/size),int(img.shape[1]/21/size))
            y=int(img.shape[0]/2)-int(5/2*size)+7*size*random.randint(-int(img.shape[1]/21/size),int(img.shape[1]/21/size))
        elif key>47 and key<58:
            size=key-48
            if size==0:
                size=10
            face=random.randint(0,3)
            x=int(img.shape[1]/2)-int(5/2*size)+7*size*random.randint(-int(img.shape[1]/21/size),int(img.shape[1]/21/size))
            y=int(img.shape[0]/2)-int(5/2*size)+7*size*random.randint(-int(img.shape[1]/21/size),int(img.shape[1]/21/size))
        elif mouseface>-1:
            if face==mouseface:
                right+=1
            times+=1
            mouseface=-1
            face=random.randint(0,3)
            x=int(img.shape[1]/2)-int(5/2*size)+7*size*random.randint(-int(img.shape[1]/21/size),int(img.shape[1]/21/size))
            y=int(img.shape[0]/2)-int(5/2*size)+7*size*random.randint(-int(img.shape[1]/21/size),int(img.shape[1]/21/size))
    print(str(right)+'/'+str(times))
    cv2.destroyAllWindows()
