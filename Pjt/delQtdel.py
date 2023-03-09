from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QTextEdit

app = QApplication([]) # initialize application
window = QWidget() # create main window
window.setWindowTitle("PyQt Trial") # set window title


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


combo_box = QComboBox(window) # create combo box
combo_box.addItems(ip_dict.keys())


label = QTextEdit(window) # create label
label.setText("Select IP Address") # set initial label text
label.setReadOnly(True)
label1 = QLabel(window)
#label1.setText("...")
label2 = QLabel(window)
label3 = QLabel(window)



def update_label(): # define function to update label text
    #item = combo_box.currentText() # get selected item text
    item=combo_box.currentText()
    value=ip_dict[item]
    #print(len(value))
    label.setText(f"Values are {value}") # set label text
    label1.setText(f"This IP have visited {len(value)} times")
    label2.setText(f"First time access was on {value[0][3:29]}")
    label3.setText(f"Recent access: {value[-1][3:29]}")
    
combo_box.currentTextChanged.connect(update_label) # connect signal and slot

combo_box.move(50, 50)
combo_box.resize(200, 30)
label.move(50, 100)
label.resize(200, 30)
label1.move(50, 150)
label1.resize(200, 30)# changes size of the label
label2.move(50, 200)
label2.resize(300, 30)
label3.move(50, 250)
label3.resize(300, 30)


window.show() # show window on screen
app.exec_() # run application loop
