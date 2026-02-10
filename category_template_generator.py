#!/usr/bin/env python3
"""
HelloComp Category Template Generator
======================================

Automaticky generuje SEO-optimalizovaný obsah z kategoriálních textů HelloComp.
Podporuje validaci struktury, formátování do HTML/Markdown a generování vzorových textů.

Použití:
    python category_template_generator.py input.md --output output.html --format html
    python category_template_generator.py input.md --validate
    python category_template_generator.py --generate-sample "Herní počítače"
"""

import re
import yaml
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum


class OutputFormat(Enum):
    """Podporované výstupní formáty"""
    HTML = "html"
    MARKDOWN = "markdown"


class ValidationLevel(Enum):
    """Úrovně validace"""
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class ValidationResult:
    """Výsledek validace jedné sekce"""
    section: str
    level: ValidationLevel
    message: str
    actual_value: Optional[str] = None
    expected_value: Optional[str] = None


@dataclass
class ContentSection:
    """Reprezentace sekce obsahu"""
    type: str
    content: str
    heading: Optional[str] = None
    subsections: List['ContentSection'] = field(default_factory=list)


@dataclass
class CategoryContent:
    """Kompletní struktura kategoriálního obsahu"""
    title: Optional[str] = None
    meta_description: Optional[str] = None
    h1: Optional[str] = None
    introduction: Optional[str] = None
    h2_sections: List[ContentSection] = field(default_factory=list)
    raw_content: str = ""
    
    def to_dict(self) -> Dict:
        """Převod na slovník"""
        return {
            'title': self.title,
            'meta_description': self.meta_description,
            'h1': self.h1,
            'introduction': self.introduction,
            'h2_sections': [
                {
                    'heading': s.heading,
                    'content': s.content
                } for s in self.h2_sections
            ]
        }


class ContentParser:
    """Parser pro kategoriální texty HelloComp"""
    
    @staticmethod
    def parse_markdown(content: str) -> CategoryContent:
        """
        Parsuje Markdown obsah do strukturované podoby
        
        Args:
            content: Markdown text kategorie
            
        Returns:
            CategoryContent objekt se strukturovaným obsahem
        """
        parsed = CategoryContent(raw_content=content)
        
        # Parsování Title
        title_match = re.search(r'\*\*Title:\*\*\s*(.+?)(?:\n|$)', content)
        if title_match:
            parsed.title = title_match.group(1).strip()
        
        # Parsování Meta Description
        meta_match = re.search(r'\*\*Meta description:\*\*\s*(.+?)(?:\n|$)', content)
        if meta_match:
            parsed.meta_description = meta_match.group(1).strip()
        
        # Parsování H1 (## nadpis)
        h1_match = re.search(r'^##\s+(.+?)$', content, re.MULTILINE)
        if h1_match:
            parsed.h1 = h1_match.group(1).strip()
            
            # Úvodní text je první odstavec po H1
            h1_pos = h1_match.end()
            next_h2_match = re.search(r'^##\s+', content[h1_pos:], re.MULTILINE)
            if next_h2_match:
                intro_text = content[h1_pos:h1_pos + next_h2_match.start()].strip()
            else:
                intro_text = content[h1_pos:].strip()
            
            # Odstranit prázdné řádky a vzít první odstavec
            intro_paragraphs = [p.strip() for p in intro_text.split('\n\n') if p.strip()]
            if intro_paragraphs:
                parsed.introduction = intro_paragraphs[0]
        
        # Parsování H2 sekcí
        h2_pattern = re.compile(r'^##\s+(.+?)$', re.MULTILINE)
        h2_matches = list(h2_pattern.finditer(content))
        
        for i, match in enumerate(h2_matches[1:], 1):  # Skip first H1
            heading = match.group(1).strip()
            start = match.end()
            end = h2_matches[i + 1].start() if i < len(h2_matches) - 1 else len(content)
            section_content = content[start:end].strip()
            
            parsed.h2_sections.append(ContentSection(
                type='h2',
                heading=heading,
                content=section_content
            ))
        
        return parsed
    
    @staticmethod
    def extract_html_content(content: str) -> CategoryContent:
        """
        Extrahuje obsah z HTML
        
        Args:
            content: HTML text kategorie
            
        Returns:
            CategoryContent objekt
        """
        parsed = CategoryContent(raw_content=content)
        
        # Základní HTML parsing
        title_match = re.search(r'<title>(.+?)</title>', content, re.IGNORECASE)
        if title_match:
            parsed.title = title_match.group(1).strip()
        
        meta_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.+?)["\']', 
                              content, re.IGNORECASE)
        if meta_match:
            parsed.meta_description = meta_match.group(1).strip()
        
        h1_match = re.search(r'<h1[^>]*>(.+?)</h1>', content, re.IGNORECASE | re.DOTALL)
        if h1_match:
            parsed.h1 = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
        
        # H2 sekce
        h2_pattern = re.compile(r'<h2[^>]*>(.+?)</h2>', re.IGNORECASE | re.DOTALL)
        for match in h2_pattern.finditer(content):
            heading = re.sub(r'<[^>]+>', '', match.group(1)).strip()
            parsed.h2_sections.append(ContentSection(
                type='h2',
                heading=heading,
                content=""
            ))
        
        return parsed


