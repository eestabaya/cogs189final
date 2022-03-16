from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                            STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

EXPERIMENT_SOURCES = "trials.csv"



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.1'
expName = '189experiment'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/eric/Downloads/189experiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1500, 1000], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
#ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
#defaultKeyboard = keyboard.Keyboard(backend='iohub')
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
text_Instruction = visual.TextStim(win=win, name='text_Instruction',
    text='Instruction:\n\nMemorize the first set of letters presented. Then, look at the single letter presented afterwards to answer whether the letter is in the set or not. If the letter is included in the previous letter sets, press "right" on your key board, otherwise, press "left". Answer as quick as possible.\n\nPress space or enter when you finished reading this.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=0.0);
key_Instrution = keyboard.Keyboard()

# Initialize components for Routine "trials"
trialsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "tests"
testsClock = core.Clock()
textLetter = visual.TextStim(win=win, name='textLetter',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_res = keyboard.Keyboard()

# Initialize components for Routine "blank"
blankClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Take a break before your next trial.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyEnd = keyboard.Keyboard()

# Initialize components for Routine "trials"
trialsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "tests"
testsClock = core.Clock()
textLetter = visual.TextStim(win=win, name='textLetter',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_res = keyboard.Keyboard()

# Initialize components for Routine "blank"
blankClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Take a break before your next trial.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyEnd = keyboard.Keyboard()

# Initialize components for Routine "trials"
trialsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "tests"
testsClock = core.Clock()
textLetter = visual.TextStim(win=win, name='textLetter',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_res = keyboard.Keyboard()

# Initialize components for Routine "blank"
blankClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Take a break before your next trial.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyEnd = keyboard.Keyboard()

# Initialize components for Routine "trials"
trialsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "tests"
testsClock = core.Clock()
textLetter = visual.TextStim(win=win, name='textLetter',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_res = keyboard.Keyboard()

# Initialize components for Routine "blank"
blankClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Take a break before your next trial.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyEnd = keyboard.Keyboard()

# Initialize components for Routine "trials"
trialsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "tests"
testsClock = core.Clock()
textLetter = visual.TextStim(win=win, name='textLetter',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_res = keyboard.Keyboard()

# Initialize components for Routine "blank"
blankClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Take a break before your next trial.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyEnd = keyboard.Keyboard()

# Initialize components for Routine "trials"
trialsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "tests"
testsClock = core.Clock()
textLetter = visual.TextStim(win=win, name='textLetter',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_res = keyboard.Keyboard()

# Initialize components for Routine "blank"
blankClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "end"
endClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Thank you!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction"-------
continueRoutine = True
# update component parameters for each repeat
key_Instrution.keys = []
key_Instrution.rt = []
_key_Instrution_allKeys = []
# keep track of which components have finished
InstructionComponents = [text_Instruction, key_Instrution]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Instruction* updates
    if text_Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Instruction.frameNStart = frameN  # exact frame index
        text_Instruction.tStart = t  # local t and not account for scr refresh
        text_Instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Instruction, 'tStartRefresh')  # time at next scr refresh
        text_Instruction.setAutoDraw(True)
    
    # *key_Instrution* updates
    waitOnFlip = False
    if key_Instrution.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_Instrution.frameNStart = frameN  # exact frame index
        key_Instrution.tStart = t  # local t and not account for scr refresh
        key_Instrution.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_Instrution, 'tStartRefresh')  # time at next scr refresh
        key_Instrution.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_Instrution.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_Instrution.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_Instrution.status == STARTED and not waitOnFlip:
        theseKeys = key_Instrution.getKeys(keyList=['space','enter'], waitRelease=False)
        _key_Instrution_allKeys.extend(theseKeys)
        if len(_key_Instrution_allKeys):
            key_Instrution.keys = _key_Instrution_allKeys[-1].name  # just the last key pressed
            key_Instrution.rt = _key_Instrution_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Instruction.started', text_Instruction.tStartRefresh)
thisExp.addData('text_Instruction.stopped', text_Instruction.tStopRefresh)
# check responses
if key_Instrution.keys in ['', [], None]:  # No response was made
    key_Instrution.keys = None
thisExp.addData('key_Instrution.keys',key_Instrution.keys)
if key_Instrution.keys != None:  # we had a response
    thisExp.addData('key_Instrution.rt', key_Instrution.rt)
thisExp.addData('key_Instrution.started', key_Instrution.tStartRefresh)
thisExp.addData('key_Instrution.stopped', key_Instrution.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
oneletter = data.TrialHandler(nReps=1.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(EXPERIMENT_SOURCES, selection='0:5'),
    seed=None, name='oneletter')
thisExp.addLoop(oneletter)  # add the loop to the experiment
thisOneletter = oneletter.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOneletter.rgb)
if thisOneletter != None:
    for paramName in thisOneletter:
        exec('{} = thisOneletter[paramName]'.format(paramName))

for thisOneletter in oneletter:
    currentLoop = oneletter
    # abbreviate parameter names if possible (e.g. rgb = thisOneletter.rgb)
    if thisOneletter != None:
        for paramName in thisOneletter:
            exec('{} = thisOneletter[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trials"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    text.setText(wordItem)
    # keep track of which components have finished
    trialsComponents = [text]
    for thisComponent in trialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trials"-------
    for thisComponent in trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    oneletter.addData('text.started', text.tStartRefresh)
    oneletter.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [text_3]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    oneletter.addData('text_3.started', text_3.tStartRefresh)
    oneletter.addData('text_3.stopped', text_3.tStopRefresh)
    
    # ------Prepare to start Routine "tests"-------
    continueRoutine = True
    # update component parameters for each repeat
    textLetter.setText(letter)
    key_res.keys = []
    key_res.rt = []
    _key_res_allKeys = []
    # keep track of which components have finished
    testsComponents = [textLetter, key_res]
    for thisComponent in testsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "tests"-------
    while continueRoutine:
        # get current time
        t = testsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textLetter* updates
        if textLetter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textLetter.frameNStart = frameN  # exact frame index
            textLetter.tStart = t  # local t and not account for scr refresh
            textLetter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textLetter, 'tStartRefresh')  # time at next scr refresh
            textLetter.setAutoDraw(True)
        
        # *key_res* updates
        waitOnFlip = False
        if key_res.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_res.frameNStart = frameN  # exact frame index
            key_res.tStart = t  # local t and not account for scr refresh
            key_res.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_res, 'tStartRefresh')  # time at next scr refresh
            key_res.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_res.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_res.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_res.status == STARTED and not waitOnFlip:
            theseKeys = key_res.getKeys(keyList=['left','right'], waitRelease=False)
            _key_res_allKeys.extend(theseKeys)
            if len(_key_res_allKeys):
                key_res.keys = _key_res_allKeys[-1].name  # just the last key pressed
                key_res.rt = _key_res_allKeys[-1].rt
                # was this correct?
                if (key_res.keys == str(cor_resp)) or (key_res.keys == cor_resp):
                    key_res.corr = 1
                else:
                    key_res.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tests"-------
    for thisComponent in testsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    oneletter.addData('textLetter.started', textLetter.tStartRefresh)
    oneletter.addData('textLetter.stopped', textLetter.tStopRefresh)
    # check responses
    if key_res.keys in ['', [], None]:  # No response was made
        key_res.keys = None
        # was no response the correct answer?!
        if str(cor_resp).lower() == 'none':
            key_res.corr = 1;  # correct non-response
        else:
            key_res.corr = 0;  # failed to respond (incorrectly)
    # store data for oneletter (TrialHandler)
    oneletter.addData('key_res.keys',key_res.keys)
    oneletter.addData('key_res.corr', key_res.corr)
    if key_res.keys != None:  # we had a response
        oneletter.addData('key_res.rt', key_res.rt)
    oneletter.addData('key_res.started', key_res.tStartRefresh)
    oneletter.addData('key_res.stopped', key_res.tStopRefresh)
    # the Routine "tests" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [text_3]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    oneletter.addData('text_3.started', text_3.tStartRefresh)
    oneletter.addData('text_3.stopped', text_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'oneletter'


# ------Prepare to start Routine "break_2"-------
continueRoutine = True
# update component parameters for each repeat
keyEnd.keys = []
keyEnd.rt = []
_keyEnd_allKeys = []
# keep track of which components have finished
break_2Components = [text_5, keyEnd]
for thisComponent in break_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_2"-------
while continueRoutine:
    # get current time
    t = break_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *keyEnd* updates
    waitOnFlip = False
    if keyEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyEnd.frameNStart = frameN  # exact frame index
        keyEnd.tStart = t  # local t and not account for scr refresh
        keyEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyEnd, 'tStartRefresh')  # time at next scr refresh
        keyEnd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyEnd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyEnd.status == STARTED and not waitOnFlip:
        theseKeys = keyEnd.getKeys(keyList=['space'], waitRelease=False)
        _keyEnd_allKeys.extend(theseKeys)
        if len(_keyEnd_allKeys):
            keyEnd.keys = _keyEnd_allKeys[-1].name  # just the last key pressed
            keyEnd.rt = _keyEnd_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if keyEnd.keys in ['', [], None]:  # No response was made
    keyEnd.keys = None
thisExp.addData('keyEnd.keys',keyEnd.keys)
if keyEnd.keys != None:  # we had a response
    thisExp.addData('keyEnd.rt', keyEnd.rt)
thisExp.addData('keyEnd.started', keyEnd.tStartRefresh)
thisExp.addData('keyEnd.stopped', keyEnd.tStopRefresh)
thisExp.nextEntry()
# the Routine "break_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
twoletter = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(EXPERIMENT_SOURCES, selection='6:11'),
    seed=None, name='twoletter')
thisExp.addLoop(twoletter)  # add the loop to the experiment
thisTwoletter = twoletter.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTwoletter.rgb)
if thisTwoletter != None:
    for paramName in thisTwoletter:
        exec('{} = thisTwoletter[paramName]'.format(paramName))

for thisTwoletter in twoletter:
    currentLoop = twoletter
    # abbreviate parameter names if possible (e.g. rgb = thisTwoletter.rgb)
    if thisTwoletter != None:
        for paramName in thisTwoletter:
            exec('{} = thisTwoletter[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trials"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    text.setText(wordItem)
    # keep track of which components have finished
    trialsComponents = [text]
    for thisComponent in trialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trials"-------
    for thisComponent in trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    twoletter.addData('text.started', text.tStartRefresh)
    twoletter.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [text_3]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    twoletter.addData('text_3.started', text_3.tStartRefresh)
    twoletter.addData('text_3.stopped', text_3.tStopRefresh)
    
    # ------Prepare to start Routine "tests"-------
    continueRoutine = True
    # update component parameters for each repeat
    textLetter.setText(letter)
    key_res.keys = []
    key_res.rt = []
    _key_res_allKeys = []
    # keep track of which components have finished
    testsComponents = [textLetter, key_res]
    for thisComponent in testsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "tests"-------
    while continueRoutine:
        # get current time
        t = testsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textLetter* updates
        if textLetter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textLetter.frameNStart = frameN  # exact frame index
            textLetter.tStart = t  # local t and not account for scr refresh
            textLetter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textLetter, 'tStartRefresh')  # time at next scr refresh
            textLetter.setAutoDraw(True)
        
        # *key_res* updates
        waitOnFlip = False
        if key_res.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_res.frameNStart = frameN  # exact frame index
            key_res.tStart = t  # local t and not account for scr refresh
            key_res.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_res, 'tStartRefresh')  # time at next scr refresh
            key_res.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_res.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_res.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_res.status == STARTED and not waitOnFlip:
            theseKeys = key_res.getKeys(keyList=['left','right'], waitRelease=False)
            _key_res_allKeys.extend(theseKeys)
            if len(_key_res_allKeys):
                key_res.keys = _key_res_allKeys[-1].name  # just the last key pressed
                key_res.rt = _key_res_allKeys[-1].rt
                # was this correct?
                if (key_res.keys == str(cor_resp)) or (key_res.keys == cor_resp):
                    key_res.corr = 1
                else:
                    key_res.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tests"-------
    for thisComponent in testsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    twoletter.addData('textLetter.started', textLetter.tStartRefresh)
    twoletter.addData('textLetter.stopped', textLetter.tStopRefresh)
    # check responses
    if key_res.keys in ['', [], None]:  # No response was made
        key_res.keys = None
        # was no response the correct answer?!
        if str(cor_resp).lower() == 'none':
            key_res.corr = 1;  # correct non-response
        else:
            key_res.corr = 0;  # failed to respond (incorrectly)
    # store data for twoletter (TrialHandler)
    twoletter.addData('key_res.keys',key_res.keys)
    twoletter.addData('key_res.corr', key_res.corr)
    if key_res.keys != None:  # we had a response
        twoletter.addData('key_res.rt', key_res.rt)
    twoletter.addData('key_res.started', key_res.tStartRefresh)
    twoletter.addData('key_res.stopped', key_res.tStopRefresh)
    # the Routine "tests" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [text_3]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    twoletter.addData('text_3.started', text_3.tStartRefresh)
    twoletter.addData('text_3.stopped', text_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'twoletter'


# ------Prepare to start Routine "break_2"-------
continueRoutine = True
# update component parameters for each repeat
keyEnd.keys = []
keyEnd.rt = []
_keyEnd_allKeys = []
# keep track of which components have finished
break_2Components = [text_5, keyEnd]
for thisComponent in break_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_2"-------
while continueRoutine:
    # get current time
    t = break_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *keyEnd* updates
    waitOnFlip = False
    if keyEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyEnd.frameNStart = frameN  # exact frame index
        keyEnd.tStart = t  # local t and not account for scr refresh
        keyEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyEnd, 'tStartRefresh')  # time at next scr refresh
        keyEnd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyEnd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyEnd.status == STARTED and not waitOnFlip:
        theseKeys = keyEnd.getKeys(keyList=['space'], waitRelease=False)
        _keyEnd_allKeys.extend(theseKeys)
        if len(_keyEnd_allKeys):
            keyEnd.keys = _keyEnd_allKeys[-1].name  # just the last key pressed
            keyEnd.rt = _keyEnd_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if keyEnd.keys in ['', [], None]:  # No response was made
    keyEnd.keys = None
thisExp.addData('keyEnd.keys',keyEnd.keys)
if keyEnd.keys != None:  # we had a response
    thisExp.addData('keyEnd.rt', keyEnd.rt)
thisExp.addData('keyEnd.started', keyEnd.tStartRefresh)
thisExp.addData('keyEnd.stopped', keyEnd.tStopRefresh)
thisExp.nextEntry()
# the Routine "break_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
threeletter = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(EXPERIMENT_SOURCES, selection='12:17'),
    seed=None, name='threeletter')
