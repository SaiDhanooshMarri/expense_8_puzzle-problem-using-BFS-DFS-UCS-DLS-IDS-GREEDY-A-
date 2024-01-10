from datetime import datetime




def childMatrix(row,col,startf,path,count,N_Gen):
	
	if row > 0:
		start1 = [row[:] for row in startf]
		start1[row][col],start1[row - 1][col] = start1[row - 1][col],start1[row][col]
		frindge.append((count+" "+str(start1[row][col]),path+' '+'DOWN', start1, row - 1, col))
		N_Gen+=1
	if col > 0:
		start2 = [row[:] for row in startf]
		
		start2[row][col],start2[row][col - 1] = start2[row][col - 1],start2[row][col]
		frindge.append((count+" "+str(start2[row][col]),path+' '+'RIGHT', start2, row, col - 1))
		N_Gen+=1
	if row < 2:
		start3 = [row[:] for row in startf]
		start3[row][col],start3[row + 1][col] = start3[row + 1][col],start3[row][col]
		frindge.append((count+" "+str(start3[row][col]),path+' '+'UP', start3, row + 1, col))
		N_Gen+=1
	if col < 2:
		start4 = [row[:] for row in startf]
		start4[row][col],start4[row][col + 1] = start4[row][col + 1],start4[row][col]
		frindge.append((count+" "+str(start4[row][col]),path+' '+'LEFT', start4, row, col + 1))
		N_Gen+=1
	return N_Gen
	

def ids(start,goal,i,j,dump):
	if dump==True:
		now = datetime.now()
		dt_string = now.strftime("%d_%m_%Y__%H_%M_%S")
		dt_string="IDS_dump//"+dt_string+".txt"
		f=open(dt_string,"a")
		f.write("Dump file for IDS: ")
	limit=0
	N_popped=0
	N_Expanded=0
	mx=0
	mx1=0
	list1=[]
	N_Gen=0
	start=start
	goal=goal
	global frindge
	ii=i
	jj=j
	global path
	path=None
	flag=0
	frindge=[]
	hi=start
	
	closed=[]
	while hi!=goal:
		ii=i
		jj=i
		frindge.clear()
		closed.clear()
		limit+=1
		frindge.append(('0','', start, ii, jj,path))
		while frindge:
			
            
            
			mx=len(frindge)
			if mx>mx1:
				mx1=mx
			new_tile=frindge.pop()
			N_popped+=1
			count=new_tile[0]
			path=new_tile[1]
			ii=int(new_tile[3])
			jj=int(new_tile[4])
			nN_Gen=N_Gen
			if new_tile[2]!=goal:
				if new_tile[2] not in closed:
					list1.clear()
					list1=new_tile[0].split(" ")
					lenlist=len(list1)
					
					if lenlist<=limit:
						N_Gen=childMatrix(ii,jj,new_tile[2],path,count,N_Gen)
						N_Expanded+=1
						closed.append(new_tile[2])
							
                
			else:
				flag=1
				hi=goal
				break
			if dump==True:
				lii=limit-1
				lii="\nLevel: "+str(lii)+"\n"
				f.write(lii)
				f.write("\nFrindge:[\n")
				for iii in frindge:
					state="State: "+str(iii[2])
					f.write(state)
					bb=iii[0].split(" ")
					bb2=iii[1].split(" ")
					bb3="{Move "+bb[-1]+" "+bb2[-1]+" }"
					f.write(bb3)
					f.write(" ]\n")

				f.write("\nNumber of new nodes generated:  ")
				nnn=N_Gen-nN_Gen
				nnn=str(nnn)
				f.write(nnn)
				f.write("\n\nClosed:")
				clo=str(closed)+"\n"
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
	
	
        
        


        


