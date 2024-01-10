from datetime import datetime



def he(node,goal):
	
	temp=0
	for i1 in range(3):
		for j1 in range(3):
			for i2 in range(3):
				for j2 in range(3):
					if node[i1][j1]==goal[i2][j2]:
						temp+=(abs(i1-i2)+abs(j1-j2))*node[i1][j1]
	
	return temp
				
		


def childMatrix(row,col,startf,path,count,N_Gen,goal):
	
	if row > 0:
		start1 = [row[:] for row in startf]
		start1[row][col],start1[row - 1][col] = start1[row - 1][col],start1[row][col]
		frindge.append((count+" "+str(start1[row][col]),path+' '+'DOWN', start1, row - 1, col,he(start1,goal)))
		N_Gen+=1
	if col > 0:
		start2 = [row[:] for row in startf]
		
		start2[row][col],start2[row][col - 1] = start2[row][col - 1],start2[row][col]
		frindge.append((count+" "+str(start2[row][col]),path+' '+'RIGHT', start2, row, col - 1,he(start2,goal)))
		N_Gen+=1
	if row < 2:
		start3 = [row[:] for row in startf]
		start3[row][col],start3[row + 1][col] = start3[row + 1][col],start3[row][col]
		frindge.append((count+" "+str(start3[row][col]),path+' '+'UP', start3, row + 1, col,he(start3,goal)))
		N_Gen+=1
	if col < 2:
		start4 = [row[:] for row in startf]
		start4[row][col],start4[row][col + 1] = start4[row][col + 1],start4[row][col]
		frindge.append((count+" "+str(start4[row][col]),path+' '+'LEFT', start4, row, col + 1,he(start4,goal)))
		N_Gen+=1
	
	return N_Gen

def sortfrindge(frindge,countofF):
	frindgee=[row[:] for row in frindge]
	n=len(countofF)
	for i in range(n):
		alreadysorted=True
		for j in range(n-i-1):
			if countofF[j]>countofF[j+1]:
				countofF[j],countofF[j+1]=countofF[j+1],countofF[j]
				frindgee[j],frindgee[j+1]=frindgee[j+1],frindgee[j]
				alreadysorted=False
		if alreadysorted:
			break
	
	return frindgee,countofF

def greedy(start,goal,i,j,dump):
	if dump==True:
		now = datetime.now()
		dt_string = now.strftime("%d_%m_%Y__%H_%M_%S")
		dt_string="GREEDY_dump//"+dt_string+".txt"
		f=open(dt_string,"a")
		f.write("Dump file for GREEDY: ")
	N_popped=0
	N_Expanded=0
	mx=0
	mx1=0
	
	N_Gen=1
	start=start
	goal=goal
	global frindge
	i=i
	j=j
	global path
	path=None
	flag=0
	frindge=[]
	frindge.append(('0','', start, i, j,path))
	countofF=[]
	countofF2=[]
	closed=[]
	
    
	while frindge:
		
		
	
		countofF.clear()
		frindge2=[]
		mx=len(frindge)
		if mx>mx1:
			mx1=mx
		for b in range(0,mx):
			val=0
			val=frindge[b][5]
			countofF.append(val)
		
		frindge2,countofF2=sortfrindge(frindge,countofF)
		frindge=[row[:] for row in frindge2]
		new_tile=frindge.pop(0)
		N_popped+=1
		count=new_tile[0]
		path=new_tile[1]
		i=new_tile[3]
		j=new_tile[4]
		
		nN_Gen=N_Gen
		if new_tile[2]!=goal:
			if new_tile[2] not in closed:
				N_Gen=childMatrix(i,j,new_tile[2],path,count,N_Gen,goal)
				N_Expanded+=1
				closed.append(new_tile[2])
			
		else:
			flag=1
			break
		if dump==True:
			f.write("\nFrindge:[\n")
			for i in frindge:
				state="State: "+str(i[2])
				f.write(state)
				bb=i[0].split(" ")
				bb2=i[1].split(" ")
				bb4=i[5]
				bb4=str(bb4)
				bb3="{Move "+bb[-1]+" "+bb2[-1]+" }"+" Heuristic value:  "+bb4
				f.write(bb3)
				f.write(" ]\n")

			f.write("\nNumber of new nodes generated:  ")
			nnn=N_Gen-nN_Gen
			nnn=str(nnn)
			f.write(nnn)
			f.write("\n\nClosed:")
			clo=str(closed)
			f.write(clo)
	if dump==True:
		f.close()
	
	
	path=path.split(" ")
	count=count.split(" ")
	path.pop(0)
	count.pop(0)
	
	sz=len(count)
	
	print("Nodes Popped: ",N_popped)
	print("Nodes Expanded: ",N_Expanded)
	print("Nodes Generated: ",N_Gen)
	print("Max Fringe Size: ",mx1)
	if flag==1:
		print("Solution Found at depth ",sz)
		print("Steps")
		for x in range (0,sz):
			print("Move",count[x],path[x])
	else:
		print("Solution not found")

	
        
        


        