thisExp.addLoop(threeletter)  # add the loop to the experiment
thisThreeletter = threeletter.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisThreeletter.rgb)
if thisThreeletter != None:
    for paramName in thisThreeletter:
        exec('{} = thisThreeletter[paramName]'.format(paramName))

for thisThreeletter in threeletter:
    currentLoop = threeletter
    # abbreviate parameter names if possible (e.g. rgb = thisThreeletter.rgb)
    if thisThreeletter != None:
        for paramName in thisThreeletter:
            exec('{} = thisThreeletter[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trials"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    text.setText(wordItem)
    # keep track of which components have finished
    trialsComponents = [text]
    for thisComponent in trialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trials"-------
    for thisComponent in trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    threeletter.addData('text.started', text.tStartRefresh)
    threeletter.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [text_3]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    threeletter.addData('text_3.started', text_3.tStartRefresh)
    threeletter.addData('text_3.stopped', text_3.tStopRefresh)
    
    # ------Prepare to start Routine "tests"-------
    continueRoutine = True
    # update component parameters for each repeat
    textLetter.setText(letter)
    key_res.keys = []
    key_res.rt = []
    _key_res_allKeys = []
    # keep track of which components have finished
    testsComponents = [textLetter, key_res]
    for thisComponent in testsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "tests"-------
    while continueRoutine:
        # get current time
        t = testsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textLetter* updates
        if textLetter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textLetter.frameNStart = frameN  # exact frame index
            textLetter.tStart = t  # local t and not account for scr refresh
            textLetter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textLetter, 'tStartRefresh')  # time at next scr refresh
            textLetter.setAutoDraw(True)
        
        # *key_res* updates
        waitOnFlip = False
        if key_res.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_res.frameNStart = frameN  # exact frame index
            key_res.tStart = t  # local t and not account for scr refresh
            key_res.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_res, 'tStartRefresh')  # time at next scr refresh
            key_res.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_res.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_res.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_res.status == STARTED and not waitOnFlip:
            theseKeys = key_res.getKeys(keyList=['left','right'], waitRelease=False)
            _key_res_allKeys.extend(theseKeys)
            if len(_key_res_allKeys):
                key_res.keys = _key_res_allKeys[-1].name  # just the last key pressed
                key_res.rt = _key_res_allKeys[-1].rt
                # was this correct?
                if (key_res.keys == str(cor_resp)) or (key_res.keys == cor_resp):
                    key_res.corr = 1
                else:
                    key_res.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tests"-------
    for thisComponent in testsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    threeletter.addData('textLetter.started', textLetter.tStartRefresh)
    threeletter.addData('textLetter.stopped', textLetter.tStopRefresh)
    # check responses
    if key_res.keys in ['', [], None]:  # No response was made
        key_res.keys = None
        # was no response the correct answer?!
        if str(cor_resp).lower() == 'none':
            key_res.corr = 1;  # correct non-response
        else:
            key_res.corr = 0;  # failed to respond (incorrectly)
    # store data for threeletter (TrialHandler)
    threeletter.addData('key_res.keys',key_res.keys)
    threeletter.addData('key_res.corr', key_res.corr)
    if key_res.keys != None:  # we had a response
        threeletter.addData('key_res.rt', key_res.rt)
    threeletter.addData('key_res.started', key_res.tStartRefresh)
    threeletter.addData('key_res.stopped', key_res.tStopRefresh)
    # the Routine "tests" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [text_3]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    threeletter.addData('text_3.started', text_3.tStartRefresh)
    threeletter.addData('text_3.stopped', text_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'threeletter'


# ------Prepare to start Routine "break_2"-------
continueRoutine = True
# update component parameters for each repeat
keyEnd.keys = []
keyEnd.rt = []
_keyEnd_allKeys = []
# keep track of which components have finished
break_2Components = [text_5, keyEnd]
for thisComponent in break_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_2"-------
while continueRoutine:
    # get current time
    t = break_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *keyEnd* updates
    waitOnFlip = False
    if keyEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyEnd.frameNStart = frameN  # exact frame index
        keyEnd.tStart = t  # local t and not account for scr refresh
        keyEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyEnd, 'tStartRefresh')  # time at next scr refresh
        keyEnd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyEnd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyEnd.status == STARTED and not waitOnFlip:
        theseKeys = keyEnd.getKeys(keyList=['space'], waitRelease=False)
        _keyEnd_allKeys.extend(theseKeys)
        if len(_keyEnd_allKeys):
            keyEnd.keys = _keyEnd_allKeys[-1].name  # just the last key pressed
            keyEnd.rt = _keyEnd_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if keyEnd.keys in ['', [], None]:  # No response was made
    keyEnd.keys = None
