def TowerofHanoi(n,source,destination,auxilary):
    if n==1:
        print("move disk1 from source",source,"to destination",destination)
        TowerofHanoi(n-1,source,auxilary,destination)
        print("move disk",n, "from source",source,"to destination",destination)
        TowerofHanoi(n-1,auxilary,destination,source)
n = 4
TowerofHanoi(n,'A','B','C')
