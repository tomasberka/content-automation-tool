#!/usr/bin/env python3
"""
Example: Adding daily metrics manually to HelloComp Dashboard
Useful when you don't have API integration set up yet
"""

import sys
import os

# Add parent directory to path to import dashboard
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hellcomp_dashboard import HelloCompDashboard
import datetime

def add_today_metrics():
    """Add today's metrics from various sources"""
    
    # Initialize dashboard
    dashboard = HelloCompDashboard()
    
    # Get today's date
    today = datetime.date.today().isoformat()
    
    print(f"📅 Adding metrics for {today}\n")
    
    # Website metrics (from Google Analytics)
    print("🌐 Website metrics:")
    dashboard.add_manual_metric('website', 'visitors', 1250, today)
    dashboard.add_manual_metric('website', 'page_views', 3420, today)
    dashboard.add_manual_metric('website', 'bounce_rate', 58.5, today)
    dashboard.add_manual_metric('website', 'avg_session', 135.0, today)  # seconds
    dashboard.add_manual_metric('website', 'conversions', 15, today)
    dashboard.add_manual_metric('website', 'revenue', 45000.0, today)  # CZK
    print("   ✓ Added 6 metrics\n")
    
    # Facebook metrics
    print("📘 Facebook metrics:")
    dashboard.add_manual_metric('facebook', 'followers', 2350, today)
    dashboard.add_manual_metric('facebook', 'engagement', 4.2, today)  # %
    dashboard.add_manual_metric('facebook', 'reach', 8500, today)
    dashboard.add_manual_metric('facebook', 'impressions', 12300, today)
    dashboard.add_manual_metric('facebook', 'likes', 320, today)
    dashboard.add_manual_metric('facebook', 'comments', 45, today)
    dashboard.add_manual_metric('facebook', 'shares', 28, today)
    print("   ✓ Added 7 metrics\n")
    
    # Instagram metrics
    print("📷 Instagram metrics:")
    dashboard.add_manual_metric('instagram', 'followers', 3200, today)
    dashboard.add_manual_metric('instagram', 'engagement', 5.8, today)  # %
    dashboard.add_manual_metric('instagram', 'reach', 9200, today)
    dashboard.add_manual_metric('instagram', 'impressions', 15600, today)
    dashboard.add_manual_metric('instagram', 'saves', 145, today)
    dashboard.add_manual_metric('instagram', 'likes', 480, today)
    dashboard.add_manual_metric('instagram', 'comments', 67, today)
    print("   ✓ Added 7 metrics\n")
    
    # Generate and display report
    print("=" * 70)
    print("📊 DAILY REPORT")
    print("=" * 70)
    report = dashboard.generate_daily_report(today)
    print(report)
    
    # Export data
    print("\n💾 Exporting data...")
    dashboard.analytics.export_to_json(f'metrics_backup_{today}.json')
    
    print("\n✅ All metrics added successfully!")
    print(f"📂 Data saved to: metrics_backup_{today}.json")


def add_weekly_metrics():
    """Add metrics for the past week (example with historical data)"""
    
    dashboard = HelloCompDashboard()
    
    print("📅 Adding weekly metrics...\n")
    
    # Add metrics for last 7 days
    for days_ago in range(7, 0, -1):
        date = (datetime.date.today() - datetime.timedelta(days=days_ago)).isoformat()
        
        # Simulate varying metrics
        import random
        base_visitors = 1200
        visitors = base_visitors + random.randint(-100, 150)
        
        dashboard.add_manual_metric('website', 'visitors', visitors, date)
        dashboard.add_manual_metric('facebook', 'reach', 8000 + random.randint(-500, 800), date)
        dashboard.add_manual_metric('instagram', 'engagement', 5.5 + random.uniform(-0.5, 0.8), date)
        
        print(f"   ✓ Added metrics for {date}")
    
    print("\n📊 Generating weekly report...\n")
    report = dashboard.generate_weekly_report()
    print(report)
    
    print("\n✅ Weekly metrics added!")


if __name__ == "__main__":
    print("=" * 70)
    print("HelloComp Dashboard - Manual Metrics Example")
    print("=" * 70)
    print()
    
    if len(sys.argv) > 1 and sys.argv[1] == '--weekly':
        add_weekly_metrics()
    else:
        add_today_metrics()
        print("\n💡 Tip: Run with --weekly to add a week of sample data")
