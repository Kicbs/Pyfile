# Open a new file for writing
with open("data121.txt", "w") as f:
    # Open the log file for reading
    with open("access.log", "r") as g:
        # Loop through each line
        for line in g:
            # Split the line by -
            data, data1 , data2  = line.partition(" - ")
            # Write the data to the new file
            f.write(data + "\n")
            f.write(data1+ "\n")
            f.write(data2[2:5] + "\n")
