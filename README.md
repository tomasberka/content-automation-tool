# Content Automation Tool 🎮

**HelloComp 2026 - Multi-Platform Content Strategy**

A production-ready content automation tool for gaming/PC creators. Automatically fetch gaming/PC news, classify content, generate video hooks, create full scripts, and format content for multiple platforms.

## ✨ Features

- **🔍 News Aggregation**: Fetch from 6+ gaming/PC RSS sources
- **🎯 Smart Classification**: AI-powered content pillar classification
- **💡 Hook Generation**: Generate attention-grabbing video hooks
- **📝 Script Building**: Full video scripts with timing markers
- **📱 Multi-Platform**: Format for TikTok, Instagram, YouTube, Twitter
- **🤖 Automation**: GitHub Actions for daily content generation

## 📋 Content Pillars

1. **Education**: Tutorials, guides, benchmarks, explainers
2. **Social Proof**: User stories, reviews, testimonials
3. **Entertainment**: Memes, fails, wins, challenges
4. **Offers**: Deals, price drops, sales, bundles

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/tomasberka/content-automation-tool.git
cd content-automation-tool

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
# Generate content for today
python generate.py --date today

# Generate content for a specific topic
python generate.py --topic "RTX 5070" --days 7

# Generate content for a specific pillar
python generate.py --pillar education

# Generate content for a specific platform
python generate.py --platform tiktok --days 3

# Get verbose output
python generate.py --date today --verbose
```

## 📖 Usage Examples

### Generate Today's Content

```bash
python generate.py --date today --output output/
```

### Filter by Topic

```bash
python generate.py --topic "AMD Ryzen" --days 7
```

### Platform-Specific Generation

```bash
python generate.py --platform tiktok --days 3 --max-items 5
```

### Custom Date Range

```bash
python generate.py --days 14 --pillar offers --format json
```

## 📂 Output Structure

```
output/
├── 2026-01-30/
│   ├── content.json          # All generated content
│   ├── hooks.md              # Quick reference hooks list
│   ├── tiktok/
│   │   └── posts.md          # TikTok-ready content
│   ├── instagram/
│   │   └── posts.md          # Instagram Reels content
│   ├── youtube/
│   │   └── posts.md          # YouTube Shorts content
│   └── twitter/
│       └── posts.md          # Twitter/X content
```

## ⚙️ Configuration

### RSS Sources (`config/sources.yaml`)

Configure news sources:

```yaml
rss_feeds:
  - name: "Tom's Hardware"
    url: "https://www.tomshardware.com/feeds/all"
    category: "hardware"
  # Add more sources...

refresh_interval: 3600
max_articles_per_source: 10
```

### Brand Voice (`config/brand_voice.yaml`)

Customize your brand voice:

```yaml
brand_name: "HelloComp"
tone:
  - professional
  - factual
  - enthusiast-friendly
signature_phrases:
  - "Build smarter."
  - "Game harder."
```

### Platforms (`config/platforms.yaml`)

Platform-specific settings:

```yaml
tiktok:
  max_caption_length: 2200
  optimal_duration: [15, 30, 60]
  hashtag_count: 5
```

## 🎯 Hook Formulas

The tool uses proven hook formulas:

- **Shock/Contrast**: "My $600 PC beat a $2,000 rig."
- **Question**: "Is your GPU already outdated?"
- **Challenge**: "I bet you can't guess the FPS."
- **FOMO**: "This deal ends in 24 hours."
- **Curiosity**: "NVIDIA doesn't want you to see this."

## 📝 Script Structure

All scripts follow this proven structure:

1. **Hook** (3 seconds): Attention grabber
2. **Context** (10 seconds): What's happening
3. **Relevance** (8 seconds): Why it matters
4. **CTA** (4 seconds): Call to action

## 🤖 Automation

### GitHub Actions

The tool includes a GitHub Action that runs daily at 8 AM UTC:

```yaml
# .github/workflows/daily_content.yaml
on:
  schedule:
    - cron: '0 8 * * *'
  workflow_dispatch:
```

To enable:
1. Push the repository to GitHub
2. The action will run automatically
3. Generated content is committed daily

### Manual Trigger

Run the workflow manually from GitHub Actions tab.

## 🔧 Development

### Project Structure

```
content-automation-tool/
├── src/
│   ├── news_fetcher.py          # RSS feed fetching
│   ├── content_classifier.py    # Content classification
│   ├── hook_generator.py        # Hook generation
│   ├── script_builder.py        # Script building
│   └── platform_formatter.py    # Platform formatting
├── config/                      # Configuration files
├── templates/                   # Hook and script templates
├── generate.py                  # Main CLI
└── requirements.txt             # Python dependencies
```

### Adding Custom Templates

1. Create new template in `templates/hooks/` or `templates/scripts/`
2. Follow the YAML format with `patterns` key
3. Reference in the generator code

### Adding New RSS Sources

Edit `config/sources.yaml`:

```yaml
rss_feeds:
  - name: "Your Source"
    url: "https://example.com/feed"
    category: "gaming"
```

## 📊 Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `--date` | Date filter (today, yesterday, week) | `--date today` |
| `--days` | Days to look back | `--days 7` |
| `--topic` | Filter by topic | `--topic "RTX 5070"` |
| `--pillar` | Filter by content pillar | `--pillar education` |
| `--platform` | Target platform | `--platform tiktok` |
| `--output` | Output directory | `--output output/` |
| `--format` | Output format (json, markdown, both) | `--format both` |
| `--verbose` | Verbose output | `--verbose` |
| `--max-items` | Max content items | `--max-items 10` |

## 🎨 Customization

### Hook Templates

Edit templates in `templates/hooks/`:

- `shock.yaml`: Shocking/contrasting hooks
- `question.yaml`: Question-based hooks
- `challenge.yaml`: Challenge hooks
- `fomo.yaml`: FOMO (urgency) hooks
- `curiosity.yaml`: Curiosity-driven hooks

### Script Templates

Edit templates in `templates/scripts/`:

- `education.yaml`: Educational content scripts
- `social_proof.yaml`: Social proof scripts
- `entertainment.yaml`: Entertainment scripts
- `offers.yaml`: Deal/offer scripts

Each template supports `short`, `medium`, and `long` variants.

## 🛠️ Troubleshooting

### No news items found

- Check your internet connection
- Verify RSS feed URLs in `config/sources.yaml`
- Try increasing `--days` parameter

### Content not generating

- Run with `--verbose` flag for detailed output
- Check that all dependencies are installed
- Verify template files exist

### GitHub Action not running

- Ensure the workflow file is in `.github/workflows/`
- Check repository permissions
- Manually trigger from Actions tab

## 📝 Brand Voice

The tool maintains HelloComp's professional, factual brand voice:

- ✅ Professional and trustworthy
- ✅ Factual and accurate
- ✅ Enthusiast-friendly
- ❌ No clickbait exaggeration
- ❌ No false claims
- ❌ No offensive language

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 🔗 Resources

- [RSS Feed Format](https://www.rssboard.org/rss-specification)
- [TikTok Best Practices](https://www.tiktok.com/creators/)
- [YouTube Creator Academy](https://creatoracademy.youtube.com/)

## 💬 Support

For issues and questions:
- Open a GitHub issue
- Check existing documentation
- Review example outputs

---

**Built with ❤️ for the PC gaming community**

*Build smarter. Game harder. Your setup, elevated.*
