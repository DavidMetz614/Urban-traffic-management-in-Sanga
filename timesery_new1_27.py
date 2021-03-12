flowList=[]
winCount=1
winSize=1
flowCount=0
avg1117=[0,0,0,0,0,0,0]

with open("nf-chunk1_new.csv") as f:
    for line in f:
        flowList.append(line[:len(line)-1].split(','))
startTS=float(flowList[0][0])


flow=flowList.pop(0)
print (float(flow[12]))





    
