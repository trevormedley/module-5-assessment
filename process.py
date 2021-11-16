# This line is using the open method to gather the data from the um-server-01.txt file
log_file = open("um-server-01.txt")

#In python, def is used to define a function. In this case the function sales_reports is being declared and taking in the variable log_file as the input. log_file is the variable holding the data from the um-server-01.txt file that we opened above. In the function we are running a loop that first applying the .rstrip() method that removes any trailing characters from the line. In the next line we are setting the variable day to the 0 index of the line, and capturing the first 3 characters. We then run an if statement seeing if the day variable we declared is equal to the day of the week we are searching for. If day is equal to what we are looking for, we print the entire line. 

def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)

#The syntax below runs the function defined above
sales_reports(log_file)

log_file = open("um-server-01.txt")

def melon_count (log_file):
    for line in log_file:
        line = line.split()
        delivered = line[2]
        if int(delivered) >= 10:
            print(line);
        
melon_count(log_file)