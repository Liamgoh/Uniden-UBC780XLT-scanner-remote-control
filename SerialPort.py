import time
import serial

def serialIO(inputTxt):

    ser = serial. Serial(
        port = 'COM4',
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