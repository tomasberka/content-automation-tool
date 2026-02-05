"""
News Fetcher Module
Fetches gaming/PC news from RSS feeds and normalizes the data.
"""

from typing import List, Dict, Optional
from datetime import datetime
import feedparser
import yaml
import requests
from pathlib import Path


class NewsFetcher:
    """Fetches and parses gaming/PC news from multiple RSS feeds."""
    
    def __init__(self, config_path: str = "config/sources.yaml"):
        """Initialize the news fetcher with RSS sources configuration."""
        self.config_path = Path(config_path)
        self.sources = self._load_sources()
        self.max_articles = self.sources.get('max_articles_per_source', 10)
        
    def _load_sources(self) -> Dict:
        """Load RSS feed sources from configuration file."""
        try:
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Error loading sources config: {e}")
            return {'rss_feeds': [], 'max_articles_per_source': 10}
    
    def fetch_news(self, days_back: Optional[int] = None) -> List[Dict]:
        """
        Fetch news from all configured RSS feeds.
        
        Args:
            days_back: Optional number of days to look back for articles
            
        Returns:
            List of normalized news items
        """
        all_news = []
        
        for feed_config in self.sources.get('rss_feeds', []):
            try:
                news_items = self._fetch_from_feed(feed_config, days_back)
                all_news.extend(news_items)
            except Exception as e:
                print(f"Error fetching from {feed_config.get('name', 'unknown')}: {e}")
                continue
        
        # Sort by date, newest first
        all_news.sort(key=lambda x: x['date'], reverse=True)
        return all_news
    
    def _fetch_from_feed(self, feed_config: Dict, days_back: Optional[int] = None) -> List[Dict]:
        """
        Fetch and parse a single RSS feed.
        
        Args:
            feed_config: Configuration for a single feed
            days_back: Optional number of days to filter articles
            
        Returns:
            List of normalized news items from this feed
        """
        feed_name = feed_config.get('name', 'Unknown')
        feed_url = feed_config.get('url')
        category = feed_config.get('category', 'general')
        
        if not feed_url:
            return []
        
        try:
            # Fetch and parse the feed
            feed = feedparser.parse(feed_url)
            
            if feed.bozo:
                print(f"Warning: Feed parsing issues for {feed_name}")
            
            news_items = []
            
            for entry in feed.entries[:self.max_articles]:
                try:
                    news_item = self._normalize_entry(entry, feed_name, category)
                    
                    # Filter by date if specified
                    if days_back is not None:
                        age_days = (datetime.now() - news_item['date']).days
                        if age_days > days_back:
                            continue
                    
                    # Filter for gaming/PC relevant content
                    if self._is_relevant(news_item):
                        news_items.append(news_item)
                        
                except Exception as e:
                    print(f"Error processing entry from {feed_name}: {e}")
                    continue
            
            return news_items
            
        except Exception as e:
            print(f"Error fetching feed {feed_name}: {e}")
            return []
    
    def _normalize_entry(self, entry, source: str, category: str) -> Dict:
        """
        Normalize a feed entry into a standard format.
        
        Args:
            entry: Feed entry from feedparser
            source: Name of the source
            category: Category of the feed
            
        Returns:
            Normalized news item dictionary
        """
        # Extract title
        title = entry.get('title', 'No title')
        
        # Extract summary/description
        summary = entry.get('summary', entry.get('description', ''))
        # Remove HTML tags from summary
        if summary:
            import re
            summary = re.sub(r'<[^>]+>', '', summary)
            summary = summary.strip()[:500]  # Limit length
        
        # Extract date
        date = None
        if hasattr(entry, 'published_parsed') and entry.published_parsed:
            from time import mktime
            date = datetime.fromtimestamp(mktime(entry.published_parsed))
        elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
            from time import mktime
            date = datetime.fromtimestamp(mktime(entry.updated_parsed))
        else:
            date = datetime.now()
        
        # Extract URL
        url = entry.get('link', '')
        
        return {
            'title': title,
            'summary': summary,
            'source': source,
            'category': category,
            'date': date,
            'url': url
        }
    
    def _is_relevant(self, news_item: Dict) -> bool:
        """
        Filter for gaming/PC relevant content using keyword matching.
        
        Args:
            news_item: Normalized news item
            
        Returns:
            True if relevant, False otherwise
        """
        # Keywords that indicate gaming/PC relevance
        gaming_keywords = [
            'gpu', 'graphics card', 'rtx', 'radeon', 'geforce', 'nvidia', 'amd',
            'cpu', 'processor', 'intel', 'ryzen', 'gaming', 'game', 'pc', 'computer',
            'fps', 'benchmark', 'performance', 'ram', 'memory', 'motherboard',
            'storage', 'ssd', 'nvme', 'pcie', 'overclock', 'cooling', 'thermal',
            'esports', 'steam', 'xbox', 'playstation', 'console', 'frame rate',
            'resolution', '4k', '1440p', 'monitor', 'display', 'rgb', 'case',
            'power supply', 'psu', 'build', 'rig', 'setup', 'hardware', 'tech'
        ]
        
        # Combine title and summary for searching
        text = (news_item['title'] + ' ' + news_item['summary']).lower()
        
        # Check if any keyword is present
        for keyword in gaming_keywords:
            if keyword in text:
                return True
        
        return False
    
    def fetch_by_topic(self, topic: str, days_back: int = 7) -> List[Dict]:
        """
        Fetch news filtered by a specific topic.
        
        Args:
            topic: Topic to search for
            days_back: Number of days to look back
            
        Returns:
            List of news items matching the topic
        """
        all_news = self.fetch_news(days_back=days_back)
        
        # Filter by topic
        topic_lower = topic.lower()
        filtered = [
            item for item in all_news
            if topic_lower in item['title'].lower() or topic_lower in item['summary'].lower()
        ]
        
        return filtered
