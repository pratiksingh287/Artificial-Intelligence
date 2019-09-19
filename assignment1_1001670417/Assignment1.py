#!/usr/bin/python
import sys


#this function is Key to help sorting the fringe
def getDistance(line):
	return float(line.split()[-1])


#this function reads those line from file where theres a path from sourceCity
def readFileLine(filename,sourceCity):
	f=open(filename,"r")
	list=[]
	for line in f:
		if (sourceCity in line):
			parts=line.split()
			if(parts[0]==sourceCity):
				list.append(line)
			else:
				list.append(parts[0]+" "+parts[1]+" "+parts[2])
		else:
			continue
	f.close()
	return list

#this function is to add paths from specified city 
#into the fringe along with respective actual and cumulative costs
def addtoFringe(source,cumuD,fileName):
	for l in readFileLine(fileName,source):
		cumu=float(cumuD)+float(l.split()[2])
		fringe.append(l.split()[0]+" "+ l.split()[1]+" "+ l.split()[2]+" "+ str(cumu))
	return fringe

#This function backtracks the actual optimal 
#path by searching cumulitive cost minus actual cost
def backTrack(fringe):	
	backList=[]
	source=fringe[-1].split()[0]
	dest=fringe[-1].split()[1]
	cost=float(fringe[-1].split()[2])
	cumuCost=float(fringe[-1].split()[3])
	backList.append(source+" to "+dest+", "+str(cost)+" km\n")
	for l in sorted(fringe,key=getDistance,reverse=True):
		if(float(l.split()[-1])==(cumuCost-cost) and l.split()[1]==source):
			source=l.split()[0]
			dest=l.split()[1]
			cost=float(l.split()[2])
			cumuCost=float(l.split()[-1])
			backList.append(source+" to "+dest+", "+str(cost)+" km\n")
		else:
			continue
	return backList[:len(backList)-1]
	
#The actual algorithm steps are in this functions
#first we extract the node and test if it's a goal node and  then check if it is present in the closed Set
#if it's not in the closed set then expand it by addding its adjacent neighbours to the fringe		
def algorithm(sourceCity,goal,fringe,closedSet,index,filename):
	while(index<len(fringe)):		
		node=fringe[index]
		index=index+1
		source=node.split()[0]
		destination=node.split()[1]
		if(destination==goal):
			print("distance:"+node.split()[-1]+" km\n")
			break
		if (destination!=goal and destination not in closedSet):
			addtoFringe(destination,node.split()[-1],filename)
			closedSet.append(destination)
			fringe[index:]=sorted(fringe[index:],key=getDistance)
	else:
		print("distance: infinity\nroute:none\n")
		return ""
	return backTrack(fringe[:index])

#main process and function calls
filename=sys.argv[1] 
source=sys.argv[2]
goal=sys.argv[3]
closedSet=[]
index=0
optimalPathLength=0
optimalPath=[]
fringe=[source+" "+source+" "+str(0)+" "+str(0)]
for l in reversed(algorithm(source,goal,fringe,closedSet,index,filename)):
	print(l)
