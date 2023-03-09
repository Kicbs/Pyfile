'''
# Open a new file for writing
with open("data.txt", "w") as f:
    # Open the log file for reading
    with open("access.log", "r") as g:
        # Loop through each line
        for line in g:
            # Split the line by -
            data, data1, data2 = line.partition(" - ")
            # Write the data to the new file
            f.write(data + "\n")
            f.write(data1 + "\n")
            f.write(data2 + "\n")

# Import re module for regular expression
#import re
'''
# Open log file for reading
with open("access.log", "r") as f:
    # Initialize an empty dictionary
    ip_dict = {}
    # Loop through each line
    for line in f:
        ip, data1, data2 = line.partition(" - ")
        # Check if IP address is already in dictionary
        if ip in ip_dict:
            # Append timestamp to existing list
            ip_dict[ip].append(data2)
        else:
            # Create a new list with timestamp
            ip_dict[ip] = [data2]

# Open new file for writing
with open("data345.txt", "w") as g:
    # Loop through dictionary items
    for key, value in ip_dict.items():
        # Write IP address, count, first time and last time to file
        g.write(f"{key} {len(value)} {value[0][3:29]} {value[-1][3:29]}\n")
        
