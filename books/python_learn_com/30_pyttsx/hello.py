#! /usr/bin/python

import pyttsx

engine = pyttsx.init()

rate = engine.getProperty('rate')-50
engine.setProperty('rate', rate)
print '\n\nCurrent Speech Rate: ', rate

volume = engine.getProperty('volume')-0.25
print 'Current Speech Volume: ', volume


print('\n\nHello World')
print('Sally sells seashells by the seashore.')
print('The quick brown fox jumped over the lazy dog.\n\n')
engine.say('Hello World')
engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumped over the lazy dog.')

engine.runAndWait()


