"""Example: Code to return current date as string"""

import time
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        
    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box
        day = time.strftime("%d")
        month = time.strftime("%B")
        year = time.strftime("%Y")
        
        dateToday = str(day) + " " + str(month) + " " + str(year)
        
        sentence = "Today is " + dateToday
        
        self.onDate(sentence)

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box