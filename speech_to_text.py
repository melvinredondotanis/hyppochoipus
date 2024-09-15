#!/usr/bin/env python3

from record import record
from faster_whisper import WhisperModel
from torch import device


def speech_to_text(model_size, language):
    """
    Transcribe speech from microphone to text

    Parameters:
        - model_size: Model size to use for transcription
        - language: Language to use for transcription

    Returns:
        str: Transcribed text
    """

    if not isinstance(model_size, str) or model_size == "":
        raise ValueError(
            "speech_to_text: model_size must be a non-empty string"
            )

    if not isinstance(language, str) or language == "":
        raise ValueError(
            "speech_to_text: language must be a non-empty string"
            )

    filename = record()
    try:
        if device.type == "cuda":
            model = WhisperModel(
                model_size,
                device="cuda",
                compute_type="int8"
                )
        else:
            model = WhisperModel(
                model_size,
                device="cpu",
                compute_type="int8"
                )

        segments, _ = model.transcribe(
            filename,
            beam_size=5,
            language=language
            )
    except ValueError as e:
        print(e)
        return ""

    text = "".join(segment.text for segment in segments)
    print("\nUSER: {}".format(text))

    return text


if __name__ == "__main__":
    print(speech_to_text("tiny", "fr"))
