"""
Platform Formatter Module
Formats content for different social media platforms.
"""

from typing import Dict, List
import yaml
from pathlib import Path
import random


class PlatformFormatter:
    """Formats content for multiple social media platforms."""
    
    def __init__(self, config_path: str = "config/platforms.yaml"):
        """Initialize platform formatter with platform specifications."""
        self.config = self._load_config(config_path)
    
    def _load_config(self, config_path: str) -> Dict:
        """Load platform configuration."""
        try:
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Error loading platforms config: {e}")
            return {}
    
    def format_for_tiktok(self, script: Dict, news_item: Dict) -> Dict:
        """
        Format content for TikTok.
        
        Args:
            script: Full script dictionary
            news_item: Original news item
            
        Returns:
            TikTok-formatted content dictionary
        """
        config = self.config.get('tiktok', {})
        
        # Build caption from script
        caption = self._build_tiktok_caption(script, news_item)
        
        # Truncate if needed
        max_length = config.get('max_caption_length', 2200)
        if len(caption) > max_length:
            caption = caption[:max_length-3] + '...'
        
        # Generate hashtags
        hashtags = self._generate_hashtags(news_item, config.get('hashtag_count', 5))
        
        # Suggest optimal duration
        optimal_durations = config.get('optimal_duration', [15, 30, 60])
        duration = script.get('duration', 30)
        suggested_duration = min(optimal_durations, key=lambda x: abs(x - duration))
        
        # Audio suggestions
        audio_suggestion = self._suggest_audio(news_item)
        
        return {
            'platform': 'tiktok',
            'caption': caption,
            'hashtags': hashtags,
            'duration': suggested_duration,
            'audio_suggestion': audio_suggestion,
            'full_text': f"{caption}\n\n{' '.join(hashtags)}"
        }
    
    def format_for_instagram_reels(self, script: Dict, news_item: Dict) -> Dict:
        """
        Format content for Instagram Reels.
        
        Args:
            script: Full script dictionary
            news_item: Original news item
            
        Returns:
            Instagram Reels-formatted content dictionary
        """
        config = self.config.get('instagram_reels', {})
        
        # Build caption with line breaks
        caption = self._build_instagram_caption(script, news_item)
        
        # Truncate if needed
        max_length = config.get('max_caption_length', 2200)
        if len(caption) > max_length:
            caption = caption[:max_length-3] + '...'
        
        # Generate hashtags (more for Instagram)
        hashtags = self._generate_hashtags(news_item, config.get('hashtag_count', 10))
        
        # Build hashtag block (separate from caption)
        hashtag_block = '\n\n' + ' '.join(hashtags)
        
        # Story text (shorter version for stories)
        story_text = self._build_story_text(script)
        
        # Optimal duration
        optimal_durations = config.get('optimal_duration', [30, 60, 90])
        duration = script.get('duration', 30)
        suggested_duration = min(optimal_durations, key=lambda x: abs(x - duration))
        
        return {
            'platform': 'instagram_reels',
            'caption': caption,
            'hashtag_block': hashtag_block,
            'hashtags': hashtags,
            'story_text': story_text,
            'duration': suggested_duration,
            'full_text': caption + hashtag_block
        }
    
    def format_for_youtube_shorts(self, script: Dict, news_item: Dict) -> Dict:
        """
        Format content for YouTube Shorts.
        
        Args:
            script: Full script dictionary
            news_item: Original news item
            
        Returns:
            YouTube Shorts-formatted content dictionary
        """
        config = self.config.get('youtube_shorts', {})
        
        # Build title (max 100 chars)
        title = self._build_youtube_title(news_item)
        max_title_length = config.get('max_title_length', 100)
        if len(title) > max_title_length:
            title = title[:max_title_length-3] + '...'
        
        # Build description
        description = self._build_youtube_description(script, news_item)
        max_desc_length = config.get('max_description_length', 5000)
        if len(description) > max_desc_length:
            description = description[:max_desc_length-3] + '...'
        
        # Generate tags
        tags = self._generate_youtube_tags(news_item)
        
        # Optimal duration
        optimal_durations = config.get('optimal_duration', [30, 60])
        duration = script.get('duration', 30)
        suggested_duration = min(optimal_durations, key=lambda x: abs(x - duration))
        
        return {
            'platform': 'youtube_shorts',
            'title': title,
            'description': description,
            'tags': tags,
            'duration': suggested_duration
        }
    
    def format_for_youtube_longform(self, script: Dict, news_item: Dict) -> Dict:
        """
        Format content for YouTube Long-form.
        
        Args:
            script: Full script dictionary
            news_item: Original news item
            
        Returns:
            YouTube Long-form-formatted content dictionary
        """
        config = self.config.get('youtube_longform', {})
        
        # Build title
        title = self._build_youtube_title(news_item, longform=True)
        max_title_length = config.get('max_title_length', 100)
        if len(title) > max_title_length:
            title = title[:max_title_length-3] + '...'
        
        # Build full description template
        description = self._build_youtube_longform_description(script, news_item)
        
        # Generate chapter suggestions
        chapters = self._generate_chapters(script)
        
        # Tags
        tags = self._generate_youtube_tags(news_item)
        
        # Minimum duration check
        min_duration = config.get('min_duration', 480)
        
        return {
            'platform': 'youtube_longform',
            'title': title,
            'description': description,
            'chapters': chapters,
            'tags': tags,
            'min_duration': min_duration
        }
    
    def format_for_twitter(self, script: Dict, news_item: Dict) -> Dict:
        """
        Format content for X/Twitter.
        
        Args:
            script: Full script dictionary
            news_item: Original news item
            
        Returns:
            Twitter-formatted content dictionary
        """
        config = self.config.get('x_twitter', {})
        
        max_tweet_length = config.get('max_tweet_length', 280)
        
        # Single tweet version
        single_tweet = self._build_single_tweet(script, news_item, max_tweet_length)
        
        # Thread version (multiple tweets)
        thread = self._build_twitter_thread(script, news_item, max_tweet_length)
        
        # Quote tweet style
        quote_tweet = self._build_quote_tweet(news_item, max_tweet_length)
        
        return {
            'platform': 'x_twitter',
            'single_tweet': single_tweet,
            'thread': thread,
            'quote_tweet': quote_tweet,
            'max_tweet_length': max_tweet_length
        }
    
    def format_all(self, script: Dict, news_item: Dict) -> Dict:
        """
        Format content for all platforms.
        
        Args:
            script: Full script dictionary
            news_item: Original news item
            
        Returns:
            Dictionary with all platform formats
        """
        return {
            'tiktok': self.format_for_tiktok(script, news_item),
            'instagram_reels': self.format_for_instagram_reels(script, news_item),
            'youtube_shorts': self.format_for_youtube_shorts(script, news_item),
            'youtube_longform': self.format_for_youtube_longform(script, news_item),
            'x_twitter': self.format_for_twitter(script, news_item)
        }
    
    # Helper methods
    
    def _build_tiktok_caption(self, script: Dict, news_item: Dict) -> str:
        """Build TikTok caption from script."""
        sections = script.get('sections', [])
        
        if sections:
            hook = sections[0].get('text', '')
            context = sections[1].get('text', '') if len(sections) > 1 else ''
            
            caption = f"{hook}\n\n{context}"
        else:
            caption = news_item.get('title', '')
        
        return caption
    
    def _build_instagram_caption(self, script: Dict, news_item: Dict) -> str:
        """Build Instagram caption with line breaks."""
        sections = script.get('sections', [])
        
        if sections:
            lines = []
            for section in sections[:3]:  # Hook, context, relevance
                lines.append(section.get('text', ''))
            
            caption = '\n\n'.join(lines)
        else:
            caption = news_item.get('title', '')
        
        return caption
    
    def _build_story_text(self, script: Dict) -> str:
        """Build short text for Instagram Story."""
        sections = script.get('sections', [])
        if sections:
            return sections[0].get('text', '')[:100]
        return "New update!"
    
    def _build_youtube_title(self, news_item: Dict, longform: bool = False) -> str:
        """Build YouTube title."""
        title = news_item.get('title', '')
        
        # Add hook elements for long-form
        if longform:
            pillar = news_item.get('pillar', '')
            if pillar == 'education':
                prefix = 'How to: '
            elif pillar == 'offers':
                prefix = 'Deal Alert: '
            elif pillar == 'entertainment':
                prefix = ''
            else:
                prefix = ''
            
            return prefix + title
        
        return title
    
    def _build_youtube_description(self, script: Dict, news_item: Dict) -> str:
        """Build YouTube Shorts description."""
        sections = script.get('sections', [])
        
        description_parts = []
        
        for section in sections:
            description_parts.append(section.get('text', ''))
        
        description = '\n\n'.join(description_parts)
        
        # Add source link
        source_url = news_item.get('url', '')
        if source_url:
            description += f"\n\nSource: {source_url}"
        
        # Add signature
        description += "\n\n#GamingPC #TechNews #PCGaming"
        
        return description
    
    def _build_youtube_longform_description(self, script: Dict, news_item: Dict) -> str:
        """Build YouTube long-form description template."""
        description = self._build_youtube_description(script, news_item)
        
        # Add timestamps section placeholder
        description += "\n\n⏱️ TIMESTAMPS:\n[Add chapters here]"
        
        # Add links section
        description += "\n\n🔗 LINKS:\n"
        if news_item.get('url'):
            description += f"Article: {news_item['url']}\n"
        
        # Add social media
        description += "\n📱 FOLLOW:\nInstagram: @hellocomp\nTwitter: @hellocomp\nTikTok: @hellocomp"
        
        return description
    
    def _generate_chapters(self, script: Dict) -> List[Dict]:
        """Generate chapter suggestions for long-form video."""
        sections = script.get('sections', [])
        
        chapters = [{'time': '0:00', 'title': 'Intro'}]
        
        for i, section in enumerate(sections):
            start_time = section.get('start', 0)
            minutes = start_time // 60
            seconds = start_time % 60
            time_str = f"{minutes}:{seconds:02d}"
            
            chapter_title = section.get('name', '').replace('_', ' ').title()
            chapters.append({'time': time_str, 'title': chapter_title})
        
        return chapters
    
    def _generate_youtube_tags(self, news_item: Dict) -> List[str]:
        """Generate YouTube tags."""
        base_tags = ['gaming', 'pc gaming', 'tech news', 'hardware']
        
        # Add category-specific tags
        category = news_item.get('category', '')
        if category == 'hardware':
            base_tags.extend(['pc hardware', 'computer build', 'gpu', 'cpu'])
        elif category == 'gaming':
            base_tags.extend(['gaming news', 'game reviews', 'gaming setup'])
        
        # Add pillar-specific tags
        pillar = news_item.get('pillar', '')
        if pillar == 'education':
            base_tags.extend(['tutorial', 'guide', 'how to'])
        elif pillar == 'offers':
            base_tags.extend(['deals', 'sale', 'discount'])
        
        return base_tags[:15]  # Limit to 15 tags
    
    def _build_single_tweet(self, script: Dict, news_item: Dict, max_length: int) -> str:
        """Build single tweet."""
        sections = script.get('sections', [])
        
        if sections:
            hook = sections[0].get('text', '')
            
            # Add hashtags
            hashtags = ' #PCGaming #Tech'
            
            # Fit within limit
            available = max_length - len(hashtags) - 1
            tweet = hook[:available]
            
            return tweet + hashtags
        
        return news_item.get('title', '')[:max_length]
    
    def _build_twitter_thread(self, script: Dict, news_item: Dict, max_length: int) -> List[str]:
        """Build Twitter thread."""
        sections = script.get('sections', [])
        thread = []
        
        for i, section in enumerate(sections, 1):
            text = section.get('text', '')
            
            # Split if too long
            while len(text) > max_length - 10:
                split_point = text[:max_length-10].rfind(' ')
                if split_point == -1:
                    split_point = max_length - 10
                
                thread.append(f"{i}/{len(sections)} {text[:split_point]}")
                text = text[split_point:].strip()
            
            if text:
                thread.append(f"{i}/{len(sections)} {text}")
        
        return thread
    
    def _build_quote_tweet(self, news_item: Dict, max_length: int) -> str:
        """Build quote tweet style."""
        title = news_item.get('title', '')
        source = news_item.get('source', '')
        
        quote = f'"{title[:max_length-50]}"\n\nvia {source}\n\n#Gaming #Tech'
        
        return quote[:max_length]
    
    def _generate_hashtags(self, news_item: Dict, count: int) -> List[str]:
        """Generate hashtags for the content."""
        hashtag_pool = [
            '#PCGaming', '#Gaming', '#Tech', '#Hardware', '#GamingSetup',
            '#PCBuild', '#TechNews', '#GamingNews', '#GPU', '#CPU',
            '#GamingPC', '#Esports', '#PCMasterRace', '#TechTok',
            '#GamingCommunity', '#BuildSmarter', '#GameHarder'
        ]
        
        # Add context-specific hashtags
        pillar = news_item.get('pillar', '')
        if pillar == 'offers':
            hashtag_pool.extend(['#Deals', '#Sale', '#TechDeals'])
        elif pillar == 'education':
            hashtag_pool.extend(['#Tutorial', '#HowTo', '#TechTips'])
        
        # Shuffle and select
        random.shuffle(hashtag_pool)
        return hashtag_pool[:count]
    
    def _suggest_audio(self, news_item: Dict) -> str:
        """Suggest audio/music for the content."""
        pillar = news_item.get('pillar', '')
        
        suggestions = {
            'education': 'Upbeat tech background music',
            'entertainment': 'Trending gaming sound',
            'offers': 'Exciting deal alert sound',
            'social_proof': 'Motivational background music'
        }
        
        return suggestions.get(pillar, 'Trending sound')
