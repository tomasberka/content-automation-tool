"""
Content Utilities for HelloComp Category Template Generator
=============================================================

Podpůrné funkce pro zpracování SEO obsahu.
"""

import re
from typing import List, Dict, Tuple
from bs4 import BeautifulSoup


def clean_html(html_content: str) -> str:
    """
    Vyčistí HTML od nepotřebných tagů a zachová pouze obsah
    
    Args:
        html_content: HTML string
        
    Returns:
        Vyčištěný text
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text(separator=' ', strip=True)


def extract_links(content: str) -> List[Dict[str, str]]:
    """
    Extrahuje všechny odkazy z obsahu
    
    Args:
        content: Markdown nebo HTML obsah
        
    Returns:
        Seznam slovníků s odkazy (text, url)
    """
    links = []
    
    # Markdown links [text](url)
    md_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    for match in re.finditer(md_pattern, content):
        links.append({
            'text': match.group(1),
            'url': match.group(2)
        })
    
    # HTML links
    if '<a' in content:
        soup = BeautifulSoup(content, 'html.parser')
        for a_tag in soup.find_all('a'):
            href = a_tag.get('href', '')
            text = a_tag.get_text(strip=True)
            if href:
                links.append({
                    'text': text,
                    'url': href
                })
    
    return links


def count_words(text: str) -> int:
    """
    Spočítá počet slov v textu
    
    Args:
        text: Text k analýze
        
    Returns:
        Počet slov
    """
    # Odstranění HTML tagů
    clean_text = re.sub(r'<[^>]+>', '', text)
    # Odstranění Markdown odkazů
    clean_text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', clean_text)
    # Spočítání slov
    words = clean_text.split()
    return len([w for w in words if w.strip()])


def extract_keywords(text: str, top_n: int = 10) -> List[Tuple[str, int]]:
    """
    Extrahuje nejčastější klíčová slova z textu
    
    Args:
        text: Text k analýze
        top_n: Počet top slov k vrácení
        
    Returns:
        Seznam tuple (slovo, četnost)
    """
    # Vyčistit text
    clean_text = re.sub(r'<[^>]+>', '', text.lower())
    clean_text = re.sub(r'[^\w\s]', ' ', clean_text)
    
    # Stopwords (česká)
    stopwords = {
        'a', 'i', 'o', 'u', 'v', 'z', 's', 'k', 'na', 'po', 'do', 'od', 'ze', 'se',
        'je', 'jsou', 'jsem', 'jsi', 'jsme', 'jste', 'byl', 'byla', 'bylo', 'byli',
        'by', 'aby', 'kdyby', 'pro', 'jako', 'ale', 'nebo', 'že', 'aby', 'když',
        'tak', 'už', 'jen', 'už', 'co', 'to', 'ta', 'ten', 'ti', 'ty', 'které', 'který'
    }
    
    words = clean_text.split()
    word_freq = {}
    
    for word in words:
        if len(word) > 2 and word not in stopwords:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Seřadit podle četnosti
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:top_n]


def format_table(data: List[List[str]], headers: List[str]) -> str:
    """
    Formátuje data do Markdown tabulky
    
    Args:
        data: Řádky dat
        headers: Hlavičky tabulky
        
    Returns:
        Markdown tabulka
    """
    # Zjistit maximální šířky sloupců
    col_widths = [len(h) for h in headers]
    for row in data:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Sestavit tabulku
    lines = []
    
    # Hlavička
    header_line = '| ' + ' | '.join(h.ljust(col_widths[i]) for i, h in enumerate(headers)) + ' |'
    lines.append(header_line)
    
    # Oddělovač
    separator = '|' + '|'.join('-' * (w + 2) for w in col_widths) + '|'
    lines.append(separator)
    
    # Data
    for row in data:
        row_line = '| ' + ' | '.join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)) + ' |'
        lines.append(row_line)
    
    return '\n'.join(lines)


def split_into_sections(text: str, max_words_per_section: int = 200) -> List[str]:
    """
    Rozdělí dlouhý text na menší sekce
    
    Args:
        text: Text k rozdělení
        max_words_per_section: Maximální počet slov na sekci
        
    Returns:
        Seznam sekcí
    """
    paragraphs = text.split('\n\n')
    sections = []
    current_section = []
    current_word_count = 0
    
    for para in paragraphs:
        para_words = len(para.split())
        
        if current_word_count + para_words > max_words_per_section and current_section:
            sections.append('\n\n'.join(current_section))
            current_section = [para]
            current_word_count = para_words
        else:
            current_section.append(para)
            current_word_count += para_words
    
    if current_section:
        sections.append('\n\n'.join(current_section))
    
    return sections


def generate_toc(content: str) -> str:
    """
    Generuje obsah (Table of Contents) z H2 nadpisů
    
    Args:
        content: Markdown obsah
        
    Returns:
        Markdown seznam odkazů
    """
    h2_pattern = re.compile(r'^##\s+(.+?)$', re.MULTILINE)
    headings = h2_pattern.findall(content)
    
    toc_lines = ['## Obsah', '']
    for i, heading in enumerate(headings, 1):
        # Vytvoření anchor linku
        anchor = heading.lower().replace(' ', '-')
        anchor = re.sub(r'[^\w\-]', '', anchor)
        toc_lines.append(f'{i}. [{heading}](#{anchor})')
    
    return '\n'.join(toc_lines)


def validate_internal_links(content: str, valid_paths: List[str]) -> List[Dict[str, str]]:
    """
    Validuje interní odkazy v obsahu
    
    Args:
        content: Obsah s odkazy
        valid_paths: Seznam platných interních cest
        
    Returns:
        Seznam problémových odkazů
    """
    links = extract_links(content)
    invalid_links = []
    
    for link in links:
        url = link['url']
        # Interní odkazy začínají / nebo obsahují hellocomp.cz
        if url.startswith('/') or 'hellocomp.cz' in url:
            # Extrakce cesty
            path = url.split('hellocomp.cz')[-1] if 'hellocomp.cz' in url else url
            path = path.split('#')[0].split('?')[0]  # Odstranění anchoru a query
            
            if path not in valid_paths:
                invalid_links.append({
                    'text': link['text'],
                    'url': url,
                    'path': path
                })
    
    return invalid_links


def add_emoji_markers(content: str) -> str:
    """
    Přidá emoji markery k důležitým částem
    
    Args:
        content: Obsah bez emoji
        
    Returns:
        Obsah s emoji markery
    """
    # Přidat ⚡ k výkonnostním metrikám
    content = re.sub(r'\b(\d+\s*FPS)\b', r'⚡ \1', content)
    content = re.sub(r'\b(\d+\s*GB)\b', r'💾 \1', content)
    content = re.sub(r'\b(\d+K)\b', r'🎮 \1', content)
    
    # Přidat ✅ k výhodám
    content = re.sub(r'^-\s+([^-])', r'- ✅ \1', content, flags=re.MULTILINE)
    
    return content


def optimize_for_seo(text: str, primary_keyword: str, secondary_keywords: List[str] = None) -> str:
    """
    Optimalizuje text pro SEO přidáním klíčových slov
    
    Args:
        text: Původní text
        primary_keyword: Primární klíčové slovo
        secondary_keywords: Seznam sekundárních klíčových slov
        
    Returns:
        SEO-optimalizovaný text
    """
    if secondary_keywords is None:
        secondary_keywords = []
    
    # Ensure primary keyword appears in first paragraph
    paragraphs = text.split('\n\n')
    if paragraphs and primary_keyword.lower() not in paragraphs[0].lower():
        # Try to naturally include it
        first_para = paragraphs[0]
        # Simple insertion at the end of first sentence
        sentences = first_para.split('.')
        if sentences:
            sentences[0] = sentences[0] + f' s {primary_keyword}'
            paragraphs[0] = '.'.join(sentences)
    
    return '\n\n'.join(paragraphs)
