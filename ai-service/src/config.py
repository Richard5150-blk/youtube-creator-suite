import os
from pathlib import Path

# Directories
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = os.getenv('OUTPUT_DIR', BASE_DIR / 'outputs')
CACHE_DIR = os.getenv('CACHE_DIR', BASE_DIR / '.cache')

# Create directories if they don't exist
for directory in [OUTPUT_DIR, CACHE_DIR]:
    Path(directory).mkdir(parents=True, exist_ok=True)

# OpenAI Configuration
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# ElevenLabs Configuration
ELEVEN_LABS_API_KEY = os.getenv('ELEVEN_LABS_API_KEY')
ELEVEN_LABS_MODEL_ID = os.getenv('ELEVEN_LABS_MODEL_ID', 'eleven_monolingual_v1')

# Video Generation Settings
VIDEO_STYLES = [
    'educational',
    'entertaining',
    'motivational',
    'tutorial',
    'storytelling',
    'comedy',
    'news',
    'review'
]

VIDEO_LENGTHS = {
    'short': (30, 60),      # 30 seconds - 1 minute
    'medium': (5, 10),      # 5-10 minutes
    'long': (10, 30),       # 10-30 minutes
}

# Prompt Templates
PROMPT_TEMPLATES = {
    'script_generation': """Generate a compelling YouTube video script for: {topic}
Style: {style}
Duration: {duration}
Target Audience: {audience}
Include: hook, main content, call-to-action
Make it engaging and optimized for retention.""",
    
    'title_generation': """Generate 5 catchy YouTube video titles for: {topic}
Style: {style}
Make them clickable and SEO-optimized.
Format: One title per line.""",
    
    'description_generation': """Generate a YouTube video description for: {topic}
Include timestamps if applicable.
Make it SEO-friendly with relevant keywords.""",
    
    'hashtag_generation': """Generate 10-15 relevant hashtags for a video about: {topic}
Format: One hashtag per line starting with #""",
}

# Thumbnail Settings
THUMBNAIL_SIZE = (1280, 720)  # YouTube standard
THUMBNAIL_QUALITY = 95
