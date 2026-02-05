#!/usr/bin/env python3
"""
Example Integration Script
===========================

Ukázka integrace Category Template Generatoru do redakčního workflow.
"""

from category_template_generator import (
    CategoryTemplateGenerator,
    OutputFormat,
    ValidationLevel
)
from pathlib import Path
import json


def example_workflow_validation():
    """
    Příklad: Validace všech SEO textů v adresáři
    """
    print("="*80)
    print("PŘÍKLAD 1: Batch validace všech kategorií")
    print("="*80)
    
    generator = CategoryTemplateGenerator()
    seo_dir = Path('docs/seo-texty')
    
    if not seo_dir.exists():
        print("⚠️  Adresář docs/seo-texty neexistuje")
        return
    
    results = {}
    for md_file in seo_dir.glob('*.md'):
        if md_file.name == 'README.md':
            continue
            
        print(f"\n📄 Validace: {md_file.name}")
        try:
            content, validation = generator.process_file(
                str(md_file),
                validate_only=True
            )
            
            errors = [r for r in validation if r.level == ValidationLevel.ERROR]
            warnings = [r for r in validation if r.level == ValidationLevel.WARNING]
            
            results[md_file.name] = {
                'errors': len(errors),
                'warnings': len(warnings),
                'status': '✅' if not errors else '❌'
            }
            
            print(f"  {results[md_file.name]['status']} Chyby: {len(errors)}, Varování: {len(warnings)}")
            
        except Exception as e:
            print(f"  ❌ Chyba při zpracování: {e}")
            results[md_file.name] = {'status': '❌', 'errors': 1, 'warnings': 0}
    
    # Souhrn
    print("\n" + "="*80)
    print("SOUHRN VALIDACE")
    print("="*80)
    
    total = len(results)
    ok = sum(1 for r in results.values() if r['status'] == '✅')
    failed = total - ok
    
    print(f"Celkem souborů: {total}")
    print(f"✅ Úspěšných: {ok}")
    print(f"❌ S chybami: {failed}")
    print(f"Úspěšnost: {ok/total*100:.1f}%")


def example_generate_new_category():
    """
    Příklad: Generování nové kategorie
    """
    print("\n" + "="*80)
    print("PŘÍKLAD 2: Generování nové kategorie")
    print("="*80)
    
    generator = CategoryTemplateGenerator()
    
    # Generování vzorového textu
    category_name = "Herní monitory"
    output_path = "/tmp/herni-monitory-vzor.md"
    
    print(f"\n📝 Generuji vzorový text pro: {category_name}")
    
    sample = generator.generate_sample(
        category_name,
        output_path,
        OutputFormat.MARKDOWN
    )
    
    print(f"✅ Vygenerováno do: {output_path}")
    print(f"\nNáhled:")
    print(f"  Title: {sample.title}")
    print(f"  Meta: {sample.meta_description[:50]}...")
    print(f"  H1: {sample.h1}")
    print(f"  H2 sekcí: {len(sample.h2_sections)}")


def example_convert_to_html():
    """
    Příklad: Konverze Markdown na HTML pro publikaci
    """
    print("\n" + "="*80)
    print("PŘÍKLAD 3: Konverze na HTML pro publikaci")
    print("="*80)
    
    generator = CategoryTemplateGenerator()
    
    input_file = "docs/seo-texty/graficke-karty-nvidia.md"
    output_file = "/tmp/publikace-graficke-karty.html"
    
    if not Path(input_file).exists():
        print(f"⚠️  Soubor {input_file} neexistuje")
        return
    
    print(f"\n🔄 Převádím: {input_file}")
    print(f"📤 Výstup: {output_file}")
    
    content, validation = generator.process_file(
        input_file,
        output_file,
        OutputFormat.HTML
    )
    
    print("✅ Konverze dokončena")
    
    # Kontrola validace
    errors = [r for r in validation if r.level == ValidationLevel.ERROR]
    if errors:
        print("\n⚠️  UPOZORNĚNÍ: Soubor má validační chyby!")
        for error in errors:
            print(f"  • {error.message}")
    else:
        print("✅ Validace OK - soubor lze publikovat")


def example_api_usage():
    """
    Příklad: Použití Python API
    """
    print("\n" + "="*80)
    print("PŘÍKLAD 4: Použití Python API")
    print("="*80)
    
    from category_template_generator import (
        ContentParser,
        ContentValidator,
        ContentFormatter,
        CategoryContent
    )
    
    # 1. Ruční parsování
    print("\n1️⃣  Ruční parsování obsahu")
    
    sample_markdown = """
**Title:** Test kategorie | HelloComp

**Meta description:** Testovací meta popis pro kategorii s dostatečnou délkou pro SEO optimalizaci webu HelloComp.

## Test kategorie – hlavní nadpis

Toto je úvodní text kategorie. Obsahuje dostatek slov pro splnění minimálních požadavků. 
HelloComp nabízí kvalitní produkty s nejlepším poměrem výkon cena pro všechny zákazníky.

## První sekce

Obsah první sekce s detaily.

## Druhá sekce

Obsah druhé sekce s informacemi.

## Třetí sekce

Obsah třetí sekce s doplňky.
"""
    
    parser = ContentParser()
    content = parser.parse_markdown(sample_markdown)
    
    print(f"  ✅ Naparsováno:")
    print(f"     Title: {content.title}")
    print(f"     H2 sekcí: {len(content.h2_sections)}")
    
    # 2. Validace
    print("\n2️⃣  Validace obsahu")
    
    validator = ContentValidator()
    validation_results = validator.validate(content)
    
    for result in validation_results:
        icon = "✅" if result.level == ValidationLevel.INFO else "⚠️" if result.level == ValidationLevel.WARNING else "❌"
        print(f"  {icon} {result.message}")
    
    # 3. Formátování
    print("\n3️⃣  Formátování výstupu")
    
    formatter = ContentFormatter()
    
    # Markdown
    md_output = formatter.to_markdown(content)
    print(f"  📝 Markdown: {len(md_output)} znaků")
    
    # HTML
    html_output = formatter.to_html(content)
    print(f"  🌐 HTML: {len(html_output)} znaků")


