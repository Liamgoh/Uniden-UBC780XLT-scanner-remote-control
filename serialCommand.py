from SerialPort import serialIO
#from Channel import Channel

class serialCommand:
    def __init__(self,channelNum):
        self.__channelNum = channelNum

    def viewScannerChannel(self, channelNum):
        self.__channelNum = channelNum
        channelNumPadded = str("{0:0>3}".format(channelNum))
        inputTxt = []
        inputTxt.append('MA' + channelNumPadded)
        outTxt = serialIO(inputTxt)
        #channelTxt = ''
        #channelTxt = 'Freq: ' + outTxt[6:10] + '.' + outTxt[10:14] + 'MHz'
        #channelTxt = ''
        #outTxtFreq = outTxt[6:14]
        #return(channelTxt.join(outTxtFreq))
        #return(outTxt, channelTxt)
        outTxtFreq = outTxt[6:14]
        # list comprehension. Turns list to string.
        # Works for list with mixed element types (if applicable)
        channelTxt = ''.join([str(element) for element in outTxtFreq])
        return channelTxt

    # def programScannerChannel(self, channelNum, channel):
    #     self.__channelNum = channelNum
    #     self._channel = channel
    #     channelNumPadded = str("{0:0>3}".format(channelNum))
    #     freqStr = str("{0:0>8}".format(round(channel.viewFreq())))
    #     #print(freqStr)
    #     inputTxt = 'PM' + str(channelNumPadded) + ' ' + freqStr
    #     outTxt = serialIO(inputTxt)
    #     return(outTxt)

    def programScannerChannel(self, channelNum, channel): #list version
        self.__channelNum = channelNum
        self._channel = channel
        channelNumPadded = str("{0:0>3}".format(channelNum))
        inputTxt = []
        freqStr = str("{0:0>8}".format(round(channel.viewFreq())))
        #print(freqStr)
        inputTxt.append('PM' + str(channelNumPadded) + ' ' + freqStr)
        modeStr = channel.viewMode()
        inputTxt.append('RM' + ' ' + modeStr)
        outTxt = serialIO(inputTxt)
        return(outTxt)

    #def readScannerBanks(selfself, ):


