from PIL import Image
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="alzheimer_solution")

cur=db.cursor()
cur.execute("TRUNCATE TABLE PAT_SCAN")

patientWeHave = range(1,5)
numbersWeHave = range(1,3)

for eachPat in patientWeHave:
    for eachNum in numbersWeHave:
        fname='Final_MRI_set/Patient'+str(eachPat)+'/Patient'+str(eachPat)+'_MRI'+str(eachNum)+'.jpg'
        img = cv2.imread(fname,cv2.IMREAD_COLOR)

        hipp_face = img[40:105,58:131]
        wname = 'MRI_pat_'+str(eachPat)+'_scan_'+str(eachNum)+'.jpg'
        cv2.imwrite(wname,hipp_face)
        #img = cv2.imread('MRI_part.jpg',cv2.IMREAD_COLOR)

        #cv2.imshow('image',img)

        #cv2.waitKey(0)
        #print ("Dataset Shape: ")


        #cv2.destroyAllWindows()

        frame = cv2.imread(wname,cv2.IMREAD_COLOR)
        laplacian = cv2.Laplacian(frame,cv2.CV_64F)
        edges = cv2.Canny(frame,100,150)


        cv2.imshow('original',frame)
        cv2.imshow('laplacian',laplacian)
        cv2.imshow('edges',edges)
        cv2.imwrite(wname,edges)

        mripart=cv2.imread(wname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)

        corners = cv2.goodFeaturesToTrack(gray,50,0.01,10)
        corners =  np.int0(corners)

        a,b = 0,0


        for corner in corners:
            x,y = corner.ravel()
            cv2.circle(mripart,(x,y),2,255,-1)
            str1=str(a)
            str2=str(b)
            #+" "+chr(y)+","+chr(a)+" "+chr(b)
            a,b = x,y
            
            #pts=np.array([])

        str3="ST_GeomFromText('LINESTRING("+str(x)+" "+str(y)+","+""+str1+" "+str2+")')"
        str4="insert into pat_scan values("+str(eachPat)+","+str3+")"
        print (str4)
        cur.execute(str4)
        db.commit()
        #pts = np.array
        cv2.line(mripart,(x,y),(a,b),(255,0,0),5)

        #print mripart
        cv2.imshow('corner',mripart)

        #cv2.destroyAllWindows()

        cv2.imwrite(wname,edges)

plt.imshow(frame,cmap='gray',interpolation='bicubic')

#plt.plot([50,100],[80,100],'c',linewidth=5)
   # print ("Dataset Shape: ", balance_data.shape)


plt.show()

