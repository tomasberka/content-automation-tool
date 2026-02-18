#!/usr/bin/env python3
"""
HTML Structure Validation Demo
===============================

This demo shows how HTML structure validation works.
"""

from category_template_generator import (
    CategoryContent,
    ContentSection,
    ContentValidator,
    ContentFormatter,
    ValidationLevel
)


def demo_1_correct_structure():
    """Demo 1: Correctly structured content"""
    print("\n" + "="*70)
    print("DEMO 1: Correctly Structured Content ✅")
    print("="*70)
    
    content = CategoryContent(
        title="Grafické karty NVIDIA | Výkonné GPU pro gaming",
        meta_description="Grafické karty NVIDIA GeForce RTX ⚡ Výkonné GPU pro gaming, 3D a AI. Špičkový výkon pro nejnáročnější hry a profesionální aplikace.",
        h1="Grafické karty NVIDIA GeForce",
        introduction=(
            "Grafické karty NVIDIA představují zlatý standard v herním světě. "
            "S technologiemi jako ray tracing a DLSS nabízejí nepřekonatelný "
            "výkon v nejnovějších AAA hrách. Ať už hledáte entry-level RTX 4060, "
            "nebo špičkovou RTX 5090, u HelloComp najdete grafiku pro každý rozpočet. "
            "Všechny karty jsou důkladně otestované a připravené k okamžitému použití "
            "ve vašem herním nebo pracovním PC."
        ),
        h2_sections=[
            ContentSection(
                type="h2",
                heading="Proč vybrat NVIDIA GPU",
                content=(
                    "NVIDIA grafické karty dominují trhu díky špičkové technologii. "
                    "Ray tracing v reálném čase vytváří fotorealistické stíny a odrazy. "
                    "DLSS 3.5 zvyšuje výkon až o 300% bez ztráty kvality."
                )
            ),
            ContentSection(
                type="h2",
                heading="Nejpopulárnější modely",
                content=(
                    "- RTX 4060: Skvělý poměr cena/výkon pro 1080p gaming\n"
                    "- RTX 4070: Ideální pro 1440p s vysokými detaily\n"
                    "- RTX 4090: Absolutní špička pro 4K a ray tracing"
                )
            ),
            ContentSection(
                type="h2",
                heading="Pro koho je NVIDIA GPU ideální",
                content=(
                    "Herní nadšenci ocení vysoký výkon v AAA hrách. "
                    "3D grafici a designéři využijí CUDA jádra pro rendering. "
                    "Streameři oceňují NVENC enkodér pro kvalitní streamování."
                )
            )
        ]
    )
    
    # Validate
    validator = ContentValidator()
    results = validator.validate(content)
    
    # Print results
    errors = [r for r in results if r.level == ValidationLevel.ERROR]
    warnings = [r for r in results if r.level == ValidationLevel.WARNING]
    
    if not errors:
        print("\n✅ ÚSPĚCH: Obsah splňuje všechny požadavky HTML struktury")
        print("\nFormátovaný HTML úvodní text:")
        formatted_intro = ContentFormatter._format_html_content(content.introduction)
        print(f"  {formatted_intro[:100]}...")
        
        print("\nFormátovaná H2 sekce (seznam):")
        formatted_list = ContentFormatter._format_html_content(content.h2_sections[1].content)
        print(f"  {formatted_list[:150]}...")
    else:
        print(f"\n❌ CHYBA: Nalezeno {len(errors)} problémů")
        for error in errors:
            print(f"  - {error.message}")


def demo_2_incorrect_structure():
    """Demo 2: Incorrect structure that will be caught"""
    print("\n" + "="*70)
    print("DEMO 2: Incorrect Structure (for demonstration) ⚠️")
    print("="*70)
    
    # Create content with HTML that doesn't start with <p>
    content = CategoryContent(
        title="Test kategorie | HelloComp",
        meta_description="Test meta description pro ukázku validace HTML struktury v našem nástroji pro automatizaci obsahu.",
        h1="Test kategorie",
        introduction="<h3>Začíná špatně</h3><p>Text...</p>",  # Incorrect!
        h2_sections=[]
    )
    
    # Validate
    validator = ContentValidator()
    results = validator.validate(content)
    
    # Print errors
    errors = [r for r in results if r.level == ValidationLevel.ERROR]
    
    if errors:
        print(f"\n❌ Nalezeno {len(errors)} problémů:")
        for error in errors:
            print(f"\n  Sekce: {error.section}")
            print(f"  Problém: {error.message}")
            if error.actual_value:
                print(f"  Aktuální: {error.actual_value}")
            if error.expected_value:
                print(f"  Očekávané: {error.expected_value}")
    
    # Show how formatter would fix it
    print("\n🔧 Automatická oprava:")
    formatted = ContentFormatter._format_html_content(content.introduction)
    print(f"  {formatted[:100]}...")


def demo_3_list_handling():
    """Demo 3: How lists are handled"""
    print("\n" + "="*70)
    print("DEMO 3: List Handling with <p> Prefix ✅")
    print("="*70)
    
    list_content = """- První vlastnost
- Druhá vlastnost
- Třetí vlastnost"""
    
    print("\nVSTUP (Markdown seznam):")
    print(f"  {list_content}")
    
    formatted = ContentFormatter._format_html_content(list_content)
    
    print("\nVÝSTUP (HTML s <p> prefixem):")
    print(f"  {formatted}")
    
    # Verify it starts with <p>
    if formatted.strip().startswith('<p>'):
        print("\n✅ Seznam má správný <p> prefix pro backend")
    else:
        print("\n⚠️  Seznam nemá <p> prefix")


def demo_4_backend_integration():
    """Demo 4: Explain backend integration"""
    print("\n" + "="*70)
    print("DEMO 4: Backend Integration Explanation 📚")
    print("="*70)
    
    print("\nProč musí obsah začínat <p> tagem?")
    print("-" * 70)
    print("""
1. Backend HelloComp.cz automaticky generuje interaktivní prvky
2. Tyto prvky (tlačítka, vysouvací bloky) jsou vloženy ZA první <p> element
3. První <p> slouží jako 'anchor point' pro backend
4. Bez něj by backend nevěděl, kam komponenty vložit

Příklad backend transformace:

  VSTUP:
    <p>Úvodní text o produktech.</p>
    <h2>Další obsah</h2>

  VÝSTUP (po backend zpracování):
    <p>Úvodní text o produktech.</p>
    <button class="auto-cta">Zobrazit produkty</button>
    <div class="sliding-block">...</div>
    <h2>Další obsah</h2>
    """)


def main():
    """Run all demos"""
    print("\n" + "="*70)
    print("HTML Structure Validation - Interactive Demos")
    print("="*70)
    print("\nTento skript demonstruje validaci HTML struktury pro HelloComp obsah.")
    
    demo_1_correct_structure()
    demo_2_incorrect_structure()
    demo_3_list_handling()
    demo_4_backend_integration()
    
    print("\n" + "="*70)
    print("✅ Všechny dema dokončeny")
    print("="*70)
    print("\nDalší informace:")
    print("  - Dokumentace: docs/HTML_STRUCTURE_VALIDATION.md")
    print("  - Testy: python test_html_structure.py")
    print("  - Konfigurace: content_structure.yaml")
    print()


if __name__ == "__main__":
    main()
