import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, 'r') as csvfile:

    data = csv.reader(csvfile, delimiter=',')
    header = next(data)

    for row in data:                       

        row_count = 1 + sum(1 for row in data) 
    

with open(csvpath, 'r') as csvfile:

    data = csv.reader(csvfile, delimiter=',')

    
    header = next(data)

    c1 = "Khan"

    c2 = "Correy"

    c3 = "Li"

    c4 = "O'Tooley"

    khan_votes = 0

    correy_votes = 0

    li_votes = 0

    otoo_votes = 0

    for row in data:

        if row[2] == c1:

            khan_votes = khan_votes + 1
   

        if row[2] == c2:

            correy_votes = correy_votes + 1
       

        if row[2] == c3:

            li_votes = li_votes + 1    

        if row[2] == c4:

            otoo_votes = otoo_votes + 1

    pkhan = (khan_votes/row_count)*100

    percent_khan = round(pkhan,2)


    pcorrey = (correy_votes/row_count)*100

    percent_correy = round(pcorrey,2)
    

    pli = (li_votes/row_count)*100

    percent_li = round(pli,2)

   

    potoo = (otoo_votes/row_count)*100

    percent_otoo = round(potoo,2)

   

    d = {"Khan": percent_khan, "Correy": percent_correy, "Li": percent_li, "O'Tooley": percent_otoo}

    

    winner = max(d, key=d.get)

    

    print("   Election Results") 

    print("---------------------------------------------------------")

    print(f'Total votes:{row_count}')

    print(f'Khan:      {percent_khan} % ({khan_votes})')

    print(f'Correy:    {percent_correy} % ({correy_votes})')

    print(f'Li:        {percent_li} % ({li_votes})')

    print(f"O'Tooley:  {percent_otoo} % ({otoo_votes})")

    print("---------------------------------------------------------")

    print(f'The winner is: {winner}')

    print("---------------------------------------------------------")

    f= open("PyPoll.txt","w+")

    f.write("   Election Results\r\n") 

    f.write("-------------------------------------------------------\r\n")

    f.write(f'Total votes:{row_count}\r\n')

    f.write(f'Khan:      {percent_khan} % ({khan_votes})\r\n')

    f.write(f'Correy:    {percent_correy} % ({correy_votes})\r\n')

    f.write(f'Li:        {percent_li} % ({li_votes})\r\n')

    f.write(f"O'Tooley:  {percent_otoo} % ({otoo_votes})\r\n")

    f.write("-------------------------------------------------------\r\n")

    f.write(f'The winner is: {winner}\r\n')

    f.write("-------------------------------------------------------\r\n")
