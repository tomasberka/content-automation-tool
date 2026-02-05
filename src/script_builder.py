"""
Script Builder Module
Generates full video scripts with timing markers.
"""

from typing import Dict, List
import yaml
from pathlib import Path


class ScriptBuilder:
    """Builds full video scripts from news items and hooks."""
    
    def __init__(self, templates_dir: str = "templates/scripts", 
                 brand_voice_config: str = "config/brand_voice.yaml"):
        """Initialize script builder with templates and brand voice."""
        self.templates_dir = Path(templates_dir)
        self.templates = self._load_templates()
        self.brand_voice = self._load_brand_voice(brand_voice_config)
    
    def _load_templates(self) -> Dict:
        """Load script templates from YAML files."""
        templates = {}
        pillars = ['education', 'social_proof', 'entertainment', 'offers']
        
        for pillar in pillars:
            template_file = self.templates_dir / f"{pillar}.yaml"
            try:
                with open(template_file, 'r') as f:
                    templates[pillar] = yaml.safe_load(f)
            except Exception as e:
                print(f"Error loading template {pillar}: {e}")
                templates[pillar] = {}
        
        return templates
    
    def _load_brand_voice(self, config_path: str) -> Dict:
        """Load brand voice configuration."""
        try:
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Error loading brand voice: {e}")
            return {'brand_name': 'HelloComp', 'signature_phrases': []}
    
    def build_script(self, news_item: Dict, hook: Dict, 
                     duration: int = 30) -> Dict:
        """
        Build a complete video script.
        
        Args:
            news_item: News item with title, summary, pillar, etc.
            hook: Hook dictionary with text and type
            duration: Target duration in seconds (15, 30, 60, or 480+ for long-form)
            
        Returns:
            Script dictionary with sections and timing
        """
        pillar = news_item.get('pillar', 'education')
        
        # Determine script length category
        if duration <= 20:
            length = 'short'
        elif duration <= 45:
            length = 'medium'
        else:
            length = 'long'
        
        # Get template for this pillar and length
        template = self._get_template(pillar, length)
        
        # Extract context from news item
        context = self._build_context(news_item)
        
        # Build script sections
        script = {
            'hook': self._build_hook_section(hook['text'], template),
            'context': self._build_context_section(context, template),
            'relevance': self._build_relevance_section(context, template),
            'cta': self._build_cta_section(template)
        }
        
        # Add timing markers
        script_with_timing = self._add_timing_markers(script, pillar, duration)
        
        # Add metadata
        script_with_timing['duration'] = duration
        script_with_timing['pillar'] = pillar
        script_with_timing['hook_type'] = hook.get('type', 'unknown')
        
        return script_with_timing
    
    def _get_template(self, pillar: str, length: str) -> Dict:
        """Get script template for pillar and length."""
        pillar_templates = self.templates.get(pillar, {})
        templates = pillar_templates.get('templates', {})
        
        # Get template for specified length, fallback to short
        template = templates.get(length, templates.get('short', {}))
        
        return template
    
    def _build_context(self, news_item: Dict) -> Dict:
        """Extract and structure context from news item."""
        title = news_item.get('title', '')
        summary = news_item.get('summary', '')
        source = news_item.get('source', '')
        
        return {
            'topic': title,
            'detail': self._extract_key_detail(summary),
            'technical_info': self._extract_technical_info(summary),
            'reason': self._extract_reason(news_item),
            'impact': self._extract_impact(news_item),
            'implications': self._extract_implications(news_item),
            'social_proof': self._extract_social_proof(summary),
            'user_feedback': self._extract_user_feedback(summary),
            'validation': self._extract_validation(news_item),
            'statistics': self._extract_statistics(summary),
            'entertaining_moment': self._extract_entertaining_moment(summary),
            'emotion': self._extract_emotion(news_item),
            'relatable_aspect': self._extract_relatable_aspect(news_item),
            'reaction': 'and the reactions are wild',
            'commentary': self._generate_commentary(news_item),
            'community_connection': 'this is why we love this community',
            'product': self._extract_product_name(title),
            'discount': self._extract_discount(summary),
            'amount': self._extract_savings_amount(summary),
            'comparison': self._generate_comparison(news_item),
            'specs': self._extract_specs(summary),
            'normal_price': self._extract_normal_price(summary),
            'value_proposition': self._generate_value_proposition(news_item)
        }
    
    def _extract_key_detail(self, text: str) -> str:
        """Extract key detail from summary."""
        sentences = text.split('.')
        if len(sentences) > 1:
            return sentences[0] + '.'
        return text[:100]
    
    def _extract_technical_info(self, text: str) -> str:
        """Extract technical information."""
        return "The specs are impressive."
    
    def _extract_reason(self, news_item: Dict) -> str:
        """Extract reason why this matters."""
        pillar = news_item.get('pillar', 'education')
        
        reasons = {
            'education': 'this impacts your build decisions',
            'social_proof': 'real users have tested this',
            'entertainment': 'this is peak gaming culture',
            'offers': 'you can save serious money'
        }
        
        return reasons.get(pillar, 'this affects your setup')
    
    def _extract_impact(self, news_item: Dict) -> str:
        """Extract impact statement."""
        return "Your performance could improve significantly."
    
    def _extract_implications(self, news_item: Dict) -> str:
        """Extract broader implications."""
        return "This could change how we approach PC building."
    
    def _extract_social_proof(self, text: str) -> str:
        """Extract social proof elements."""
        return "overwhelming positive feedback from the community"
    
    def _extract_user_feedback(self, text: str) -> str:
        """Extract user feedback."""
        return "Users are reporting excellent results."
    
    def _extract_validation(self, news_item: Dict) -> str:
        """Extract validation statement."""
        return "it works as promised"
    
    def _extract_statistics(self, text: str) -> str:
        """Extract statistics."""
        return "Thousands of users confirm this."
    
    def _extract_entertaining_moment(self, text: str) -> str:
        """Extract entertaining moment."""
        return "something unexpected happened"
    
    def _extract_emotion(self, news_item: Dict) -> str:
        """Extract emotional response."""
        return "gold"
    
    def _extract_relatable_aspect(self, news_item: Dict) -> str:
        """Extract relatable aspect."""
        return "We've all been there."
    
    def _generate_commentary(self, news_item: Dict) -> str:
        """Generate commentary."""
        return "Here's what I think about this."
    
    def _extract_product_name(self, text: str) -> str:
        """Extract product name."""
        import re
        gpu_match = re.search(r'(RTX|RX|GTX)\s*\d{4}', text, re.IGNORECASE)
        if gpu_match:
            return gpu_match.group(0)
        return "this hardware"
    
    def _extract_discount(self, text: str) -> str:
        """Extract discount percentage."""
        import re
        discount_match = re.search(r'(\d+)%', text)
        if discount_match:
            return discount_match.group(1)
        return "25"
    
    def _extract_savings_amount(self, text: str) -> str:
        """Extract savings amount."""
        import re
        price_match = re.search(r'\$(\d+)', text)
        if price_match:
            return price_match.group(1)
        return "150"
    
    def _generate_comparison(self, news_item: Dict) -> str:
        """Generate price comparison."""
        return "That's better than last month's prices."
    
    def _extract_specs(self, text: str) -> str:
        """Extract product specs."""
        return "It features impressive specifications."
    
    def _extract_normal_price(self, text: str) -> str:
        """Extract normal price."""
        return "Usually $500."
    
    def _generate_value_proposition(self, news_item: Dict) -> str:
        """Generate value proposition."""
        return "This is genuinely solid value for the performance you get."
    
    def _build_hook_section(self, hook_text: str, template: Dict) -> str:
        """Build the hook section of the script."""
        return hook_text
    
    def _build_context_section(self, context: Dict, template: Dict) -> str:
        """Build the context section of the script."""
        context_template = template.get('context', 'Here\'s what happened: {topic}')
        return self._fill_template(context_template, context)
    
    def _build_relevance_section(self, context: Dict, template: Dict) -> str:
        """Build the relevance section of the script."""
        relevance_template = template.get('relevance', 'This matters because {reason}')
        return self._fill_template(relevance_template, context)
    
    def _build_cta_section(self, template: Dict) -> str:
        """Build the call-to-action section."""
        cta_template = template.get('cta', 'Follow for more.')
        
        # Add brand signature phrase randomly
        import random
        signature_phrases = self.brand_voice.get('signature_phrases', [])
        if signature_phrases and random.random() > 0.5:
            cta_template += ' ' + random.choice(signature_phrases)
        
        return cta_template
    
    def _fill_template(self, template: str, context: Dict) -> str:
        """Fill template placeholders with context."""
        result = template
        
        for key, value in context.items():
            placeholder = '{' + key + '}'
            if placeholder in result:
                result = result.replace(placeholder, str(value))
        
        return result
    
    def _add_timing_markers(self, script: Dict, pillar: str, 
                            duration: int) -> Dict:
        """Add timing markers to script sections."""
        # Get timing structure for pillar
        pillar_template = self.templates.get(pillar, {})
        structure = pillar_template.get('structure', {})
        
        hook_duration = structure.get('hook_duration', 3)
        context_duration = structure.get('context_duration', 10)
        relevance_duration = structure.get('relevance_duration', 8)
        cta_duration = structure.get('cta_duration', 4)
        
        # Scale durations to fit target duration
        total_template_duration = hook_duration + context_duration + relevance_duration + cta_duration
        scale_factor = duration / total_template_duration
        
        result = {
            'sections': [
                {
                    'name': 'hook',
                    'text': script['hook'],
                    'start': 0,
                    'duration': int(hook_duration * scale_factor)
                },
                {
                    'name': 'context',
                    'text': script['context'],
                    'start': int(hook_duration * scale_factor),
                    'duration': int(context_duration * scale_factor)
                },
                {
                    'name': 'relevance',
                    'text': script['relevance'],
                    'start': int((hook_duration + context_duration) * scale_factor),
                    'duration': int(relevance_duration * scale_factor)
                },
                {
                    'name': 'cta',
                    'text': script['cta'],
                    'start': int((hook_duration + context_duration + relevance_duration) * scale_factor),
                    'duration': int(cta_duration * scale_factor)
                }
            ]
        }
        
        return result
