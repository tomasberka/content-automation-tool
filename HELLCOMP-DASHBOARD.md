# HelloComp.cz - Centralizovaný systém správy a sledování

**Kompletní systém pro správu a sledování výkonnosti portálu www.hellcomp.cz, všech sociálních sítí, dosahu webu a všech dostupných dat na jednom místě**

## 🎯 Co tento systém umožňuje

### ✅ Sledování výkonnosti webu
- Google Analytics 4 integrace
- Návštěvnost webu (visitors, page views)
- Bounce rate a průměrná doba relace
- Konverze a revenue
- Sledování výkonnosti jednotlivých stránek

### ✅ Správa všech sociálních sítí
- **Facebook**: followers, reach, engagement, likes, comments, shares
- **Instagram**: followers, engagement rate, saves, impressions, Reels performance
- **TikTok**: sledování videí a engagement
- **YouTube**: subscribers, views, watch time

### ✅ Centralizované reporty
- Denní reporty
- Týdenní přehledy
- Měsíční hodnocení
- Export do Markdown/JSON formátu
- Srovnání s předchozím obdobím

### ✅ Vše na jednom místě
- Jednotné rozhraní pro všechny platformy
- Automatická synchronizace dat
- Agregované metriky napříč platformami
- Historie dat pro dlouhodobé analýzy

---

## 🚀 Rychlý start

### 1. Instalace

```bash
# Přejděte do složky projektu
cd /home/runner/work/content-automation-tool/content-automation-tool

# Nainstalujte závislosti
pip install -r requirements.txt
```

### 2. Konfigurace

```bash
# Spusťte dashboard poprvé - vytvoří konfigurační soubor
python hellcomp_dashboard.py --overview
```

Tím se vytvoří soubor `dashboard_config.json` s výchozím nastavením:

```json
{
  "website": {
    "url": "https://www.hellcomp.cz",
    "google_analytics": {
      "property_id": "YOUR_GA4_PROPERTY_ID",
      "credentials_path": "ga4_credentials.json"
    }
  },
  "social_media": {
    "facebook": {
      "page_id": "YOUR_FACEBOOK_PAGE_ID",
      "access_token": "YOUR_FACEBOOK_ACCESS_TOKEN"
    },
    "instagram": {
      "account_id": "YOUR_INSTAGRAM_ACCOUNT_ID",
      "access_token": "YOUR_INSTAGRAM_ACCESS_TOKEN"
    }
  },
  "reporting": {
    "default_period_days": 30,
    "export_directory": "./reports",
    "auto_export": true
  }
}
```

**⚠️ Důležité:** Aktualizujte konfiguraci s vašimi skutečnými přihlašovacími údaji a ID.

### 3. Základní použití

```bash
# Zobrazit přehled dashboardu
python hellcomp_dashboard.py --overview

# Synchronizovat data ze všech platforem (posledních 30 dní)
python hellcomp_dashboard.py --sync

# Synchronizovat data za konkrétní období
python hellcomp_dashboard.py --sync --start-date 2026-02-01 --end-date 2026-02-19

# Vygenerovat denní report
python hellcomp_dashboard.py --report daily

# Vygenerovat týdenní report
python hellcomp_dashboard.py --report weekly

# Vygenerovat měsíční report
python hellcomp_dashboard.py --report monthly

# Exportovat report do souboru
python hellcomp_dashboard.py --report weekly --export
```

---

## 📊 Detailní dokumentace

### Analytics Manager API

Modul `analytics_manager.py` poskytuje Python API pro práci s metrikami:

```python
from analytics_manager import AnalyticsManager, Platform, MetricType

# Inicializace
manager = AnalyticsManager()

# Přidání metriky
manager.add_metric(
    platform=Platform.WEBSITE,
    metric_type=MetricType.VISITORS,
    value=1250,
    date="2026-02-19"
)

# Získání statistik pro platformu
stats = manager.get_platform_stats(
    platform=Platform.FACEBOOK,
    start_date="2026-02-01",
    end_date="2026-02-19"
)

# Generování reportu
report = manager.generate_report(
    start_date="2026-02-01",
    end_date="2026-02-19",
    output_format='markdown'
)
print(report)

# Export dat
manager.export_to_json('metrics_export.json')

# Import dat
manager.import_from_json('metrics_export.json')
```

### Podporované platformy

