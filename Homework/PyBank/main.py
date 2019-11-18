import os 
import csv

#find the file (locate the path)
budget_csv=os.path.join("Resources","budget_data.csv")

#open the file 
with open(budget_csv, "r") as csvfile:
    
    # Create a csv reader
    csvreader = csv.reader(csvfile,delimiter=",")

    row_count = 0
    total = 0
    month=[]
    values=[]
    new_values=[]
    old_values=[]
    amount_change=[]
    
    # Loop through the rows
    for row in csvreader:
        
        # Skip the header
        if row_count > 0:
            total = total + int(row[1])
            # Last Value
            last_value = int(row[1])
            values.append(int(row[1]))
            month.append(row[0])
            

        # First Value
        if row_count == 1:
            first_value = int(row[1])

        # Count rows
        row_count = row_count + 1        
   #taking row 2 and everything below
    new_values=values[1:]
    old_values=values[:-1]
    #within for list 
    amount_change = [new-old for(new,old) in zip(new_values,old_values)]
    
    month_adjusted = month[1:]

    #greatest_inc = [max(x) for (x,y) in zip(amount_change, month_adjusted)]
  
    #print(greatest_inc)
   
    total_months = row_count - 1
    average_change = ((last_value - first_value) / (total_months -1))
    #absolutes=[abs(elem) for elem in values]
 
    
    print("Total Months equals",total_months)
    print("Total Profit Loss equals",total)
    print("Total Average Change equals", average_change)
    #print(amount_change)
    print("Maximum increase",max(amount_change))
    print("Maximum decrease",min(amount_change))

    
    

csvfile.close()




    
        
   

    


