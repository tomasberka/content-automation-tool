"""
HelloComp Analytics Manager
Centralized system for tracking and managing all HelloComp.cz data:
- Website analytics (Google Analytics 4)
- Social media metrics (Facebook, Instagram, TikTok, YouTube)
- Performance monitoring
- Unified reporting dashboard
"""

import json
import datetime
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Any
from enum import Enum


class Platform(Enum):
    """Supported platforms for analytics tracking"""
    WEBSITE = "website"
    FACEBOOK = "facebook"
    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    YOUTUBE = "youtube"
    GOOGLE_ADS = "google_ads"
    FACEBOOK_ADS = "facebook_ads"


class MetricType(Enum):
    """Types of metrics to track"""
    VISITORS = "visitors"
    PAGE_VIEWS = "page_views"
    BOUNCE_RATE = "bounce_rate"
    AVG_SESSION = "avg_session_duration"
    CONVERSIONS = "conversions"
    REVENUE = "revenue"
    FOLLOWERS = "followers"
    ENGAGEMENT = "engagement_rate"
    REACH = "reach"
    IMPRESSIONS = "impressions"
    CLICKS = "clicks"
    SHARES = "shares"
    SAVES = "saves"
    COMMENTS = "comments"
    LIKES = "likes"


@dataclass
class Metric:
    """Single metric data point"""
    platform: str
    metric_type: str
    value: float
    date: str
    metadata: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class PlatformStats:
    """Statistics for a specific platform"""
    platform: str
    period_start: str
    period_end: str
    metrics: Dict[str, float]
    change_from_previous: Optional[Dict[str, float]] = None

    def to_dict(self) -> Dict:
        return asdict(self)


class AnalyticsManager:
    """
    Main class for managing analytics across all platforms
    Provides unified interface for data collection, storage, and reporting
    """

    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize Analytics Manager
        
        Args:
            config_file: Path to configuration file with API credentials
        """
        self.config = self._load_config(config_file) if config_file else {}
        self.data_store = []

    def _load_config(self, config_file: str) -> Dict:
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️  Configuration file {config_file} not found. Using default settings.")
            return {}

    def add_metric(self, platform: Platform, metric_type: MetricType, 
                   value: float, date: Optional[str] = None,
                   metadata: Optional[Dict] = None) -> None:
        """
        Add a single metric to the data store
        
        Args:
            platform: Platform enum
            metric_type: Type of metric
            value: Metric value
            date: Date in ISO format (YYYY-MM-DD), defaults to today
            metadata: Additional metadata for the metric
        """
        if date is None:
            date = datetime.date.today().isoformat()
        
        metric = Metric(
            platform=platform.value,
            metric_type=metric_type.value,
            value=value,
            date=date,
            metadata=metadata or {}
        )
        self.data_store.append(metric)

    def get_platform_stats(self, platform: Platform, 
                          start_date: str, end_date: str) -> PlatformStats:
        """
        Get aggregated statistics for a platform within date range
        
        Args:
            platform: Platform to get stats for
            start_date: Start date (ISO format)
            end_date: End date (ISO format)
            
        Returns:
            PlatformStats object with aggregated metrics
        """
        metrics = {}
        
        # Filter metrics for this platform and date range
        filtered = [
            m for m in self.data_store
            if m.platform == platform.value 
            and start_date <= m.date <= end_date
        ]
        
        # Aggregate by metric type
        for metric in filtered:
            if metric.metric_type not in metrics:
                metrics[metric.metric_type] = []
            metrics[metric.metric_type].append(metric.value)
        
        # Calculate averages
        aggregated = {
            k: sum(v) / len(v) if v else 0
            for k, v in metrics.items()
        }
        
        return PlatformStats(
            platform=platform.value,
            period_start=start_date,
            period_end=end_date,
            metrics=aggregated
        )

    def get_all_platforms_summary(self, start_date: str, 
                                  end_date: str) -> List[PlatformStats]:
        """
        Get summary statistics for all platforms
        
        Args:
            start_date: Start date (ISO format)
            end_date: End date (ISO format)
            
        Returns:
            List of PlatformStats for each platform
        """
        summaries = []
        for platform in Platform:
            stats = self.get_platform_stats(platform, start_date, end_date)
            if stats.metrics:  # Only include platforms with data
                summaries.append(stats)
        return summaries

    def export_to_json(self, filepath: str) -> None:
        """
        Export all metrics to JSON file
        
        Args:
            filepath: Path to output JSON file
        """
        data = [m.to_dict() for m in self.data_store]
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ Data exported to {filepath}")

    def import_from_json(self, filepath: str) -> None:
        """
        Import metrics from JSON file
        
        Args:
            filepath: Path to input JSON file
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for item in data:
            metric = Metric(**item)
            self.data_store.append(metric)
        print(f"✅ Imported {len(data)} metrics from {filepath}")

    def generate_report(self, start_date: str, end_date: str, 
                       output_format: str = 'text') -> str:
        """
        Generate a comprehensive report for the specified period
        
        Args:
            start_date: Start date (ISO format)
            end_date: End date (ISO format)
            output_format: 'text' or 'markdown'
            
        Returns:
            Formatted report string
        """
        summaries = self.get_all_platforms_summary(start_date, end_date)
        
        if output_format == 'markdown':
            return self._generate_markdown_report(summaries, start_date, end_date)
        else:
            return self._generate_text_report(summaries, start_date, end_date)

    def _generate_text_report(self, summaries: List[PlatformStats], 
                             start_date: str, end_date: str) -> str:
        """Generate plain text report"""
        lines = []
        lines.append("=" * 60)
        lines.append(f"HelloComp.cz Analytics Report")
        lines.append(f"Period: {start_date} to {end_date}")
        lines.append("=" * 60)
        lines.append("")
        
        for stats in summaries:
            lines.append(f"\n{stats.platform.upper()}")
            lines.append("-" * 40)
            for metric, value in stats.metrics.items():
                lines.append(f"  {metric:.<30} {value:>10.2f}")
        
        lines.append("\n" + "=" * 60)
        return "\n".join(lines)

    def _generate_markdown_report(self, summaries: List[PlatformStats],
                                 start_date: str, end_date: str) -> str:
        """Generate Markdown formatted report"""
        lines = []
        lines.append("# HelloComp.cz Analytics Report")
        lines.append(f"\n**Period:** {start_date} to {end_date}\n")
        
        for stats in summaries:
            lines.append(f"## {stats.platform.title()}")
            lines.append("\n| Metric | Value |")
            lines.append("|--------|-------|")
            for metric, value in stats.metrics.items():
                lines.append(f"| {metric.replace('_', ' ').title()} | {value:.2f} |")
            lines.append("")
        
        return "\n".join(lines)


