from SerialPort import SerialConnection as sc

inputTxt = []
inputTxt.append('MA050')
ser=sc.serObj(sc)
outTxt = ser.serialIO(inputTxt)
print(outTxt)