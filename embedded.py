import random

a = open("test.txt", "w")
a.write("Light Intensity,Temperature,Relative Humidity,Favourable/Unfavourable\n")	
for i in range(1,4000):
	num=random.uniform(23,40)
	#print "%.4f" % num
	num2=random.uniform(132,180)
	num3=int(random.uniform(55,80))
	if ((num >= 15) and (num <= 30) and (num2 > 165) and (num2 < 200) and (num3 >= 60) and (num3 <= 75)):
		num4=1	
	else:
		num4=0
	num=str(int(num))
	num2=str(int(num2))
	num3=str(num3)
	num4=str(num4)+'\n'
	num4=num+','+num2+','+num3+','+num4
	a.write(num4)
	num=random.uniform(16,30)
	num2=random.uniform(166,200)
	num3=int(random.uniform(61,75))
	num4=1
	num=str(int(num))
	num2=str(int(num2))
	num3=str(num3)
	num4=str(num4)+'\n'
	num4=num+','+num2+','+num3+','+num4
	a.write(num4)
a.close()


