from celery import shared_task
from src.utils.logger import logger
from src.generators.gpt_generator import GPTContentGenerator
from src.generators.voice_generator import VoiceGenerator
from src.generators.thumbnail_generator import ThumbnailGenerator
from datetime import datetime


@shared_task(bind=True, max_retries=3)
def generate_script(self, topic: str, style: str, duration: str, audience: str):
    """Generate video script using GPT"""
    try:
        logger.info(f"Task: Generating script for topic: {topic}")
        
        generator = GPTContentGenerator()
        script = generator.generate_script(topic, style, duration, audience)
        
        if script:
            return {
                'status': 'completed',
                'topic': topic,
                'script': script
            }
        else:
            return {
                'status': 'failed',
                'topic': topic,
                'error': 'Script generation failed'
            }
            
    except Exception as exc:
        logger.error(f"Script generation task failed: {exc}")
        raise self.retry(exc=exc, countdown=60)


@shared_task
def generate_titles(topic: str, style: str, count: int = 5):
    """Generate video titles"""
    try:
        logger.info(f"Task: Generating titles for topic: {topic}")
        
        generator = GPTContentGenerator()
        titles = generator.generate_titles(topic, style, count)
        
        if titles:
            return {
                'status': 'completed',
                'topic': topic,
                'titles': titles
            }
        else:
            return {
                'status': 'failed',
                'topic': topic,
                'error': 'Title generation failed'
            }
            
    except Exception as e:
        logger.error(f"Title generation failed: {e}")
        return {
            'status': 'failed',
            'topic': topic,
            'error': str(e)
        }


@shared_task
def generate_description(topic: str):
    """Generate video description"""
    try:
        logger.info(f"Task: Generating description for topic: {topic}")
        
        generator = GPTContentGenerator()
        description = generator.generate_description(topic)
        
        if description:
            return {
                'status': 'completed',
                'topic': topic,
                'description': description
            }
        else:
            return {
                'status': 'failed',
                'topic': topic,
                'error': 'Description generation failed'
            }
            
    except Exception as e:
        logger.error(f"Description generation failed: {e}")
        return {
            'status': 'failed',
            'topic': topic,
            'error': str(e)
        }


@shared_task
def generate_hashtags(topic: str, count: int = 15):
    """Generate hashtags"""
    try:
        logger.info(f"Task: Generating hashtags for topic: {topic}")
        
        generator = GPTContentGenerator()
        hashtags = generator.generate_hashtags(topic, count)
        
        if hashtags:
            return {
                'status': 'completed',
                'topic': topic,
                'hashtags': hashtags
            }
        else:
            return {
                'status': 'failed',
                'topic': topic,
                'error': 'Hashtag generation failed'
            }
            
    except Exception as e:
        logger.error(f"Hashtag generation failed: {e}")
        return {
            'status': 'failed',
            'topic': topic,
            'error': str(e)
        }


@shared_task
def generate_voiceover(text: str, voice_id: str, output_filename: str):
    """Generate voice over"""
    try:
        logger.info(f"Task: Generating voice over")
        
        generator = VoiceGenerator()
        output_path = generator.generate_voiceover(text, voice_id, output_filename)
        
        if output_path:
            return {
                'status': 'completed',
                'output_path': output_path,
                'output_filename': output_filename
            }
        else:
            return {
                'status': 'failed',
                'error': 'Voice generation failed'
            }
            
    except Exception as e:
        logger.error(f"Voice generation failed: {e}")
        return {
            'status': 'failed',
            'error': str(e)
        }


@shared_task
def generate_ai_thumbnail(prompt: str, output_filename: str):
    """Generate AI thumbnail"""
    try:
        logger.info(f"Task: Generating AI thumbnail")
        
        generator = ThumbnailGenerator()
        output_path = generator.generate_ai_thumbnail(prompt, output_filename)
        
        if output_path:
            return {
                'status': 'completed',
                'output_path': output_path,
                'output_filename': output_filename
            }
        else:
            return {
                'status': 'failed',
                'error': 'AI thumbnail generation failed'
            }
            
    except Exception as e:
        logger.error(f"AI thumbnail generation failed: {e}")
        return {
            'status': 'failed',
            'error': str(e)
        }


@shared_task
def generate_text_thumbnail(text: str, output_filename: str, bg_color: str = '#000000', 
                           text_color: str = '#FFFFFF'):
    """Generate text-based thumbnail"""
    try:
        logger.info(f"Task: Generating text thumbnail")
        
        generator = ThumbnailGenerator()
        output_path = generator.create_text_thumbnail(text, output_filename, bg_color, text_color)
        
        if output_path:
            return {
                'status': 'completed',
                'output_path': output_path,
                'output_filename': output_filename
            }
        else:
            return {
                'status': 'failed',
                'error': 'Text thumbnail generation failed'
            }
            
    except Exception as e:
        logger.error(f"Text thumbnail generation failed: {e}")
        return {
            'status': 'failed',
            'error': str(e)
        }
