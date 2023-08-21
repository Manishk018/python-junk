import random
import matplotlib.pyplot as plt

class RandomOne:
    def isWin(self, selected, removed, d1, d2, d3):
       if removed==0:
           if selected==1:
               if d2==1:
                   return True
               else:
                    return False
           else:
               if d3==1:
                   return True
               else:
                   return False
               
       elif removed==1:
           if selected==2:
               if d3==1:
                   return True
               else:
                   return False
           else:
               if d1==1:
                   return True
               else:
                   return False
               
       else:
           if selected==0:
               if d1==1:
                   return True
               else:
                   return False
           else:
               if d2==1:
                   return True
               else:
                   return False
           

    def get_three_values(self):
        # Generate a list with two 0s and one 1 randomly arranged
        values = [0, 0, 1]
        random.shuffle(values)
        
        # Return the three variables
        return values[0], values[1], values[2]
    
    def remove1door(self,selected,d1,d2,d3):
        if selected==0:
            if d2==1:
                return 2
            else:
                return 1
        elif selected==1:
            if d3==1:
                return 0
            else:
                return 2
        else:
            if d1==1:
                return 1
            else:
                return 0

# Usage example:
random_one = RandomOne()

win=0
loose=0

results = []

switch=0
switch=int(input('Do you want to run simulation door switch?(0/1) : '))
itr=int(input('Run simulation for..? : '))

for i in range(itr):
    d1, d2, d3 = random_one.get_three_values()
    # print(d1, d2, d3)
    selected=random.randint(0,2)
    # print('Selected:',selected)
    removed=random_one.remove1door(selected,d1,d2,d3)
    # print('removed:',removed)
    res=random_one.isWin(selected,removed,d1,d2,d3)
    # print('win?:',res)
    if switch==0:
        if res==True:
            win+=1
        else:
            loose+=1
    else:
         if res==True:
            loose+=1
         else:
            win+=1
    results.append("Win" if res else "Lose")

# Count the occurrences of each result
win_count = results.count("Win")
lose_count = results.count("Lose")

# Plot a pie chart
labels = ['Wins', 'Losses']
sizes = [win_count, lose_count]
colors = ['green', 'red']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures the pie is circular.
plt.title('Distribution of Wins and Losses')
plt.show()

if switch==0:  
    print('When there was no door switch done!')
else:
    print('When there was door switch done!')
print('win:      ',win)
print('loose:    ',loose)