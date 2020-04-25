import scanner


def inputException(inputText, inputTypeKey, isAlpha, menuChoices='', inputValidationKey='', inputValidation=''):
    inputType = {
        'integer': int,
        'float': float,
        'string': str
    }

    exceptionText = {
        'integer': 'Please enter an integer!\n',
        'float': 'Please enter a float!\n',
        'string': 'Please enter a string!\n'
    }

    typeStr = inputType[inputTypeKey]
    exceptionStr = exceptionText[inputTypeKey]

    if inputValidationKey != '':
        validationCheck = inputValidation[inputValidationKey]

    if menuChoices == '':  # if not choosing initial menu option
        error = True
        while error:
            try:
                userInput = typeStr(input(inputText))
            except ValueError:
                print(exceptionStr)
            else:
                if inputValidationKey == 'channelRange':
                    if userInput >= validationCheck[0] and userInput <= validationCheck[1]:
                        output = userInput
                        error = False
                    else:
                        print('Error: channel out of range. Enter channel between ', validationCheck[0], ' and',
                              validationCheck[1])
                elif inputValidationKey == 'freqRange':
                    range1 = False
                    range2 = False
                    range3 = False
                    if userInput >= validationCheck[0][0] and userInput <= validationCheck[0][1]:
                        range1 = True
                    elif userInput >= validationCheck[1][0] and userInput <= validationCheck[1][1]:
                        range2 = True
                    elif userInput >= validationCheck[2][0] and userInput <= validationCheck[2][1]:
                        range3 = True
                    if range1 or range2 or range3:
                        output = userInput
                        error = False
                    else:
                        print('Error: frequency out of range. Enter frequency between ', validationCheck[0], ', ',
                              validationCheck[1], ' and', validationCheck[2])
                elif inputValidationKey == 'validModes':
                    userInput = userInput.upper()
                    if userInput.isalpha() == False:
                        print('Please enter only letters!')
                    else:
                        if userInput in validationCheck:
                            output = userInput
                            error = False
                        else:
                            print('Error: mode not supported. Enter one of the following modes ', str(validationCheck))
                elif inputValidationKey == 'validSteps':
                    if userInput in validationCheck:
                        output = userInput
                        error = False
                    else:
                        print('Error: step not supported. Choose one of the following: ', str(validationCheck))
                elif inputValidationKey == 'validDelay':
                    range1 = False
                    if userInput >= validationCheck[0] and userInput <= validationCheck[1]:
                        range1 = True
                    if range1:
                        output = userInput
                        error = False
                    else:
                        print('Error: delay not supported. Enter integer delay value between: ', validationCheck[0],
                              ' and', validationCheck[1])
                elif inputValidationKey == 'validChars':
                    if len(userInput) <= validationCheck:
                        output = userInput
                        error = False
                    else:
                        print('Error: exceeded maximum of ', str(validationCheck), 'characters')
                elif inputValidationKey == 'validPriorityLockout':
                    userInput = userInput.upper()
                    if userInput.isalpha() == False:
                        print('Please enter only letters!')
                    else:
                        if userInput in validationCheck:
                            output = userInput
                            if userInput == 'Y':
                                output = userInput
                            else:
                                output = False
                            error = False
                        else:
                            print('Error: Please enter one of the following: ', str(validationCheck))

        return output
    else:
        error = True
        while error:
            try:
                choice = typeStr(input(menuChoices))
                error = False
            except ValueError:
                print(exceptionStr)
        return choice
