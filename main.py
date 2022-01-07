# Write a Python program that opens a file for input and prints the count of four letter words in it 
txt = open("file1.txt")
lst=[]
count=0;
lst = txt.read().split()
for i in lst:
  if (len(i)==4):
    count=count+1
print(count)
    