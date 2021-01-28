import struct
filename='2.raw'
fp = open(filename,'rb')
# angle
fp.seek(2962)
data = fp.read(4)
x = struct.unpack('f',data)
angle_start=float(x[0])

fp.seek(2966)
data = fp.read(4)
x = struct.unpack('f',data)
angle_end=float(x[0])

fp.seek(2970)
data = fp.read(4)
x = struct.unpack('f',data)
angle_step=round(float(x[0]), 5)

# intensity
intensity=[]
twoangle=[]
fp.seek(3154)
data = fp.read(4)
x = struct.unpack('i',data)
count=int(x[0])

m=3158
n=angle_start
for i in range(1,count):
    fp.seek(m)
    data = fp.read(4)
    x = struct.unpack('f',data)
    intensity.append(float(x[0]))
    twoangle.append(n)
    n+=angle_step
    m+=4
    
print(twoangle,intensity)

   


