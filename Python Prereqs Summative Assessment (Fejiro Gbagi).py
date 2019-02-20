import random as rd
import datetime as dt

#Append data to file so historical data is not overwritten and no data is lost
fhand = open("generated_output.txt","a+")

#Date and timestamp each interval of data collection
now = dt.datetime.now()
fhand.write('Date and Time Stamp: ' + str(now))
fhand.write('\n \n')

#Loop to generate data set
for i in range(1,33):
    readings = [rd.random() for reading in range(1,17)]
    fhand.write('Sensor {0}: {1}\n '.format(i,readings))

fhand.write('\n \n \n') #Blank line after each output for readability
fhand.close() #Close File


def corrupted_data():
    #Open previously generated output file and create a new file for recording errors
    xfile = open("error_log.txt","a+")
    yfile = open("generated_output.txt","r")
    stamp = ''
    for line in yfile:
        line = line.rstrip()
        if '2019-' in line:
            stamp = line #Store last TimeStamp
        if not 'err' in line:
            continue
        xfile.write(stamp)
        xfile.write('\n')  # For Readability
        xfile.write(line)
        xfile.write('\n \n') #For Readability

    xfile.close()
    yfile.close()

corrupted_data()



