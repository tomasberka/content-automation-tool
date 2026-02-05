"""
Content Classifier Module
Classifies news into content pillars: Education, Social Proof, Entertainment, Offers.
"""

from typing import Dict, Tuple
import re


class ContentClassifier:
    """Classifies gaming/PC news into content pillars."""
    
    # Define keywords for each pillar
    EDUCATION_KEYWORDS = [
        'guide', 'tutorial', 'how to', 'benchmark', 'review', 'comparison',
        'explainer', 'explained', 'what is', 'understanding', 'analysis',
        'performance', 'test', 'testing', 'settings', 'optimize', 'tips',
        'best practices', 'learn', 'specs', 'specifications', 'tech specs'
    ]
    
    SOCIAL_PROOF_KEYWORDS = [
        'users', 'community', 'reddit', 'forum', 'discussion', 'feedback',
        'review', 'rating', 'testimonial', 'experience', 'opinion', 'reaction',
        'viral', 'trending', 'popular', 'vote', 'poll', 'survey', 'award',
        'best of', 'top rated', 'recommended by', 'users love', 'fan favorite'
    ]
    
    ENTERTAINMENT_KEYWORDS = [
        'meme', 'funny', 'hilarious', 'fail', 'epic', 'insane', 'crazy',
        'wtf', 'lol', 'roast', 'reaction', 'drama', 'controversy', 'debate',
        'versus', 'vs', 'battle', 'challenge', 'stream', 'clip', 'moment',
        'highlights', 'gameplay', 'montage', 'compilation'
    ]
    
    OFFERS_KEYWORDS = [
        'deal', 'sale', 'discount', 'price drop', 'off', '% off', 'save',
        'cheap', 'budget', 'affordable', 'price', 'cost', 'value', 'deal',
        'promo', 'promotion', 'offer', 'limited time', 'clearance', 'bargain',
        'bundle', 'free', 'coupon', 'rebate', 'msrp', 'reduced'
    ]
    
    def classify(self, news_item: Dict) -> Tuple[str, float]:
        """
        Classify a news item into one of the four content pillars.
        
        Args:
            news_item: Dictionary with title, summary, and other fields
            
        Returns:
            Tuple of (pillar_name, confidence_score)
        """
        # Combine title and summary for analysis
        text = (news_item.get('title', '') + ' ' + news_item.get('summary', '')).lower()
        
        # Calculate scores for each pillar
        scores = {
            'education': self._calculate_score(text, self.EDUCATION_KEYWORDS),
            'social_proof': self._calculate_score(text, self.SOCIAL_PROOF_KEYWORDS),
            'entertainment': self._calculate_score(text, self.ENTERTAINMENT_KEYWORDS),
            'offers': self._calculate_score(text, self.OFFERS_KEYWORDS)
        }
        
        # Apply additional heuristics
        scores = self._apply_heuristics(text, scores)
        
        # Find the pillar with highest score
        best_pillar = max(scores.items(), key=lambda x: x[1])
        pillar_name = best_pillar[0]
        confidence = best_pillar[1]
        
        # Normalize confidence to 0-1 range
        if confidence > 0:
            confidence = min(confidence / 10.0, 1.0)
        else:
            # Default to education if no clear match
            pillar_name = 'education'
            confidence = 0.3
        
        return pillar_name, confidence
    
    def _calculate_score(self, text: str, keywords: list) -> float:
        """
        Calculate matching score for a set of keywords.
        
        Args:
            text: Text to analyze
            keywords: List of keywords to match
            
        Returns:
            Score based on keyword matches
        """
        score = 0.0
        
        for keyword in keywords:
            # Check for whole word matches (more accurate)
            pattern = r'\b' + re.escape(keyword) + r'\b'
            matches = len(re.findall(pattern, text))
            score += matches
        
        return score
    
    def _apply_heuristics(self, text: str, scores: Dict[str, float]) -> Dict[str, float]:
        """
        Apply additional heuristics to refine classification.
        
        Args:
            text: Text to analyze
            scores: Current scores dictionary
            
        Returns:
            Updated scores dictionary
        """
        # Boost offers if price indicators are present
        if re.search(r'\$\d+', text) or re.search(r'\d+%', text):
            scores['offers'] += 2.0
        
        # Boost entertainment for exclamatory content
        exclamations = text.count('!') + text.count('?')
        if exclamations > 2:
            scores['entertainment'] += 1.0
        
        # Boost social proof for community-related content
        if 'users' in text or 'community' in text or 'reddit' in text:
            scores['social_proof'] += 1.5
        
        # Boost education for technical/analytical content
        technical_indicators = ['benchmark', 'test', 'review', 'comparison', 'vs']
        for indicator in technical_indicators:
            if indicator in text:
                scores['education'] += 1.0
        
        return scores
    
    def classify_batch(self, news_items: list) -> list:
        """
        Classify multiple news items.
        
        Args:
            news_items: List of news item dictionaries
            
        Returns:
            List of news items with added 'pillar' and 'confidence' fields
        """
        classified = []
        
        for item in news_items:
            pillar, confidence = self.classify(item)
            classified_item = item.copy()
            classified_item['pillar'] = pillar
            classified_item['confidence'] = confidence
            classified.append(classified_item)
        
        return classified
