#!/usr/bin/env python3
"""
Example: Compare performance between two periods
Useful for monthly/weekly reviews
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analytics_manager import AnalyticsManager, Platform, MetricType
import datetime


def compare_periods(period1_start, period1_end, period2_start, period2_end):
    """
    Compare metrics between two time periods
    
    Args:
        period1_start: Start of first period (YYYY-MM-DD)
        period1_end: End of first period (YYYY-MM-DD)
        period2_start: Start of second period (YYYY-MM-DD)
        period2_end: End of second period (YYYY-MM-DD)
    """
    
    manager = AnalyticsManager()
    
    # Load historical data if exists
    try:
        manager.import_from_json('metrics_backup.json')
        print(f"✅ Loaded {len(manager.data_store)} historical metrics\n")
    except FileNotFoundError:
        print("⚠️  No historical data found. Add some metrics first.\n")
        return
    
    # Get stats for both periods
    print("=" * 70)
    print("PERIOD COMPARISON")
    print("=" * 70)
    
    print(f"\n📅 Period 1: {period1_start} to {period1_end}")
    print(f"📅 Period 2: {period2_start} to {period2_end}\n")
    
    platforms = [Platform.WEBSITE, Platform.FACEBOOK, Platform.INSTAGRAM]
    
    for platform in platforms:
        print(f"\n{'='*70}")
        print(f"{platform.value.upper()}")
        print('='*70)
        
        stats1 = manager.get_platform_stats(platform, period1_start, period1_end)
        stats2 = manager.get_platform_stats(platform, period2_start, period2_end)
        
        if not stats1.metrics and not stats2.metrics:
            print("  No data available for this platform")
            continue
        
        # Compare each metric
        all_metrics = set(list(stats1.metrics.keys()) + list(stats2.metrics.keys()))
        
        print(f"\n{'Metric':<25} {'Period 1':>15} {'Period 2':>15} {'Change':>15}")
        print('-' * 70)
        
        for metric in sorted(all_metrics):
            val1 = stats1.metrics.get(metric, 0)
            val2 = stats2.metrics.get(metric, 0)
            
            if val1 > 0:
                change = ((val2 - val1) / val1) * 100
                change_str = f"{change:+.1f}%"
                
                # Color code the change (using emoji)
                if change > 10:
                    indicator = "📈"
                elif change < -10:
                    indicator = "📉"
                else:
                    indicator = "➡️ "
            else:
                change_str = "N/A"
                indicator = "  "
            
            print(f"{metric:<25} {val1:>15.2f} {val2:>15.2f} {indicator} {change_str:>12}")


def compare_this_vs_last_month():
    """Compare current month vs last month"""
    
    today = datetime.date.today()
    
    # This month
    this_month_start = datetime.date(today.year, today.month, 1)
    this_month_end = today
    
    # Last month
    if today.month == 1:
        last_month_start = datetime.date(today.year - 1, 12, 1)
        import calendar
        last_day = calendar.monthrange(today.year - 1, 12)[1]
        last_month_end = datetime.date(today.year - 1, 12, last_day)
    else:
        last_month_start = datetime.date(today.year, today.month - 1, 1)
        import calendar
        last_day = calendar.monthrange(today.year, today.month - 1)[1]
        last_month_end = datetime.date(today.year, today.month - 1, last_day)
    
    compare_periods(
        last_month_start.isoformat(),
        last_month_end.isoformat(),
        this_month_start.isoformat(),
        this_month_end.isoformat()
    )


def compare_this_vs_last_week():
    """Compare current week vs last week"""
    
    today = datetime.date.today()
    
    # This week (last 7 days)
    this_week_start = today - datetime.timedelta(days=6)
    this_week_end = today
    
    # Last week (7 days before that)
    last_week_start = today - datetime.timedelta(days=13)
    last_week_end = today - datetime.timedelta(days=7)
    
    compare_periods(
        last_week_start.isoformat(),
        last_week_end.isoformat(),
        this_week_start.isoformat(),
        this_week_end.isoformat()
    )


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("HelloComp Dashboard - Period Comparison")
    print("=" * 70 + "\n")
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--month':
            compare_this_vs_last_month()
        elif sys.argv[1] == '--week':
            compare_this_vs_last_week()
        elif len(sys.argv) >= 5:
            # Custom periods: p1_start p1_end p2_start p2_end
            compare_periods(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print("Usage:")
            print("  python compare_periods.py --week")
            print("  python compare_periods.py --month")
            print("  python compare_periods.py 2026-01-01 2026-01-31 2026-02-01 2026-02-28")
    else:
        print("Usage:")
        print("  python compare_periods.py --week       # Compare this week vs last week")
        print("  python compare_periods.py --month      # Compare this month vs last month")
        print("  python compare_periods.py <start1> <end1> <start2> <end2>  # Custom comparison")
