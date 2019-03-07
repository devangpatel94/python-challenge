import os

import csv

months = []     

profitlist = []      

changelist = []     

profitsum = 0

csvpath = os.path.join('budget_data.csv')

with open(csvpath, 'r') as csvfile:

    data = csv.reader(csvfile, delimiter=',')

    header = next(data)

    for row in data:                           

        rowcount = 1 + sum(1 for row in data) 
      
with open(csvpath, 'r') as csvfile:

    data = csv.reader(csvfile, delimiter=',')

    headerline = next(data)

    for row in data:

        profitsum += int(row[1])

with open(csvpath, 'r') as csvfile:

    data = csv.reader(csvfile, delimiter=',')

    headerline = next(data)


    for row in data:                    

        months.append(row[0])           

        profitlist.append(float(row[1]))
 

    for i in range(1, len(profitlist)):

        change = profitlist[i] - profitlist[i-1] 

        changelist.append(change)
    x = len(changelist) 
 

    avgchange = sum(changelist) / x

    roundedavgchange = (round(avgchange,2))

    

    maxprofits = (max(changelist))

    monthmaxid = (changelist.index(max(changelist))) + 1

    monthmaxprofit = months[monthmaxid]

    

    minprofits =(min(changelist))

    monthminid = (changelist.index(min(changelist))) + 1

    monthminprofit = months[monthminid]


    print("   Financial Analysis") 

    print("--------------------------------------------------------------------------------")

    print(f'Total months:                       {rowcount}')

    print(f'Total:                              ${profitsum}')

    print(f'Average Change:                     ${roundedavgchange}')  

    print(f'Greatest increase in Profits:       {monthmaxprofit}  ${maxprofits}')   

    print(f'Greatest decrease in Profits:       {monthminprofit}  ${minprofits}')   
 
    f= open("PyBank.txt","w+")

    f.write("Financial Analysis\r\n") 

    f.write("--------------------------------------------------------------------------------\r\n")

    f.write(f'Total months:                       {rowcount}\r\n')

    f.write(f'Total:                              ${profitsum}\r\n')

    f.write(f'Average Change:                     ${roundedavgchange}\r\n')  

    f.write(f'Greatest increase in Profits:       {monthmaxprofit}  ${maxprofits}\r\n')   

    f.write(f'Greatest decrease in Profits:       {monthminprofit}  ${minprofits}\r\n')
