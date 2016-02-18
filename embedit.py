import csv as csv
import numpy as np
from pylab import *
from sklearn.linear_model import SGDClassifier
from sklearn import tree
from sklearn.neighbors.nearest_centroid import NearestCentroid

csv_file = csv.reader(open('dataset.csv'))
header= csv_file.next()

data = []

for row in csv_file:
	data.append(row)

data = np.array(data)

'''
xtrain = data[1:5600,0:3].astype(np.float)
ytrain = data[1:5600,3].astype(np.int)
xtest = data[5601:7999,0:3].astype(np.float)
ytest = data[5601:7999,3].astype(np.int)

'''
xtrain = data[1:5600,0:3].astype(np.float)
ytrain = data[1:5600,3].astype(np.int)
xtest = data[1:5600,0:3].astype(np.float)
ytest = data[1:5600,3].astype(np.int)



clf = SGDClassifier(loss="modified_huber", penalty="elasticnet").fit(xtrain,ytrain)
#clf = NearestCentroid().fit(xtrain,ytrain)
#clf = tree.DecisionTreeClassifier().fit(xtrain,ytrain)
p = map(clf.predict,xtest)
#print ('test actual values',ytest)
#print
#print p
score1="favourable"
score2="unfavourable"

index=0
arr=[]

for index in range(len(p)):
	if p[index]>0:
		print 'Conditions for weather Conditions',index+1,'are ',score1	
	else:
		print 'Conditions for weather Conditions',index+1,'are ',score2
	arr.append(p[index][0]-ytest[index])
	
#print type(p[0])
'''
#testing accuracy
f11=0.0
f10=0.0
f01=0.0
f00=0.0
for j in range(0,2397):
	if ytest[j]==1 and p[j]==1:
		f11=f11+1
	if ytest[j]==1 and p[j]!=1:
		f10=f10+1	
	if ytest[j]==0 and p[j]!=0:
		f01=f01+1
	if ytest[j]==0 and p[j]==0:
		f00=f00+1 
print 'accuracy of testing is',((f11+f00)/(f11+f00+f10+f01))*100

#training accuracy
f11=0.0
f10=0.0
f01=0.0
f00=0.0
for j in range(0,5599):
	if ytest[j]==1 and p[j]==1:
		f11=f11+1
	if ytest[j]==1 and p[j]!=1:
		f10=f10+1	
	if ytest[j]==0 and p[j]!=0:
		f01=f01+1
	if ytest[j]==0 and p[j]==0:
		f00=f00+1 
print 'accuracy of training is',((f11+f00)/(f11+f00+f10+f01))*100
'''

 #MAPE value
arr=np.abs(arr)
print 'difference array is'
print arr
error=21.21
count=(np.count_nonzero(arr))+0.0
length=len(p)+0.0
error=((length-count)/length)*100
print 'Accuracy in classification task was ',error,'%'

'''
#for testing set
flag=0
flag1=0
scatter(data[5601:7999,0],ytest, s=220, facecolors='none', edgecolors='r',label="actual value")
for i in range(0,2397):
	if int(ytest[i]) == int(p[i]):
		if flag ==0:
			scatter(data[5601+i,0],p[i],s=140,color='lightskyblue',alpha=0.4,label=" correct prediction")
			flag=1
		else:
			scatter(data[5601+i,0],p[i],s=140,color='lightskyblue',alpha=0.4)

for i in range(0,2397):
	if int(ytest[i]) != int(p[i]):
		if flag1== 0:
			scatter(data[5601+i,0],p[i],s=180,marker='x',color='black',alpha=0.9,label="incorrect prediction")
			flag1=1
		else:
			scatter(data[5601+i,0],p[i],s=180,marker='x',color='black',alpha=0.9)

xticks([10,20,30,40,50])

yticks([-1,0,1,2])
yticks([0,1],[r'$unfavourable$',r'$favourable$'],size=20)
legend(loc="upper right")
title('Testing set',size=22)
xlabel('Temperature',size=15)
ylabel('Conditions',size=15,position=(2,0.5))

show()

'''

#for training set

flag=0
flag1=0
scatter(data[1:5600,0],ytest, s=220, facecolors='none', edgecolors='r',label="actual value")
for i in range(0,5599):
	if int(ytest[i]) == int(p[i]):
		if flag ==0:
			scatter(data[1+i,0],p[i],s=140,color='lightskyblue',alpha=0.4,label=" correct prediction")
			flag=1
		else:
			scatter(data[1+i,0],p[i],s=140,color='lightskyblue',alpha=0.4)
for i in range(0,5599):
	if int(ytest[i]) != int(p[i]):
		if flag1== 0:
			scatter(data[1+i,0],p[i],s=180,marker='x',color='black',alpha=0.9,label="incorrect prediction")
			flag1=1
		else:
			scatter(data[1+i,0],p[i],s=180,marker='x',color='black',alpha=0.9)

xticks([10,20,30,40,50])

yticks([-1,0,1,2])
yticks([0,1],[r'$unfavourable$',r'$favourable$'],size=20)
legend(loc="upper right")
title('Training set',size=22)
xlabel('Temperature',size=15)
ylabel('Conditions',size=15,position=(2,0.5))
show()


















