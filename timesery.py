flowList=[]
winCount=1
winSize=1
flowCount=0
avg1117=[0,0,0,0,0,0,0]

with open("norm14-4-2013-8-9h.csv") as f:
    for line in f:
        flowList.append(line[:len(line)-1].split(','))
startTS=float(flowList[0][0])
while len(flowList)>0:
    flow=flowList.pop(0)
    if int((float(flow[0])-startTS)/winSize)<winCount:
        flowCount+=1
        for i in range(7):
            avg1117[i]+=int(flow[i+10])
    else:
        for i in range(7):
            avg1117[i]=round(float(avg1117[i])/flowCount,2)
        print winCount,",",flowCount,",",avg1117
        for i in range(int((float(flow[0])-startTS)/winSize)-winCount):
            winCount+=1
            print winCount,",",0,",",[0,0,0,0,0,0,0]
        winCount+=1                   
        flowCount=1
        avg1117=[int(flow[10]),int(flow[11]),int(flow[12]),int(flow[13]),int(flow[14]),int(flow[15]),int(flow[16])]
        
for i in range(7):
    avg1117[i]=round(float(avg1117[i])/flowCount,2)
print winCount,",",flowCount,",",avg1117

    