```python
Platform.WEBSITE       # www.hellcomp.cz
Platform.FACEBOOK      # Facebook stránka
Platform.INSTAGRAM     # Instagram účet
Platform.TIKTOK        # TikTok profil
Platform.YOUTUBE       # YouTube kanál
Platform.GOOGLE_ADS    # Google Ads kampaně
Platform.FACEBOOK_ADS  # Facebook Ads kampaně
```

### Podporované metriky

```python
# Webové metriky
MetricType.VISITORS           # Návštěvníci
MetricType.PAGE_VIEWS         # Zobrazení stránek
MetricType.BOUNCE_RATE        # Bounce rate (%)
MetricType.AVG_SESSION        # Průměrná doba relace (sec)
MetricType.CONVERSIONS        # Konverze
MetricType.REVENUE            # Tržby (Kč)

# Social media metriky
MetricType.FOLLOWERS          # Sledující/fans
MetricType.ENGAGEMENT         # Engagement rate (%)
MetricType.REACH              # Dosah
MetricType.IMPRESSIONS        # Zobrazení
MetricType.CLICKS             # Kliknutí
MetricType.SHARES             # Sdílení
MetricType.SAVES              # Uložení (Instagram)
MetricType.COMMENTS           # Komentáře
MetricType.LIKES              # Lajky
```

---

## 🔧 Pokročilé nastavení

### Google Analytics 4 integrace

