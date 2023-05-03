tuple=(10,20,30,10,10,50,60);
#Number of occurrance of 10 without in build function:-
count=0;
for x in tuple:
    if x==10:
        count=count+1;
print(count);

#with in build function:-
print(tuple.count(10));

#concat touples elements:-

tuple=("B",'O','O','K');
output="";
for s in tuple:
    output=output+s;
print(output);

#Write a program to display sum of all the number in a given tuple:-

tuple=(1,2,3,'A','B',4,'Sun');
sum=0;
for i in tuple:
    if isinstance(i,int):
        sum=sum+i;
print(sum);
