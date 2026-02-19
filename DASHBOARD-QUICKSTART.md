# HelloComp.cz Dashboard - Rychlý start

**5minutový průvodce spuštěním centralizovaného systému správy a sledování**

## Co tento systém dělá?

✅ Sleduje výkonnost www.hellcomp.cz  
✅ Monitoruje všechny sociální sítě (Facebook, Instagram, TikTok, YouTube)  
✅ Agreguje všechna data na jednom místě  
✅ Generuje automatické reporty  
✅ Umožňuje srovnání období  

---

## Krok 1: Instalace (2 minuty)

```bash
# Nainstalujte závislosti
pip install -r requirements.txt
```

---

## Krok 2: První spuštění (1 minuta)

```bash
# Zobrazit přehled dashboardu
python hellcomp_dashboard.py --overview
```

Tím se vytvoří konfigurační soubor `dashboard_config.json`.

---

## Krok 3: Konfigurace (5-30 minut)

### Rychlá varianta (testování)
Můžete začít ihned přidávat metriky manuálně, bez nastavení API:

```bash
# Spustit Python interaktivně
python
```

```python
from hellcomp_dashboard import HelloCompDashboard

dashboard = HelloCompDashboard()

# Přidat dnes metriky
dashboard.add_manual_metric('website', 'visitors', 1250)
dashboard.add_manual_metric('website', 'conversions', 15)
dashboard.add_manual_metric('facebook', 'followers', 2350)
dashboard.add_manual_metric('instagram', 'engagement', 5.8)

# Vygenerovat report
print(dashboard.generate_daily_report())
```

### Plná varianta (s API integrací)
Upravte `dashboard_config.json` s reálnými přihlašovacími údaji:

1. **Google Analytics 4** (návod v [HELLCOMP-DASHBOARD.md](HELLCOMP-DASHBOARD.md))
2. **Facebook/Instagram** (návod v [HELLCOMP-DASHBOARD.md](HELLCOMP-DASHBOARD.md))
3. Ostatní platformy podle potřeby

---

## Krok 4: Základní použití

### Zobrazit přehled
```bash
python hellcomp_dashboard.py --overview
```

### Vygenerovat denní report
```bash
python hellcomp_dashboard.py --report daily
```

### Vygenerovat týdenní report
```bash
python hellcomp_dashboard.py --report weekly
```

### Export reportu do souboru
```bash
python hellcomp_dashboard.py --report weekly --export
```
Soubor se uloží do složky `./reports/`

---

## Příklad výstupu

```markdown
# HelloComp.cz Analytics Report

**Period:** 2026-02-19 to 2026-02-19

## Website

| Metric | Value |
|--------|-------|
| Visitors | 1250.00 |
| Page Views | 3420.00 |
| Conversions | 15.00 |
| Revenue | 45000.00 |

## Facebook

| Metric | Value |
|--------|-------|
| Followers | 2350.00 |
| Engagement Rate | 4.20 |
| Reach | 8500.00 |

## Instagram

| Metric | Value |
|--------|-------|
| Followers | 3200.00 |
| Engagement Rate | 5.80 |
| Saves | 145.00 |
```

---

## Denní workflow

### Každé ráno (10 minut)
```bash
# 1. Synchronizovat data (pokud máte nastavené API)
python hellcomp_dashboard.py --sync

# 2. Vygenerovat denní report
python hellcomp_dashboard.py --report daily

# 3. Zkontrolovat klíčové metriky
```

### Každé pondělí (30 minut)
```bash
# Vygenerovat a exportovat týdenní report
python hellcomp_dashboard.py --report weekly --export

# Analyzovat trendy a naplánovat content
```

### První den v měsíci (1 hodina)
```bash
# Vygenerovat měsíční report
python hellcomp_dashboard.py --report monthly --export

# Vyhodnotit KPI a připravit prezentaci
```

---

## Tipy pro začátečníky

### 1. Začněte s manuálním zadáváním
Není nutné hned nastavovat všechna API. Začněte přidávat metriky ručně:

```python
from hellcomp_dashboard import HelloCompDashboard
import datetime

dashboard = HelloCompDashboard()

# Dnes
today = datetime.date.today().isoformat()
dashboard.add_manual_metric('website', 'visitors', 1250, today)

# Včera
yesterday = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
dashboard.add_manual_metric('website', 'visitors', 1180, yesterday)

# Vygenerovat report
print(dashboard.generate_daily_report())
```

### 2. Exportujte data pravidelně
```bash
# Exportovat všechna data do JSON
python -c "
from analytics_manager import AnalyticsManager
manager = AnalyticsManager()
# ... přidejte metriky ...
manager.export_to_json('backup_data.json')
"
```

### 3. Používejte šablonu konfigurace
Zkopírujte a upravte:
```bash
cp dashboard_config.example.json dashboard_config.json
# Pak upravte v editoru
```

---

## Další kroky

📚 **Detailní dokumentace**: [HELLCOMP-DASHBOARD.md](HELLCOMP-DASHBOARD.md)  
🎯 **Social Media strategie**: [docs/facebook-instagram-strategie-2026.md](docs/facebook-instagram-strategie-2026.md)  
✅ **Denní checklist**: [DENNI-CHECKLIST.md](DENNI-CHECKLIST.md)  

---

## Potřebujete pomoc?

**Časté problémy:**
- "No module named 'analytics_manager'" → Spusťte z hlavní složky projektu
- "Configuration file not found" → První spuštění vytvoří konfiguraci automaticky
- "Cannot connect to API" → Zkontrolujte přihlašovací údaje v `dashboard_config.json`

**Podpora:** hello@hellcomp.cz

---

**Vytvořeno:** 2026-02-19  
**Čas na zprovoznění:** ~5 minut  
**Obtížnost:** ⭐⭐☆☆☆ (Snadné)
