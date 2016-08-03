import matplotlib.pyplot as plt
import os.path

#naming the current directory
directory = os.path.dirname(os.path.abspath(__file__)) 

#open the data file for that year
filename = os.path.join(directory, 'powerball w&r csv.txt')
datafile = open(filename,'r')    #'r' means 'read-only'

frequency=[]
number=[]

minnum = None
maxnum = None 

#for each line in the file
for line in datafile:

    #split the line into the three separate pieces of info        
    num, white, red, total = line.split(',')

    if minnum is None:
        minnum = white
       
    elif white < minnum:
        minnum = white
    
    if maxnum is None:
        maxnum = white
    
    elif white > maxnum:
        maxnum = white

print maxnum
print minnum
        
#frequency.append(maxnum)
#number.append()

datafile.close()

fig, ax = plt.subplots(1,1)
ax.plot(number, frequency,'#0000FF')

ax.set_title('Powerball Numbers')

plt.xlabel('Number')
plt.ylabel('Frequency')

fig.show()
