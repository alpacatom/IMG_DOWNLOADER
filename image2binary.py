from PIL import Image
import numpy as np
import os
import sys
import re

fname = 'train-data.d'

path = '/Users/tom/Program/Python/gochiusa/'
input_path = path+'syaro-resize/'
output_path = path+'train-data/' 

#files = os.listdir(input_path)
args = sys.argv

if os.path.exists(output_path+fname) :
    os.remove(output_path+fname)


ii=len(args)
if ii<3:
    print "Usage : $ python image2binary.py [0's dir] [1's dir]"
    exit(1)

sum=0
count = 0
f = open(output_path+fname,'a')

while ii>1 :
    files = os.listdir(path+args[count+1])
    print "Image2binary : " + args[count+1] + "  label : " + str(count)
    for file in files :
        jpg = re.compile("jpg")
        if (jpg.search(file)) :
            img = Image.open(input_path+file)
            img = (np.array(img))

            label = [count]
            r = img[:,:,0].flatten()
            g = img[:,:,1].flatten()
            b = img[:,:,2].flatten()

            output = np.array(list(label) + list(r) + list(g) + list(b), np.uint8)
            f.write(output)
            sum+=1
    ii-=1
    count+=1

print "finished to convert images to binary files"
print sum
f.close()
