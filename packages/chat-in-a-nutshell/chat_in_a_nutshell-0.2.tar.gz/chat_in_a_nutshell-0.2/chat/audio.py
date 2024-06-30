#!/usr/bin/env python3

class Speaker:
    def __init__(self, client, model: str = "tts-1-hd", voice: str = "nova"):
        """Initialize the Speaker with a client, model, and voice."""
        self.model = model
        self.voice = voice
        self.client = client

    def _save_audio(self, audio_response, audio_file_path: str) -> None:
        """Save the audio response to a file."""
        audio_response.stream_to_file(audio_file_path)

    def create_audio(self, text: str, audio_save: bool = False, audio_file_path: str = 'speech.mp3') -> str:
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

        return 'Success'