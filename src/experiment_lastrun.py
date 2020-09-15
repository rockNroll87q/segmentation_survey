#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Wed May  6 15:27:00 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'expert_evaluation'  # from the Builder filename that created this script
expInfo = {'password': '', 'your position': '', 'rate your expertise (1-10)': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'out/%s_%s' % (expName, data.getDateStr(format="%Y-%m-%d-%H.%M.%S"))

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/micheles/ownCloud/_Glasgow/_Projects/segmentator/Step_05/expert_evaluation_7T/experiment/experiment_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1600, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-0.9,-0.9,-0.9], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "password_check"
password_checkClock = core.Clock()
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Initialize components for Routine "initial_instructions"
initial_instructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="Thank you for your participation!\n\nPlease, read carefully the instructions below.\n\nTwo different segmentations of 7T data will be shown to you.\n\nYour task is to select the one you think is overall the best (the one you would use for your experiment).\n\nYou have the possibility to change slide with 'left'-'right' arrows and the transparency with 'up'-'down' arrows.\n\nPress 'space' if you can't decide between the two o 'q' if you can't carry out the task.\n\nOnce the task is complete, you will be notified with a final message.\n\n\nPress any key to start.",
    font='Arial',
    pos=(0, +0.3*0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "ready_go"
ready_goClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Ready? GO!',
    font='Helvetica',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
end_of_the_routine = keyboard.Keyboard()
Transparency_level_increment = 0.1
transparency_level = 0.3

image_R_text_string = ""
image_T1_L_m_2 = visual.ImageStim(
    win=win,
    name='image_T1_L_m_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_T1_L_m_1 = visual.ImageStim(
    win=win,
    name='image_T1_L_m_1', 
    image='sin', mask=None,
    ori=0, pos=(-0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_T1_L = visual.ImageStim(
    win=win,
    name='image_T1_L', 
    image='sin', mask=None,
    ori=0, pos=(-0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image_T1_L_p_1 = visual.ImageStim(
    win=win,
    name='image_T1_L_p_1', 
    image='sin', mask=None,
    ori=0, pos=(-0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
image_T1_L_p_2 = visual.ImageStim(
    win=win,
    name='image_T1_L_p_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
image_segm_L_m_2 = visual.ImageStim(
    win=win,
    name='image_segm_L_m_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
image_segm_L_m_1 = visual.ImageStim(
    win=win,
    name='image_segm_L_m_1', 
    image='sin', mask=None,
    ori=0, pos=(-0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
image_segm_L = visual.ImageStim(
    win=win,
    name='image_segm_L', 
    image='sin', mask=None,
    ori=0, pos=(-0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
image_segm_L_p_1 = visual.ImageStim(
    win=win,
    name='image_segm_L_p_1', 
    image='sin', mask=None,
    ori=0, pos=(-0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
image_segm_L_p_2 = visual.ImageStim(
    win=win,
    name='image_segm_L_p_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
image_L_text = visual.TextStim(win=win, name='image_L_text',
    text='default text',
    font='Helvetica',
    pos=(-0.5+0.40,0+0.60), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
image_T1_R_m_2 = visual.ImageStim(
    win=win,
    name='image_T1_R_m_2', 
    image='sin', mask=None,
    ori=0, pos=(+0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
image_T1_R_m_1 = visual.ImageStim(
    win=win,
    name='image_T1_R_m_1', 
    image='sin', mask=None,
    ori=0, pos=(+0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
image_T1_R = visual.ImageStim(
    win=win,
    name='image_T1_R', 
    image='sin', mask=None,
    ori=0, pos=(+0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
image_T1_R_p_1 = visual.ImageStim(
    win=win,
    name='image_T1_R_p_1', 
    image='sin', mask=None,
    ori=0, pos=(+0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
image_T1_R_p_2 = visual.ImageStim(
    win=win,
    name='image_T1_R_p_2', 
    image='sin', mask=None,
    ori=0, pos=(+0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
image_segm_R_m_2 = visual.ImageStim(
    win=win,
    name='image_segm_R_m_2', 
    image='sin', mask=None,
    ori=0, pos=(+0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
image_segm_R_m_1 = visual.ImageStim(
    win=win,
    name='image_segm_R_m_1', 
    image='sin', mask=None,
    ori=0, pos=(+0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
image_segm_R = visual.ImageStim(
    win=win,
    name='image_segm_R', 
    image='sin', mask=None,
    ori=0, pos=(+0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
image_segm_R_p_1 = visual.ImageStim(
    win=win,
    name='image_segm_R_p_1', 
    image='sin', mask=None,
    ori=0, pos=(+0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
image_segm_R_p_2 = visual.ImageStim(
    win=win,
    name='image_segm_R_p_2', 
    image='sin', mask=None,
    ori=0, pos=(+0.5,0), size=(0.9, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
image_R_text = visual.TextStim(win=win, name='image_R_text',
    text='default text',
    font='Helvetica',
    pos=(+0.5+0.40,0+0.60), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-24.0);
options_esc_space = visual.TextStim(win=win, name='options_esc_space',
    text="   'esc' (twice) to exit\n    'space' to skip slice",
    font='Helvetica',
    pos=(0.80, -0.9), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-25.0);
burron_LR = visual.ImageStim(
    win=win,
    name='burron_LR', 
    image='in/arrows_LR.png', mask=None,
    ori=0, pos=(0.1, 0.85), size=(0.09, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-26.0)
button_LR_text = visual.TextStim(win=win, name='button_LR_text',
    text='change slice (L/R)',
    font='helvetica',
    pos=(0.1+0.17, 0.85), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-27.0);
button_UD = visual.ImageStim(
    win=win,
    name='button_UD', 
    image='in/arrows_UD.png', mask=None,
    ori=0, pos=(-0.3, 0.85), size=(0.05, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-28.0)
button_UD_text = visual.TextStim(win=win, name='button_UD_text',
    text='change opacity (U/D)',
    font='Helvetica',
    pos=(-0.3+0.17, 0.85), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-29.0);
choise_selection = event.Mouse(win=win)
x, y = [None, None]
choise_selection.mouseClock = core.Clock()
trial_count = visual.TextStim(win=win, name='trial_count',
    text='default text',
    font='Helvetica',
    pos=[0.9, +0.9], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-32.0);
choice_L = visual.ImageStim(
    win=win,
    name='choice_L', 
    image='in/choice.png', mask=None,
    ori=0, pos=(-0.5, -0.7), size=(0.1, 0.17),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-33.0)
choice_R = visual.ImageStim(
    win=win,
    name='choice_R', 
    image='in/choice.png', mask=None,
    ori=0, pos=(+0.5, -0.7), size=(0.1, 0.17),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-34.0)
question_asked = visual.TextStim(win=win, name='question_asked',
    text='default text',
    font='Arial',
    pos=(0,-0.90), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-35.0);

# Initialize components for Routine "final_message"
final_messageClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Thanks for your collaboration!\n\nFor any question or suggestion please send an email to michele.svanera@glasgow.ac.uk',
    font='Helvetica',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='in/final_message.jpg', mask=None,
    ori=0, pos=(0, -.5), size=(0.5, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "password_check"-------
continueRoutine = True
# update component parameters for each repeat
if (expInfo['password'] != 'squash' and expInfo['password'] != 'muckli' and expInfo['password'] != 'ccni'):
    # Need to save everything is important, like log file

    # Display error text
    text_error = visual.TextStim(win=win, name='text_error',
                                text='    Wrong password!\n\nPlease reload the page.',
                                font='Helvetica',
                                pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
                                color='white', colorSpace='rgb', opacity=1, 
                                languageStyle='LTR',
                                depth=-1.0);

    timer_error = core.CountdownTimer(2.0)
    while (timer_error.getTime() > 0):
        text_error.draw()
        win.flip() # Update screen

    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    win.close()
    core.quit()
rate_submitted = expInfo['rate your expertise (1-10)']
check_flag = is_number(rate_submitted)

if (check_flag == False or float(rate_submitted)>10 or float(rate_submitted)<=0):
    # Need to save everything is important, like log file

    # Display error text
    text_error = visual.TextStim(win=win, name='text_error',
                                text='Error in rating (are you that bad!?)!\n\n       Please reload the page.',
                                font='Helvetica',
                                pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
                                color='white', colorSpace='rgb', opacity=1, 
                                languageStyle='LTR',
                                depth=-1.0);

    timer_error = core.CountdownTimer(2.0)
    while (timer_error.getTime() > 0):
        text_error.draw()
        win.flip() # Update screen

    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    win.close()
    core.quit()
# keep track of which components have finished
password_checkComponents = []
for thisComponent in password_checkComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
password_checkClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "password_check"-------
while continueRoutine:
    # get current time
    t = password_checkClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=password_checkClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in password_checkComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "password_check"-------
for thisComponent in password_checkComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "password_check" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "initial_instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
initial_instructionsComponents = [text, key_resp_2]
for thisComponent in initial_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initial_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "initial_instructions"-------
while continueRoutine:
    # get current time
    t = initial_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initial_instructionsClock)
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
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
            key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initial_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initial_instructions"-------
for thisComponent in initial_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "initial_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ready_go"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
ready_goComponents = [text_2]
for thisComponent in ready_goComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ready_goClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ready_go"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ready_goClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ready_goClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ready_goComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready_go"-------
for thisComponent in ready_goComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
loop_over_all_images = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('image_paths.csv'),
    seed=None, name='loop_over_all_images')
thisExp.addLoop(loop_over_all_images)  # add the loop to the experiment
thisLoop_over_all_image = loop_over_all_images.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_over_all_image.rgb)
if thisLoop_over_all_image != None:
    for paramName in thisLoop_over_all_image:
        exec('{} = thisLoop_over_all_image[paramName]'.format(paramName))

for thisLoop_over_all_image in loop_over_all_images:
    currentLoop = loop_over_all_images
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_over_all_image.rgb)
    if thisLoop_over_all_image != None:
        for paramName in thisLoop_over_all_image:
            exec('{} = thisLoop_over_all_image[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    end_of_the_routine.keys = []
    end_of_the_routine.rt = []
    _end_of_the_routine_allKeys = []
    T1_opacity = [0,0,1,0,0]
    
    slice_depth = 2     # Slide N [0,4]
    
    
    
    
    
    image_R_text_string = "slice " + str(slice_depth-2)
    image_T1_L_m_2.setImage(T1_slideN_m_2)
    image_T1_L_m_1.setImage(T1_slideN_m_1)
    image_T1_L.setImage(T1_slideN)
    image_T1_L_p_1.setImage(T1_slideN_p_1)
    image_T1_L_p_2.setImage(T1_slideN_p_2)
    image_segm_L_m_2.setImage(segm_L_slideN_m_2)
    image_segm_L_m_1.setImage(segm_L_slideN_m_1)
    image_segm_L.setImage(segm_L_slideN)
    image_segm_L_p_1.setImage(segm_L_slideN_p_1)
    image_segm_L_p_2.setImage(segm_L_slideN_p_2)
    image_T1_R_m_2.setImage(T1_slideN_m_2)
    image_T1_R_m_1.setImage(T1_slideN_m_1)
    image_T1_R.setImage(T1_slideN)
    image_T1_R_p_1.setImage(T1_slideN_p_1)
    image_T1_R_p_2.setImage(T1_slideN_p_2)
    image_segm_R_m_2.setImage(segm_R_slideN_m_2)
    image_segm_R_m_1.setImage(segm_R_slideN_m_1)
    image_segm_R.setImage(segm_R_slideN)
    image_segm_R_p_1.setImage(segm_R_slideN_p_1)
    image_segm_R_p_2.setImage(segm_R_slideN_p_2)
    # setup some python lists for storing info about the choise_selection
    choise_selection.x = []
    choise_selection.y = []
    choise_selection.leftButton = []
    choise_selection.midButton = []
    choise_selection.rightButton = []
    choise_selection.time = []
    choise_selection.clicked_name = []
    gotValidClick = False  # until a click is received
    trail_count_text = str(loop_over_all_images.thisN+1)+"/"+str(len(loop_over_all_images.trialList))
    question_asked.setText(question)
    # keep track of which components have finished
    trialComponents = [end_of_the_routine, image_T1_L_m_2, image_T1_L_m_1, image_T1_L, image_T1_L_p_1, image_T1_L_p_2, image_segm_L_m_2, image_segm_L_m_1, image_segm_L, image_segm_L_p_1, image_segm_L_p_2, image_L_text, image_T1_R_m_2, image_T1_R_m_1, image_T1_R, image_T1_R_p_1, image_T1_R_p_2, image_segm_R_m_2, image_segm_R_m_1, image_segm_R, image_segm_R_p_1, image_segm_R_p_2, image_R_text, options_esc_space, burron_LR, button_LR_text, button_UD, button_UD_text, choise_selection, trial_count, choice_L, choice_R, question_asked]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_of_the_routine* updates
        waitOnFlip = False
        if end_of_the_routine.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_of_the_routine.frameNStart = frameN  # exact frame index
            end_of_the_routine.tStart = t  # local t and not account for scr refresh
            end_of_the_routine.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_of_the_routine, 'tStartRefresh')  # time at next scr refresh
            end_of_the_routine.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_of_the_routine.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_of_the_routine.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_of_the_routine.status == STARTED and not waitOnFlip:
            theseKeys = end_of_the_routine.getKeys(keyList=['space'], waitRelease=False)
            _end_of_the_routine_allKeys.extend(theseKeys)
            if len(_end_of_the_routine_allKeys):
                end_of_the_routine.keys = _end_of_the_routine_allKeys[-1].name  # just the last key pressed
                end_of_the_routine.rt = _end_of_the_routine_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # Check for input (left and right arrows)
        old_slice_depth = slice_depth
        for key in event.getKeys():
            if key == 'left':
                slice_depth -= 1
            if key == 'right':
                slice_depth += 1
            if key == 'up':
                transparency_level += Transparency_level_increment
            if key == 'down':
                transparency_level -= Transparency_level_increment
            if key == 'q':
                core.quit()
            if key == 'esc':
                core.quit()
        
        # This avoid mess (repetitions) in the log file
        if old_slice_depth != slice_depth:
            # Set max and min values [0,4]
            slice_depth = np.clip(slice_depth, 0, len(T1_opacity)-1)
        
            # Set images to display
            T1_opacity = np.zeros((len(T1_opacity),))
            T1_opacity[slice_depth] = 1
        
        
        image_R_text_string = "slice " + str(slice_depth-2)
        
        # *image_T1_L_m_2* updates
        if image_T1_L_m_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_T1_L_m_2.frameNStart = frameN  # exact frame index
            image_T1_L_m_2.tStart = t  # local t and not account for scr refresh
            image_T1_L_m_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_T1_L_m_2, 'tStartRefresh')  # time at next scr refresh
            image_T1_L_m_2.setAutoDraw(True)
        if image_T1_L_m_2.status == STARTED:  # only update if drawing
            image_T1_L_m_2.setOpacity(T1_opacity[0], log=False)
        
        # *image_T1_L_m_1* updates
        if image_T1_L_m_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_T1_L_m_1.frameNStart = frameN  # exact frame index
            image_T1_L_m_1.tStart = t  # local t and not account for scr refresh
            image_T1_L_m_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_T1_L_m_1, 'tStartRefresh')  # time at next scr refresh
            image_T1_L_m_1.setAutoDraw(True)
        if image_T1_L_m_1.status == STARTED:  # only update if drawing
            image_T1_L_m_1.setOpacity(T1_opacity[1], log=False)
        
        # *image_T1_L* updates
        if image_T1_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_T1_L.frameNStart = frameN  # exact frame index
            image_T1_L.tStart = t  # local t and not account for scr refresh
            image_T1_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_T1_L, 'tStartRefresh')  # time at next scr refresh
            image_T1_L.setAutoDraw(True)
        if image_T1_L.status == STARTED:  # only update if drawing
            image_T1_L.setOpacity(T1_opacity[2], log=False)
        
        # *image_T1_L_p_1* updates
        if image_T1_L_p_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_T1_L_p_1.frameNStart = frameN  # exact frame index
            image_T1_L_p_1.tStart = t  # local t and not account for scr refresh
            image_T1_L_p_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_T1_L_p_1, 'tStartRefresh')  # time at next scr refresh
            image_T1_L_p_1.setAutoDraw(True)
        if image_T1_L_p_1.status == STARTED:  # only update if drawing
            image_T1_L_p_1.setOpacity(T1_opacity[3], log=False)
        
        # *image_T1_L_p_2* updates
        if image_T1_L_p_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_T1_L_p_2.frameNStart = frameN  # exact frame index
            image_T1_L_p_2.tStart = t  # local t and not account for scr refresh
            image_T1_L_p_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_T1_L_p_2, 'tStartRefresh')  # time at next scr refresh
            image_T1_L_p_2.setAutoDraw(True)
        if image_T1_L_p_2.status == STARTED:  # only update if drawing
            image_T1_L_p_2.setOpacity(T1_opacity[4], log=False)
        
        # *image_segm_L_m_2* updates
        if image_segm_L_m_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_segm_L_m_2.frameNStart = frameN  # exact frame index
            image_segm_L_m_2.tStart = t  # local t and not account for scr refresh
            image_segm_L_m_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_segm_L_m_2, 'tStartRefresh')  # time at next scr refresh
            image_segm_L_m_2.setAutoDraw(True)
        if image_segm_L_m_2.status == STARTED:  # only update if drawing
            image_segm_L_m_2.setOpacity(T1_opacity[0]*transparency_level, log=False)
        
        # *image_segm_L_m_1* updates
        if image_segm_L_m_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_segm_L_m_1.frameNStart = frameN  # exact frame index
            image_segm_L_m_1.tStart = t  # local t and not account for scr refresh
            image_segm_L_m_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_segm_L_m_1, 'tStartRefresh')  # time at next scr refresh
            image_segm_L_m_1.setAutoDraw(True)
        if image_segm_L_m_1.status == STARTED:  # only update if drawing
            image_segm_L_m_1.setOpacity(T1_opacity[1]*transparency_level, log=False)
        
        # *image_segm_L* updates
        if image_segm_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_segm_L.frameNStart = frameN  # exact frame index
            image_segm_L.tStart = t  # local t and not account for scr refresh
            image_segm_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_segm_L, 'tStartRefresh')  # time at next scr refresh
            image_segm_L.setAutoDraw(True)
        if image_segm_L.status == STARTED:  # only update if drawing
            image_segm_L.setOpacity(T1_opacity[2]*transparency_level, log=False)
        
        # *image_segm_L_p_1* updates
        if image_segm_L_p_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_segm_L_p_1.frameNStart = frameN  # exact frame index
            image_segm_L_p_1.tStart = t  # local t and not account for scr refresh
            image_segm_L_p_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_segm_L_p_1, 'tStartRefresh')  # time at next scr refresh
            image_segm_L_p_1.setAutoDraw(True)
        if image_segm_L_p_1.status == STARTED:  # only update if drawing
            image_segm_L_p_1.setOpacity(T1_opacity[3]*transparency_level, log=False)
        
        # *image_segm_L_p_2* updates
        if image_segm_L_p_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_segm_L_p_2.frameNStart = frameN  # exact frame index
            image_segm_L_p_2.tStart = t  # local t and not account for scr refresh
            image_segm_L_p_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_segm_L_p_2, 'tStartRefresh')  # time at next scr refresh
            image_segm_L_p_2.setAutoDraw(True)
        if image_segm_L_p_2.status == STARTED:  # only update if drawing
            image_segm_L_p_2.setOpacity(T1_opacity[4]*transparency_level, log=False)
        
        # *image_L_text* updates
        if image_L_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_L_text.frameNStart = frameN  # exact frame index
            image_L_text.tStart = t  # local t and not account for scr refresh
            image_L_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_L_text, 'tStartRefresh')  # time at next scr refresh
            image_L_text.setAutoDraw(True)
        if image_L_text.status == STARTED:  # only update if drawing
            image_L_text.setText(image_R_text_string, log=False)
        
        # *image_T1_R_m_2* updates
        if image_T1_R_m_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_T1_R_m_2.frameNStart = frameN  # exact frame index
            image_T1_R_m_2.tStart = t  # local t and not account for scr refresh
            image_T1_R_m_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_T1_R_m_2, 'tStartRefresh')  # time at next scr refresh
            image_T1_R_m_2.setAutoDraw(True)
        if image_T1_R_m_2.status == STARTED:  # only update if drawing
            image_T1_R_m_2.setOpacity(T1_opacity[0], log=False)
        
        # *image_T1_R_m_1* updates
        if image_T1_R_m_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_T1_R_m_1.frameNStart = frameN  # exact frame index
            image_T1_R_m_1.tStart = t  # local t and not account for scr refresh
            image_T1_R_m_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_T1_R_m_1, 'tStartRefresh')  # time at next scr refresh
            image_T1_R_m_1.setAutoDraw(True)
        if image_T1_R_m_1.status == STARTED:  # only update if drawing
            image_T1_R_m_1.setOpacity(T1_opacity[1], log=False)
        
        # *image_T1_R* updates
        if image_T1_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_T1_R.frameNStart = frameN  # exact frame index
            image_T1_R.tStart = t  # local t and not account for scr refresh
            image_T1_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_T1_R, 'tStartRefresh')  # time at next scr refresh
            image_T1_R.setAutoDraw(True)
        if image_T1_R.status == STARTED:  # only update if drawing
            image_T1_R.setOpacity(T1_opacity[2], log=False)
        
        # *image_T1_R_p_1* updates
        if image_T1_R_p_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_T1_R_p_1.frameNStart = frameN  # exact frame index
            image_T1_R_p_1.tStart = t  # local t and not account for scr refresh
            image_T1_R_p_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_T1_R_p_1, 'tStartRefresh')  # time at next scr refresh
            image_T1_R_p_1.setAutoDraw(True)
        if image_T1_R_p_1.status == STARTED:  # only update if drawing
            image_T1_R_p_1.setOpacity(T1_opacity[3], log=False)
        
        # *image_T1_R_p_2* updates
        if image_T1_R_p_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_T1_R_p_2.frameNStart = frameN  # exact frame index
            image_T1_R_p_2.tStart = t  # local t and not account for scr refresh
            image_T1_R_p_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_T1_R_p_2, 'tStartRefresh')  # time at next scr refresh
            image_T1_R_p_2.setAutoDraw(True)
        if image_T1_R_p_2.status == STARTED:  # only update if drawing
            image_T1_R_p_2.setOpacity(T1_opacity[4], log=False)
        
        # *image_segm_R_m_2* updates
        if image_segm_R_m_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_segm_R_m_2.frameNStart = frameN  # exact frame index
            image_segm_R_m_2.tStart = t  # local t and not account for scr refresh
            image_segm_R_m_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_segm_R_m_2, 'tStartRefresh')  # time at next scr refresh
            image_segm_R_m_2.setAutoDraw(True)
        if image_segm_R_m_2.status == STARTED:  # only update if drawing
            image_segm_R_m_2.setOpacity(T1_opacity[0]*transparency_level, log=False)
        
        # *image_segm_R_m_1* updates
        if image_segm_R_m_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_segm_R_m_1.frameNStart = frameN  # exact frame index
            image_segm_R_m_1.tStart = t  # local t and not account for scr refresh
            image_segm_R_m_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_segm_R_m_1, 'tStartRefresh')  # time at next scr refresh
            image_segm_R_m_1.setAutoDraw(True)
        if image_segm_R_m_1.status == STARTED:  # only update if drawing
            image_segm_R_m_1.setOpacity(T1_opacity[1]*transparency_level, log=False)
        
        # *image_segm_R* updates
        if image_segm_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_segm_R.frameNStart = frameN  # exact frame index
            image_segm_R.tStart = t  # local t and not account for scr refresh
            image_segm_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_segm_R, 'tStartRefresh')  # time at next scr refresh
            image_segm_R.setAutoDraw(True)
        if image_segm_R.status == STARTED:  # only update if drawing
            image_segm_R.setOpacity(T1_opacity[2]*transparency_level, log=False)
        
        # *image_segm_R_p_1* updates
        if image_segm_R_p_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_segm_R_p_1.frameNStart = frameN  # exact frame index
            image_segm_R_p_1.tStart = t  # local t and not account for scr refresh
            image_segm_R_p_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_segm_R_p_1, 'tStartRefresh')  # time at next scr refresh
            image_segm_R_p_1.setAutoDraw(True)
        if image_segm_R_p_1.status == STARTED:  # only update if drawing
            image_segm_R_p_1.setOpacity(T1_opacity[3]*transparency_level, log=False)
        
        # *image_segm_R_p_2* updates
        if image_segm_R_p_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_segm_R_p_2.frameNStart = frameN  # exact frame index
            image_segm_R_p_2.tStart = t  # local t and not account for scr refresh
            image_segm_R_p_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_segm_R_p_2, 'tStartRefresh')  # time at next scr refresh
            image_segm_R_p_2.setAutoDraw(True)
        if image_segm_R_p_2.status == STARTED:  # only update if drawing
            image_segm_R_p_2.setOpacity(T1_opacity[4]*transparency_level, log=False)
        
        # *image_R_text* updates
        if image_R_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_R_text.frameNStart = frameN  # exact frame index
            image_R_text.tStart = t  # local t and not account for scr refresh
            image_R_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_R_text, 'tStartRefresh')  # time at next scr refresh
            image_R_text.setAutoDraw(True)
        if image_R_text.status == STARTED:  # only update if drawing
            image_R_text.setText(image_R_text_string, log=False)
        
        # *options_esc_space* updates
        if options_esc_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            options_esc_space.frameNStart = frameN  # exact frame index
            options_esc_space.tStart = t  # local t and not account for scr refresh
            options_esc_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(options_esc_space, 'tStartRefresh')  # time at next scr refresh
            options_esc_space.setAutoDraw(True)
        
        # *burron_LR* updates
        if burron_LR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            burron_LR.frameNStart = frameN  # exact frame index
            burron_LR.tStart = t  # local t and not account for scr refresh
            burron_LR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(burron_LR, 'tStartRefresh')  # time at next scr refresh
            burron_LR.setAutoDraw(True)
        
        # *button_LR_text* updates
        if button_LR_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_LR_text.frameNStart = frameN  # exact frame index
            button_LR_text.tStart = t  # local t and not account for scr refresh
            button_LR_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_LR_text, 'tStartRefresh')  # time at next scr refresh
            button_LR_text.setAutoDraw(True)
        
        # *button_UD* updates
        if button_UD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_UD.frameNStart = frameN  # exact frame index
            button_UD.tStart = t  # local t and not account for scr refresh
            button_UD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_UD, 'tStartRefresh')  # time at next scr refresh
            button_UD.setAutoDraw(True)
        
        # *button_UD_text* updates
        if button_UD_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_UD_text.frameNStart = frameN  # exact frame index
            button_UD_text.tStart = t  # local t and not account for scr refresh
            button_UD_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_UD_text, 'tStartRefresh')  # time at next scr refresh
            button_UD_text.setAutoDraw(True)
        # *choise_selection* updates
        if choise_selection.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choise_selection.frameNStart = frameN  # exact frame index
            choise_selection.tStart = t  # local t and not account for scr refresh
            choise_selection.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choise_selection, 'tStartRefresh')  # time at next scr refresh
            choise_selection.status = STARTED
            choise_selection.mouseClock.reset()
            prevButtonState = choise_selection.getPressed()  # if button is down already this ISN'T a new click
        if choise_selection.status == STARTED:  # only update if started and not finished!
            buttons = choise_selection.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [choice_L, choice_R]:
                        if obj.contains(choise_selection):
                            gotValidClick = True
                            choise_selection.clicked_name.append(obj.name)
                    x, y = choise_selection.getPos()
                    choise_selection.x.append(x)
                    choise_selection.y.append(y)
                    buttons = choise_selection.getPressed()
                    choise_selection.leftButton.append(buttons[0])
                    choise_selection.midButton.append(buttons[1])
                    choise_selection.rightButton.append(buttons[2])
                    choise_selection.time.append(choise_selection.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        trail_count_text = str(loop_over_all_images.thisN+1)+"/"+str(len(loop_over_all_images.trialList))
        
        # *trial_count* updates
        if trial_count.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_count.frameNStart = frameN  # exact frame index
            trial_count.tStart = t  # local t and not account for scr refresh
            trial_count.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_count, 'tStartRefresh')  # time at next scr refresh
            trial_count.setAutoDraw(True)
        if trial_count.status == STARTED:  # only update if drawing
            trial_count.setText(trail_count_text, log=False)
        
        # *choice_L* updates
        if choice_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_L.frameNStart = frameN  # exact frame index
            choice_L.tStart = t  # local t and not account for scr refresh
            choice_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_L, 'tStartRefresh')  # time at next scr refresh
            choice_L.setAutoDraw(True)
        
        # *choice_R* updates
        if choice_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_R.frameNStart = frameN  # exact frame index
            choice_R.tStart = t  # local t and not account for scr refresh
            choice_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_R, 'tStartRefresh')  # time at next scr refresh
            choice_R.setAutoDraw(True)
        
        # *question_asked* updates
        if question_asked.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_asked.frameNStart = frameN  # exact frame index
            question_asked.tStart = t  # local t and not account for scr refresh
            question_asked.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_asked, 'tStartRefresh')  # time at next scr refresh
            question_asked.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if end_of_the_routine.keys in ['', [], None]:  # No response was made
        end_of_the_routine.keys = None
    loop_over_all_images.addData('end_of_the_routine.keys',end_of_the_routine.keys)
    if end_of_the_routine.keys != None:  # we had a response
        loop_over_all_images.addData('end_of_the_routine.rt', end_of_the_routine.rt)
    loop_over_all_images.addData('end_of_the_routine.started', end_of_the_routine.tStartRefresh)
    loop_over_all_images.addData('end_of_the_routine.stopped', end_of_the_routine.tStopRefresh)
    loop_over_all_images.addData('image_T1_L_m_2.started', image_T1_L_m_2.tStartRefresh)
    loop_over_all_images.addData('image_T1_L_m_2.stopped', image_T1_L_m_2.tStopRefresh)
    loop_over_all_images.addData('image_T1_L_m_1.started', image_T1_L_m_1.tStartRefresh)
    loop_over_all_images.addData('image_T1_L_m_1.stopped', image_T1_L_m_1.tStopRefresh)
    loop_over_all_images.addData('image_T1_L.started', image_T1_L.tStartRefresh)
    loop_over_all_images.addData('image_T1_L.stopped', image_T1_L.tStopRefresh)
    loop_over_all_images.addData('image_T1_L_p_1.started', image_T1_L_p_1.tStartRefresh)
    loop_over_all_images.addData('image_T1_L_p_1.stopped', image_T1_L_p_1.tStopRefresh)
    loop_over_all_images.addData('image_T1_L_p_2.started', image_T1_L_p_2.tStartRefresh)
    loop_over_all_images.addData('image_T1_L_p_2.stopped', image_T1_L_p_2.tStopRefresh)
    loop_over_all_images.addData('image_segm_L_m_2.started', image_segm_L_m_2.tStartRefresh)
    loop_over_all_images.addData('image_segm_L_m_2.stopped', image_segm_L_m_2.tStopRefresh)
    loop_over_all_images.addData('image_segm_L_m_1.started', image_segm_L_m_1.tStartRefresh)
    loop_over_all_images.addData('image_segm_L_m_1.stopped', image_segm_L_m_1.tStopRefresh)
    loop_over_all_images.addData('image_segm_L.started', image_segm_L.tStartRefresh)
    loop_over_all_images.addData('image_segm_L.stopped', image_segm_L.tStopRefresh)
    loop_over_all_images.addData('image_segm_L_p_1.started', image_segm_L_p_1.tStartRefresh)
    loop_over_all_images.addData('image_segm_L_p_1.stopped', image_segm_L_p_1.tStopRefresh)
    loop_over_all_images.addData('image_segm_L_p_2.started', image_segm_L_p_2.tStartRefresh)
    loop_over_all_images.addData('image_segm_L_p_2.stopped', image_segm_L_p_2.tStopRefresh)
    loop_over_all_images.addData('image_L_text.started', image_L_text.tStartRefresh)
    loop_over_all_images.addData('image_L_text.stopped', image_L_text.tStopRefresh)
    loop_over_all_images.addData('image_T1_R_m_2.started', image_T1_R_m_2.tStartRefresh)
    loop_over_all_images.addData('image_T1_R_m_2.stopped', image_T1_R_m_2.tStopRefresh)
    loop_over_all_images.addData('image_T1_R_m_1.started', image_T1_R_m_1.tStartRefresh)
    loop_over_all_images.addData('image_T1_R_m_1.stopped', image_T1_R_m_1.tStopRefresh)
    loop_over_all_images.addData('image_T1_R.started', image_T1_R.tStartRefresh)
    loop_over_all_images.addData('image_T1_R.stopped', image_T1_R.tStopRefresh)
    loop_over_all_images.addData('image_T1_R_p_1.started', image_T1_R_p_1.tStartRefresh)
    loop_over_all_images.addData('image_T1_R_p_1.stopped', image_T1_R_p_1.tStopRefresh)
    loop_over_all_images.addData('image_T1_R_p_2.started', image_T1_R_p_2.tStartRefresh)
    loop_over_all_images.addData('image_T1_R_p_2.stopped', image_T1_R_p_2.tStopRefresh)
    loop_over_all_images.addData('image_segm_R_m_2.started', image_segm_R_m_2.tStartRefresh)
    loop_over_all_images.addData('image_segm_R_m_2.stopped', image_segm_R_m_2.tStopRefresh)
    loop_over_all_images.addData('image_segm_R_m_1.started', image_segm_R_m_1.tStartRefresh)
    loop_over_all_images.addData('image_segm_R_m_1.stopped', image_segm_R_m_1.tStopRefresh)
    loop_over_all_images.addData('image_segm_R.started', image_segm_R.tStartRefresh)
    loop_over_all_images.addData('image_segm_R.stopped', image_segm_R.tStopRefresh)
    loop_over_all_images.addData('image_segm_R_p_1.started', image_segm_R_p_1.tStartRefresh)
    loop_over_all_images.addData('image_segm_R_p_1.stopped', image_segm_R_p_1.tStopRefresh)
    loop_over_all_images.addData('image_segm_R_p_2.started', image_segm_R_p_2.tStartRefresh)
    loop_over_all_images.addData('image_segm_R_p_2.stopped', image_segm_R_p_2.tStopRefresh)
    loop_over_all_images.addData('image_R_text.started', image_R_text.tStartRefresh)
    loop_over_all_images.addData('image_R_text.stopped', image_R_text.tStopRefresh)
    loop_over_all_images.addData('options_esc_space.started', options_esc_space.tStartRefresh)
    loop_over_all_images.addData('options_esc_space.stopped', options_esc_space.tStopRefresh)
    loop_over_all_images.addData('burron_LR.started', burron_LR.tStartRefresh)
    loop_over_all_images.addData('burron_LR.stopped', burron_LR.tStopRefresh)
    loop_over_all_images.addData('button_LR_text.started', button_LR_text.tStartRefresh)
    loop_over_all_images.addData('button_LR_text.stopped', button_LR_text.tStopRefresh)
    loop_over_all_images.addData('button_UD.started', button_UD.tStartRefresh)
    loop_over_all_images.addData('button_UD.stopped', button_UD.tStopRefresh)
    loop_over_all_images.addData('button_UD_text.started', button_UD_text.tStartRefresh)
    loop_over_all_images.addData('button_UD_text.stopped', button_UD_text.tStopRefresh)
    # store data for loop_over_all_images (TrialHandler)
    if len(choise_selection.x): loop_over_all_images.addData('choise_selection.x', choise_selection.x[0])
    if len(choise_selection.y): loop_over_all_images.addData('choise_selection.y', choise_selection.y[0])
    if len(choise_selection.leftButton): loop_over_all_images.addData('choise_selection.leftButton', choise_selection.leftButton[0])
    if len(choise_selection.midButton): loop_over_all_images.addData('choise_selection.midButton', choise_selection.midButton[0])
    if len(choise_selection.rightButton): loop_over_all_images.addData('choise_selection.rightButton', choise_selection.rightButton[0])
    if len(choise_selection.time): loop_over_all_images.addData('choise_selection.time', choise_selection.time[0])
    if len(choise_selection.clicked_name): loop_over_all_images.addData('choise_selection.clicked_name', choise_selection.clicked_name[0])
    loop_over_all_images.addData('choise_selection.started', choise_selection.tStart)
    loop_over_all_images.addData('choise_selection.stopped', choise_selection.tStop)
    loop_over_all_images.addData('trial_count.started', trial_count.tStartRefresh)
    loop_over_all_images.addData('trial_count.stopped', trial_count.tStopRefresh)
    loop_over_all_images.addData('choice_L.started', choice_L.tStartRefresh)
    loop_over_all_images.addData('choice_L.stopped', choice_L.tStopRefresh)
    loop_over_all_images.addData('choice_R.started', choice_R.tStartRefresh)
    loop_over_all_images.addData('choice_R.stopped', choice_R.tStopRefresh)
    loop_over_all_images.addData('question_asked.started', question_asked.tStartRefresh)
    loop_over_all_images.addData('question_asked.stopped', question_asked.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_over_all_images'

# get names of stimulus parameters
if loop_over_all_images.trialList in ([], [None], None):
    params = []
else:
    params = loop_over_all_images.trialList[0].keys()
# save data for this loop
loop_over_all_images.saveAsText(filename + 'loop_over_all_images.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "final_message"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
final_messageComponents = [text_3, image]
for thisComponent in final_messageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
final_messageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "final_message"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = final_messageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=final_messageClock)
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
        if tThisFlipGlobal > text_3.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in final_messageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "final_message"-------
for thisComponent in final_messageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
