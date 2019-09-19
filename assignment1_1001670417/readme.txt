Name : Pratik Pramod Singh
UTA ID: 1001670417

algorithm(sourceCity,goal,fringe,closedSet,index):
This function does basic steps
1. takes node out of fringe
2. check if it has goal node
3. check if it is present in the closed set
4. if not in closed set, expands it by adding its adjacent neighbours or successors
index passed here divides fringe into two parts first part consisting of nodes that are visited
Taking out a node from fringe simply means incrementing the index.
5.sort second part of fringe(divided by index).

addtoFringe(source,cumuD):
This function reads lines from file that has source in it
adds such lines into fringe with an extra attribute which is sum of cost mentioned in line and cumuD passed to the function
this gives cumulative distance from original source

readFileLine(sourceCity):
reads lines from file that has sourceCity in it and returns the lines.

getDistance():
This is key for sorting fringe it returns cumulative cost in the line on basis of which fringe is sorted

backTrack():
It reverses the fringe[:index] obtained after finding goal state
then first line if line that containes goal state along with total "cumulative cost" in line representing 
total cost from source to destination.
In this line we subtract cost from cumulative cost and search a record having equal cumulative cost.
after finding such record we check that source of first record is matching with destination
of found record if yes then it is the next hop in backtracking.
we do above procedure iteratively till we reach original source.

How to run code:
Pass three command line arguments
1.input file path
2.source
3.destination