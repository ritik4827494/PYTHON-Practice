#merging two list
List=[];
for i in range(4):
    List.append(i);
l=len(List);
print(List[l-1]);
List1=[34,12,2,4,1];
for x in List1:
    List.append(x);
print(List);

#finding highest and lowest in List
high=List[0];
Low=List[0];
for j in List:
    if(j>high):
        high=j;
    elif(j<Low):
        Low=j;
print(high);
print(Low);