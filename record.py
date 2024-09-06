#!/usr/bin/env python3

import sounddevice
from scipy.io.wavfile import write


def record(filename="audio.wav", duration=7, sample_rate=16000):
    """
    Record audio for a specified duration.

    Parameters:
        - filename (str): The name of the output file. Default is "audio.wav".
        - duration (int): The duration of the recording in seconds.
          Default is 7 seconds.
        - sample_rate (int): The sample rate of the audio. Default is 16000.

    Returns:
        None
    """
    print("Recording... ({}s)".format(duration))
    try:
        audio_data = sounddevice.rec(int(duration * sample_rate),
                                     samplerate=sample_rate,
                                     channels=1,
                                     dtype='int16'
                                     )
        sounddevice.wait()
    except Exception as e:
        print(e)
        return

    print("Recording done")
    try:
        write(filename, sample_rate, audio_data)
    except Exception as e:
        print(e)
        return

    print("Audio saved as", filename)
    return filename
