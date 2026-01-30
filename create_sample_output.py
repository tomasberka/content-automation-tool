#!/usr/bin/env python3
"""
Create sample output to demonstrate the tool's capabilities.
"""

import json
from datetime import datetime
from pathlib import Path
from src.content_classifier import ContentClassifier
from src.hook_generator import HookGenerator
from src.script_builder import ScriptBuilder
from src.platform_formatter import PlatformFormatter

# Comprehensive mock news items showcasing all pillars
mock_news = [
    {
        'title': 'Complete Guide: How to Optimize Your PC for Maximum FPS',
        'summary': 'Learn the best settings, tweaks, and configurations to boost your gaming performance. Includes step-by-step benchmarks and comparisons.',
        'source': "Tom's Hardware",
        'category': 'hardware',
        'date': datetime.now(),
        'url': 'https://example.com/optimize-fps-guide'
    },
    {
        'title': 'RTX 4070 Ti Super Just Dropped to $599 - Best Deal This Year',
        'summary': 'Major price drop alert! The RTX 4070 Ti Super is now available for $599, saving you $200 off MSRP. Stock is limited across major retailers.',
        'source': 'PC Gamer',
        'category': 'hardware',
        'date': datetime.now(),
        'url': 'https://example.com/rtx-4070-ti-deal'
    },
    {
        'title': 'Community Confirms: New BIOS Update Fixes Ryzen 9000 Issues',
        'summary': 'Thousands of users report that the latest BIOS update resolves the performance problems. Reddit and forums filled with positive feedback.',
        'source': 'The Verge Tech',
        'category': 'hardware',
        'date': datetime.now(),
        'url': 'https://example.com/ryzen-bios-fix'
    },
    {
        'title': 'Gamer Rage Quits After GPU Explodes During Stream',
        'summary': 'Viral moment as popular streamer watches in horror as their graphics card literally catches fire mid-game. Epic fail caught on camera.',
        'source': 'VideoCardz',
        'category': 'gaming',
        'date': datetime.now(),
        'url': 'https://example.com/gpu-explodes-stream'
    }
]

