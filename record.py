#!/usr/bin/env python3

import sounddevice
from scipy.io.wavfile import write


def record(filename="audio.wav", duration=5, sample_rate=16000):
    """
    Record audio for a specified duration.

    Parameters:
        - filename (str): The name of the output file. Default is "audio.wav".
        - duration (int): The duration of the recording in seconds.
          Default is 5 seconds.
        - sample_rate (int): The sample rate of the audio. Default is 16000.

    Returns:
        str: The name of the output file.
    """

    if not isinstance(filename, str):
        raise ValueError("record: filename must be a string")

    if filename == "":
        raise ValueError("record: filename cannot be an empty string")

    if not isinstance(duration, int):
        raise ValueError("record: duration must be an integer")

    if not isinstance(sample_rate, int):
        raise ValueError("record: sample_rate must be an integer")

    print(f"Recording... ({int(duration)}s)")
    try:
        audio_data = sounddevice.rec(int(duration * sample_rate),
                                     samplerate=sample_rate,
                                     channels=1,
                                     dtype='int16'
                                     )
        sounddevice.wait()
    except sounddevice.PortAudioError as e:
        print(e)
        return

    print("Recording done")
    try:
        write(filename, sample_rate, audio_data)
    except FileNotFoundError as e:
        print(e)
        return

    return filename