class ContentValidator:
    """Validátor SEO struktury obsahu"""
    
    def __init__(self, config_path: str = "content_structure.yaml"):
        """
        Inicializace validátoru
        
        Args:
            config_path: Cesta ke konfiguračnímu souboru
        """
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
    
    def validate(self, content: CategoryContent) -> List[ValidationResult]:
        """
        Validuje obsah podle pravidel
        
        Args:
            content: Obsah k validaci
            
        Returns:
            Seznam ValidationResult objektů
        """
        results = []
        
        # Validace povinných sekcí
        required = self.config['required_sections']
        if 'title' in required and not content.title:
            results.append(ValidationResult(
                section='title',
                level=ValidationLevel.ERROR,
                message='Title je povinný a chybí'
            ))
        
        if 'meta_description' in required and not content.meta_description:
            results.append(ValidationResult(
                section='meta_description',
                level=ValidationLevel.ERROR,
                message='Meta description je povinná a chybí'
            ))
        
        if 'h1' in required and not content.h1:
            results.append(ValidationResult(
                section='h1',
                level=ValidationLevel.ERROR,
                message='H1 nadpis je povinný a chybí'
            ))
        
        if 'introduction' in required and not content.introduction:
            results.append(ValidationResult(
                section='introduction',
                level=ValidationLevel.ERROR,
                message='Úvodní text je povinný a chybí'
            ))
        
        # Validace délek
        sections_spec = self.config['sections']
        
        if content.title:
            title_len = len(content.title)
            title_spec = sections_spec['title']
            if title_len > title_spec['max_length']:
                results.append(ValidationResult(
                    section='title',
                    level=ValidationLevel.WARNING,
                    message=f'Title je příliš dlouhý ({title_len} znaků, max {title_spec["max_length"]})',
                    actual_value=str(title_len),
                    expected_value=f"max {title_spec['max_length']}"
                ))
            elif title_len < title_spec['min_length']:
                results.append(ValidationResult(
                    section='title',
                    level=ValidationLevel.WARNING,
                    message=f'Title je příliš krátký ({title_len} znaků, min {title_spec["min_length"]})',
                    actual_value=str(title_len),
                    expected_value=f"min {title_spec['min_length']}"
                ))
        
        if content.meta_description:
            meta_len = len(content.meta_description)
            meta_spec = sections_spec['meta_description']
            if meta_len > meta_spec['max_length']:
                results.append(ValidationResult(
                    section='meta_description',
                    level=ValidationLevel.WARNING,
                    message=f'Meta description je příliš dlouhá ({meta_len} znaků, max {meta_spec["max_length"]})',
                    actual_value=str(meta_len),
                    expected_value=f"max {meta_spec['max_length']}"
                ))
            elif meta_len < meta_spec['min_length']:
                results.append(ValidationResult(
                    section='meta_description',
                    level=ValidationLevel.WARNING,
                    message=f'Meta description je příliš krátká ({meta_len} znaků, min {meta_spec["min_length"]})',
                    actual_value=str(meta_len),
                    expected_value=f"min {meta_spec['min_length']}"
                ))
        
        # Validace úvodního textu
        if content.introduction:
            word_count = len(content.introduction.split())
            intro_spec = sections_spec['introduction']
            if word_count < intro_spec['word_count_min']:
                results.append(ValidationResult(
                    section='introduction',
                    level=ValidationLevel.WARNING,
                    message=f'Úvodní text je příliš krátký ({word_count} slov, min {intro_spec["word_count_min"]})',
                    actual_value=str(word_count),
                    expected_value=f"min {intro_spec['word_count_min']}"
                ))
            elif word_count > intro_spec['word_count_max']:
                results.append(ValidationResult(
                    section='introduction',
                    level=ValidationLevel.WARNING,
                    message=f'Úvodní text je příliš dlouhý ({word_count} slov, max {intro_spec["word_count_max"]})',
                    actual_value=str(word_count),
                    expected_value=f"max {intro_spec['word_count_max']}"
                ))
        
        # Validace H2 sekcí
        h2_spec = sections_spec['h2_sections']
        h2_count = len(content.h2_sections)
        if h2_count < h2_spec['min_count']:
            results.append(ValidationResult(
                section='h2_sections',
                level=ValidationLevel.WARNING,
                message=f'Málo H2 sekcí ({h2_count}, minimum {h2_spec["min_count"]})',
                actual_value=str(h2_count),
                expected_value=f"min {h2_spec['min_count']}"
            ))
        
        # Celkový počet slov
        total_words = self._count_total_words(content)
        word_guidelines = self.config['content_guidelines']['total_word_count']
        if total_words < word_guidelines['min']:
            results.append(ValidationResult(
                section='total_content',
                level=ValidationLevel.WARNING,
                message=f'Celkový obsah je příliš krátký ({total_words} slov, min {word_guidelines["min"]})',
                actual_value=str(total_words),
                expected_value=f"min {word_guidelines['min']}"
            ))
        elif total_words > word_guidelines['max']:
            results.append(ValidationResult(
                section='total_content',
                level=ValidationLevel.WARNING,
                message=f'Celkový obsah je příliš dlouhý ({total_words} slov, max {word_guidelines["max"]})',
                actual_value=str(total_words),
                expected_value=f"max {word_guidelines['max']}"
            ))
        
        # Pokud vše OK
        if not results:
            results.append(ValidationResult(
                section='all',
                level=ValidationLevel.INFO,
                message='✅ Veškerý obsah splňuje SEO požadavky'
            ))
        
        return results
    
    def _count_total_words(self, content: CategoryContent) -> int:
        """Spočítá celkový počet slov v obsahu"""
        total = 0
        if content.introduction:
            total += len(content.introduction.split())
        for section in content.h2_sections:
            total += len(section.content.split())
        return total