1. **Vytvoření Service Account**:
   - Přejděte na [Google Cloud Console](https://console.cloud.google.com)
   - Vytvořte nový projekt nebo vyberte existující
   - Povolte "Google Analytics Data API"
   - Vytvořte Service Account
   - Stáhněte JSON klíč a uložte jako `ga4_credentials.json`

2. **Přidání přístupu v GA4**:
   - V Google Analytics přejděte na Admin → Property Access Management
   - Přidejte Service Account email s rolí "Viewer"

3. **Aktualizace konfigurace**:
   ```json
   "google_analytics": {
     "property_id": "123456789",
     "credentials_path": "ga4_credentials.json"
   }
   ```

### Facebook/Instagram integrace

1. **Vytvoření Facebook App**:
   - Přejděte na [Facebook Developers](https://developers.facebook.com)
   - Vytvořte novou aplikaci
   - Přidejte produkt "Facebook Login"
   - Získejte Page Access Token

2. **Instagram Business Account**:
   - Propojte Instagram účet s Facebook stránkou
   - Použijte stejný Access Token jako pro Facebook

3. **Aktualizace konfigurace**:
   ```json
   "facebook": {
     "page_id": "YOUR_PAGE_ID",
     "access_token": "YOUR_LONG_LIVED_TOKEN"
   },
   "instagram": {
     "account_id": "YOUR_IG_BUSINESS_ACCOUNT_ID",
     "access_token": "YOUR_LONG_LIVED_TOKEN"
   }
   ```

**Tip:** Pro získání long-lived tokenu použijte [Access Token Debugger](https://developers.facebook.com/tools/debug/accesstoken/).

---

## 📈 Příklady použití

### Příklad 1: Manuální přidání metrik

```python
from hellcomp_dashboard import HelloCompDashboard

dashboard = HelloCompDashboard()

# Přidat dnešní metriky z Facebooku
dashboard.add_manual_metric(
    platform='facebook',
    metric_type='followers',
    value=2350
)

dashboard.add_manual_metric(
    platform='facebook',
    metric_type='reach',
    value=8500
)

# Přidat metriky z Instagramu
dashboard.add_manual_metric(
    platform='instagram',
    metric_type='engagement',
    value=5.8
)

# Vygenerovat report
report = dashboard.generate_daily_report()
print(report)
```

### Příklad 2: Automatická synchronizace a export

```python
from hellcomp_dashboard import HelloCompDashboard
import datetime

dashboard = HelloCompDashboard()

# Synchronizovat data za poslední týden
end_date = datetime.date.today().isoformat()
start_date = (datetime.date.today() - datetime.timedelta(days=7)).isoformat()

dashboard.sync_all_platforms(start_date, end_date)

# Vygenerovat a exportovat týdenní report
dashboard.export_reports(period='weekly')
```

### Příklad 3: Porovnání období

```python
from analytics_manager import AnalyticsManager, Platform

manager = AnalyticsManager()

# Získat statistiky pro tento měsíc
current_stats = manager.get_platform_stats(
    Platform.WEBSITE,
    start_date='2026-02-01',
    end_date='2026-02-28'
)

# Získat statistiky pro minulý měsíc
previous_stats = manager.get_platform_stats(
    Platform.WEBSITE,
    start_date='2026-01-01',
    end_date='2026-01-31'
)

# Porovnat
print("Změna návštěvnosti:")
current_visitors = current_stats.metrics.get('visitors', 0)
previous_visitors = previous_stats.metrics.get('visitors', 0)
change = ((current_visitors - previous_visitors) / previous_visitors) * 100
print(f"{change:+.1f}%")
```

---

## 📋 Denní checklist pro správu dat

### Ranní rutina (30 minut)
- [ ] Spustit synchronizaci dat: `python hellcomp_dashboard.py --sync`
- [ ] Vygenerovat denní report: `python hellcomp_dashboard.py --report daily`
- [ ] Zkontrolovat klíčové metriky (návštěvnost, konverze, engagement)
- [ ] Zaznamenat anomálie nebo významné změny

### Týdenní review (každé pondělí, 1 hodina)
- [ ] Vygenerovat týdenní report: `python hellcomp_dashboard.py --report weekly --export`
- [ ] Analyzovat trendy napříč platformami
- [ ] Identifikovat nejúspěšnější content
- [ ] Naplánovat content na další týden

### Měsíční hodnocení (první pracovní den v měsíci, 2 hodiny)
- [ ] Vygenerovat měsíční report: `python hellcomp_dashboard.py --report monthly --export`
- [ ] Porovnat s předchozím měsícem
- [ ] Vyhodnotit plnění KPI
- [ ] Připravit prezentaci pro stakeholdery

---

## 🎯 KPI a cílové hodnoty

### Website (www.hellcomp.cz)
- **Návštěvnost**: > 30,000 návštěvníků/měsíc
- **Konverzní poměr**: > 1.5%
- **Bounce rate**: < 60%
- **Průměrná doba na stránce**: > 2 minuty

### Facebook
- **Followers growth**: +5% měsíčně
- **Engagement rate**: > 3%
- **Reach**: > 50,000 uživatelů/měsíc
- **Post frequency**: 3-5x týdně

### Instagram
- **Followers growth**: +8% měsíčně
- **Engagement rate**: > 5%
- **Saves**: > 100/příspěvek (quality content)
- **Reels views**: > 5,000/video

---

## 🛠️ Troubleshooting

### Problém: "Cannot connect to Google Analytics"
**Řešení:**
1. Zkontrolujte, že `ga4_credentials.json` existuje
2. Ověřte property_id v konfiguraci
3. Ujistěte se, že je povoleno Google Analytics Data API
4. Zkontrolujte přístupová práva Service Accountu

### Problém: "Facebook Access Token expired"
**Řešení:**
1. Access tokeny expirují po 60 dnech
2. Vygenerujte nový long-lived token
3. Aktualizujte `dashboard_config.json`

### Problém: "No data available"
**Řešení:**
1. Spusťte sync: `python hellcomp_dashboard.py --sync`
2. Zkontrolujte, že jsou správně nastavené přihlašovací údaje
3. Ověřte datum synchronizace

---

## 📚 Další zdroje

### Dokumentace API
- [Google Analytics Data API](https://developers.google.com/analytics/devguides/reporting/data/v1)
- [Facebook Graph API](https://developers.facebook.com/docs/graph-api/)
- [Instagram Graph API](https://developers.facebook.com/docs/instagram-api/)

### Interní dokumentace
- [Facebook & Instagram Strategie 2026](docs/facebook-instagram-strategie-2026.md)
- [Social Media Quick Reference](docs/social-media-quick-reference.md)
- [Denní průvodce prací](DENNI-PRUVODCE-PRACI.md)

### Podpora
Pro technickou podporu nebo dotazy kontaktujte: hello@hellcomp.cz

---

## 🔒 Bezpečnost

### ⚠️ DŮLEŽITÉ
- **NIKDY** necommitujte `dashboard_config.json` s reálnými přihlašovacími údaji
- Přidejte do `.gitignore`:
  ```
  dashboard_config.json
  ga4_credentials.json
  *_token.json
  reports/
  ```
- Používejte environment variables pro citlivé údaje v produkci
- Pravidelně obnovujte access tokeny

---

**Vytvořeno:** 2026-02-19  
**Verze:** 1.0  
**Status:** ✅ Ready for Use  
**Licence:** Proprietární - HelloComp © 2026
