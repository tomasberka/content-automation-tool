# HelloComp Content Automation Tool

**Multi-Platform Content Strategy & SEO Generator**

Automatický nástroj pro tvorbu, validaci a správu SEO-optimalizovaného obsahu pro HelloComp.cz e-shop.

## 🚀 Co tento nástroj umí

- ✅ **Automatická validace** kategoriálního obsahu podle SEO pravidel
- ✅ **Generování vzorových textů** pro nové kategorie
- ✅ **Převod mezi formáty** (Markdown ↔ HTML)
- ✅ **Zachování HTML tagů a odkazů** při zpracování
- ✅ **Batch operace** pro hromadné zpracování
- ✅ **Python API** pro integraci do redakčních systémů
- ✅ **Quality reporting** pro monitoring kvality obsahu

## 📁 Obsah repozitáře

```
content-automation-tool/
├── category_template_generator.py  # 🔧 Hlavní generátor
├── content_utils.py                # 🛠️ Utility funkce
├── content_structure.yaml          # ⚙️ SEO pravidla a konfigurace
├── example_integration.py          # 📚 Příklady použití
├── QUICKSTART.md                   # 🚀 Rychlý start
├── README_GENERATOR.md             # 📖 Detailní dokumentace
├── requirements.txt                # 📦 Python závislosti
└── docs/
    ├── hellocomp-category-structure.md         # Struktura kategorií
    ├── facebook-instagram-strategie-2026.md    # 📱 FB & IG Strategie
    ├── social-media-quick-reference.md         # ⚡ Social Media Quick Ref
    └── seo-texty/                              # 32 SEO textů (hotovo)
```

## ⚡ Quick Start

```bash
# Instalace
pip install -r requirements.txt

# Validace existující kategorie
python category_template_generator.py docs/seo-texty/graficke-karty-nvidia.md --validate

# Generování nové kategorie
python category_template_generator.py --generate-sample "Herní počítače" -o output.md

# Převod na HTML
python category_template_generator.py input.md -o output.html -f html
```

## 📚 Dokumentace

### Hlavní dokumentace
- **[QUICKSTART.md](QUICKSTART.md)** - Rychlý start pro začátečníky
- **[README_GENERATOR.md](README_GENERATOR.md)** - Kompletní dokumentace a API reference
- **[example_integration.py](example_integration.py)** - Ukázky integrace do workflow

### Social Media Strategie
- **[Facebook & Instagram Strategie 2026](docs/facebook-instagram-strategie-2026.md)** - Kompletní strategie pro FB & IG včetně Master Research Promptu
- **[Social Media Quick Reference](docs/social-media-quick-reference.md)** - Rychlá referenční příručka pro denní práci

## 🎯 Hlavní funkce

### 1. Category Template Generator

Hlavní nástroj pro práci s kategoriálním obsahem:

```bash
# Validace
python category_template_generator.py input.md --validate

# Konverze
python category_template_generator.py input.md -o output.html -f html

# Generování vzorku
python category_template_generator.py --generate-sample "Kategorie" -o output.md
```

### 2. Validace SEO struktury

Automaticky kontroluje:
- ✅ TITLE (30-60 znaků)
- ✅ META description (140-160 znaků)
- ✅ H1 nadpis
- ✅ Úvodní text (50-80 slov)
- ✅ Minimálně 3 H2 sekce
- ✅ Celkový obsah (600-900 slov)

### 3. Workflow integrace

```python
from category_template_generator import CategoryTemplateGenerator, OutputFormat

generator = CategoryTemplateGenerator()

# Zpracování souboru
content, validation = generator.process_file('input.md', 'output.html', OutputFormat.HTML)

# Validace
errors = [r for r in validation if r.level == ValidationLevel.ERROR]
if not errors:
    print("✅ Lze publikovat")
```

## 📊 Status projektu

- ✅ **32 SEO textů** dokončeno (docs/seo-texty/)
- ✅ **Category Template Generator** implementován
- ✅ **Validační systém** funkční
- ✅ **HTML/Markdown export** připraven
- ✅ **Příklady a dokumentace** hotovo
- ✅ **FB & IG Strategie 2026** - Kompletní social media plán

## 📱 Social Media Management

### Nová funkce: Facebook & Instagram Strategie

Kompletní strategie pro správu sociálních sítí v režimu "One-Man Show":

- 📋 **Analýza trendů** - Co funguje v gamingu na FB/IG (2025/2026)
- 🎯 **Akční kroky** - Konkrétní strategie pro one-man team
- 🤖 **Master Research Prompt** - AI-powered výzkum konkurence a trendů
- 📅 **Content plánování** - Týdenní a měsíční plány
- 📊 **Metriky a KPI** - Co sledovat a jak měřit úspěch

**Dokumenty:**
- [Facebook & Instagram Strategie 2026](docs/facebook-instagram-strategie-2026.md) - Detailní 10-sekční strategie
- [Social Media Quick Reference](docs/social-media-quick-reference.md) - Denní checklist a rychlé šablony

## 🤝 Pro redaktory

1. Vytvořte novou kategorii: `python category_template_generator.py --generate-sample "Název" -o nova-kategorie.md`
2. Upravte obsah v editoru
3. Validujte: `python category_template_generator.py nova-kategorie.md --validate`
4. Exportujte: `python category_template_generator.py nova-kategorie.md -o output.html -f html`

## 🔧 Pro vývojáře

- Python 3.8+
- Modularní architektura
- Rozšiřitelná konfigurace (YAML)
- Kompletní Python API
- Připraveno pro CI/CD integraci

## 📄 Licence

Proprietární software HelloComp © 2026

---

**Vytvořeno:** 2026-02-05  
**Status:** ✅ Production Ready
