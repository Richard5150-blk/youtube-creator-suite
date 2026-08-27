from celery import shared_task
from src.utils.logger import logger
from src.processors.ffmpeg_processor import FFmpegProcessor
from src.config import RENDERS_DIR
import os
from datetime import datetime


@shared_task(bind=True, max_retries=3)
def process_video(self, video_id: str, input_path: str, quality: str = 'medium'):
    """Process video and render it"""
    try:
        logger.info(f"Processing video {video_id}")
        
        # Generate output path
        output_filename = f"{video_id}_{quality}_{datetime.now().timestamp()}.mp4"
        output_path = os.path.join(RENDERS_DIR, output_filename)
        
        # Convert video
        success = FFmpegProcessor.convert_video(input_path, output_path, quality)
        
        if success:
            logger.info(f"Video processing completed: {video_id}")
            return {
                'status': 'completed',
                'video_id': video_id,
                'output_path': output_path,
                'output_filename': output_filename
            }
        else:
            logger.error(f"Video processing failed: {video_id}")
            return {
                'status': 'failed',
                'video_id': video_id,
                'error': 'Conversion failed'
            }
            
    except Exception as exc:
        logger.error(f"Task failed: {exc}")
        raise self.retry(exc=exc, countdown=60)


@shared_task
def extract_thumbnail(video_id: str, input_path: str, timestamp: str = '00:00:01'):
    """Extract thumbnail from video"""
    try:
        logger.info(f"Extracting thumbnail for video {video_id}")
        
        output_filename = f"thumb_{video_id}_{datetime.now().timestamp()}.jpg"
        output_path = os.path.join(RENDERS_DIR, output_filename)
        
        success = FFmpegProcessor.extract_thumbnail(input_path, output_path, timestamp)
        
        if success:
            return {
                'status': 'completed',
                'video_id': video_id,
                'thumbnail_path': output_path
            }
        else:
            return {
                'status': 'failed',
                'video_id': video_id,
                'error': 'Thumbnail extraction failed'
            }
    except Exception as e:
        logger.error(f"Thumbnail extraction failed: {e}")
        return {
            'status': 'failed',
            'video_id': video_id,
            'error': str(e)
        }


@shared_task
def cleanup_temp_files():
    """Clean up temporary files"""
    try:
        import shutil
        from src.config import TEMP_DIR
        
        logger.info("Starting cleanup of temporary files")
        if os.path.exists(TEMP_DIR):
            shutil.rmtree(TEMP_DIR)
            os.makedirs(TEMP_DIR)
        logger.info("Cleanup completed")
    except Exception as e:
        logger.error(f"Cleanup failed: {e}")
