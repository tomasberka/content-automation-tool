# HTML Structure Validation

## Přehled

Tento dokument popisuje validaci HTML struktury pro kategoriální obsah na HelloComp.cz.

## Proč je to důležité?

Backend HelloComp.cz má jasná pravidla pro strukturu obsahu každé kategorie:

- **Obsah musí začínat `<p>` tagem** (paragraph/odstavec)
- Backend automaticky vytváří interaktivní tlačítka a vysouvací bloky **za prvním `<p>` elementem**
- Pokud obsah nezačíná `<p>` tagem, backend nemůže správně vložit své komponenty

## Jak to funguje

### 1. Konfigurace

V souboru `content_structure.yaml` je definována HTML struktura:

```yaml
# HTML structure requirements
html_structure:
  must_start_with_p: true  # Content must start with <p> tag
  description: "Backend creates buttons and sliding blocks after first <p> tag"
  allowed_first_tags:
    - p  # Paragraph - required first tag

# Validation levels
validation:
  validate_html_structure: true  # Validate HTML tag structure
```

### 2. Automatické formátování

Metoda `ContentFormatter._format_html_content()` zajišťuje:

- **Plain text** je automaticky zabalen do `<p>` tagů
- **Seznamy** (začínající `-` nebo `*`) jsou převedeny na `<ul><li>` strukturu
- Pokud obsah začíná seznamem, před něj se vloží prázdný `<p></p>` tag
- **Existující HTML** je zachováno, pokud už začíná správně

### 3. Validace

Třída `ContentValidator` kontroluje:

- **Úvodní text (introduction)** musí začínat `<p>` tagem
- **Každá sekce s H2** musí začínat buď `<p>` tagem nebo `<ul>` (seznam)
- Pokud pravidlo není dodrženo, vrací se **ERROR** level

## Příklady

### ✅ Správně - Plain text

**Vstup (Markdown):**
```
Grafické karty NVIDIA představují zlatý standard v herním světě.
```

**Výstup (HTML):**
```html
<p>Grafické karty NVIDIA představují zlatý standard v herním světě.</p>
```

### ✅ Správně - Seznam s prefixem

**Vstup (Markdown):**
```
- První vlastnost
- Druhá vlastnost
- Třetí vlastnost
```

**Výstup (HTML):**
```html
<p></p>
<ul>
    <li>První vlastnost</li>
    <li>Druhá vlastnost</li>
    <li>Třetí vlastnost</li>
</ul>
```

### ✅ Správně - Existující HTML

**Vstup (HTML):**
```html
<p>Text s <strong>důležitými</strong> slovy.</p>
```

**Výstup (HTML):**
```html
<p>Text s <strong>důležitými</strong> slovy.</p>
```

### ❌ Chybně - Začíná nadpisem

**Vstup:**
```html
<h3>Podnadpis</h3>
<p>Text...</p>
```

**Výstup s automatickou opravou:**
```html
<p></p>
<h3>Podnadpis</h3>
<p>Text...</p>
```

## Použití

### CLI validace

```bash
# Validace existujího souboru
python category_template_generator.py moje-kategorie.md --validate

# Generování HTML s validací
python category_template_generator.py moje-kategorie.md -o output.html -f html
```

### Python API

```python
from category_template_generator import (
    CategoryContent,
    ContentValidator,
    ContentFormatter
)

# Vytvoř obsah
content = CategoryContent(
    title="Test",
    meta_description="Test meta description",
    h1="Test H1",
    introduction="Úvodní text začíná správně."
)

# Validuj strukturu
validator = ContentValidator()
results = validator.validate(content)

# Zkontroluj chyby
errors = [r for r in results if r.level == ValidationLevel.ERROR]
if errors:
    print("⚠️ Chyby v HTML struktuře:")
    for error in errors:
        print(f"  - {error.message}")
```

## Testování

Spusť testy HTML struktury:

```bash
python test_html_structure.py
```

Testy kontrolují:
1. Úvodní text začíná `<p>` tagem
2. Sekce začínají `<p>` tagem
3. Seznamy mají `<p>` prefix
4. Plain text je správně formátován
5. Existující HTML je zachován

## Časté otázky (FAQ)

### Proč prázdný `<p></p>` před seznamy?

Backend potřebuje první `<p>` element jako anchor pro vložení svých komponent. Prázdný `<p>` tag slouží jako tento anchor, i když obsah začíná seznamem.

### Co když už mám HTML obsah?

Existující HTML je zachován, pokud je správně strukturován. Pokud začíná `<h1>`, `<div>` nebo jiným non-paragraph tagem, automaticky se před něj vloží `<p></p>`.

### Ovlivní to SEO?

Ne, prázdný `<p>` tag neovlivňuje SEO. Vyhledávače ho ignorují a je využíván pouze pro technické účely backendu.

### Mohu validaci vypnout?

Ano, v `content_structure.yaml` nastav:

```yaml
validation:
  validate_html_structure: false
```

Nedoporučujeme to však, protože backend očekává správnou strukturu.

## Technické detaily

### Struktura validace

1. **ContentParser** - Parsuje Markdown/HTML vstup
2. **ContentValidator** - Validuje strukturu včetně HTML tagů
3. **ContentFormatter** - Formátuje výstup s garancí správné struktury
4. **ValidationResult** - Vrací výsledky s úrovněmi ERROR/WARNING/INFO

### Návratové hodnoty

```python
@dataclass
class ValidationResult:
    section: str              # Název sekce (např. "introduction_html")
    level: ValidationLevel    # ERROR, WARNING, nebo INFO
    message: str              # Popis problému
    actual_value: str         # Aktuální hodnota
    expected_value: str       # Očekávaná hodnota
```

## Související dokumentace

- [QUICKSTART.md](../QUICKSTART.md) - Rychlý start
- [README_GENERATOR.md](../README_GENERATOR.md) - Kompletní dokumentace API
- [content_structure.yaml](../content_structure.yaml) - Konfigurace pravidel

## Verze

- **v1.0** (2026-02-18): První implementace HTML strukture validation
- Vytvořeno pro: HelloComp.cz Multi-Platform Content Strategy 2026
