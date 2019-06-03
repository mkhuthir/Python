#! /usr/bin/python

import pyttsx

engine = pyttsx.init()
voices = engine.getProperty('voices')
for voice in voices:
   print voice
