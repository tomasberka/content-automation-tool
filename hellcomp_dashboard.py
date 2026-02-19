#!/usr/bin/env python3
"""
HelloComp.cz - Centralized Management Dashboard
Complete system for tracking and managing:
- Website performance (www.hellcomp.cz)
- Social media (Facebook, Instagram, TikTok, YouTube)
- All metrics in one place
"""

import argparse
import datetime
import json
import os
from typing import Dict, List, Optional
from analytics_manager import (
    AnalyticsManager, Platform, MetricType,
    GoogleAnalyticsConnector, SocialMediaConnector
)


class HelloCompDashboard:
    """Main dashboard for HelloComp.cz analytics and management"""
    
    def __init__(self, config_file: str = "dashboard_config.json"):
        """
        Initialize HelloComp Dashboard
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.config = self._load_or_create_config()
        self.analytics = AnalyticsManager(config_file)
        
    def _load_or_create_config(self) -> Dict:
        """Load configuration or create default if not exists"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Create default configuration
            default_config = {
                "website": {
                    "url": "https://www.hellcomp.cz",
                    "google_analytics": {
                        "property_id": "YOUR_GA4_PROPERTY_ID",
                        "credentials_path": "ga4_credentials.json"
                    }
                },
                "social_media": {
                    "facebook": {
                        "page_id": "YOUR_FACEBOOK_PAGE_ID",
                        "access_token": "YOUR_FACEBOOK_ACCESS_TOKEN"
                    },
                    "instagram": {
                        "account_id": "YOUR_INSTAGRAM_ACCOUNT_ID",
                        "access_token": "YOUR_INSTAGRAM_ACCESS_TOKEN"
                    },
                    "tiktok": {
                        "username": "YOUR_TIKTOK_USERNAME"
                    },
                    "youtube": {
                        "channel_id": "YOUR_YOUTUBE_CHANNEL_ID",
                        "api_key": "YOUR_YOUTUBE_API_KEY"
                    }
                },
                "reporting": {
                    "default_period_days": 30,
                    "export_directory": "./reports",
                    "auto_export": True
                }
            }
            
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(default_config, f, indent=2)
            
            print(f"✅ Created default configuration file: {self.config_file}")
            print("⚠️  Please update with your actual credentials and IDs")
            
            return default_config
    
    def sync_all_platforms(self, start_date: str, end_date: str) -> None:
        """
        Sync data from all configured platforms
        
        Args:
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
        """
        print("\n🔄 Syncing data from all platforms...")
        print(f"📅 Period: {start_date} to {end_date}\n")
        
        # Sync Google Analytics
        if 'google_analytics' in self.config.get('website', {}):
            print("📊 Syncing Google Analytics...")
            self._sync_google_analytics(start_date, end_date)
        
        # Sync Social Media
        social_config = self.config.get('social_media', {})
        
        if 'facebook' in social_config:
            print("📘 Syncing Facebook...")
            self._sync_facebook(start_date, end_date)
        
        if 'instagram' in social_config:
            print("📷 Syncing Instagram...")
            self._sync_instagram(start_date, end_date)
        
        if 'tiktok' in social_config:
            print("🎵 Syncing TikTok...")
            self._sync_tiktok(start_date, end_date)
        
        if 'youtube' in social_config:
            print("📺 Syncing YouTube...")
            self._sync_youtube(start_date, end_date)
        
        print("\n✅ Sync completed!")
    
    def _sync_google_analytics(self, start_date: str, end_date: str) -> None:
        """Sync Google Analytics data"""
        ga_config = self.config['website']['google_analytics']
        connector = GoogleAnalyticsConnector(
            property_id=ga_config.get('property_id'),
            credentials_path=ga_config.get('credentials_path')
        )
        metrics = connector.fetch_metrics(start_date, end_date)
        
        for metric in metrics:
            self.analytics.data_store.append(metric)
    
    def _sync_facebook(self, start_date: str, end_date: str) -> None:
        """Sync Facebook data"""
        fb_config = self.config['social_media']['facebook']
        connector = SocialMediaConnector(
            platform=Platform.FACEBOOK,
            access_token=fb_config.get('access_token')
        )
        metrics = connector.fetch_metrics(start_date, end_date)
        
        for metric in metrics:
            self.analytics.data_store.append(metric)
    
    def _sync_instagram(self, start_date: str, end_date: str) -> None:
        """Sync Instagram data"""
        ig_config = self.config['social_media']['instagram']
        connector = SocialMediaConnector(
            platform=Platform.INSTAGRAM,
            access_token=ig_config.get('access_token')
        )
        metrics = connector.fetch_metrics(start_date, end_date)
        
        for metric in metrics:
            self.analytics.data_store.append(metric)
    
    def _sync_tiktok(self, start_date: str, end_date: str) -> None:
        """Sync TikTok data"""
        print("   ℹ️  TikTok sync not yet implemented")
    
    def _sync_youtube(self, start_date: str, end_date: str) -> None:
        """Sync YouTube data"""
        print("   ℹ️  YouTube sync not yet implemented")
    
    def generate_daily_report(self, date: Optional[str] = None) -> str:
        """
        Generate daily report
        
        Args:
            date: Date for report (YYYY-MM-DD), defaults to today
            
        Returns:
            Report as string
        """
        if date is None:
            date = datetime.date.today().isoformat()
        
        return self.analytics.generate_report(date, date, output_format='markdown')
    
    def generate_weekly_report(self, end_date: Optional[str] = None) -> str:
        """
        Generate weekly report
        
        Args:
            end_date: End date (YYYY-MM-DD), defaults to today
            
        Returns:
            Report as string
        """
        if end_date is None:
            end_date = datetime.date.today()
        else:
            end_date = datetime.date.fromisoformat(end_date)
        
        start_date = end_date - datetime.timedelta(days=7)
        
        return self.analytics.generate_report(
            start_date.isoformat(),
            end_date.isoformat(),
            output_format='markdown'
        )
    
    def generate_monthly_report(self, year: int, month: int) -> str:
        """
        Generate monthly report
        
        Args:
            year: Year
            month: Month (1-12)
            
        Returns:
            Report as string
        """
        import calendar
        
        start_date = datetime.date(year, month, 1)
        last_day = calendar.monthrange(year, month)[1]
        end_date = datetime.date(year, month, last_day)
        
        return self.analytics.generate_report(
            start_date.isoformat(),
            end_date.isoformat(),
            output_format='markdown'
        )
    
    def export_reports(self, period: str = 'daily') -> None:
        """
        Export reports to files
        
        Args:
            period: 'daily', 'weekly', or 'monthly'
        """
        export_dir = self.config['reporting'].get('export_directory', './reports')
        os.makedirs(export_dir, exist_ok=True)
        
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        
        if period == 'daily':
            report = self.generate_daily_report()
            filename = f"daily_report_{timestamp}.md"
        elif period == 'weekly':
            report = self.generate_weekly_report()
            filename = f"weekly_report_{timestamp}.md"
        elif period == 'monthly':
            today = datetime.date.today()
            report = self.generate_monthly_report(today.year, today.month)
            filename = f"monthly_report_{timestamp}.md"
        else:
            raise ValueError(f"Invalid period: {period}")
        
        filepath = os.path.join(export_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✅ Report exported to: {filepath}")
    
    def show_overview(self) -> None:
        """Display overview of all platforms"""
        print("\n" + "=" * 70)
        print("HelloComp.cz - Centralized Management Dashboard")
        print("=" * 70)
        print(f"\n🌐 Website: {self.config['website']['url']}")
        print("\n📱 Social Media Platforms:")
        
        social = self.config.get('social_media', {})
        platforms = []
        
        if 'facebook' in social:
            platforms.append("Facebook")
        if 'instagram' in social:
            platforms.append("Instagram")
        if 'tiktok' in social:
            platforms.append("TikTok")
        if 'youtube' in social:
            platforms.append("YouTube")
        
        for platform in platforms:
            print(f"   ✓ {platform}")
        
        print(f"\n📊 Total metrics stored: {len(self.analytics.data_store)}")
        print("\n" + "=" * 70 + "\n")
    
    def add_manual_metric(self, platform: str, metric_type: str, 
                         value: float, date: Optional[str] = None) -> None:
        """
        Manually add a metric
        
        Args:
            platform: Platform name
            metric_type: Type of metric
            value: Metric value
            date: Date (YYYY-MM-DD), defaults to today
        """
        platform_enum = Platform[platform.upper()]
        metric_enum = MetricType[metric_type.upper()]
        
        self.analytics.add_metric(platform_enum, metric_enum, value, date)
        print(f"✅ Added {metric_type} = {value} for {platform}")


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="HelloComp.cz Centralized Management Dashboard"
    )
    
    parser.add_argument(
        '--sync',
        action='store_true',
        help='Sync data from all platforms'
    )
    
    parser.add_argument(
        '--report',
        choices=['daily', 'weekly', 'monthly'],
        help='Generate report for specified period'
    )
    
    parser.add_argument(
        '--export',
        action='store_true',
        help='Export report to file'
    )
    
    parser.add_argument(
        '--overview',
        action='store_true',
        help='Show dashboard overview'
    )
    
    parser.add_argument(
        '--start-date',
        help='Start date for sync (YYYY-MM-DD)'
    )
    
    parser.add_argument(
        '--end-date',
        help='End date for sync (YYYY-MM-DD)'
    )
    
    parser.add_argument(
        '--config',
        default='dashboard_config.json',
        help='Path to configuration file'
    )
    
    args = parser.parse_args()
    
    # Initialize dashboard
    dashboard = HelloCompDashboard(config_file=args.config)
    
    # Show overview if requested or no other action
    if args.overview or not any([args.sync, args.report]):
        dashboard.show_overview()
    
    # Sync data
    if args.sync:
        end_date = args.end_date or datetime.date.today().isoformat()
        start_date = args.start_date or (
            datetime.date.today() - datetime.timedelta(days=30)
        ).isoformat()
        
        dashboard.sync_all_platforms(start_date, end_date)
    
    # Generate report
    if args.report:
        print(f"\n📊 Generating {args.report} report...\n")
        
        if args.report == 'daily':
            report = dashboard.generate_daily_report()
        elif args.report == 'weekly':
            report = dashboard.generate_weekly_report()
        elif args.report == 'monthly':
            today = datetime.date.today()
            report = dashboard.generate_monthly_report(today.year, today.month)
        
        print(report)
        
        if args.export:
            dashboard.export_reports(args.report)


if __name__ == "__main__":
    main()
