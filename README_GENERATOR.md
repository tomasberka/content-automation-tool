# HelloComp Category Template Generator

Automatický generátor SEO-optimalizovaného obsahu pro kategorie webu HelloComp.cz. Systém umožňuje validaci, transformaci a generování kategoriálního obsahu podle stanovených SEO pravidel.

## 🚀 Funkce

- ✅ **Validace obsahu** - Kontrola všech povinných SEO elementů (TITLE, META, H1, H2 sekce)
- ✅ **Automatické formátování** - Převod mezi Markdown a HTML formáty
- ✅ **Generování vzorových textů** - Automatické vytváření šablon pro nové kategorie
- ✅ **Zachování HTML/odkazů** - Plná podpora HTML tagů, odkazů a formátování
- ✅ **SEO optimalizace** - Kontrola délek, počtu slov, struktury nadpisů
- ✅ **Rozšiřitelnost** - Snadné přidávání nových pravidel a sekcí
- ✅ **Workflow integrace** - Připraveno pro napojení na redakční systémy

## 📋 Požadavky

```bash
Python 3.8+
pyyaml>=6.0
markdown>=3.5
beautifulsoup4>=4.12.0
html5lib>=1.1
```

## 🔧 Instalace

1. Naklonujte repozitář:
```bash
git clone https://github.com/tomasberka/content-automation-tool.git
cd content-automation-tool
```

2. Nainstalujte závislosti:
```bash
pip install -r requirements.txt
```

## 💻 Použití

### Základní příklady

#### 1. Validace existujícího obsahu

```bash
python category_template_generator.py docs/seo-texty/graficke-karty-nvidia.md --validate
```

Výstup:
```
================================================================================
VALIDAČNÍ VÝSLEDKY
================================================================================

  ✅ Veškerý obsah splňuje SEO požadavky

================================================================================
```

#### 2. Převod Markdown na HTML

```bash
python category_template_generator.py docs/seo-texty/graficke-karty-nvidia.md -o output.html -f html
```

#### 3. Generování vzorového textu

```bash
python category_template_generator.py --generate-sample "Herní počítače" -o herni-pc-sample.md
```

#### 4. Generování vzorového textu v HTML

```bash
python category_template_generator.py --generate-sample "Grafické karty" -o graficke-karty.html -f html
```

### Pokročilé použití

#### Vlastní konfigurační soubor

```bash
python category_template_generator.py input.md -c custom_config.yaml -o output.html
```

#### Batch zpracování

```bash
for file in docs/seo-texty/*.md; do
    python category_template_generator.py "$file" --validate
done
```

## 📁 Struktura projektu

```
content-automation-tool/
├── category_template_generator.py  # Hlavní modul
├── content_utils.py                # Utility funkce
├── content_structure.yaml          # Konfigurační soubor s SEO pravidly
├── requirements.txt                # Python závislosti
├── docs/
│   ├── hellocomp-category-structure.md  # Struktura kategorií
│   └── seo-texty/                  # Existující SEO texty
│       ├── graficke-karty-nvidia.md
│       ├── procesory-intel.md
│       └── ...
└── README_GENERATOR.md             # Tato dokumentace
```

## 🎯 Struktura SEO obsahu

Každý kategoriální text obsahuje:

### Povinné sekce

1. **TITLE** (30-60 znaků)
   - Formát: `Název kategorie – klíčové slovo | HelloComp`
   - Příklad: `Grafické karty NVIDIA – RTX 4090, 4080, 5090 | HelloComp`

2. **META DESCRIPTION** (140-160 znaků)
   - Obsahuje emoji, klíčová slova, USP
   - Příklad: `Grafické karty NVIDIA GeForce RTX ⚡ Výkonné GPU...`

3. **H1 Nadpis** (20-100 znaků)
   - Hlavní nadpis stránky
   - Obsahuje rozšířený název kategorie

4. **Úvodní text** (50-80 slov)
   - První odstavec pod H1
   - Popisuje kategorii a hodnoty HelloComp

5. **H2 Sekce** (minimálně 3)
   - Jak vybrat správnou [kategorii]
   - Co zvládne [kategorie] – výkon a možnosti
   - Typické konfigurace a varianty
   - Pro koho je [kategorie] ideální
   - Nakupujte s jistotou u HelloComp (CTA sekce)

### Celkový rozsah

- **Celkem:** 600-900 slov
- **Ideálně:** ~750 slov
- **Formátování:** Odrážky, tabulky, číslované seznamy

## 🔍 Validační pravidla

Systém kontroluje:

