import subprocess
import os
from pathlib import Path
from src.utils.logger import logger
from src.config import FFMPEG_TIMEOUT


class FFmpegProcessor:
    """Handle video processing with FFmpeg"""

    @staticmethod
    def get_video_info(input_path: str) -> dict:
        """Get video information"""
        cmd = [
            'ffprobe',
            '-v', 'error',
            '-show_format',
            '-show_streams',
            '-of', 'json',
            input_path
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            import json
            return json.loads(result.stdout)
        except Exception as e:
            logger.error(f"Failed to get video info: {e}")
            raise

    @staticmethod
    def convert_video(input_path: str, output_path: str, quality: str = 'medium') -> bool:
        """Convert video with specified quality"""
        from src.config import VIDEO_QUALITY_PRESETS
        
        preset = VIDEO_QUALITY_PRESETS.get(quality, VIDEO_QUALITY_PRESETS['medium'])
        
        cmd = [
            'ffmpeg',
            '-i', input_path,
            '-b:v', preset['bitrate'],
            '-s', preset['resolution'],
            '-r', str(preset['fps']),
            '-c:v', 'libx264',
            '-preset', 'medium',
            '-c:a', 'aac',
            '-b:a', '128k',
            output_path
        ]
        
        try:
            logger.info(f"Starting video conversion: {input_path} -> {output_path}")
            subprocess.run(cmd, timeout=FFMPEG_TIMEOUT, check=True)
            logger.info(f"Video conversion completed: {output_path}")
            return True
        except subprocess.TimeoutExpired:
            logger.error("FFmpeg conversion timeout")
            return False
        except Exception as e:
            logger.error(f"FFmpeg conversion failed: {e}")
            return False

    @staticmethod
    def add_watermark(input_path: str, watermark_path: str, output_path: str) -> bool:
        """Add watermark to video"""
        cmd = [
            'ffmpeg',
            '-i', input_path,
            '-i', watermark_path,
            '-filter_complex', 'overlay=10:10',
            output_path
        ]
        
        try:
            subprocess.run(cmd, timeout=FFMPEG_TIMEOUT, check=True)
            logger.info(f"Watermark added: {output_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to add watermark: {e}")
            return False

    @staticmethod
    def extract_thumbnail(input_path: str, output_path: str, timestamp: str = '00:00:01') -> bool:
        """Extract thumbnail from video"""
        cmd = [
            'ffmpeg',
            '-i', input_path,
            '-ss', timestamp,
            '-vframes', '1',
            '-vf', 'scale=1280:720',
            output_path
        ]
        
        try:
            subprocess.run(cmd, timeout=60, check=True)
            logger.info(f"Thumbnail extracted: {output_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to extract thumbnail: {e}")
            return False
