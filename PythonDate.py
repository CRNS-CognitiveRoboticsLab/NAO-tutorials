#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Say current date
The code for using ALTextToSpeech comes from SoftBank tutorial:
http://doc.aldebaran.com/2-4/naoqi/audio/altexttospeech-api.html#altexttospeech-api"""

import qi
import argparse
import sys
import time

def main(session):
    """
    This example uses time library and ALTextToSpeech module to get and say the date.
    """
    # Get the service ALTextToSpeech.
    tts = session.service("ALTextToSpeech")
    
    day = time.strftime("%d")
    month = time.strftime("%B")
    year = time.strftime("%Y")
    dateToday = str(day) + " " + str(month) + " " + str(year)
    
    sentence = "Today is " + dateToday

    # Say sentence
    tts.say(sentence)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)