thisExp.addData('keyEnd.keys',keyEnd.keys)
if keyEnd.keys != None:  # we had a response
    thisExp.addData('keyEnd.rt', keyEnd.rt)
thisExp.addData('keyEnd.started', keyEnd.tStartRefresh)
thisExp.addData('keyEnd.stopped', keyEnd.tStopRefresh)
thisExp.nextEntry()
# the Routine "break_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
fourletter = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(EXPERIMENT_SOURCES, selection='18:23'),
    seed=None, name='fourletter')
thisExp.addLoop(fourletter)  # add the loop to the experiment
thisFourletter = fourletter.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFourletter.rgb)
if thisFourletter != None:
    for paramName in thisFourletter:
        exec('{} = thisFourletter[paramName]'.format(paramName))

for thisFourletter in fourletter:
    currentLoop = fourletter
    # abbreviate parameter names if possible (e.g. rgb = thisFourletter.rgb)
    if thisFourletter != None:
        for paramName in thisFourletter:
            exec('{} = thisFourletter[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trials"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    text.setText(wordItem)
    # keep track of which components have finished
    trialsComponents = [text]
    for thisComponent in trialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trials"-------
    for thisComponent in trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fourletter.addData('text.started', text.tStartRefresh)
    fourletter.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [text_3]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fourletter.addData('text_3.started', text_3.tStartRefresh)
    fourletter.addData('text_3.stopped', text_3.tStopRefresh)
    
    # ------Prepare to start Routine "tests"-------
    continueRoutine = True
    # update component parameters for each repeat
    textLetter.setText(letter)
    key_res.keys = []
    key_res.rt = []
    _key_res_allKeys = []
    # keep track of which components have finished
    testsComponents = [textLetter, key_res]
    for thisComponent in testsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "tests"-------
    while continueRoutine:
        # get current time
        t = testsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textLetter* updates
        if textLetter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textLetter.frameNStart = frameN  # exact frame index
            textLetter.tStart = t  # local t and not account for scr refresh
            textLetter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textLetter, 'tStartRefresh')  # time at next scr refresh
            textLetter.setAutoDraw(True)
        
        # *key_res* updates
        waitOnFlip = False
        if key_res.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_res.frameNStart = frameN  # exact frame index
            key_res.tStart = t  # local t and not account for scr refresh
            key_res.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_res, 'tStartRefresh')  # time at next scr refresh
            key_res.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_res.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_res.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_res.status == STARTED and not waitOnFlip:
            theseKeys = key_res.getKeys(keyList=['left','right'], waitRelease=False)
            _key_res_allKeys.extend(theseKeys)
            if len(_key_res_allKeys):
                key_res.keys = _key_res_allKeys[-1].name  # just the last key pressed
                key_res.rt = _key_res_allKeys[-1].rt
                # was this correct?
                if (key_res.keys == str(cor_resp)) or (key_res.keys == cor_resp):
                    key_res.corr = 1
                else:
                    key_res.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tests"-------
    for thisComponent in testsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fourletter.addData('textLetter.started', textLetter.tStartRefresh)
    fourletter.addData('textLetter.stopped', textLetter.tStopRefresh)
    # check responses
    if key_res.keys in ['', [], None]:  # No response was made
        key_res.keys = None
        # was no response the correct answer?!
        if str(cor_resp).lower() == 'none':
            key_res.corr = 1;  # correct non-response
        else:
            key_res.corr = 0;  # failed to respond (incorrectly)
    # store data for fourletter (TrialHandler)
    fourletter.addData('key_res.keys',key_res.keys)
    fourletter.addData('key_res.corr', key_res.corr)
    if key_res.keys != None:  # we had a response
        fourletter.addData('key_res.rt', key_res.rt)
    fourletter.addData('key_res.started', key_res.tStartRefresh)
    fourletter.addData('key_res.stopped', key_res.tStopRefresh)
    # the Routine "tests" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [text_3]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fourletter.addData('text_3.started', text_3.tStartRefresh)
    fourletter.addData('text_3.stopped', text_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'fourletter'


# ------Prepare to start Routine "break_2"-------
continueRoutine = True
# update component parameters for each repeat
keyEnd.keys = []
keyEnd.rt = []
_keyEnd_allKeys = []
# keep track of which components have finished
break_2Components = [text_5, keyEnd]
for thisComponent in break_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_2"-------
while continueRoutine:
    # get current time
    t = break_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *keyEnd* updates
    waitOnFlip = False
    if keyEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyEnd.frameNStart = frameN  # exact frame index
        keyEnd.tStart = t  # local t and not account for scr refresh
        keyEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyEnd, 'tStartRefresh')  # time at next scr refresh
        keyEnd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyEnd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyEnd.status == STARTED and not waitOnFlip:
        theseKeys = keyEnd.getKeys(keyList=['space'], waitRelease=False)
        _keyEnd_allKeys.extend(theseKeys)
        if len(_keyEnd_allKeys):
            keyEnd.keys = _keyEnd_allKeys[-1].name  # just the last key pressed
            keyEnd.rt = _keyEnd_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if keyEnd.keys in ['', [], None]:  # No response was made
    keyEnd.keys = None