def example_batch_export():
    """
    Příklad: Hromadný export všech kategorií do HTML
    """
    print("\n" + "="*80)
    print("PŘÍKLAD 5: Hromadný export do HTML")
    print("="*80)
    
    generator = CategoryTemplateGenerator()
    seo_dir = Path('docs/seo-texty')
    output_dir = Path('/tmp/html-export')
    
    if not seo_dir.exists():
        print("⚠️  Adresář docs/seo-texty neexistuje")
        return
    
    output_dir.mkdir(exist_ok=True)
    
    print(f"\n📁 Exportuji kategorie z {seo_dir}")
    print(f"📂 Výstupní adresář: {output_dir}")
    
    exported = 0
    for md_file in seo_dir.glob('*.md'):
        if md_file.name == 'README.md':
            continue
        
        output_file = output_dir / f"{md_file.stem}.html"
        
        try:
            generator.process_file(
                str(md_file),
                str(output_file),
                OutputFormat.HTML
            )
            print(f"  ✅ {md_file.name} → {output_file.name}")
            exported += 1
        except Exception as e:
            print(f"  ❌ {md_file.name}: {e}")
    
    print(f"\n✅ Exportováno {exported} kategorií do {output_dir}")


def example_quality_report():
    """
    Příklad: Generování quality reportu
    """
    print("\n" + "="*80)
    print("PŘÍKLAD 6: Quality Report pro všechny kategorie")
    print("="*80)
    
    generator = CategoryTemplateGenerator()
    seo_dir = Path('docs/seo-texty')
    
    if not seo_dir.exists():
        print("⚠️  Adresář docs/seo-texty neexistuje")
        return
    
    report = {
        'total': 0,
        'with_errors': 0,
        'with_warnings': 0,
        'perfect': 0,
        'details': []
    }
    
    for md_file in seo_dir.glob('*.md'):
        if md_file.name == 'README.md':
            continue
        
        try:
            content, validation = generator.process_file(
                str(md_file),
                validate_only=True
            )
            
            errors = [r for r in validation if r.level == ValidationLevel.ERROR]
            warnings = [r for r in validation if r.level == ValidationLevel.WARNING]
            
            report['total'] += 1
            
            if errors:
                report['with_errors'] += 1
                status = 'ERROR'
            elif warnings:
                report['with_warnings'] += 1
                status = 'WARNING'
            else:
                report['perfect'] += 1
                status = 'OK'
            
            report['details'].append({
                'file': md_file.name,
                'status': status,
                'errors': len(errors),
                'warnings': len(warnings)
            })
            
        except Exception as e:
            report['total'] += 1
            report['with_errors'] += 1
            report['details'].append({
                'file': md_file.name,
                'status': 'FAILED',
                'errors': 1,
                'warnings': 0
            })
    
    # Výstup reportu
    print(f"\n📊 QUALITY REPORT")
    print(f"{'='*80}")
    print(f"Celkem kategorií: {report['total']}")
    print(f"✅ Perfektní: {report['perfect']} ({report['perfect']/report['total']*100:.1f}%)")
    print(f"⚠️  S varováními: {report['with_warnings']} ({report['with_warnings']/report['total']*100:.1f}%)")
    print(f"❌ S chybami: {report['with_errors']} ({report['with_errors']/report['total']*100:.1f}%)")
    
    # Top 5 nejhorších
    print(f"\n⚠️  Kategorie vyžadující pozornost:")
    sorted_details = sorted(
        report['details'],
        key=lambda x: (x['errors'], x['warnings']),
        reverse=True
    )
    
    for detail in sorted_details[:5]:
        if detail['errors'] > 0 or detail['warnings'] > 0:
            print(f"  • {detail['file']}: {detail['errors']} chyb, {detail['warnings']} varování")
    
    # Uložení do JSON
    report_file = '/tmp/quality-report.json'
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 Report uložen do: {report_file}")


if __name__ == '__main__':
    print("\n" + "="*80)
    print("HelloComp Category Template Generator - Integration Examples")
    print("="*80)
    
    # Spustit všechny příklady
    example_workflow_validation()
    example_generate_new_category()
    example_convert_to_html()
    example_api_usage()
    example_batch_export()
    example_quality_report()
    
    print("\n" + "="*80)
    print("✅ Všechny příklady dokončeny")
    print("="*80)
