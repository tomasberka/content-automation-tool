"""
Hook Generator Module
Generates video hooks using proven formulas.
"""

from typing import List, Dict
import yaml
import random
import re
from pathlib import Path


class HookGenerator:
    """Generates attention-grabbing video hooks for content."""
    
    HOOK_TYPES = ['shock', 'question', 'challenge', 'fomo', 'curiosity']
    
    def __init__(self, templates_dir: str = "templates/hooks"):
        """Initialize hook generator with templates."""
        self.templates_dir = Path(templates_dir)
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict[str, List[str]]:
        """Load hook templates from YAML files."""
        templates = {}
        
        for hook_type in self.HOOK_TYPES:
            template_file = self.templates_dir / f"{hook_type}.yaml"
            try:
                with open(template_file, 'r') as f:
                    data = yaml.safe_load(f)
                    templates[hook_type] = data.get('patterns', [])
            except Exception as e:
                print(f"Error loading template {hook_type}: {e}")
                templates[hook_type] = []
        
        return templates
    
    def generate_hooks(self, news_item: Dict, num_variations: int = 3) -> List[Dict]:
        """
        Generate multiple hook variations for a news item.
        
        Args:
            news_item: News item dictionary with title, summary, etc.
            num_variations: Number of hook variations to generate
            
        Returns:
            List of hook dictionaries with text and type
        """
        hooks = []
        
        # Extract key information from news item
        context = self._extract_context(news_item)
        
        # Determine which hook types are most appropriate
        suitable_types = self._select_hook_types(news_item)
        
        # Generate hooks from each suitable type
        for hook_type in suitable_types[:num_variations]:
            hook = self._generate_hook(hook_type, context, news_item)
            if hook:
                hooks.append({
                    'text': hook,
                    'type': hook_type,
                    'source': news_item.get('title', '')
                })
        
        return hooks
    
    def _extract_context(self, news_item: Dict) -> Dict:
        """
        Extract relevant context from news item for hook generation.
        
        Args:
            news_item: News item dictionary
            
        Returns:
            Context dictionary with extracted information
        """
        title = news_item.get('title', '')
        summary = news_item.get('summary', '')
        text = title + ' ' + summary
        
        context = {
            'topic': title,
            'brand': self._extract_brand(text),
            'product': self._extract_product(text),
            'component': self._extract_component(text),
            'game': self._extract_game(text),
            'low_price': self._extract_price(text, prefer='low'),
            'high_price': self._extract_price(text, prefer='high'),
            'discount': self._extract_discount(text)
        }
        
        return context
    
    def _extract_brand(self, text: str) -> str:
        """Extract brand name from text."""
        brands = ['nvidia', 'amd', 'intel', 'asus', 'msi', 'gigabyte', 
                  'corsair', 'razer', 'logitech', 'evga', 'zotac']
        text_lower = text.lower()
        
        for brand in brands:
            if brand in text_lower:
                return brand.upper()
        
        return 'This brand'
    
    def _extract_product(self, text: str) -> str:
        """Extract product name from text."""
        # Look for GPU model numbers
        gpu_match = re.search(r'(RTX|RX|GTX)\s*\d{4}', text, re.IGNORECASE)
        if gpu_match:
            return gpu_match.group(0)
        
        # Look for CPU model numbers
        cpu_match = re.search(r'(Core\s*i[3579]|Ryzen\s*[3579])\s*\d{4}', text, re.IGNORECASE)
        if cpu_match:
            return cpu_match.group(0)
        
        return 'this product'
    
    def _extract_component(self, text: str) -> str:
        """Extract component type from text."""
        components = {
            'gpu': ['gpu', 'graphics card', 'video card'],
            'cpu': ['cpu', 'processor'],
            'ram': ['ram', 'memory'],
            'motherboard': ['motherboard', 'mobo'],
            'ssd': ['ssd', 'storage'],
            'monitor': ['monitor', 'display'],
            'case': ['case', 'chassis']
        }
        
        text_lower = text.lower()
        
        for component, keywords in components.items():
            for keyword in keywords:
                if keyword in text_lower:
                    return component.upper()
        
        return 'GPU'
    
    def _extract_game(self, text: str) -> str:
        """Extract game name from text."""
        # Common games
        games = ['fortnite', 'valorant', 'warzone', 'cyberpunk', 'elden ring',
                 'starfield', 'baldur', 'counter-strike', 'cs2', 'cs:go']
        
        text_lower = text.lower()
        
        for game in games:
            if game in text_lower:
                return game.title()
        
        return 'the latest games'
    
    def _extract_price(self, text: str, prefer: str = 'any') -> str:
        """Extract price from text."""
        prices = re.findall(r'\$(\d+(?:,\d{3})*(?:\.\d{2})?)', text)
        
        if prices:
            # Convert to integers for comparison
            price_values = [int(p.replace(',', '')) for p in prices]
            
            if prefer == 'low':
                return str(min(price_values))
            elif prefer == 'high':
                return str(max(price_values))
            else:
                return prices[0]
        
        return '600' if prefer == 'low' else '2000'
    
    def _extract_discount(self, text: str) -> str:
        """Extract discount percentage from text."""
        discount_match = re.search(r'(\d+)%\s*off', text, re.IGNORECASE)
        if discount_match:
            return discount_match.group(1)
        
        return '20'
    
    def _select_hook_types(self, news_item: Dict) -> List[str]:
        """
        Select appropriate hook types based on news content and pillar.
        
        Args:
            news_item: News item with pillar classification
            
        Returns:
            List of hook types, ordered by suitability
        """
        pillar = news_item.get('pillar', 'education')
        
        # Map pillars to preferred hook types
        pillar_hooks = {
            'education': ['question', 'curiosity', 'shock'],
            'social_proof': ['curiosity', 'question', 'shock'],
            'entertainment': ['shock', 'challenge', 'curiosity'],
            'offers': ['fomo', 'shock', 'question']
        }
        
        preferred = pillar_hooks.get(pillar, self.HOOK_TYPES)
        
        # Shuffle remaining types
        remaining = [t for t in self.HOOK_TYPES if t not in preferred]
        random.shuffle(remaining)
        
        return preferred + remaining
    
    def _generate_hook(self, hook_type: str, context: Dict, news_item: Dict) -> str:
        """
        Generate a hook from a template and context.
        
        Args:
            hook_type: Type of hook to generate
            context: Context dictionary with extracted info
            news_item: Original news item
            
        Returns:
            Generated hook text
        """
        templates = self.templates.get(hook_type, [])
        if not templates:
            return f"Breaking: {news_item.get('title', 'News update')}"
        
        # Select a random template
        template = random.choice(templates)
        
        # Replace placeholders with context
        hook = template
        for key, value in context.items():
            placeholder = '{' + key + '}'
            if placeholder in hook:
                hook = hook.replace(placeholder, str(value))
        
        return hook
