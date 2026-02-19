#!/usr/bin/env python3
"""
Example: Import metrics from CSV or export to various formats
Useful for integrating with Google Sheets, Excel, or other tools
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analytics_manager import AnalyticsManager, Platform, MetricType
import json
import datetime


def export_to_csv(json_file: str, csv_file: str):
    """
    Export metrics from JSON to CSV format
    
    Args:
        json_file: Input JSON file
        csv_file: Output CSV file
    """
    manager = AnalyticsManager()
    
    try:
        manager.import_from_json(json_file)
        print(f"✅ Loaded {len(manager.data_store)} metrics from {json_file}")
    except FileNotFoundError:
        print(f"❌ File not found: {json_file}")
        return
    
    # Write CSV
    with open(csv_file, 'w', encoding='utf-8') as f:
        # Header
        f.write("Date,Platform,Metric,Value\n")
        
        # Data rows
        for metric in manager.data_store:
            f.write(f"{metric.date},{metric.platform},{metric.metric_type},{metric.value}\n")
    
    print(f"✅ Exported to {csv_file}")
    print(f"📊 Total rows: {len(manager.data_store)}")


def import_from_csv(csv_file: str, json_file: str):
    """
    Import metrics from CSV to JSON format
    
    Args:
        csv_file: Input CSV file
        json_file: Output JSON file
    
    CSV format expected:
    Date,Platform,Metric,Value
    2026-02-19,website,visitors,1250
    """
    manager = AnalyticsManager()
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            # Skip header
            for line in lines[1:]:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    date, platform, metric, value = parts[0], parts[1], parts[2], parts[3]
                    
                    try:
                        # Convert to enums
                        platform_enum = Platform[platform.upper()]
                        metric_enum = MetricType[metric.upper()]
                        
                        manager.add_metric(
                            platform_enum,
                            metric_enum,
                            float(value),
                            date
                        )
                    except (KeyError, ValueError) as e:
                        print(f"⚠️  Skipping invalid row: {line.strip()} ({e})")
        
        print(f"✅ Imported {len(manager.data_store)} metrics from {csv_file}")
        
        # Export to JSON
        manager.export_to_json(json_file)
        
    except FileNotFoundError:
        print(f"❌ File not found: {csv_file}")


def create_sample_csv(csv_file: str):
    """Create a sample CSV file for testing"""
    
    with open(csv_file, 'w', encoding='utf-8') as f:
        f.write("Date,Platform,Metric,Value\n")
        
        # Add sample data for last 7 days
        for days_ago in range(7, 0, -1):
            date = (datetime.date.today() - datetime.timedelta(days=days_ago)).isoformat()
            
            # Website
            f.write(f"{date},website,visitors,{1200 + days_ago * 10}\n")
            f.write(f"{date},website,conversions,{10 + days_ago}\n")
            
            # Facebook
            f.write(f"{date},facebook,reach,{8000 + days_ago * 100}\n")
            f.write(f"{date},facebook,engagement,{4.5 + days_ago * 0.1}\n")
            
            # Instagram
            f.write(f"{date},instagram,followers,{3000 + days_ago * 5}\n")
            f.write(f"{date},instagram,saves,{100 + days_ago * 2}\n")
    
    print(f"✅ Created sample CSV: {csv_file}")
    print("📝 Edit this file and then import it with:")
    print(f"   python examples/import_export.py --import {csv_file} output.json")


def print_usage():
    """Print usage instructions"""
    print("Usage:")
    print("  # Export JSON to CSV")
    print("  python examples/import_export.py --export metrics.json output.csv")
    print()
    print("  # Import CSV to JSON")
    print("  python examples/import_export.py --import data.csv output.json")
    print()
    print("  # Create sample CSV template")
    print("  python examples/import_export.py --create-sample template.csv")
    print()
    print("CSV Format:")
    print("  Date,Platform,Metric,Value")
    print("  2026-02-19,website,visitors,1250")
    print("  2026-02-19,facebook,reach,8500")
    print()
    print("Supported platforms: website, facebook, instagram, tiktok, youtube")
    print("Supported metrics: visitors, page_views, conversions, followers, engagement, reach, etc.")


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("HelloComp Dashboard - Import/Export Utility")
    print("=" * 70 + "\n")
    
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == '--export' and len(sys.argv) >= 4:
        export_to_csv(sys.argv[2], sys.argv[3])
    
    elif command == '--import' and len(sys.argv) >= 4:
        import_from_csv(sys.argv[2], sys.argv[3])
    
    elif command == '--create-sample' and len(sys.argv) >= 3:
        create_sample_csv(sys.argv[2])
    
    else:
        print("❌ Invalid command or missing arguments\n")
        print_usage()