thisExp.addData('keyEnd.keys',keyEnd.keys)
if keyEnd.keys != None:  # we had a response
    thisExp.addData('keyEnd.rt', keyEnd.rt)
thisExp.addData('keyEnd.started', keyEnd.tStartRefresh)
thisExp.addData('keyEnd.stopped', keyEnd.tStopRefresh)
thisExp.nextEntry()
# the Routine "break_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
fiveletter = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(EXPERIMENT_SOURCES, selection='24:29'),
    seed=None, name='fiveletter')
thisExp.addLoop(fiveletter)  # add the loop to the experiment
thisFiveletter = fiveletter.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFiveletter.rgb)
if thisFiveletter != None:
    for paramName in thisFiveletter:
        exec('{} = thisFiveletter[paramName]'.format(paramName))

for thisFiveletter in fiveletter:
    currentLoop = fiveletter
    # abbreviate parameter names if possible (e.g. rgb = thisFiveletter.rgb)
    if thisFiveletter != None:
        for paramName in thisFiveletter:
            exec('{} = thisFiveletter[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trials"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    text.setText(wordItem)
    # keep track of which components have finished
    trialsComponents = [text]
    for thisComponent in trialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trials"-------
    for thisComponent in trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fiveletter.addData('text.started', text.tStartRefresh)
    fiveletter.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [text_3]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fiveletter.addData('text_3.started', text_3.tStartRefresh)
    fiveletter.addData('text_3.stopped', text_3.tStopRefresh)
    
    # ------Prepare to start Routine "tests"-------
    continueRoutine = True
    # update component parameters for each repeat
    textLetter.setText(letter)
    key_res.keys = []
    key_res.rt = []
    _key_res_allKeys = []
    # keep track of which components have finished
    testsComponents = [textLetter, key_res]
    for thisComponent in testsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "tests"-------
    while continueRoutine:
        # get current time
        t = testsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textLetter* updates
        if textLetter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textLetter.frameNStart = frameN  # exact frame index
            textLetter.tStart = t  # local t and not account for scr refresh
            textLetter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textLetter, 'tStartRefresh')  # time at next scr refresh
            textLetter.setAutoDraw(True)
        
        # *key_res* updates
        waitOnFlip = False
        if key_res.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_res.frameNStart = frameN  # exact frame index
            key_res.tStart = t  # local t and not account for scr refresh
            key_res.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_res, 'tStartRefresh')  # time at next scr refresh
            key_res.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_res.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_res.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_res.status == STARTED and not waitOnFlip:
            theseKeys = key_res.getKeys(keyList=['left','right'], waitRelease=False)
            _key_res_allKeys.extend(theseKeys)
            if len(_key_res_allKeys):
                key_res.keys = _key_res_allKeys[-1].name  # just the last key pressed
                key_res.rt = _key_res_allKeys[-1].rt
                # was this correct?
                if (key_res.keys == str(cor_resp)) or (key_res.keys == cor_resp):
                    key_res.corr = 1
                else:
                    key_res.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tests"-------
    for thisComponent in testsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fiveletter.addData('textLetter.started', textLetter.tStartRefresh)
    fiveletter.addData('textLetter.stopped', textLetter.tStopRefresh)
    # check responses
    if key_res.keys in ['', [], None]:  # No response was made
        key_res.keys = None
        # was no response the correct answer?!
        if str(cor_resp).lower() == 'none':
            key_res.corr = 1;  # correct non-response
        else:
            key_res.corr = 0;  # failed to respond (incorrectly)
    # store data for fiveletter (TrialHandler)
    fiveletter.addData('key_res.keys',key_res.keys)
    fiveletter.addData('key_res.corr', key_res.corr)
    if key_res.keys != None:  # we had a response
        fiveletter.addData('key_res.rt', key_res.rt)
    fiveletter.addData('key_res.started', key_res.tStartRefresh)
    fiveletter.addData('key_res.stopped', key_res.tStopRefresh)
    # the Routine "tests" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [text_3]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fiveletter.addData('text_3.started', text_3.tStartRefresh)
    fiveletter.addData('text_3.stopped', text_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'fiveletter'


# ------Prepare to start Routine "break_2"-------
continueRoutine = True
# update component parameters for each repeat
keyEnd.keys = []
keyEnd.rt = []
_keyEnd_allKeys = []
# keep track of which components have finished
break_2Components = [text_5, keyEnd]
for thisComponent in break_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_2"-------
while continueRoutine:
    # get current time
    t = break_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *keyEnd* updates
    waitOnFlip = False
    if keyEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyEnd.frameNStart = frameN  # exact frame index
        keyEnd.tStart = t  # local t and not account for scr refresh
        keyEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyEnd, 'tStartRefresh')  # time at next scr refresh
        keyEnd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyEnd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyEnd.status == STARTED and not waitOnFlip:
        theseKeys = keyEnd.getKeys(keyList=['space'], waitRelease=False)
        _keyEnd_allKeys.extend(theseKeys)
        if len(_keyEnd_allKeys):
            keyEnd.keys = _keyEnd_allKeys[-1].name  # just the last key pressed
            keyEnd.rt = _keyEnd_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if keyEnd.keys in ['', [], None]:  # No response was made
    keyEnd.keys = None