- ✅ Přítomnost všech povinných sekcí
- ✅ Délku TITLE (30-60 znaků)
- ✅ Délku META description (140-160 znaků)
- ✅ Počet slov v úvodním textu (50-80)
- ✅ Minimální počet H2 sekcí (3+)
- ✅ Celkový počet slov (600-900)
- ⚠️ Varování při odchylkách od ideálních hodnot

## 🎨 Výstupní formáty

### HTML

```html
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <title>Grafické karty NVIDIA – RTX 4090...</title>
    <meta name="description" content="Grafické karty NVIDIA...">
</head>
<body>
    <article class="category-content">
        <h1>Grafické karty NVIDIA GeForce...</h1>
        <p class="introduction">...</p>
        <section class="content-section">
            <h2>Jak vybrat správnou NVIDIA grafickou kartu</h2>
            <div class="section-content">...</div>
        </section>
    </article>
</body>
</html>
```

### Markdown

```markdown
# Grafické karty NVIDIA – RTX 4090, 4080, 5090 | HelloComp

**Title:** Grafické karty NVIDIA – RTX 4090, 4080, 5090 | HelloComp

**Meta description:** Grafické karty NVIDIA GeForce RTX ⚡ ...

## Grafické karty NVIDIA GeForce – od RTX 4070 po špičkovou RTX 5090

Úvodní text kategorie...

## Jak vybrat správnou NVIDIA grafickou kartu

Obsah sekce...
```

## 🛠️ Konfigurace (content_structure.yaml)

Konfigurační soubor definuje:

```yaml
required_sections:
  - title
  - meta_description
  - h1
  - introduction
  - h2_sections

sections:
  title:
    max_length: 60
    min_length: 30
  
  meta_description:
    max_length: 160
    min_length: 140
  
  # ... další sekce

content_guidelines:
  total_word_count:
    min: 600
    max: 900
    ideal: 750
  
  hellocomp_values:
    - "Hotové PC sestavy"
    - "Možnost individuálního upgradu"
    - "FPS kalkulačka u počítačů"
    # ... další hodnoty
```

## 🔌 Integrace do workflow

### Python API

```python
from category_template_generator import CategoryTemplateGenerator, OutputFormat

# Inicializace
generator = CategoryTemplateGenerator('content_structure.yaml')

# Zpracování souboru
content, validation = generator.process_file(
    'input.md',
    'output.html',
    OutputFormat.HTML
)

# Generování vzorku
sample = generator.generate_sample('Herní počítače', 'output.md')

# Validace
for result in validation:
    print(f"{result.level}: {result.message}")
```

### Redakční systém

```python
# Import obsahu z redakčního systému
raw_content = cms.get_category_content(category_id)

# Parsování a validace
parser = ContentParser()
content = parser.parse_markdown(raw_content)

validator = ContentValidator()
results = validator.validate(content)

# Kontrola chyb
errors = [r for r in results if r.level == ValidationLevel.ERROR]
if errors:
    # Vrátit do redakce s poznámkami
    cms.mark_for_revision(category_id, errors)
else:
    # Publikovat
    formatter = ContentFormatter()
    html_output = formatter.to_html(content)
    cms.publish(category_id, html_output)
```

## 📊 Utility funkce (content_utils.py)

Podpůrné funkce pro práci s obsahem:

```python
from content_utils import *

# Počítání slov
word_count = count_words(text)

# Extrakce odkazů
links = extract_links(content)

# Generování obsahu (TOC)
toc = generate_toc(markdown_content)

# Formátování tabulek
table = format_table(data, headers)

# Extrakce klíčových slov
keywords = extract_keywords(text, top_n=10)

# Validace interních odkazů
invalid = validate_internal_links(content, valid_paths)
```

## 🎯 Příklady vzorového výstupu

### Generování pro "Herní počítače"

```bash
python category_template_generator.py --generate-sample "Herní počítače" -o herni-pc.md
```

Vytvoří:
- ✅ Kompletní title a meta description
- ✅ H1 nadpis specifický pro kategorii
- ✅ Úvodní text s hodnotami HelloComp
- ✅ 5 H2 sekcí (výběr, výkon, konfigurace, cílová skupina, CTA)
- ✅ Tabulku s konfiguracemi
- ✅ Interní odkazy na relevantní stránky
- ✅ Celkem ~750 slov

## 🚦 Validační výstupy

### ✅ Úspěšná validace

```
================================================================================
VALIDAČNÍ VÝSLEDKY
================================================================================

  ✅ Veškerý obsah splňuje SEO požadavky

================================================================================
```

### ⚠️ Varování

