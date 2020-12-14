from PythonEuterpeaN import *

'''
Duration constants:
WN = 1.0        # whole note = one measure in 4/4
DHN = 0.75      # dotted half
HN = 0.5        # half note
DQN = 0.375     # dotted quarter
QN = 0.25       # quarter note
DEN = 0.1875    # dotted eighth
EN = 0.125      # eighth note
DSN = 0.09375   # dotted sixteenth
SN = 0.0625     # sixteenth note
DTN = 0.046875  # dotted thirtysecond
TN = 0.03125    # thirtysecond note
'''

myPDPairs = [(60, QN), (60, QN), (67, QN), (67, QN), (69, QN), (69, QN), (67, HN)]

def pdPairsToMusic(pdPairs):
    notes = list()
    defVol = 100
    for pd in pdPairs:
        n = Note(pd[0], pd[1], defVol)
        notes.append(n)
    s = Seq(notes) # create a sequential tree structure
    bpm = 120
    m = Music(s,bpm) # create a music wrapper
    return m
    
myMusic = pdPairsToMusic(myPDPairs)

print(myMusic)

musicToMidi("test.mid", myMusic)

