#!/usr/bin/env python3

from io import BytesIO
import numpy as np
import sounddevice as sd
from pydub import AudioSegment
from typing import Tuple

class Speaker:
    def __init__(self, client, model: str = "tts-1-hd", voice: str = "nova"):
        """Initialize the Speaker with a client, model, and voice."""
        self.model = model
        self.voice = voice
        self.client = client

    def _save_audio(self, audio_response, audio_file_path: str) -> None:
        """Save the audio response to a file."""
        audio_response.stream_to_file(audio_file_path)

    def create_audio(self, text: str, audio_save: bool = False, audio_file_path: str = 'speech.mp3') -> BytesIO:
        """Create audio from text using the specified model and voice."""
        try:
            response = self.client.audio.speech.create(
                model=self.model,
                voice=self.voice,
                input=text
            )
        except Exception as e:
            raise RuntimeError(f"Failed to create audio: {e}")

        if audio_save:
            self._save_audio(response, audio_file_path)

        return BytesIO(response.content)

    def process_audio(self, audio_bytes: BytesIO, format: str = "mp3") -> Tuple[np.ndarray, int]:
        """Process audio bytes into a numpy array and return the sample rate."""
        audio_segment = AudioSegment.from_file(audio_bytes, format=format)
        sample_rate = audio_segment.frame_rate
        channels = audio_segment.channels

        audio_array = np.array(audio_segment.get_array_of_samples())
        if channels > 1:
            audio_array = audio_array.reshape((-1, channels))

        return audio_array, sample_rate

    def play_audio(self, audio_array: np.ndarray, sample_rate: int) -> None:
        """Play the audio array using the specified sample rate."""
        sd.play(audio_array, samplerate=sample_rate)
        sd.wait()

    def play(self, content: str, format: str = "mp3") -> None:
        """Create, process, and play audio from the given content."""
        try:
            audio_array, sample_rate = self.process_audio(self.create_audio(content), format=format)
            self.play_audio(audio_array, sample_rate)
        except Exception as e:
            raise RuntimeError(f"Failed to play audio: {e}")