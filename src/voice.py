#!/usr/bin/env python3

import os
import torch
from TTS.api import TTS
import simpleaudio as sa


class TextToSpeech:
    def __init__(self,
                 language='en',
                 voice_model='dataset/voice_model.wav',
                 output_path='output.wav',
                 debug=False,
                 model_name="tts_models/multilingual/multi-dataset/xtts_v2"
                 ):
        self.language = language
        self.voice_model = voice_model
        self.output_path = output_path

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        try:
            self.tts = TTS(model_name, progress_bar=debug).to(self.device)
        except Exception as e:
            raise RuntimeError(f"Failed to initialize TTS model: {e}")

    def say(self, text):
        try:
            output_path = self.tts.tts_to_file(
                text=text,
                speaker_wav=self.voice_model,
                language=self.language,
                file_path=self.output_path
            )

            wave_obj = sa.WaveObject.from_wave_file(self.output_path)
            play_obj = wave_obj.play()
            play_obj.wait_done()

            os.remove(self.output_path)
            return output_path
        except Exception as e:
            raise RuntimeError(f"Error during TTS processing: {e}")
