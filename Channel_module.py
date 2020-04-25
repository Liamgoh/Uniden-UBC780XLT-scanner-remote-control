class Channel:
    # construct a Channel object
    def __init__(self, channelNum, freq=0, mode='', step=0, delay=0, alphaTag='',
                 priority=False, lockout=False):
        self.__channelNum = channelNum
        self.__freq = freq
        self.__mode = mode
        self.__step = step
        self.__delay = delay
        self.__alphaTag = alphaTag
        self.__priority = priority
        self.__lockout = lockout

    def viewFreq(self):
        return self.__freq

    def viewMode(self):
        return self.__mode

    def viewStep(self):
        return self.__step

    def viewDelay(self):
        return self.__delay

    def viewAlphaTag(self):
        return self.__alphaTag

    def viewPriority(self):
        if self.__priority:
            PriorityTxt = 'Yes'
            return PriorityTxt
        else:
            PriorityTxt = 'No'
            return PriorityTxt

    def viewLockout(self):
        if self.__lockout:
            LockOutTxt = 'Yes'
            return LockOutTxt
        else:
            LockOutTxt = 'No'
            return LockOutTxt