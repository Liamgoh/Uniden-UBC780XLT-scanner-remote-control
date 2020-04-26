import csv
from Channel import Channel
from serialCommand import serialCommand

def write_csv(ChannelList):
    with open('channels.csv', mode = 'w', newline = '') as file:
        writer = csv.writer(file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        headerRow = ['Channel', 'Frequency', 'Mode', 'Step', 'Delay', 'Alpha tag', 'Priority', 'Lock out']
        writer.writerow(headerRow)
        maxChannel = len(ChannelList)
        for i in range(1,maxChannel):
            #channelNum in ChannelList:
            channel = ChannelList[i]
            channelNum = str(i)
            freq = str(channel.viewFreq())
            mode = str(channel.viewMode())
            step = str(channel.viewStep())
            delay = str(channel.viewDelay())
            alphaTag = str(channel.viewAlphaTag())
            priority = str(channel.viewPriority())
            lockout = str(channel.viewLockout())
            writer.writerow([channelNum, freq, mode, step,delay, alphaTag, priority, lockout])

def read_csv_program_scanner():
    channelList = []
    print('option 6')
    with open('channels.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ',')

        #create a channel list of row data (i.e. a list of lists) using list cmprehension
        channelList = [row for row in readCSV]
        del channelList[0] #remove header row



        for channel in channelList:
            print(channel[0])
            print(channel[1])
            channelNum = int(channel[0])
            freq = float(channel[1]) * 10000
            mode = str(channel[2])
            # step = channel[3]
            # delay = channel[4]
            # alphaTag = channel[5]
            # priority = channel[6]
            # lockout = channel[7]
            channel = Channel(channelNum, freq, mode)
            #print('csv channel data: ', channel)
            scannerChannel = serialCommand(channelNum)
            scannerChannel.programScannerChannel(channelNum, channel)

    csvfile.close()
    return None


