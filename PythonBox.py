"""Example: Say current date
The code for using ALTextToSpeech comes from Say box in Choregraphe"""

import time
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.tts = ALProxy('ALTextToSpeech')
        self.ttsStop = ALProxy('ALTextToSpeech', True) #Create another proxy as wait is blocking if audioout is remote

    def onLoad(self):
        #put initialization code here
        self.bIsRunning = False
        self.ids = []

    def onUnload(self):
        #put clean-up code here
        for id in self.ids:
            try:
                self.ttsStop.stop(id)
            except:
                pass
        while( self.bIsRunning ):
            time.sleep( 0.2 )

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box
        day = time.strftime("%d")
        month = time.strftime("%B")
        year = time.strftime("%Y")
        dateToday = str(day) + " " + str(month) + " " + str(year)
        self.bIsRunning = True
        try:
            sentence = "Today is " + dateToday
            id = self.tts.post.say(sentence)
            self.ids.append(id)
            self.tts.wait(id, 0)
        finally:
            try:
                self.ids.remove(id)
            except:
                pass
            if( self.ids == [] ):
                self.onStopped() # activate output of the box
                self.bIsRunning = False


    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box