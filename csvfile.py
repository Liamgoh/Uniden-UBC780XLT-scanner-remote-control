import csv
from Channel_module import Channel
from serialCommand_module import serialCommand


def write_csv(ChannelList):
    with open('channels.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        headerRow = ['Channel', 'Frequency', 'Mode', 'Step', 'Delay', 'Alpha tag', 'Priority', 'Lock out']
        writer.writerow(headerRow)
        maxChannel = len(ChannelList)
        for i in range(1, maxChannel):
            # channelNum in ChannelList:
            channel = ChannelList[i]
            channelNum = str(i)
            freq = str(channel.viewFreq())
            mode = str(channel.viewMode())
            step = str(channel.viewStep())
            delay = str(channel.viewDelay())
            alphaTag = str(channel.viewAlphaTag())
            priority = str(channel.viewPriority())
            lockout = str(channel.viewLockout())
            writer.writerow([channelNum, freq, mode, step, delay, alphaTag, priority, lockout])


def read_csv_program_scanner():

    save_path = 'C:"\"'
    file_name = 'channels'
    complete_name = os.path.join(save_path, file_name+'.csv')

    channelList = []

    with open(complete_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # create a channel list of row data (i.e. a list of lists) using list comprehension
        channelList = [row for row in readCSV]
        csvfile.close()
        del channelList[0]  # remove header row
        for channel in channelList:
            channelNum = int(channel[0])
            freq = float(channel[1])
            mode = str(channel[2])
            step = float(channel[3])
            delay = int(channel[4])
            alphaTag = str(channel[5])
            priority = str(channel[6])
            lockout = str(channel[7])
            channel = Channel(channelNum, freq, mode, step, delay, alphaTag, priority, lockout)
            # print('csv channel data: ', channel)
            scannerChannel = serialCommand(channelNum)
            scannerChannel.programScannerChannel(channelNum, channel)
    return None
