import os
from pathlib import Path

# Directories
BASE_DIR = Path(__file__).resolve().parent.parent
UPLOADS_DIR = os.getenv('UPLOADS_DIR', BASE_DIR / 'uploads')
RENDERS_DIR = os.getenv('RENDERS_DIR', BASE_DIR / 'renders')
TEMP_DIR = os.getenv('TEMP_DIR', BASE_DIR / 'temp')

# Create directories if they don't exist
for directory in [UPLOADS_DIR, RENDERS_DIR, TEMP_DIR]:
    Path(directory).mkdir(parents=True, exist_ok=True)

# Video processing settings
VIDEO_QUALITY_PRESETS = {
    'low': {
        'bitrate': '500k',
        'resolution': '854x480',
        'fps': 24,
    },
    'medium': {
        'bitrate': '2500k',
        'resolution': '1280x720',
        'fps': 30,
    },
    'high': {
        'bitrate': '5000k',
        'resolution': '1920x1080',
        'fps': 30,
    },
    'ultra': {
        'bitrate': '8000k',
        'resolution': '3840x2160',
        'fps': 30,
    },
}

# Supported formats
SUPPORTED_INPUT_FORMATS = ['mp4', 'mov', 'avi', 'mkv', 'flv', 'wmv']
SUPPORTED_OUTPUT_FORMATS = ['mp4', 'webm', 'mov']

# FFmpeg settings
FFMPEG_TIMEOUT = 3600  # 1 hour
MAX_VIDEO_DURATION = 600  # 10 minutes in seconds
MAX_FILE_SIZE = 5 * 1024 * 1024 * 1024  # 5 GB
