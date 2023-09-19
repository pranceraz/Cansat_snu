import serial


'''   
give a better file name
gotta add a data collection threshold for values that are too simillar
also make a way to add headers to the columns
find the arduino port or is it XBEE???

'''
arduinoport = "COM3" # idk this well need to know the port for this  apparantly some COM5 Format
baud = 9600 #baud rate
file_n = "datatest.csv" # temp file name
collect = True # data collect state

ser = serial.Serial(arduinoport,baud)
print("connected to port" + arduinoport)
file = open(file_n,"a")# csv file created in append mode 
print("file made")

line_no=0 #counting line nos

while collect == True: #gotta fix this collect condition later cuz its always collecting lol
    get_data= str(ser.readline())
    data = get_data[0:][:-2]# slice this string better i just copied this slice from somwhere 
    print(data)


    file = open(file_n,"a") 
    file.write(data + "\n")
    line_no += 1
