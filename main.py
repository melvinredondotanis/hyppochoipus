#!/usr/bin/env python3

from faster_whisper import WhisperModel

from header import welcome
from record import record

# Settings
model_size = "large-v3"


def main():
    welcome()
    filename = record()
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe(filename, beam_size=5)
    print("Detected language '{}' with probability {}".format(info.language, info.language_probability))
    for segment in segments:
        print("[{:.2f}s -> {:.2f}s] {}".format(segment.start, segment.end, segment.text))


if __name__ == "__main__":
    main()