class ContentFormatter:
    """Formátování obsahu do různých výstupních formátů"""
    
    @staticmethod
    def to_html(content: CategoryContent) -> str:
        """
        Převede obsah do HTML formátu
        
        Args:
            content: Strukturovaný obsah
            
        Returns:
            HTML string
        """
        html_parts = ['<!DOCTYPE html>', '<html lang="cs">', '<head>']
        html_parts.append('    <meta charset="UTF-8">')
        html_parts.append('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
        
        if content.title:
            html_parts.append(f'    <title>{ContentFormatter._escape_html(content.title)}</title>')
        
        if content.meta_description:
            html_parts.append(f'    <meta name="description" content="{ContentFormatter._escape_html(content.meta_description)}">')
        
        html_parts.append('</head>')
        html_parts.append('<body>')
        html_parts.append('    <article class="category-content">')
        
        if content.h1:
            html_parts.append(f'        <h1>{ContentFormatter._escape_html(content.h1)}</h1>')
        
        if content.introduction:
            html_parts.append(f'        <p class="introduction">{ContentFormatter._format_html_content(content.introduction)}</p>')
        
        for section in content.h2_sections:
            html_parts.append(f'        <section class="content-section">')
            if section.heading:
                html_parts.append(f'            <h2>{ContentFormatter._escape_html(section.heading)}</h2>')
            html_parts.append(f'            <div class="section-content">')
            html_parts.append(f'                {ContentFormatter._format_html_content(section.content)}')
            html_parts.append(f'            </div>')
            html_parts.append(f'        </section>')
        
        html_parts.append('    </article>')
        html_parts.append('</body>')
        html_parts.append('</html>')
        
        return '\n'.join(html_parts)
    
    @staticmethod
    def to_markdown(content: CategoryContent) -> str:
        """
        Převede obsah do Markdown formátu
        
        Args:
            content: Strukturovaný obsah
            
        Returns:
            Markdown string
        """
        md_parts = []
        
        if content.title:
            md_parts.append(f'# {content.title}')
            md_parts.append('')
            md_parts.append(f'**Title:** {content.title}')
            md_parts.append('')
        
        if content.meta_description:
            md_parts.append(f'**Meta description:** {content.meta_description}')
            md_parts.append('')
        
        if content.h1:
            md_parts.append(f'## {content.h1}')
            md_parts.append('')
        
        if content.introduction:
            md_parts.append(content.introduction)
            md_parts.append('')
        
        for section in content.h2_sections:
            if section.heading:
                md_parts.append(f'## {section.heading}')
                md_parts.append('')
            md_parts.append(section.content)
            md_parts.append('')
        
        return '\n'.join(md_parts)
    
    @staticmethod
    def _escape_html(text: str) -> str:
        """Escapuje HTML znaky"""
        return (text.replace('&', '&amp;')
                   .replace('<', '&lt;')
                   .replace('>', '&gt;')
                   .replace('"', '&quot;')
                   .replace("'", '&#39;'))
    
    @staticmethod
    def _format_html_content(content: str) -> str:
        """Formátuje Markdown-like obsah do HTML"""
        # Zachovat existující HTML tagy
        if '<' in content and '>' in content:
            return content
        
        # Převod Markdown seznamů
        lines = content.split('\n')
        html_lines = []
        in_list = False
        
        for line in lines:
            stripped = line.strip()
            
            # Odrážkové seznamy
            if stripped.startswith('- ') or stripped.startswith('* '):
                if not in_list:
                    html_lines.append('<ul>')
                    in_list = True
                html_lines.append(f'    <li>{stripped[2:]}</li>')
            else:
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                if stripped:
                    html_lines.append(f'<p>{stripped}</p>')
        
        if in_list:
            html_lines.append('</ul>')
        
        return '\n'.join(html_lines)


class SampleGenerator:
    """Generátor vzorových textů pro kategorie"""
    
    def __init__(self, config_path: str = "content_structure.yaml"):
        """
        Inicializace generátoru
        
        Args:
            config_path: Cesta ke konfiguračnímu souboru
        """
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
    
    def generate_sample(self, category_name: str) -> CategoryContent:
        """
        Generuje vzorový text pro kategorii
        
        Args:
            category_name: Název kategorie (např. "Herní počítače")
            
        Returns:
            CategoryContent s vzorovým obsahem
        """
        content = CategoryContent()
        
        # Generování Title
        content.title = f'{category_name} – Výkonné PC sestavy | HelloComp'
        
        # Generování Meta Description
        content.meta_description = (
            f'{category_name} ⚡ Odborně sestavené PC s nejlepším poměrem výkon/cena. '
            f'Hotové konfigurace i PC na míru. Záruka a podpora.'
        )
        
        # Generování H1
        content.h1 = f'{category_name} – Odborně sestavené a připravené k použití'
        
        # Generování úvodního textu
        content.introduction = (
            f'{category_name} od HelloComp kombinují špičkový výkon, kvalitní komponenty '
            f'a ideální poměr cena/výkon. Každý počítač je profesionálně sestaven, otestován '
            f'a připraven k okamžitému použití. Díky možnosti individuálního upgradu si můžete '
            f'vybrat přesně takovou konfiguraci, jakou potřebujete.'
        )
        
        # Generování H2 sekcí
        typical_sections = self.config['sections']['h2_sections']['typical_sections']
        
        for section_template in typical_sections:
            section_heading = section_template.replace('[kategorie]', category_name.lower())
            
            if 'Jak vybrat' in section_heading:
                section_content = self._generate_selection_guide(category_name)
            elif 'Co zvládne' in section_heading:
                section_content = self._generate_performance_section(category_name)
            elif 'Typické konfigurace' in section_heading:
                section_content = self._generate_configurations(category_name)
            elif 'Pro koho' in section_heading:
                section_content = self._generate_target_audience(category_name)
            elif 'HelloComp' in section_heading:
                section_content = self._generate_cta_section(category_name)
            else:
                section_content = f'Obsah sekce: {section_heading}'
            
            content.h2_sections.append(ContentSection(
                type='h2',
                heading=section_heading.capitalize(),
                content=section_content
            ))
        
        return content
    
    def _generate_selection_guide(self, category: str) -> str:
        """Generuje sekci výběrového průvodce"""
        return f'''Při výběru {category.lower()} zvažte několik klíčových faktorů:

**Účel použití:**
- Gaming – vysoký výkon pro moderní hry
- Práce – stabilita a produktivita
- Multimedia – tvorba obsahu a rendering
- Universal – vyvážená konfigurace pro každodenní použití

**Rozpočet:**
- Entry level – dostupné řešení pro začátečníky
- Mid-range – optimální poměr výkon/cena
- High-end – špičkový výkon bez kompromisů

**Komponenty:**
- Procesor (CPU) – výpočetní výkon
- Grafická karta (GPU) – herní výkon a grafika
- RAM – multitasking a rychlost
- SSD – rychlé načítání systému a aplikací'''
    
    def _generate_performance_section(self, category: str) -> str:
        """Generuje sekci o výkonu"""
        return f'''{category} od HelloComp excelují v široké škále scénářů:

### Gaming
- Vysoké snímkové frekvence ve všech oblíbených hrách
- Podpora nejnovějších technologií (Ray Tracing, DLSS)
- Plynulý gameplay i v náročných AAA titulech

### Produktivita
- Rychlá práce v kancelářských aplikacích
- Multitasking bez zpomalení
- Spolehlivost pro každodenní použití

### Kreativita
- Video editing a renderování
- 3D modelování a animace
- Streamování a tvorba obsahu'''
    
    def _generate_configurations(self, category: str) -> str:
        """Generuje sekci s typickými konfiguracemi"""
        return f'''HelloComp nabízí předkonfigurované sestavy {category.lower()} optimalizované pro různé scénáře:

| Konfigurace | Procesor | GPU | RAM | Využití |
|-------------|----------|-----|-----|---------|
| Starter | Intel i5 / AMD Ryzen 5 | GTX 1660 / RX 6600 | 16GB | Základní gaming, práce |
| Gaming | Intel i7 / AMD Ryzen 7 | RTX 4070 / RX 7800 XT | 32GB | Vysoký výkon v 1440p |
| Pro | Intel i9 / AMD Ryzen 9 | RTX 4080 / RX 7900 XTX | 64GB | 4K gaming, kreativa |

Všechny sestavy lze individuálně upravit podle vašich preferencí.'''
    
    def _generate_target_audience(self, category: str) -> str:
        """Generuje sekci cílové skupiny"""
        hellocomp_values = self.config['content_guidelines']['hellocomp_values']
        values_list = '\n'.join([f'- ✅ {value}' for value in hellocomp_values])
        
        return f'''{category} jsou ideální pro:

### Hráče
Pokud hledáte maximální herní výkon a chcete si užívat nejnovější tituly bez kompromisů.

### Kreativce
Pro video editory, 3D umělce a všechny, kdo potřebují výkonný nástroj pro tvorbu.

### Profesionály
Stabilní a výkonné řešení pro náročné pracovní úlohy.

### Začátečníky
I s menším rozpočtem získáte kvalitní počítač připravený k použití.

HelloComp nabízí:
{values_list}'''
    
    def _generate_cta_section(self, category: str) -> str:
        """Generuje závěrečnou CTA sekci"""
        return f'''HelloComp vám poskytuje:
- ✅ **Odborně sestavenou konfiguraci** – každý PC je testován před odesláním
- ✅ **FPS kalkulačku** – zjistěte přesný výkon v konkrétních hrách
- ✅ **Flexibilní upgrade** – přizpůsobte si PC podle svých potřeb
- ✅ **Záruku a podporu** – jsme tu pro vás i po nákupu
- ✅ **Ideální poměr cena/výkon** – žádné předražené komponenty

Prohlédněte si naši nabídku [{category.lower()}](https://hellocomp.cz/herni-pc) nebo si nechte sestavit [PC na míru](https://hellocomp.cz/pc-na-miru). Potřebujete poradit? Náš tým vám rád pomůže s výběrem té nejlepší konfigurace pro vaše potřeby.'''


class CategoryTemplateGenerator:
    """Hlavní třída pro generování kategoriálních šablon"""
    
    def __init__(self, config_path: str = "content_structure.yaml"):
        """
        Inicializace generátoru
        
        Args:
            config_path: Cesta ke konfiguračnímu souboru
        """
        self.parser = ContentParser()
        self.validator = ContentValidator(config_path)
        self.formatter = ContentFormatter()
        self.sample_generator = SampleGenerator(config_path)
    
    def process_file(self, input_path: str, output_path: Optional[str] = None,
                    output_format: OutputFormat = OutputFormat.HTML,
                    validate_only: bool = False) -> Tuple[CategoryContent, List[ValidationResult]]:
        """
        Zpracuje vstupní soubor
        
        Args:
            input_path: Cesta ke vstupnímu souboru
            output_path: Cesta k výstupnímu souboru (optional)
            output_format: Výstupní formát
            validate_only: Pouze validovat, negenerovat výstup
            
        Returns:
            Tuple (CategoryContent, List[ValidationResult])
        """
        # Načtení vstupního souboru
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parsování podle typu souboru
        if input_path.endswith('.md'):
            parsed_content = self.parser.parse_markdown(content)
        elif input_path.endswith('.html'):
            parsed_content = self.parser.extract_html_content(content)
        else:
            raise ValueError(f"Nepodporovaný formát souboru: {input_path}")
        
        # Validace
        validation_results = self.validator.validate(parsed_content)
        
        # Pokud jen validujeme, končíme
        if validate_only:
            return parsed_content, validation_results
        
        # Generování výstupu
        if output_path:
            if output_format == OutputFormat.HTML:
                output = self.formatter.to_html(parsed_content)
            else:
                output = self.formatter.to_markdown(parsed_content)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(output)
        
        return parsed_content, validation_results
    
    def generate_sample(self, category_name: str, output_path: Optional[str] = None,
                       output_format: OutputFormat = OutputFormat.MARKDOWN) -> CategoryContent:
        """
        Generuje vzorový text pro kategorii
        
        Args:
            category_name: Název kategorie
            output_path: Cesta k výstupnímu souboru (optional)
            output_format: Výstupní formát
            
        Returns:
            CategoryContent s vzorovým obsahem
        """
        sample_content = self.sample_generator.generate_sample(category_name)
        
        if output_path:
            if output_format == OutputFormat.HTML:
                output = self.formatter.to_html(sample_content)
            else:
                output = self.formatter.to_markdown(sample_content)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(output)
        
        return sample_content


def main():
    """Hlavní funkce pro CLI"""
    parser = argparse.ArgumentParser(
        description='HelloComp Category Template Generator - SEO Content Automation Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Příklady použití:
  # Převod Markdown na HTML s validací
  python category_template_generator.py docs/seo-texty/graficke-karty-nvidia.md -o output.html -f html
  
  # Pouze validace existujícího souboru
  python category_template_generator.py docs/seo-texty/graficke-karty-nvidia.md --validate
  
  # Generování vzorového textu
  python category_template_generator.py --generate-sample "Herní počítače" -o sample.md
  
  # Generování vzorového textu v HTML
  python category_template_generator.py --generate-sample "Grafické karty" -o sample.html -f html
        '''
    )
    
    parser.add_argument('input', nargs='?', help='Vstupní soubor (Markdown nebo HTML)')
    parser.add_argument('-o', '--output', help='Výstupní soubor')
    parser.add_argument('-f', '--format', choices=['html', 'markdown'], default='html',
                       help='Výstupní formát (default: html)')
    parser.add_argument('-v', '--validate', action='store_true',
                       help='Pouze validovat obsah, negenerovat výstup')
    parser.add_argument('-g', '--generate-sample', metavar='CATEGORY',
                       help='Generovat vzorový text pro zadanou kategorii')
    parser.add_argument('-c', '--config', default='content_structure.yaml',
                       help='Cesta ke konfiguračnímu souboru (default: content_structure.yaml)')
    
    args = parser.parse_args()
    
    # Inicializace generátoru
    generator = CategoryTemplateGenerator(args.config)
    
    # Generování vzorového textu
    if args.generate_sample:
        output_format = OutputFormat.HTML if args.format == 'html' else OutputFormat.MARKDOWN
        sample = generator.generate_sample(args.generate_sample, args.output, output_format)
        
        print(f"\n✅ Vzorový text pro '{args.generate_sample}' byl vygenerován")
        if args.output:
            print(f"📄 Uloženo do: {args.output}")
        else:
            print("\n" + "="*80)
            if output_format == OutputFormat.HTML:
                print(generator.formatter.to_html(sample))
            else:
                print(generator.formatter.to_markdown(sample))
        return
    
    # Zpracování vstupního souboru
    if not args.input:
        parser.print_help()
        return
    
    if not Path(args.input).exists():
        print(f"❌ Chyba: Soubor '{args.input}' neexistuje")
        return
    
    output_format = OutputFormat.HTML if args.format == 'html' else OutputFormat.MARKDOWN
    content, validation_results = generator.process_file(
        args.input,
        args.output,
        output_format,
        args.validate
    )
    
    # Výpis validačních výsledků
    print("\n" + "="*80)
    print("VALIDAČNÍ VÝSLEDKY")
    print("="*80)
    
    errors = [r for r in validation_results if r.level == ValidationLevel.ERROR]
    warnings = [r for r in validation_results if r.level == ValidationLevel.WARNING]
    infos = [r for r in validation_results if r.level == ValidationLevel.INFO]
    
    if errors:
        print("\n❌ CHYBY:")
        for result in errors:
            print(f"  • [{result.section}] {result.message}")
    
    if warnings:
        print("\n⚠️  VAROVÁNÍ:")
        for result in warnings:
            print(f"  • [{result.section}] {result.message}")
    
    if infos:
        print("\n")
        for result in infos:
            print(f"  {result.message}")
    
    if not args.validate and args.output:
        print(f"\n📄 Výstup uložen do: {args.output}")
    
    print("\n" + "="*80)


if __name__ == '__main__':
    main()
