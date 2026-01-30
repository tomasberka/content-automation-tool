#!/usr/bin/env python3
"""
Content Automation Tool - Main CLI
Generates content for gaming/PC creators across multiple platforms.
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional

from rich.console import Console
from rich.table import Table
from rich.progress import track

from src.news_fetcher import NewsFetcher
from src.content_classifier import ContentClassifier
from src.hook_generator import HookGenerator
from src.script_builder import ScriptBuilder
from src.platform_formatter import PlatformFormatter


console = Console()


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Content Automation Tool for Gaming/PC Creators',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate.py --date today
  python generate.py --topic "RTX 5070" --days 7
  python generate.py --pillar education --platform tiktok
  python generate.py --days 7 --output output/ --format json
        """
    )
    
    parser.add_argument(
        '--date',
        type=str,
        choices=['today', 'yesterday', 'week'],
        help='Date filter for news (today, yesterday, week)'
    )
    
    parser.add_argument(
        '--days',
        type=int,
        default=1,
        help='Number of days to look back (default: 1)'
    )
    
    parser.add_argument(
        '--topic',
        type=str,
        help='Filter by specific topic (e.g., "RTX 5070", "Ryzen")'
    )
    
    parser.add_argument(
        '--pillar',
        type=str,
        choices=['education', 'social_proof', 'entertainment', 'offers'],
        help='Filter by content pillar'
    )
    
    parser.add_argument(
        '--platform',
        type=str,
        choices=['tiktok', 'instagram', 'youtube', 'twitter', 'all'],
        default='all',
        help='Target platform (default: all)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='output/',
        help='Output directory (default: output/)'
    )
    
    parser.add_argument(
        '--format',
        type=str,
        choices=['json', 'markdown', 'both'],
        default='both',
        help='Output format (default: both)'
    )
    
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Verbose output for debugging'
    )
    
    parser.add_argument(
        '--max-items',
        type=int,
        default=10,
        help='Maximum number of content items to generate (default: 10)'
    )
    
    return parser.parse_args()


def process_date_filter(args) -> int:
    """Process date filter argument and return days back."""
    if args.date == 'today':
        return 1
    elif args.date == 'yesterday':
        return 2
    elif args.date == 'week':
        return 7
    else:
        return args.days


def main():
    """Main execution function."""
    args = parse_arguments()
    
    console.print("\n[bold cyan]🎮 Content Automation Tool - HelloComp[/bold cyan]\n")
    
    # Initialize components
    try:
        news_fetcher = NewsFetcher()
        classifier = ContentClassifier()
        hook_generator = HookGenerator()
        script_builder = ScriptBuilder()
        platform_formatter = PlatformFormatter()
    except Exception as e:
        console.print(f"[red]Error initializing components: {e}[/red]")
        return 1
    
    # Fetch news
    console.print("[yellow]📰 Fetching news...[/yellow]")
    days_back = process_date_filter(args)
    
    try:
        if args.topic:
            news_items = news_fetcher.fetch_by_topic(args.topic, days_back=days_back)
        else:
            news_items = news_fetcher.fetch_news(days_back=days_back)
    except Exception as e:
        console.print(f"[red]Error fetching news: {e}[/red]")
        return 1
    
    if not news_items:
        console.print("[red]No news items found![/red]")
        return 1
    
    console.print(f"[green]✓ Found {len(news_items)} news items[/green]\n")
    
    # Classify content
    console.print("[yellow]🔍 Classifying content...[/yellow]")
    try:
        classified_items = classifier.classify_batch(news_items)
    except Exception as e:
        console.print(f"[red]Error classifying content: {e}[/red]")
        return 1
    
    # Filter by pillar if specified
    if args.pillar:
        classified_items = [
            item for item in classified_items
            if item['pillar'] == args.pillar
        ]
        console.print(f"[green]✓ Filtered to {len(classified_items)} {args.pillar} items[/green]\n")
    
    # Limit items
    classified_items = classified_items[:args.max_items]
    
    # Generate content
    console.print(f"[yellow]✨ Generating content for {len(classified_items)} items...[/yellow]\n")
    
    all_content = []
    
    for item in track(classified_items, description="Processing..."):
        try:
            # Generate hooks
            hooks = hook_generator.generate_hooks(item, num_variations=3)
            
            # Use the first hook for script generation
            if not hooks:
                continue
            
            hook = hooks[0]
            
            # Generate script (default 30s)
            script = script_builder.build_script(item, hook, duration=30)
            
            # Format for platforms
            if args.platform == 'all':
                platform_content = platform_formatter.format_all(script, item)
            else:
                platform_map = {
                    'tiktok': platform_formatter.format_for_tiktok,
                    'instagram': platform_formatter.format_for_instagram_reels,
                    'youtube': platform_formatter.format_for_youtube_shorts,
                    'twitter': platform_formatter.format_for_twitter
                }
                format_func = platform_map.get(args.platform)
                if format_func:
                    platform_content = {args.platform: format_func(script, item)}
                else:
                    platform_content = {}
            
            # Compile all content
            content_item = {
                'news': item,
                'hooks': hooks,
                'script': script,
                'platforms': platform_content,
                'generated_at': datetime.now().isoformat()
            }
            
            all_content.append(content_item)
            
        except Exception as e:
            if args.verbose:
                console.print(f"[red]Error processing item: {e}[/red]")
            continue
    
    console.print(f"\n[green]✓ Generated {len(all_content)} content items[/green]\n")
    
    # Save output
    if all_content:
        save_output(all_content, args)
    else:
        console.print("[red]No content generated![/red]")
        return 1
    
    console.print("\n[bold green]✓ Content generation complete![/bold green]\n")
    return 0