thisExp.addData('keyEnd.keys',keyEnd.keys)
if keyEnd.keys != None:  # we had a response
    thisExp.addData('keyEnd.rt', keyEnd.rt)
thisExp.addData('keyEnd.started', keyEnd.tStartRefresh)
thisExp.addData('keyEnd.stopped', keyEnd.tStopRefresh)
thisExp.nextEntry()
# the Routine "break_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
sixletter = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(EXPERIMENT_SOURCES, selection='30:35'),
    seed=None, name='sixletter')
thisExp.addLoop(sixletter)  # add the loop to the experiment
thisSixletter = sixletter.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSixletter.rgb)
if thisSixletter != None:
    for paramName in thisSixletter:
        exec('{} = thisSixletter[paramName]'.format(paramName))

for thisSixletter in sixletter:
    currentLoop = sixletter
    # abbreviate parameter names if possible (e.g. rgb = thisSixletter.rgb)
    if thisSixletter != None:
        for paramName in thisSixletter:
            exec('{} = thisSixletter[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trials"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    text.setText(wordItem)
    # keep track of which components have finished
    trialsComponents = [text]
    for thisComponent in trialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trials"-------
    for thisComponent in trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sixletter.addData('text.started', text.tStartRefresh)
    sixletter.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [text_3]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sixletter.addData('text_3.started', text_3.tStartRefresh)
    sixletter.addData('text_3.stopped', text_3.tStopRefresh)
    
    # ------Prepare to start Routine "tests"-------
    continueRoutine = True
    # update component parameters for each repeat
    textLetter.setText(letter)
    key_res.keys = []
    key_res.rt = []
    _key_res_allKeys = []
    # keep track of which components have finished
    testsComponents = [textLetter, key_res]
    for thisComponent in testsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "tests"-------
    while continueRoutine:
        # get current time
        t = testsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textLetter* updates
        if textLetter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textLetter.frameNStart = frameN  # exact frame index
            textLetter.tStart = t  # local t and not account for scr refresh
            textLetter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textLetter, 'tStartRefresh')  # time at next scr refresh
            textLetter.setAutoDraw(True)
        
        # *key_res* updates
        waitOnFlip = False
        if key_res.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_res.frameNStart = frameN  # exact frame index
            key_res.tStart = t  # local t and not account for scr refresh
            key_res.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_res, 'tStartRefresh')  # time at next scr refresh
            key_res.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_res.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_res.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_res.status == STARTED and not waitOnFlip:
            theseKeys = key_res.getKeys(keyList=['left','right'], waitRelease=False)
            _key_res_allKeys.extend(theseKeys)
            if len(_key_res_allKeys):
                key_res.keys = _key_res_allKeys[-1].name  # just the last key pressed
                key_res.rt = _key_res_allKeys[-1].rt
                # was this correct?
                if (key_res.keys == str(cor_resp)) or (key_res.keys == cor_resp):
                    key_res.corr = 1
                else:
                    key_res.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tests"-------
    for thisComponent in testsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sixletter.addData('textLetter.started', textLetter.tStartRefresh)
    sixletter.addData('textLetter.stopped', textLetter.tStopRefresh)
    # check responses
    if key_res.keys in ['', [], None]:  # No response was made
        key_res.keys = None
        # was no response the correct answer?!
        if str(cor_resp).lower() == 'none':
            key_res.corr = 1;  # correct non-response
        else:
            key_res.corr = 0;  # failed to respond (incorrectly)
    # store data for sixletter (TrialHandler)
    sixletter.addData('key_res.keys',key_res.keys)
    sixletter.addData('key_res.corr', key_res.corr)
    if key_res.keys != None:  # we had a response
        sixletter.addData('key_res.rt', key_res.rt)
    sixletter.addData('key_res.started', key_res.tStartRefresh)
    sixletter.addData('key_res.stopped', key_res.tStopRefresh)
    # the Routine "tests" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [text_3]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sixletter.addData('text_3.started', text_3.tStartRefresh)
    sixletter.addData('text_3.stopped', text_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'sixletter'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text_4]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