class GoogleAnalyticsConnector:
    """Connector for Google Analytics 4"""
    
    def __init__(self, property_id: str, credentials_path: Optional[str] = None):
        """
        Initialize GA4 connector
        
        Args:
            property_id: GA4 property ID
            credentials_path: Path to service account JSON credentials
        """
        self.property_id = property_id
        self.credentials_path = credentials_path

    def fetch_metrics(self, start_date: str, end_date: str) -> List[Metric]:
        """
        Fetch metrics from Google Analytics
        
        Note: This is a placeholder. Actual implementation requires
        google-analytics-data package and authentication setup.
        
        Args:
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            
        Returns:
            List of Metric objects
        """
        # Placeholder - would use Google Analytics Data API
        print("⚠️  Google Analytics integration requires setup:")
        print("   1. Install: pip install google-analytics-data")
        print("   2. Create service account and download credentials")
        print("   3. Enable Google Analytics Data API")
        return []


class SocialMediaConnector:
    """Connector for social media platforms (Facebook, Instagram, etc.)"""
    
    def __init__(self, platform: Platform, access_token: Optional[str] = None):
        """
        Initialize social media connector
        
        Args:
            platform: Social media platform
            access_token: API access token
        """
        self.platform = platform
        self.access_token = access_token

    def fetch_metrics(self, start_date: str, end_date: str) -> List[Metric]:
        """
        Fetch metrics from social media platform
        
        Note: This is a placeholder. Actual implementation requires
        platform-specific API libraries and authentication.
        
        Args:
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            
        Returns:
            List of Metric objects
        """
        print(f"⚠️  {self.platform.value} integration requires setup:")
        print("   1. Create app in platform developer console")
        print("   2. Get access token with required permissions")
        print("   3. Install platform-specific SDK")
        return []


if __name__ == "__main__":
    # Example usage
    print("HelloComp Analytics Manager - Example Usage\n")
    
    # Initialize manager
    manager = AnalyticsManager()
    
    # Add sample data
    today = datetime.date.today().isoformat()
    
    # Website metrics
    manager.add_metric(Platform.WEBSITE, MetricType.VISITORS, 1250, today)
    manager.add_metric(Platform.WEBSITE, MetricType.PAGE_VIEWS, 3420, today)
    manager.add_metric(Platform.WEBSITE, MetricType.CONVERSIONS, 15, today)
    manager.add_metric(Platform.WEBSITE, MetricType.REVENUE, 45000, today)
    
    # Facebook metrics
    manager.add_metric(Platform.FACEBOOK, MetricType.FOLLOWERS, 2350, today)
    manager.add_metric(Platform.FACEBOOK, MetricType.ENGAGEMENT, 4.2, today)
    manager.add_metric(Platform.FACEBOOK, MetricType.REACH, 8500, today)
    
    # Instagram metrics
    manager.add_metric(Platform.INSTAGRAM, MetricType.FOLLOWERS, 3200, today)
    manager.add_metric(Platform.INSTAGRAM, MetricType.ENGAGEMENT, 5.8, today)
    manager.add_metric(Platform.INSTAGRAM, MetricType.SAVES, 145, today)
    
    # Generate report
    report = manager.generate_report(today, today, output_format='markdown')
    print(report)