```
================================================================================
VALIDAČNÍ VÝSLEDKY
================================================================================

⚠️  VAROVÁNÍ:
  • [title] Title je příliš dlouhý (65 znaků, max 60)
  • [introduction] Úvodní text je příliš krátký (45 slov, min 50)

================================================================================
```

### ❌ Chyby

```
================================================================================
VALIDAČNÍ VÝSLEDKY
================================================================================

❌ CHYBY:
  • [title] Title je povinný a chybí
  • [h1] H1 nadpis je povinný a chybí

⚠️  VAROVÁNÍ:
  • [h2_sections] Málo H2 sekcí (2, minimum 3)

================================================================================
```

## 🔄 Workflow návod

### 1. Tvorba nové kategorie

```bash
# Generovat vzor
python category_template_generator.py --generate-sample "Nová kategorie" -o nova-kategorie.md

# Upravit v editoru
nano nova-kategorie.md

# Validovat
python category_template_generator.py nova-kategorie.md --validate

# Převést na HTML pro publikaci
python category_template_generator.py nova-kategorie.md -o nova-kategorie.html -f html
```

### 2. Aktualizace existující kategorie

```bash
# Načíst existující obsah
python category_template_generator.py docs/seo-texty/existujici.md --validate

# Upravit dle výsledků validace
nano docs/seo-texty/existujici.md

# Znovu validovat
python category_template_generator.py docs/seo-texty/existujici.md --validate

# Publikovat
python category_template_generator.py docs/seo-texty/existujici.md -o publish/existujici.html -f html
```

### 3. Batch validace všech kategorií

```bash
# Validovat všechny soubory
for file in docs/seo-texty/*.md; do
    echo "Validating: $file"
    python category_template_generator.py "$file" --validate
    echo "---"
done
```

## 🎓 Best Practices

### Pro redaktory

1. **Vždy začněte validací** - Ujistěte se, že struktura je správná
2. **Používejte vzorové texty** - Pro nové kategorie generujte vzor a upravte
3. **Zachovejte HTML tagy** - Odkazy a formátování zůstanou zachovány
4. **Kontrolujte délky** - TITLE max 60 znaků, META max 160 znaků
5. **Minimum 3 H2 sekce** - Pro dobrou strukturu obsahu

### Pro vývojáře

1. **Rozšiřujte konfiguraci** - Přidávejte pravidla do `content_structure.yaml`
2. **Používejte API** - Integrujte přes Python objekty, ne jen CLI
3. **Validujte před publikací** - Automaticky v CI/CD pipeline
4. **Logujte chyby** - Pro debugging a monitoring kvality

## 🐛 Troubleshooting

### Problém: "Soubor neexistuje"
```bash
# Ujistěte se, že cesta je správná
ls -la docs/seo-texty/

# Použijte absolutní cestu
python category_template_generator.py /full/path/to/file.md
```

### Problém: "Chybí konfigurace"
```bash
# Zkontrolujte, že content_structure.yaml existuje
ls -la content_structure.yaml

# Nebo zadejte vlastní cestu
python category_template_generator.py input.md -c /path/to/config.yaml
```

### Problém: "Encoding error"
```bash
# Všechny soubory musí být UTF-8
file -i docs/seo-texty/file.md

# Případně převést
iconv -f ISO-8859-2 -t UTF-8 input.md > output.md
```

## 📈 Budoucí rozšíření

- [ ] **GUI interface** - Webové rozhraní pro redaktory
- [ ] **AI generování** - Integrace GPT-4 pro automatickou tvorbu
- [ ] **Analýza konkurence** - Porovnání s jinými e-shopy
- [ ] **Keyword research** - Automatický výběr klíčových slov
- [ ] **A/B testing** - Podpora variant pro testování
- [ ] **Multi-language** - Podpora více jazyků
- [ ] **Image optimization** - Kontrola a optimalizace obrázků
- [ ] **Schema.org** - Automatické generování strukturovaných dat

## 🤝 Přispívání

Pro přispění do projektu:

1. Fork repozitář
2. Vytvořte feature branch (`git checkout -b feature/nova-funkce`)
3. Commit změny (`git commit -am 'Přidána nová funkce'`)
4. Push do branch (`git push origin feature/nova-funkce`)
5. Vytvořte Pull Request

## 📄 Licence

Tento projekt je proprietární software společnosti HelloComp.

## 📞 Kontakt

Pro otázky a podporu kontaktujte HelloComp tým.

---

**Vytvořeno:** 2026-02-05  
**Verze:** 1.0.0  
**Status:** ✅ Production Ready
