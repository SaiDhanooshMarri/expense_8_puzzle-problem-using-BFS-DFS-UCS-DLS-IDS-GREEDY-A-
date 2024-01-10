import sys

def startrowcolvalue(start):
    for i in range(0,3):
        for j in range(0,3):
            if start[i][j]==0:
                return i,j

def main():     
    stt=sys.argv[1:]
    st=stt[0]
    go=stt[1]
    algo=stt[2]
    algo=algo.lower()
    if len(stt)==4:
        x1=stt[3]
        x1=x1.lower() 
    else:
        x1=False
    if algo=="dls":       
        x=input("Please enter the depth limit: ")
        x=int(x)
    if x1=="true":
        dump=True
    else:
        dump=False
    s=open(st,"r")
    g=open(go,"r")
    sstart=[]
    startt=[]
    start=[]
    ggoal=[]
    goall=[]
    goal=[]
    for lines in s:
        sstart.append(lines)
    sstart.pop()
    for sub in sstart:
        startt.append(sub.replace("\n", ""))

    for lines in g:
        ggoal.append(lines)
    ggoal.pop()
    for sub in ggoal:
        goall.append(sub.replace("\n", ""))
    for v in startt:
        start.append(v.split(" "))
    for v in goall:
        goal.append(v.split(" "))
    i=0
    j=0
    for h in range(3):
        for h1 in range(3):
            start[h][h1]=int(start[h][h1])
            goal[h][h1]=int(goal[h][h1])
    
    i,j=startrowcolvalue(start)
    
    match algo:
        case "bfs":
            from bfs import bfs
            bfs(start,goal,i,j,dump)
        case "ucs":
            from ucs import ucs
            ucs(start,goal,i,j,dump)
        case "dfs":
            from dfs import dfs
            dfs(start,goal,i,j,dump)
        case "dls":
            from dls import dls
            dls(start,goal,i,j,x,dump)
        case "greedy":
            from greedy import greedy
            greedy(start,goal,i,j,dump)
        case "a*":
            from a_star import a_star
            a_star(start,goal,i,j,dump)
        case "ids":
            from ids import ids
            ids(start,goal,i,j,dump)


if __name__ == "__main__":
   main()