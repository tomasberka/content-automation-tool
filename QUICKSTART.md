# Quick Start Guide - HelloComp Category Template Generator

Rychlý průvodce pro začátek práce s generátorem kategoriálního obsahu.

## 🚀 Instalace za 1 minutu

```bash
# 1. Naklonujte repozitář
git clone https://github.com/tomasberka/content-automation-tool.git
cd content-automation-tool

# 2. Nainstalujte závislosti
pip install -r requirements.txt

# 3. Hotovo! Můžete začít používat
```

## 📝 První kroky

### 1. Validace existující kategorie

```bash
python category_template_generator.py docs/seo-texty/graficke-karty-nvidia.md --validate
```

**Výstup:**
```
✅ Veškerý obsah splňuje SEO požadavky
```

### 2. Generování nové kategorie

```bash
python category_template_generator.py --generate-sample "Gaming PC" -o gaming-pc.md
```

**Vytvoří:**
- ✅ Kompletní SEO strukturu (TITLE, META, H1, H2)
- ✅ Úvodní text s hodnotami HelloComp
- ✅ 5 obsahových sekcí
- ✅ ~750 slov optimalizovaných pro SEO

### 3. Převod na HTML

```bash
python category_template_generator.py gaming-pc.md -o gaming-pc.html -f html
```

## 🎯 Nejčastější použití

### Vytvořit novou kategorii "krok za krokem"

```bash
# 1. Generovat vzor
python category_template_generator.py --generate-sample "Herní notebooky" -o herni-notebooky.md

# 2. Upravit v editoru (nano, vim, VS Code...)
nano herni-notebooky.md

# 3. Validovat úpravy
python category_template_generator.py herni-notebooky.md --validate

# 4. Převést na HTML pro web
python category_template_generator.py herni-notebooky.md -o herni-notebooky.html -f html
```

### Validovat všechny kategorie

```bash
for file in docs/seo-texty/*.md; do
    echo "=== $file ==="
    python category_template_generator.py "$file" --validate
done
```

### Export všech kategorií do HTML

```bash
mkdir -p output/html

for file in docs/seo-texty/*.md; do
    if [ "$file" != "docs/seo-texty/README.md" ]; then
        filename=$(basename "$file" .md)
        python category_template_generator.py "$file" -o "output/html/${filename}.html" -f html
    fi
done
```

## 💡 Tipy a triky

### ✅ Co DĚLAT

1. **Vždy začněte validací** - Ujistěte se, že struktura je správná
2. **Používejte vzorové texty** - Ušetří čas při tvorbě nových kategorií
3. **Zachovejte HTML tagy** - Parser je zachová automaticky
4. **Testujte průběžně** - Validujte po každé větší úpravě

### ❌ Co NEDĚLAT

1. **Nemazat povinné sekce** - TITLE, META, H1, úvodní text jsou nutné
2. **Nepřekračovat limity** - TITLE max 60 znaků, META max 160 znaků
3. **Neignorovat varování** - I když nejsou chyby, varování stojí za pozornost

## 🔍 Příklady validačních výstupů

### ✅ Perfektní obsah

```
================================================================================
VALIDAČNÍ VÝSLEDKY
================================================================================

  ✅ Veškerý obsah splňuje SEO požadavky

================================================================================
```

### ⚠️ S varováními (lze publikovat, ale doporučuje se upravit)

```
================================================================================
VALIDAČNÍ VÝSLEDKY
================================================================================

⚠️  VAROVÁNÍ:
  • [title] Title je příliš dlouhý (65 znaků, max 60)
  • [introduction] Úvodní text je příliš krátký (45 slov, min 50)

================================================================================
```

### ❌ S chybami (nutno opravit před publikací)

```
================================================================================
VALIDAČNÍ VÝSLEDKY
================================================================================

❌ CHYBY:
  • [title] Title je povinný a chybí
  • [h1] H1 nadpis je povinný a chybí

================================================================================
```

## 📚 Struktura SEO obsahu

Každá kategorie musí obsahovat:

```markdown
**Title:** Název kategorie – klíčová slova | HelloComp

**Meta description:** Popis kategorie s emoji ⚡ a USP (140-160 znaků)

## Hlavní H1 nadpis kategorie

Úvodní odstavec (50-80 slov) s popisem kategorie...

## Jak vybrat správnou [kategorii]

Obsah první sekce...

## Co zvládne [kategorie]

Obsah druhé sekce...

## Typické konfigurace

Obsah třetí sekce s tabulkou...

## Pro koho je [kategorie] ideální

Cílová skupina...

## Nakupujte s jistotou u HelloComp

CTA sekce s odkazy...
```

## 🛠️ Řešení problémů

### "Soubor neexistuje"

```bash
# Zkontrolujte cestu
ls -la docs/seo-texty/

# Použijte absolutní cestu
python category_template_generator.py /plna/cesta/k/souboru.md
```

### "Konfigurace nenalezena"

```bash
# Ujistěte se, že jste v kořenovém adresáři projektu
cd /path/to/content-automation-tool

# Nebo zadejte cestu ke konfiguraci
python category_template_generator.py input.md -c /path/to/content_structure.yaml
```

### "Encoding error"

```bash
# Ujistěte se, že soubor je v UTF-8
file -i soubor.md

# Případně převeďte
iconv -f ISO-8859-2 -t UTF-8 vstup.md > vystup.md
```

## 🎓 Další kroky

1. **Přečtěte si plnou dokumentaci**: `README_GENERATOR.md`
2. **Prohlédněte si příklady**: Spusťte `python example_integration.py`
3. **Prozkoumejte konfiguraci**: Otevřete `content_structure.yaml`
4. **Upravte si pravidla**: Přizpůsobte validaci svým potřebám

## 📞 Potřebujete pomoc?

- 📖 Dokumentace: `README_GENERATOR.md`
- 🔧 Příklady použití: `example_integration.py`
- ⚙️ Konfigurace: `content_structure.yaml`
- 🐛 Utility funkce: `content_utils.py`

---

**Happy content generating! 🚀**
