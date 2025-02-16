import serial
ard=serial.Serial("COM3",timeout=1, baudrate=9600)
c=0
s=""
while c<10:
	s+=(str(ard.readline()))
	c+=1
l=[]
l=s.split("#")
m=l[1]
print(m[0])