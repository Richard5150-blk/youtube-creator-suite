import requests
from src.config import ELEVEN_LABS_API_KEY, ELEVEN_LABS_MODEL_ID
from src.utils.logger import logger
from typing import Optional
import os
from src.config import OUTPUT_DIR


class VoiceGenerator:
    """Generate voice using ElevenLabs API"""

    def __init__(self):
        self.api_key = ELEVEN_LABS_API_KEY
        self.model_id = ELEVEN_LABS_MODEL_ID
        self.base_url = "https://api.elevenlabs.io/v1"

    def get_available_voices(self) -> Optional[list]:
        """Get list of available voices"""
        try:
            url = f"{self.base_url}/voices"
            headers = {"xi-api-key": self.api_key}
            
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            voices = response.json().get('voices', [])
            logger.info(f"Retrieved {len(voices)} available voices")
            return voices
            
        except Exception as e:
            logger.error(f"Failed to get voices: {e}")
            return None

    def generate_voiceover(self, text: str, voice_id: str, output_filename: str) -> Optional[str]:
        """Generate voice over from text"""
        try:
            url = f"{self.base_url}/text-to-speech/{voice_id}"
            headers = {
                "xi-api-key": self.api_key,
                "Content-Type": "application/json"
            }
            
            data = {
                "text": text,
                "model_id": self.model_id,
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75
                }
            }
            
            logger.info(f"Generating voice over with voice ID: {voice_id}")
            
            response = requests.post(url, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            
            # Save audio file
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            logger.info(f"Voice over generated successfully: {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"Failed to generate voice over: {e}")
            return None
