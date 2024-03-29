#Task2
#1.Read content from a file and write it into another one.
f1=open("_File1.txt","rt")
content=f1.read()
f2=open("_File2.txt","wt")
f2.write(content)
f1.close
f2.close 

#2.To write a dictionary in a file

dict={
    "college":"NITP","city":"Patna","country":"India"
}
with open("_File1.txt", 'w') as f1:  
    for key, value in dict.items():  
        f1.write('%s:%s\n' % (key, value))
        f1.close()


#3.Find size of a file in python
        
import os
f= os.path.getsize("./_File1.txt")
print(" Size of file is :",f)

#4.Find the most repeated word in a file

file = open("_File1.txt","r")
repeat = ""
freq = 0
words = []

for line in file:
	line_word = line.lower().replace(',','').replace('.','').split(" "); 
	for w in line_word: 
		words.append(w); 
for i in range(0, len(words)): 
	count = 1;  
	for j in range(i+1,len(words)): 
		if(words[i]==words[j]): 
			count=count + 1; 
	if(count > freq): 
		freq=count; 
		repeat=words[i]; 
print("Most repeated word: "+repeat)
print("Frequency: "+str(freq))
file.close();

#5.Read specific Lines from a file
 
f=open("_File1.txt","rt")
content=file.readlines() 
print("fifth line") 
print(content[4]) 
print("first five lines") 
print(content[0:5]) 
