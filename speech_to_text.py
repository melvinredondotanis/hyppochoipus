#!/usr/bin/env python3

from faster_whisper import WhisperModel

from record import record


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
            "speech_to_text: model_size must be a string and cannot be empty"
            )

    if not isinstance(language, str) or language == "":
        raise ValueError(
            "speech_to_text: language must be a string and cannot be empty"
            )

    filename = record()
    try:
        model = WhisperModel(model_size, device="cpu", compute_type="int8")
        segments, _ = model.transcribe(
                                        filename,
                                        beam_size=5,
                                        language=language
                                        )
    except ValueError as e:
        print(e)
        return

    return "".join(segment.text for segment in segments)