def save_output(content: List[Dict], args):
    """Save generated content to files."""
    # Create output directory structure
    date_str = datetime.now().strftime('%Y-%m-%d')
    output_dir = Path(args.output) / date_str
    output_dir.mkdir(parents=True, exist_ok=True)
    
    console.print(f"[yellow]💾 Saving output to {output_dir}...[/yellow]")
    
    # Save JSON
    if args.format in ['json', 'both']:
        json_file = output_dir / 'content.json'
        with open(json_file, 'w') as f:
            json.dump(content, f, indent=2, default=str)
        console.print(f"[green]✓ Saved JSON: {json_file}[/green]")
    
    # Save Markdown
    if args.format in ['markdown', 'both']:
        # Save hooks reference
        hooks_file = output_dir / 'hooks.md'
        save_hooks_markdown(content, hooks_file)
        console.print(f"[green]✓ Saved hooks: {hooks_file}[/green]")
        
        # Save platform-specific content
        if args.platform == 'all':
            save_platform_markdown(content, output_dir)
        else:
            save_single_platform_markdown(content, output_dir, args.platform)


def save_hooks_markdown(content: List[Dict], filepath: Path):
    """Save hooks as markdown reference."""
    with open(filepath, 'w') as f:
        f.write("# Video Hooks - Quick Reference\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        
        for i, item in enumerate(content, 1):
            f.write(f"## {i}. {item['news']['title']}\n\n")
            f.write(f"**Source:** {item['news']['source']}\n")
            f.write(f"**Pillar:** {item['news']['pillar']}\n\n")
            f.write("**Hooks:**\n\n")
            
            for hook in item['hooks']:
                f.write(f"- [{hook['type']}] {hook['text']}\n")
            
            f.write("\n---\n\n")


def save_platform_markdown(content: List[Dict], output_dir: Path):
    """Save platform-specific markdown files."""
    platforms = {
        'tiktok': 'TikTok',
        'instagram_reels': 'Instagram Reels',
        'youtube_shorts': 'YouTube Shorts',
        'youtube_longform': 'YouTube Long-form',
        'x_twitter': 'X/Twitter'
    }
    
    for platform_key, platform_name in platforms.items():
        platform_dir = output_dir / platform_key.split('_')[0]
        platform_dir.mkdir(exist_ok=True)
        
        filepath = platform_dir / 'posts.md'
        
        with open(filepath, 'w') as f:
            f.write(f"# {platform_name} Content\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            
            for i, item in enumerate(content, 1):
                platform_data = item['platforms'].get(platform_key)
                if not platform_data:
                    continue
                
                f.write(f"## Post {i}: {item['news']['title']}\n\n")
                
                if platform_key == 'tiktok':
                    f.write(f"**Caption:**\n{platform_data['caption']}\n\n")
                    f.write(f"**Hashtags:** {' '.join(platform_data['hashtags'])}\n\n")
                    f.write(f"**Duration:** {platform_data['duration']}s\n\n")
                    f.write(f"**Audio:** {platform_data['audio_suggestion']}\n\n")
                
                elif platform_key == 'instagram_reels':
                    f.write(f"**Caption:**\n{platform_data['caption']}\n\n")
                    f.write(f"**Hashtags:**{platform_data['hashtag_block']}\n\n")
                    f.write(f"**Duration:** {platform_data['duration']}s\n\n")
                
                elif platform_key == 'youtube_shorts':
                    f.write(f"**Title:** {platform_data['title']}\n\n")
                    f.write(f"**Description:**\n{platform_data['description']}\n\n")
                    f.write(f"**Tags:** {', '.join(platform_data['tags'])}\n\n")
                
                elif platform_key == 'youtube_longform':
                    f.write(f"**Title:** {platform_data['title']}\n\n")
                    f.write(f"**Description:**\n{platform_data['description']}\n\n")
                    f.write("**Chapters:**\n")
                    for chapter in platform_data['chapters']:
                        f.write(f"- {chapter['time']} {chapter['title']}\n")
                    f.write("\n")
                
                elif platform_key == 'x_twitter':
                    f.write(f"**Single Tweet:**\n{platform_data['single_tweet']}\n\n")
                    f.write("**Thread:**\n")
                    for tweet in platform_data['thread']:
                        f.write(f"{tweet}\n\n")
                
                f.write("---\n\n")
        
        console.print(f"[green]✓ Saved {platform_name}: {filepath}[/green]")


def save_single_platform_markdown(content: List[Dict], output_dir: Path, platform: str):
    """Save markdown for a single platform."""
    # Map platform argument to platform key
    platform_map = {
        'tiktok': 'tiktok',
        'instagram': 'instagram_reels',
        'youtube': 'youtube_shorts',
        'twitter': 'x_twitter'
    }
    
    platform_key = platform_map.get(platform, platform)
    
    filepath = output_dir / f'{platform}_posts.md'
    
    with open(filepath, 'w') as f:
        f.write(f"# {platform.title()} Content\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        
        for i, item in enumerate(content, 1):
            platform_data = item['platforms'].get(platform_key)
            if not platform_data:
                continue
            
            f.write(f"## Post {i}: {item['news']['title']}\n\n")
            f.write(f"{platform_data.get('full_text', platform_data.get('caption', ''))}\n\n")
            f.write("---\n\n")
    
    console.print(f"[green]✓ Saved {platform}: {filepath}[/green]")


if __name__ == '__main__':
    sys.exit(main())
