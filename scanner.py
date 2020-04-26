import Channel
import csvfile
import serialCommand

ChannelList = []

def scanner():
    minChannel = 1
    maxChannel = 500
    global ChannelList
    error = False
    ChannelList = [Channel.Channel(i) for i in range(maxChannel - 1)] #list comprehension
    #for i in range(maxChannel):
     #   ChannelList.append(Channel(i))

    menuChoices = """
Choose a menu item:
1: Create a new channel in internal memory
2: View channel in internal memory
3: Delete channel in internal memory
4: Write channels to csv
5: View all current channels in internal memory
6: Program scanner from csv file
7: View scanner channel
8: Write scanner channel
9: Read scanner bank(s)
10: Read all scanner channels
11: Exit        
    """

    while True:
        quit = False
        invalidMenuChoice = False
        while quit == False:
            error = True
            while error == True:
                try:
                    choice = int(input(menuChoices))
                    error = False
                except ValueError:
                    print('Please enter an integer!\n')

            if choice == 1:

                error = True
                while error == True:
                    try:
                        channelNum = int(input('Enter the channel number to create\n'))
                        error = False
                    except ValueError:
                        print('Please enter an integer!\n') #enhance to check between min & max channels

                error = True
                while error == True:
                    try:
                        freq = float(input('Enter frequency in MHz\n'))
                        error = False
                    except ValueError:
                        print('Please enter a float!\n') #enhance to check frequency range of scanner

                error = True
                while error == True:
                    try:
                        mode = str(input('Enter mode: AM, FM, NFM, WFM\n'))
                    except ValueError:
                        print('Please enter a string!\n') #enhance to ensure a valid mode
                    else:
                        if mode.isalpha() == True:
                            error = False
                        else:
                            print('Please enter only letters!\n')

                error = True
                while error == True:
                    try:
                        step = float(input('Enter step\n'))
                        error = False
                    except ValueError:
                        print('Please enter a float!\n') #enhance to ensure valid step

                error = True
                while error == True:
                    try:
                        delay = int(input('Enter delay\n'))
                        error = False
                    except ValueError:
                        print('Please enter a float!\n') #enhance to ensure valid delay

                error = True
                while error == True:
                    try:
                        alphaTag = str(input('Enter alpha tag\n'))
                        error = False
                    except ValueError:
                        print('Please enter a string!\n') #enhance to ensure within max number of characters

                error = True
                while error == True:
                    try:
                        priorityStr = str(input('Priorty y or n?\n'))
                    except ValueError:
                        print('Enter y or n\n')
                    else:
                        if priorityStr.isalpha() == True:
                            if priorityStr == 'y':
                                priority = True
                            else:
                                priority = False
                            error = False
                        else:
                            print('Please enter only letters!')

                error = True
                while error == True:
                    try:
                        lockoutStr = str(input('Lockout y or n?\n'))
                    except ValueError:
                        print('Enter y or n\n')
                    else:
                        if lockoutStr.isalpha() == True:
                            if lockoutStr == 'y':
                                lockout = True
                            else:
                                lockout = False
                            error = False
                        else:
                            print('Please enter only letters!')

                channel = Channel.Channel(channelNum, freq, mode, step, delay, alphaTag, priority, lockout)
                ChannelList.insert(channelNum - 1,channel)

            elif choice == 2:


                error = True
                while error == True:
                    try:
                        channelNum = int(input('Enter channel number\n'))
                        error = False
                    except ValueError:
                        print('Please enter an integer between', minChannel, 'and', maxChannel,'!\n')  # enhance to check between min & max channels
                    else:
                        if channelNum < minChannel or channelNum > maxChannel:
                            print('Channel out of range')
                        else:
                            channel = ChannelList[channelNum - 1]
                            print('Properties of channel', channelNum)
                            print('Frequency: ', channel.viewFreq())
                            print('Mode: ', channel.viewMode())
                            print('Step: ', channel.viewStep())
                            print('Delay: ', channel.viewDelay())
                            print('Alpha tag: ', channel.viewAlphaTag())
                            print('Priority: ', channel.viewPriority())
                            print('Lockout: ', channel.viewLockout())

            elif choice == 3:
                channelNum = int(input('Enter channel number to delete\n'))
                channel = Channel(channelNum)
                ChannelList.insert(channelNum - 1, channel)

            elif choice == 4:
                 write_csv(ChannelList)

            elif choice == 5:
                for i in range(maxChannel):
                    channel = ChannelList[i]
                    channelNum = i + 1
                    print('Properties of channel', channelNum)
                    print('Frequency: ', channel.viewFreq())
                    print('Mode: ', channel.viewMode())
                    print('Step: ', channel.viewStep())
                    print('Delay: ', channel.viewDelay())
                    print('Alpha tag: ', channel.viewAlphaTag())
                    print('Priority: ', channel.viewPriority())
                    print('Lockout: ', channel.viewLockout())

            elif choice == 6:
                read_csv_program_scanner()

            elif choice == 7:
                channelNum = str(input('Enter scanner channel number\n'))
                scannerChannel = serialCommand(channelNum)
                print('Scanner data for channel', channelNum, 'is:', scannerChannel.viewScannerChannel(channelNum))

            elif choice == 8:
                #channelNum = str(input('Enter scanner channel number to program\n'))
                channelNum = int(input('Enter the channel number to create\n'))
                freq = float(input('Enter a frequency in format 243MHz = 2430000\n'))
                mode = str(input('Enter a mode\n').upper())
                #step = float(input('Enter a step\n'))
                #delay = int(input('Enter a delay\n'))
                #alphaTag = str(input('Enter an alpha tag\n'))
                #priorityStr = str(input('Priority y or n?\n'))
                #if priorityStr == 'y':
                 #   priority = True
                #else:
                 #   priority = False
                #lockoutStr = str(input('Lockout y or n?\n'))
                #if lockoutStr == 'y':
                 #   lockout = True
                #else:
                 #   lockout = False
                channel = Channel(channelNum, freq, mode)
                scannerChannel = serialCommand(channelNum)
                print(scannerChannel.programScannerChannel(channelNum, channel))

            elif choice == 9:
                bankNum = int(input('Enter a bank number to read'))
                readBank(bankNum)

            elif choice == 10:
                readAll(maxChannel)

            elif choice == 11:
                quit = True

            else:
                print('Invalid choice')
                invalidMenuChoice = True
                   # else:
                      #  print('Invalid account id')



