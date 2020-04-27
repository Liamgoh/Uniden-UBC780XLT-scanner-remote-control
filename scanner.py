from Channel_module import Channel
from csvfile import write_csv, read_csv_program_scanner
from serialCommand_module import serialCommand
import inputCheck
import SerialPort
from tkinter import *
from tkinter import scrolledtext

ChannelList = []
minChannel = 1
maxChannel = 500
inputValidation = {}
connection = None


def scanner():
    global ChannelList
    global minChannel
    global maxChannel
    global inputValidation
    global connection

    inputValidation = {
        'channelRange': [minChannel, maxChannel],
        'freqRange': [[25, 512], [806, 956], [1240, 1300]],
        'validModes': ['AM', 'FM', 'NFM', 'WFM'],
        'validSteps': [5, 10, 12.5, 50, 100],
        'validDelay': [1, 4],
        'validChars': 16,
        'validPriorityLockout': ['Y', 'N']
    }

    minRange = str(inputValidation['channelRange'][0])
    maxRange = str(inputValidation['channelRange'][1])
    permissableFreqRanges = str(inputValidation['freqRange'])
    modeChoices = str(inputValidation['validModes'])
    stepChoices = str(inputValidation['validSteps'])
    delayChoices = str(inputValidation['validDelay'])
    maxChars = int(inputValidation['validChars'])
    validEntries = str(inputValidation['validPriorityLockout'])

    error = False
    ChannelList = [Channel(i) for i in range(maxChannel)]  # list comprehension
    # ChannelList = [Channel(i) for i in range(maxChannel - 1)]  # list comprehension
    # for i in range(maxChannel):
    #  ChannelList.append(Channel(i))

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
11. Open serial port
12. Close serial port
13. Scan
14. MAN (manual) key press
15: Exit        
    """

    quit = False
    while not quit:

        choice = inputCheck.inputException(menuChoices, 'integer', False, menuChoices, '', '')
        print('Menu choice is:', choice)

        if choice == 1:

            inputText = 'Enter the channel number to create. Range between: ' + minRange + ' and ' + maxRange
            channelNum = inputCheck.inputException(inputText, 'integer', False, '', 'channelRange', inputValidation)
            print('Channel is:', channelNum)

            inputText = 'Enter the frequency in MHz. Allowable ranges: ' + permissableFreqRanges
            freq = inputCheck.inputException(inputText, 'float', False, '', 'freqRange', inputValidation)
            print('Frequency is:', freq, 'MHz')

            inputText = 'Enter mode. Mode choices: ' + modeChoices
            mode = inputCheck.inputException(inputText, 'string', True, '', 'validModes', inputValidation)
            print('Mode is:', mode)

            inputText = 'Enter step. Step choices: ' + stepChoices
            step = inputCheck.inputException(inputText, 'float', False, '', 'validSteps', inputValidation)
            print('Step is:', step)

            inputText = 'Enter delay. Integer values between: ' + delayChoices
            delay = inputCheck.inputException(inputText, 'integer', False, '', 'validDelay', inputValidation)

            inputText = 'Enter alpha tag. Maximum characters: ' + str(maxChars)
            alphaTag = inputCheck.inputException(inputText, 'string', False, '', 'validChars', inputValidation)
            print('Alpha tag is:', alphaTag)

            inputText = 'Priority channel. Enter: ' + str(validEntries)
            priority = inputCheck.inputException(inputText, 'string', True, '', 'validPriorityLockout', inputValidation)

            inputText = 'Lockout channel? Enter:' + str(validEntries)
            lockout = inputCheck.inputException(inputText, 'string', True, '', 'validPriorityLockout', inputValidation)
            print('Lockout channel:', lockout)

            channel = Channel(channelNum, freq, mode, step, delay, alphaTag, priority, lockout)
            ChannelList.insert(channelNum - 1, channel)

        elif choice == 2:

            error = True
            while error:
                try:
                    channelNum = int(input('Enter channel number\n'))
                    error = False
                except ValueError:
                    print('Please enter an integer between', minChannel, 'and', maxChannel, '!\n')  # enhance to
                    # check between min & max channels
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
                print(i)
                channel = ChannelList[i]
                print(len(ChannelList))
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
            inputText = 'Enter the channel number to create. Range between: ' + minRange + ' and ' + maxRange
            channelNum = inputCheck.inputException(inputText, 'integer', False, '', 'channelRange', inputValidation)

            inputText = 'Enter the frequency in MHz. Allowable ranges: ' + permissableFreqRanges
            freq = inputCheck.inputException(inputText, 'float', True, '', 'freqRange', inputValidation) * 10000  #
            # eg format to use to speak to communicate with scanner: 243MHz = 2430000

            inputText = 'Enter mode. Mode choices: ' + modeChoices
            mode = inputCheck.inputException(inputText, 'string', True, '', 'validModes', inputValidation)

            inputText = 'Enter step. Step choices: ' + stepChoices
            step = inputCheck.inputException(inputText, 'float', False, '', 'validSteps', inputValidation)

            inputText = 'Enter delay. Integer values between: ' + delayChoices
            delay = inputCheck.inputException(inputText, 'integer', False, '', 'validDelay', inputValidation)

            inputText = 'Enter alpha tag. Maximum characters: ' + str(maxChars)
            alphaTag = inputCheck.inputException(inputText, 'string', False, '', 'validChars', inputValidation)

            inputText = 'Priority channel. Enter: ' + str(validEntries)
            priority = inputCheck.inputException(inputText, 'string', True, '', 'validPriorityLockout', inputValidation)

            inputText = 'Lockoutchannel? Enter: ' + str(validEntries)
            lockout = inputCheck.inputException(inputText, 'string', True, '', 'validPriorityLockout', inputValidation)

            channel = Channel(channelNum, freq, mode, step, delay, alphaTag, priority, lockout)
            scannerChannel = serialCommand(channelNum)
            print(scannerChannel.programScannerChannel(channelNum, channel))

        elif choice == 9:
            bankNum = int(input('Enter a bank number to read'))
            readBank(bankNum)

        elif choice == 10:
            readAll(maxChannel)

        elif choice == 11:  # add exception handling for integer port numbers & permissable baud rates: 2400, 4800,
            # 9600, 19200...
            port = int(input('Enter COM port to connect to scanner'))
            portStr = 'COM' + str(port)
            baudrate = int(input('Enter baudrate'))
            connection = SerialPort.SerialConnection()
            print(connection.open_connection(portStr, baudrate, 1))

        elif choice == 12:
            try:
                print(connection.close_connection())
            except AttributeError:  # COM port has not been opened yet...
                print('COM port has not been opened yet.')

        elif choice == 13:
            scan = '1'
            dummy_channel = serialCommand(scan)
            # scanner_mode = dummy_channel.checkMode()  # no need to check scanner mode of operation...
            # if scanner_mode == '00':
            #     scanner_mode = dummy_channel.manualMode()
            #     print('Manual mode')
            # else:
            #     scanner_mode = dummy_channel.scanMode()
            #     print('Scan mode')
            dummy_channel.scanMode()

        elif choice == 14:
            scan = '1'
            dummy_channel = serialCommand(scan)
            # scanner_mode = dummy_channel.checkMode()  # no need to check scanner mode of operation...
            # if scanner_mode == '00':
            #     scanner_mode = dummy_channel.manualMode()
            #     print('Manual mode')
            # else:
            #     scanner_mode = dummy_channel.scanMode()
            #     print('Scan mode')
            dummy_channel.manualMode()

        elif choice == 15:
            quit = True

        else:
            print('Invalid menu choice')


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
            outTxt = scannerChannelCommand.viewScannerChannel(channelNumStr)
            freq = float(outTxt[6:14]) / 10000
        print(channelNum, freq)
        scannerChannel = Channel(channelNum, freq)
        ChannelList[channelNum] = scannerChannel
    print(ChannelList)

def freq_display():
    inputTxt = []
    inputTxt.append('MA')  # get frequency
    serialportObj = SerialPort.SerialConnection()
    ser = serialportObj.open_connection()
    outTxt = serialportObj.serialIO(inputTxt, ser)
    #channelTxt = 'Freq: ' + outTxt[6:10] + '.' + outTxt[10:14] + 'MHz'
    outTxtFreq = outTxt[6:13]
    channelTxt = ''.join([str(element) for element in outTxtFreq])
    outFreq = float(channelTxt) / 1000
    outFreq4dp = "{:.4f}".format(outFreq)
    display_message = 'Freq: ' + outFreq4dp + 'MHz'
    window = Tk()
    window.title("Frequency")
    window.geometry('350x200')
    txt = scrolledtext.ScrolledText(window, font='Verdana 11', width=40, height=10)
    txt.grid(column=0, row=0)
    txt.insert(INSERT, display_message)
    window.mainloop()



