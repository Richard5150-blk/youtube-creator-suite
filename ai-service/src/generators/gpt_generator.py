import openai
from src.config import OPENAI_API_KEY, OPENAI_MODEL
from src.utils.logger import logger
from typing import Optional


class GPTContentGenerator:
    """Generate content using OpenAI GPT"""

    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.model = OPENAI_MODEL

    def generate_script(self, topic: str, style: str, duration: str, audience: str) -> Optional[str]:
        """Generate video script using GPT"""
        try:
            from src.config import PROMPT_TEMPLATES
            
            prompt = PROMPT_TEMPLATES['script_generation'].format(
                topic=topic,
                style=style,
                duration=duration,
                audience=audience
            )
            
            logger.info(f"Generating script for topic: {topic}")
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a professional YouTube content writer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            script = response.choices[0].message.content
            logger.info("Script generated successfully")
            return script
            
        except Exception as e:
            logger.error(f"Failed to generate script: {e}")
            return None

    def generate_titles(self, topic: str, style: str, count: int = 5) -> Optional[list]:
        """Generate video titles using GPT"""
        try:
            from src.config import PROMPT_TEMPLATES
            
            prompt = PROMPT_TEMPLATES['title_generation'].format(
                topic=topic,
                style=style
            )
            
            logger.info(f"Generating {count} titles for topic: {topic}")
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a YouTube SEO expert."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=500
            )
            
            titles = response.choices[0].message.content.strip().split('\n')
            titles = [t.strip() for t in titles if t.strip()]
            logger.info(f"Generated {len(titles)} titles")
            return titles[:count]
            
        except Exception as e:
            logger.error(f"Failed to generate titles: {e}")
            return None

    def generate_description(self, topic: str) -> Optional[str]:
        """Generate video description using GPT"""
        try:
            from src.config import PROMPT_TEMPLATES
            
            prompt = PROMPT_TEMPLATES['description_generation'].format(topic=topic)
            
            logger.info(f"Generating description for topic: {topic}")
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a YouTube SEO expert."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            description = response.choices[0].message.content
            logger.info("Description generated successfully")
            return description
            
        except Exception as e:
            logger.error(f"Failed to generate description: {e}")
            return None

    def generate_hashtags(self, topic: str, count: int = 15) -> Optional[list]:
        """Generate hashtags using GPT"""
        try:
            from src.config import PROMPT_TEMPLATES
            
            prompt = PROMPT_TEMPLATES['hashtag_generation'].format(topic=topic)
            
            logger.info(f"Generating hashtags for topic: {topic}")
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a social media expert."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=300
            )
            
            hashtags = response.choices[0].message.content.strip().split('\n')
            hashtags = [h.strip() for h in hashtags if h.strip().startswith('#')]
            logger.info(f"Generated {len(hashtags)} hashtags")
            return hashtags[:count]
            
        except Exception as e:
            logger.error(f"Failed to generate hashtags: {e}")
            return None
