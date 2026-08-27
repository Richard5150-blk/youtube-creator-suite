from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from src.utils.logger import logger
from src.config import OUTPUT_DIR, THUMBNAIL_SIZE, THUMBNAIL_QUALITY
from typing import Optional
import os


class ThumbnailGenerator:
    """Generate thumbnails using AI and image processing"""

    @staticmethod
    def generate_ai_thumbnail(prompt: str, output_filename: str) -> Optional[str]:
        """Generate thumbnail using DALL-E"""
        try:
            import openai
            from src.config import OPENAI_API_KEY
            
            openai.api_key = OPENAI_API_KEY
            
            logger.info(f"Generating AI thumbnail with prompt: {prompt}")
            
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1280x720"
            )
            
            image_url = response['data'][0]['url']
            
            # Download image
            img_response = requests.get(image_url)
            img = Image.open(BytesIO(img_response.content))
            
            # Save thumbnail
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            img.save(output_path, quality=THUMBNAIL_QUALITY)
            
            logger.info(f"AI thumbnail generated: {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"Failed to generate AI thumbnail: {e}")
            return None

    @staticmethod
    def create_text_thumbnail(text: str, output_filename: str, bg_color: str = '#000000', 
                              text_color: str = '#FFFFFF') -> Optional[str]:
        """Create simple text-based thumbnail"""
        try:
            logger.info(f"Creating text thumbnail with text: {text}")
            
            # Create new image
            img = Image.new('RGB', THUMBNAIL_SIZE, color=bg_color)
            draw = ImageDraw.Draw(img)
            
            # Try to use a bold font, fallback to default
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
            except:
                font = ImageFont.load_default()
            
            # Draw text
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            x = (THUMBNAIL_SIZE[0] - text_width) // 2
            y = (THUMBNAIL_SIZE[1] - text_height) // 2
            
            draw.text((x, y), text, fill=text_color, font=font)
            
            # Save thumbnail
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            img.save(output_path, quality=THUMBNAIL_QUALITY)
            
            logger.info(f"Text thumbnail created: {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"Failed to create text thumbnail: {e}")
            return None
