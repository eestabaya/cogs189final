"""This script tries to access neurosky to record eeg data. Non-LSL version.
Based on: https://github.com/D1o0g9s/EEGFaceDetection/blob/master/mindwave_code/CollectRawData.py
"""

## IMPORTS
import mindwave
from psychopy import visual
import json
import time
import pandas as pd
from random import choices
from tqdm import tqdm
import sys
import os
from os.path import join as pjoin

##########################################################################
##########################################################################

### PATHS
BASE_PATH = "./"
DATA_PATH = pjoin(BASE_PATH, "eeg_data")
EEG_PATH = pjoin(DATA_PATH, 'eeg.csv')
if not os.path.isdir(DATA_PATH):
    os.makedirs(DATA_PATH)

##########################################################################
##########################################################################

## FUNCTIONS
def on_raw(headset, rawvalue):
    '''
    Save values collected from the headset
    Inputs:
        headset (obj) : argument provided by the headset
        data (global dict) : where this function saves new datapoints
        label (global int) : where this function takes the current label marker status
    Output: 
        one data point to each item of data
    Examples:
        >>> data = {'timestamp': [], 'raw_value': [], 'attention': [], 'label':[]}
        >>> label = 0
        >>> headset.raw_value_handlers.append(on_raw) # Start Collecting EEG
    '''
    (eeg, attention) = (headset.raw_value, headset.attention)
    
    ts = time.time()
    data['timestamp'].append(ts)
    data['raw_value'].append(eeg)
    data['attention'].append(attention)

##########################################################################
##########################################################################

# if this script is run as a script rather than imported
if __name__ == "__main__": 

    ###################### Headset Starting Sequence #####################
    currentTimestamp = None
    currentRawValue = None
    currentAttention = None

    data = {
        'timestamp': [],
        'raw_value': [],
        'attention': []
    }

    print("Connecting...")
    headset = mindwave.Headset('/dev/tty.MindWaveMobile-SerialPo') # mac version
    #headset = mindwave.Headset('/dev/tty.MindWaveMobile') # mac version
    #headset = mindwave.Headset('/dev/tty.Bluetooth-Incoming-Port') # mac version
    #headset = mindwave.Headset('COM6') # windows version. set up COM port first (see video)
    print("Connected!")

    print("Starting...")
    # Wait for the headset to steady down
    while (headset.poor_signal > 5 or headset.attention == 0):
        time.sleep(0.1)
    headset.raw_value_handlers.append(on_raw) # Start Collecting EEG
    print('Started!')
    ######################################################################

    try:
        START_TIME = time.time() # session start time constant
        trial_stime = time.time() # trial start time

        # run the experiment
        import experiment_gui

    except:
        headset.stop()
        df = pd.DataFrame.from_dict(data)
        df.to_csv(EEG_PATH, index=False)
        print("Stopped!")
        sys.exit(0)
    finally:
        time.sleep(0.2)
        df = pd.DataFrame.from_dict(data)
        df.to_csv(EEG_PATH, index=False)