def main():
    print("Creating comprehensive sample output...\n")
    
    # Initialize components
    classifier = ContentClassifier()
    hook_generator = HookGenerator()
    script_builder = ScriptBuilder()
    platform_formatter = PlatformFormatter()
    
    all_content = []
    
    for news_item in mock_news:
        # Classify
        pillar, confidence = classifier.classify(news_item)
        news_item['pillar'] = pillar
        news_item['confidence'] = confidence
        
        # Generate hooks
        hooks = hook_generator.generate_hooks(news_item, num_variations=3)
        
        if hooks:
            # Build script
            script = script_builder.build_script(news_item, hooks[0], duration=30)
            
            # Format for all platforms
            platform_content = platform_formatter.format_all(script, news_item)
            
            # Compile content
            content_item = {
                'news': news_item,
                'hooks': hooks,
                'script': script,
                'platforms': platform_content,
                'generated_at': datetime.now().isoformat()
            }
            
            all_content.append(content_item)
    
    # Create sample output directory
    sample_dir = Path('output') / 'sample-2026-01-30'
    sample_dir.mkdir(parents=True, exist_ok=True)
    
    # Save JSON
    json_file = sample_dir / 'content.json'
    with open(json_file, 'w') as f:
        json.dump(all_content, f, indent=2, default=str)
    print(f"✓ Created: {json_file}")
    
    # Save hooks markdown
    hooks_file = sample_dir / 'hooks.md'
    with open(hooks_file, 'w') as f:
        f.write("# Video Hooks - Quick Reference\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write("This is a sample output demonstrating the Content Automation Tool's capabilities.\n\n")
        
        for i, item in enumerate(all_content, 1):
            f.write(f"## {i}. {item['news']['title']}\n\n")
            f.write(f"**Source:** {item['news']['source']}\n")
            f.write(f"**Pillar:** {item['news']['pillar']} (confidence: {item['news']['confidence']:.2f})\n\n")
            f.write("**Hooks:**\n\n")
            for hook in item['hooks']:
                f.write(f"- **[{hook['type'].upper()}]** {hook['text']}\n")
            f.write("\n---\n\n")
    print(f"✓ Created: {hooks_file}")
    
    # Save platform-specific content
    platforms = [
        ('tiktok', 'TikTok'),
        ('instagram_reels', 'Instagram Reels'),
        ('youtube_shorts', 'YouTube Shorts'),
        ('youtube_longform', 'YouTube Long-form'),
        ('x_twitter', 'X/Twitter')
    ]
    
    for platform_key, platform_name in platforms:
        platform_dir = sample_dir / platform_key.split('_')[0]
        platform_dir.mkdir(exist_ok=True)
        
        filepath = platform_dir / 'posts.md'
        
        with open(filepath, 'w') as f:
            f.write(f"# {platform_name} Content\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(f"Sample output from Content Automation Tool\n\n")
            f.write("---\n\n")
            
            for i, item in enumerate(all_content, 1):
                platform_data = item['platforms'].get(platform_key)
                if not platform_data:
                    continue
                
                f.write(f"## Post {i}: {item['news']['title']}\n\n")
                f.write(f"**Pillar:** {item['news']['pillar']}\n\n")
                
                if platform_key == 'tiktok':
                    f.write(f"**Caption:**\n```\n{platform_data['caption']}\n```\n\n")
                    f.write(f"**Hashtags:** {' '.join(platform_data['hashtags'])}\n\n")
                    f.write(f"**Duration:** {platform_data['duration']}s\n\n")
                    f.write(f"**Audio Suggestion:** {platform_data['audio_suggestion']}\n\n")
                
                elif platform_key == 'instagram_reels':
                    f.write(f"**Caption:**\n```\n{platform_data['caption']}\n```\n\n")
                    f.write(f"**Hashtags:**\n```{platform_data['hashtag_block']}\n```\n\n")
                    f.write(f"**Duration:** {platform_data['duration']}s\n\n")
                    f.write(f"**Story Text:** {platform_data['story_text']}\n\n")
                
                elif platform_key == 'youtube_shorts':
                    f.write(f"**Title:** {platform_data['title']}\n\n")
                    f.write(f"**Description:**\n```\n{platform_data['description']}\n```\n\n")
                    f.write(f"**Tags:** {', '.join(platform_data['tags'][:10])}\n\n")
                    f.write(f"**Duration:** {platform_data['duration']}s\n\n")
                
                elif platform_key == 'youtube_longform':
                    f.write(f"**Title:** {platform_data['title']}\n\n")
                    f.write(f"**Description:**\n```\n{platform_data['description'][:500]}...\n```\n\n")
                    f.write("**Chapters:**\n")
                    for chapter in platform_data['chapters']:
                        f.write(f"- {chapter['time']} - {chapter['title']}\n")
                    f.write("\n")
                    f.write(f"**Tags:** {', '.join(platform_data['tags'][:10])}\n\n")
                
                elif platform_key == 'x_twitter':
                    f.write(f"**Single Tweet:**\n```\n{platform_data['single_tweet']}\n```\n\n")
                    f.write("**Thread:**\n")
                    for j, tweet in enumerate(platform_data['thread'][:3], 1):
                        f.write(f"{j}. ```{tweet}```\n")
                    if len(platform_data['thread']) > 3:
                        f.write(f"\n... and {len(platform_data['thread']) - 3} more tweets\n")
                    f.write("\n")
                
                f.write("---\n\n")
        
        print(f"✓ Created: {filepath}")
    
    print(f"\n✅ Sample output created in: {sample_dir}")
    print(f"\nThis demonstrates all features:")
    print(f"  - 4 content pillars (Education, Offers, Social Proof, Entertainment)")
    print(f"  - Multiple hook types (Question, Shock, FOMO, Curiosity)")
    print(f"  - Full scripts with timing")
    print(f"  - All platform formats")

if __name__ == '__main__':
    main()