def readBank(bankNum):
    if bankNum == 1:
        startChannel = 1
        endChannel = 50
    elif bankNum == 2:
        startChannel = 51
        endChannel = 100
    elif bankNum == 3:
        startChannel = 101
        endChannel = 150
    elif bankNum == 4:
        startChannel = 151
        endChannel = 200
    elif bankNum == 5:
        startChannel = 201
        endChannel = 250
    elif bankNum == 6:
        startChannel = 251
        endChannel = 300
    elif bankNum == 7:
        startChannel = 301
        endChannel = 350
    elif bankNum == 8:
        startChannel = 351
        endChannel = 400
    elif bankNum == 9:
        startChannel = 401
        endChannel = 450
    elif bankNum == 10:
        startChannel = 4511
        endChannel = 500
    else:
        print('Invalid bank selected')
    global ChannelList
    ChannelList = [Channel(i) for i in range(startChannel, endChannel + 2)]
    for channelNum in range(startChannel, endChannel + 1):
        scannerChannelCommand = serialCommand(channelNum)
        channelNumStr = str(channelNum)
        if scannerChannelCommand.viewScannerChannel(channelNumStr) == '':
            freq = 0
        else:
            freq = float(scannerChannelCommand.viewScannerChannel(channelNumStr)) / 10000
        print(channelNum, freq)
        scannerChannel = Channel(channelNum, freq)
        ChannelList[channelNum] = scannerChannel
    print(ChannelList)

def readAll(maxChannel):
    global ChannelList
    ChannelList = [Channel(i) for i in range(1, maxChannel + 2)]
    for channelNum in range(1, maxChannel + 1):
        scannerChannelCommand = serialCommand(channelNum)
        channelNumStr = str(channelNum)
        if scannerChannelCommand.viewScannerChannel(channelNumStr) == '':
            freq = 0
        else:
            freq = float(scannerChannelCommand.viewScannerChannel(channelNumStr)) / 10000
        print(channelNum, freq)
        scannerChannel = Channel(channelNum, freq)
        ChannelList[channelNum] = scannerChannel
    print(ChannelList)









