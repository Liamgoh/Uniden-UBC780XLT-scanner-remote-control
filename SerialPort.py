import time
import serial

ser = None


class SerialConnection:
    def __init__(self):
        None

    def open_connection(self, port='', baudrate=0, requestOpen=0):
        self.__port = port
        self.__baudrate = baudrate
        self.__requestOpen = requestOpen
        # self.__portStr = portStr
        global ser
        # exitmethod = False
        if ser == None:
            strSuccess = 'Port successfully opened'
            strAlreadyOpen = 'COM port ' + str(self.__port) + ' is already in use'
            strError1 = 'Invalid port number or Port is already in use'
            try:
                ser = serial.Serial(
                    port,
                    baudrate,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    # xonxoff = serial.False
                )
                if ser.isOpen():
                    return strSuccess
                else:
                    return strAlreadyOpen
            except (OSError, serial.SerialException):
                return strError1

        # elif requestOpen == 1:
        #     strError3 = 'Port ' + str(self.__port) + ' already opened by this program!'
        #     return strError3
        else:
            # if  # enhance to detect if trying to open a new connection on already opened COM port by the program...
            return ser  # ...otherwise this returns the already opened ser object

    # def serObj(self):
    #     self.open_connection(self)
    #     return self.ser

    def close_connection(self):
        if ser.isOpen():
            ser.close()
            strClosed = 'Connection closed'
            return strClosed
        else:
            strPortNotOpen = 'Port has not been opened. Cannot close connection.'
            return strPortNotOpen

    def serialIO(self, inputTxt, ser):
        # if ser is None:  # exit if no port opened
        #     return 'No connection'
        # else:
        strValue = []
        for i in range(len(inputTxt)):
            txt = inputTxt[i].upper()
            # print(txt)  # to debug the string sent to scanner
            ser.write(str.encode(txt + '\r'))
            time.sleep(0.035)  # experiment for fastest speed to read/write
            while ser.inWaiting() > 0:
                out = ser.readline(1)
                strValue.append(out.decode('utf-8'))
        return strValue


'''

def serialIO(inputTxt):

    ser = serial.Serial(
        port = 'COM1',
        baudrate = 19200,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS
        #xonxoff = serial.False
    )

    # ser.isOpen()
    # txt = inputTxt.upper()
    # ser.write(str.encode(txt + '\r'))
    # time.sleep(0.03)
    # strValue = ''
    # while ser.inWaiting() > 0:
    #     out = ser.readline(1)
    #     strValue += out.decode('utf-8')
    # return(strValue)
    # ser.close()

    ser.isOpen() #list version
    strValue = []
    for i in range(len(inputTxt)):
        txt = inputTxt[i].upper()
        print(txt)
        ser.write(str.encode(txt + '\r'))
        time.sleep(0.03)
        while ser.inWaiting() > 0:
            out = ser.readline(1)
            strValue.append(out.decode('utf-8'))
    return (strValue)
    ser.close()

    # while True:
    #     print('Enter your commands below.\r\nType "exit" to leave the application')
    #     txt = input('>>')
    #     checktxt = txt.upper()
    #     if checktxt == 'EXIT':
    #         ser.close()
    #         exit()
    #     else:
    #         ser.write(str.encode(txt + '\r'))
    #         time.sleep(1)
    #         strValue = ''
    #         while ser.inWaiting() > 0:
    #             out = ser.readline(1)
    #             strValue += out.decode('utf-8')
    #         print(strValue)

'''
