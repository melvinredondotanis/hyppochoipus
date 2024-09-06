#!/usr/bin/env python3

import whisper

from header import welcome
from record import record


def main():
    welcome()
    filename = record()
    model = whisper.load_model("medium")
    audio = whisper.load_audio(filename)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    print("Language detected: {}".format(max(probs, key=probs.get)))
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    print(result.text)


if __name__ == "__main__":
    main()
