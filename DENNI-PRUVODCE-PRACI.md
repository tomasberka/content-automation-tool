# 🚀 Denní průvodce prací - HelloComp Multi-Role Position

**Kompletní návod pro SEO specialistu, content creatora, copywritera a správce sociálních sítí**

---

## 📋 Obsah

1. [Denní harmonogram](#denní-harmonogram)
2. [SEO Specialist - Denní workflow](#seo-specialist---denní-workflow)
3. [Content Creator - Tvorba obsahu](#content-creator---tvorba-obsahu)
4. [Copywriter - Psaní textů](#copywriter---psaní-textů)
5. [Správce sociálních sítí](#správce-sociálních-sítí)
6. [Týdenní plán](#týdenní-plán)
7. [Měsíční checklist](#měsíční-checklist)
8. [Jak se zlepšovat](#jak-se-zlepšovat)
9. [Maximalizace výkonu](#maximalizace-výkonu)
10. [Nástroje a zdroje](#nástroje-a-zdroje)

---

## ⏰ Denní harmonogram

### 🌅 Ráno (8:00 - 10:00) - Start a Analytics

**Priorita: Komunikace a monitoring**

- [ ] **08:00-08:30** - Kontrola emailů a zpráv
  - Odpověz na urgentní emaily
  - Zkontroluj Slack/interní komunikaci
  - Přečti si notifications z Google Analytics a Search Console

- [ ] **08:30-09:00** - Social Media Check
  - Odpověz na všechny komentáře z noci (FB, IG)
  - Zkontroluj a odpověz na DM (do 1 hodiny!)
  - Check trending topics v gaming komunitě

- [ ] **09:00-09:30** - Analytics & SEO Monitoring
  - Google Analytics: Včerejší výkon
  - Google Search Console: Nové chyby, pozice, CTR
  - Ranking check pro hlavní klíčová slova
  - Zaznamenej anomálie nebo zajímavé trendy

- [ ] **09:30-10:00** - Plánování dne
  - Zkontroluj content kalendář na dnes
  - Prioritizuj úkoly podle důležitosti
  - Připrav si materiály na dnešní content

### ☀️ Dopoledne (10:00 - 12:30) - Deep Work (Tvorba obsahu)

**Priorita: Hlavní tvůrčí práce**

- [ ] **10:00-12:30** - Content Creation Block
  - **SEO texty:** Vytvoř/aktualizuj 1-2 kategoriální texty
  - **Blog články:** Napiš nebo dokončuj článek (500-1000 slov)
  - **Product descriptions:** Optimalizuj popisy produktů
  - **Validace:** Použij `category_template_generator.py --validate`

**Tip:** Tohle je tvůj "flow state" čas. Vypni notifikace, používej Pomodoro (25 min práce, 5 min pauza).

### 🍽️ Polední pauza (12:30 - 13:30)

- Oběd a odpočinek
- Light social media engagement (5-10 min)

### 🌤️ Odpoledne (13:30 - 17:00) - Sociální sítě a operativa

**Priorita: Social media a publikování**

- [ ] **13:30-14:30** - Social Media Content Creation
  - Připrav Reel/video na dnes (editace, titulky)
  - Vytvoř 2-3 Stories
  - Připrav carousel nebo static post (pokud plánováno)

- [ ] **14:30-15:00** - SEO technická práce
  - Oprav chyby ze Search Console
  - Aktualizuj meta descriptions/titles podle potřeby
  - Kontrola a oprava broken links
  - Internal linking - přidej odkazy mezi souvisejícími kategoriemi

- [ ] **15:00-16:00** - Copywriting úkoly
  - Email marketing copy
  - Landing pages
  - Call-to-action optimalizace
  - A/B testing varianty

- [ ] **16:00-17:00** - Publikování a engagement
  - **16:45-17:00:** Publikuj hlavní Reel (17:00 = prime time!)
  - Engage s gaming komunitou (like, comment na relevantní obsah)
  - Sdílej do FB skupin (hodnotu, ne spam)

### 🌆 Večer (17:00 - 18:00) - Wrap-up a plánování

**Priorita: Dokončení a příprava na zítra**

- [ ] **17:00-17:30** - Admin a organizace
  - Odpověz na nové komentáře na social media
  - Zkontroluj, co se povedlo dnes dokončit
  - Aktualizuj content kalendář

- [ ] **17:30-18:00** - Plánování na zítra
  - Co musím vytvořit zítra?
  - Připrav si podklady a researche na zítra
  - Quick analytics check (jak jde dnešní Reel?)
  - Stories update (3-5x denně celkem)

---

## 🔍 SEO Specialist - Denní workflow

### Každý den musíš

1. **Monitoring (15-30 min)**
   ```bash
   # Kontroluj:
   - Google Search Console - chyby, pozice, CTR
   - Google Analytics - traffic, bounce rate, konverze
   - Ranking tools - pozice hlavních klíčových slov
   - Konkurence - co dělají, kde rankují
   ```

2. **Technické SEO (30-60 min)**
   ```bash
   # Úkoly:
   - Oprava 404 chyb
   - Kontrola site speed (PageSpeed Insights)
   - Mobile-friendliness check
   - Strukturovaná data (Schema.org)
   - XML sitemap aktualizace
   ```

3. **On-page SEO (60-120 min)**
   ```bash
   # Optimalizace:
   - Meta titles (30-60 znaků)
   - Meta descriptions (140-160 znaků)
   - H1, H2, H3 struktura
   - Internal linking
   - Image alt texts
   - URL struktura
   ```

### Validace SEO textu pomocí nástroje

```bash
# Validace existující kategorie
python category_template_generator.py docs/seo-texty/graficke-karty-nvidia.md --validate

# Co kontroluje:
✅ TITLE (30-60 znaků)
✅ META description (140-160 znaků)
✅ H1 nadpis
✅ Úvodní text (50-80 slov)
✅ Minimálně 3 H2 sekce
✅ Celkový obsah (600-900 slov)
```

### Keyword Research proces

1. **Najdi příležitosti**
   - Google Search Console → "Queries" s pozicí 11-20
   - Konkurence: Ahrefs/SEMrush gap analysis
   - Google Autocomplete a "People also ask"

2. **Analyzuj intent**
   - Informační (jak vybrat...)
   - Transakční (koupit, cena...)
   - Navigační (HelloComp...)

3. **Vytvoř content brief**
   - Hlavní klíčové slovo
   - LSI keywords (související)
   - Konkurenční analýza top 3 výsledků
   - Content struktura (H2, H3)

### SEO Checklist pro novou stránku

- [ ] Keyword research hotový
- [ ] Content brief vytvořen
- [ ] TITLE optimalizován (30-60 znaků, keyword na začátku)
- [ ] META description atraktivní (140-160 znaků, obsahuje CTA)
- [ ] H1 obsahuje hlavní keyword
- [ ] H2/H3 struktura logická
- [ ] Minimálně 600 slov (ideálně 800-1200)
- [ ] 3-5 internal links na související stránky
- [ ] 1-2 external links na autoritativní zdroje
- [ ] Images optimalizované (alt text, compressed)
- [ ] Mobile-friendly ověřeno
- [ ] Page speed OK (<3s load time)
- [ ] Schema.org markup přidán (Product, FAQ, BreadcrumbList)

---

## 🎨 Content Creator - Tvorba obsahu

### Obsahová strategie: "Show, Don't Just Sell"

Jako content creator pro HelloComp tvořit **autentický, hodnotný obsah** který:
1. Vzdělává zákazníky
2. Buduje důvěru
3. Ukazuje expertizu
4. Přirozeně vede k prodeji

### Typy obsahu a frekvence

| Typ obsahu | Frekvence | Čas na přípravu | Priorita |
|------------|-----------|-----------------|----------|
| **Blog článek** | 2-3x týdně | 2-3h | ⭐⭐⭐⭐⭐ |
| **SEO kategoriální text** | 1-2x týdně | 1-2h | ⭐⭐⭐⭐⭐ |
| **Reels/Video** | 1x denně | 1-2h | ⭐⭐⭐⭐⭐ |
| **Carousel (IG)** | 2-3x týdně | 30-45 min | ⭐⭐⭐⭐ |
| **Stories** | 3-5x denně | 5-10 min | ⭐⭐⭐⭐ |
| **Product description** | Průběžně | 15-20 min/ks | ⭐⭐⭐ |
| **Email newsletter** | 1x týdně | 1h | ⭐⭐⭐ |

### Blog článek - Workflow

**1. Research (30 min)**
```
- Keyword research (Ahrefs, Google Trends)
- Konkurenční analýza (top 3 výsledky v Google)
- Co už máme napsané na toto téma?
- Jaké otázky pokládají lidé? (People also ask, Reddit, Facebook skupiny)
```

**2. Outline (15 min)**
```
- H1: Hlavní titulek (keyword na začátku)
- Intro (2-3 odstavce, hook)
- H2: Hlavní sekce (3-5 sekcí)
  - H3: Podsekce
- Závěr + CTA
```

**3. Psaní (90-120 min)**
```
- First draft - jen piš, neupravuj
- Optimální délka: 800-1500 slov
- Používej bullet points, tabulky, zvýraznění
- Přidej příklady a konkrétní čísla
```

**4. Optimalizace (30 min)**
```
- SEO check (keyword density 1-2%)
- Internal linking (3-5 odkazů)
- Meta description atraktivní
- Featured image (16:9, optimalizovaný)
- Alt texty u obrázků
```

**5. Publikace a promotion (15 min)**
```
- Publikuj na blog
- Sdílej na social media
- Email newsletter (pokud relevant)
- Pošli na Slack/tým
```

### Video/Reels - Production Workflow

**Témata, která fungují:**
- Stavby PC (ASMR, timelapsy)
- Benchmarky (kolik FPS dá CS2 na této sestavě)
- Rychlé tipy (jak zrychlit Windows)
- Edukační obsah (jak vybrat GPU, CPU...)
- Behind the scenes
- Rozbalování nových produktů

**Produkční proces:**

1. **Plánování (10 min)**
   - Co natočím? (téma)
   - Jaký bude hook? (první 3 sekundy)
   - Jaký bude CTA? (link v bio, komentuj...)

2. **Natáčení (20-30 min)**
   - Telefon + tripod nebo gimbal
   - Světlo! (přirozené nebo ring light)
   - Audio důležitější než obraz (lav mic nebo blízko)
   - Natoč víc, než potřebuješ

3. **Editace (30-60 min)**
   - CapCut nebo Adobe Premiere Rush
   - Dynamický střih každé 2-3 sekundy
   - **Titulky!** (80% lidí kouká bez zvuku)
   - Trending audio (zvýší dosah)
   - Call to action na konci

4. **Publikace**
   - Instagram Reels: 17:00 (prime time)
   - Facebook Reels: Stejně
   - TikTok: 17:00 nebo 21:00
   - YouTube Shorts: kdykoliv

**Video šablony (Copy-Paste skripty)**

```
ŠABLONA 1: Benchmark Video
HOOK (0-3s): "Tohle PC stojí 25 000 Kč. Kolik FPS myslíš, že dá?"
BODY (3-45s): Ukázka benchmarku, FPS counter na obrazovce
CLOSE (45-60s): "Link v BIO pro tuto sestavu. Co bys na tom hrál?"

ŠABLONA 2: Edukační Reel
HOOK: "3 věci, které MUSÍŠ vědět před koupí GPU"
BODY: Point 1, Point 2, Point 3 (vizuální, rychlé)
CLOSE: "Follow pro víc tipů. Co tě zajímá příště?"

ŠABLONA 3: PC Build Timelapse
HOOK: "Stavíme PC za 30k od nuly"
BODY: Timelapse stavby (2-3 minuty → 30 sekund)
CLOSE: "Výsledek? 200 FPS v CS2. Detaily v komentáři"
```

### Content Calendar - Týdenní plán

| Den | Blog/SEO | Social Media | Email |
|-----|----------|--------------|-------|
| **Po** | Keyword research + outline | Reel + Stories | - |
| **Út** | Psaní článku | Carousel + Stories | - |
| **St** | Dokončení + publikace | Reel + Stories | - |
| **Čt** | SEO text kategorie | Reel + Stories | Newsletter draft |
| **Pá** | SEO optimalizace stávajícího | Reel + Stories | Publikace newsletteru |
| **So** | - | Reel + Stories (lehčí obsah) | - |
| **Ne** | Plánování na příští týden | Stories | - |

---

## ✍️ Copywriter - Psaní textů

### Copywriting pravidla pro HelloComp

**1. Know Your Audience**
- Primární: Muži 18-35, hráči, tech-savvy
- Sekundární: Rodiče kupující PC dětem
- Terciární: Firmy, profesionálové

**2. Tone of Voice**
```
✅ DO: Přátelský, odborný, autentický
✅ DO: "Víme, co potřebuješ. Sestavíme ti to."
✅ DO: Používej "ty", ne "vy"

❌ DON'T: Příliš formální
❌ DON'T: Tech jargon bez vysvětlení
❌ DON'T: Prázdné fráze ("nejlepší kvalita", "špičkové služby")
```

**3. Copywriting formule**

**AIDA Model** (Classic)
```
A - Attention (upoutej pozornost)
I - Interest (vzbuď zájem)
D - Desire (vytvoř touhu)
A - Action (vyzvi k akci)
```

**PAS Model** (Pro pain points)
```
P - Problem (problém)
A - Agitate (rozviř, zhoř)
S - Solution (řešení)
```

**BAB Model** (Before-After-Bridge)
```
B - Before (jak to je teď)
A - After (jak by to mohlo být)
B - Bridge (jak se tam dostaneš)
```

### Copywriting šablony

**Product Description šablona:**
```markdown
# [Název produktu] - [Hlavní benefit]

[Odstavec 1: Hook + hlavní benefit]
Potřebuješ [řešení problému]? [Produkt] ti [benefit] díky [feature].

[Odstavec 2: Features + Benefits]
- **[Feature 1]:** [Benefit]
- **[Feature 2]:** [Benefit]
- **[Feature 3]:** [Benefit]

[Odstavec 3: Social proof]
Stovky spokojených zákazníků [konkrétní výsledek].

[CTA]
👉 [Akční CTA tlačítko]
```

**Call-to-Action (CTA) příklady:**
```
Silné CTAs:
✅ "Začni teď – postav si PC na míru"
✅ "Zjisti, které PC je pro tebe"
✅ "Objednej do 24h a získej dopravu zdarma"

Slabé CTAs:
❌ "Klikni zde"
❌ "Více informací"
❌ "Odeslat"
```

**Email copywriting šablona:**
```
Subject line (35-50 znaků):
"[Benefit] za [cena/čas] – [urgence]"
Příklad: "RTX 4070 PC za 35k – pouze tento týden"

Preview text (40-100 znaků):
Upřesni benefit nebo přidej social proof

Tělo emailu:
[Personalizace] Ahoj [jméno],

[Hook - 1 věta proč čteš tento email]

[Benefit paragraf - co z toho máš]

[Features - 3 bullets]

[Social proof - "Už 500+ lidí..."]

[CTA - jasné, výrazné]

[P.S. - Urgence nebo bonus]
```

### Landing page struktura

**Above the fold:**
1. **Headline:** Hlavní benefit (6-12 slov)
2. **Subheadline:** Rozšíření benefitu (10-20 slov)
3. **Hero image/video:** Vizualizace produktu
4. **CTA button:** Primární akce

**Below the fold:**
5. **Benefits section:** 3-5 hlavních benefitů s ikonami
6. **How it works:** 3-4 kroky procesu
7. **Social proof:** Recenze, počet zákazníků, hodnocení
8. **Features:** Detailní funkce produktu
9. **FAQ:** 5-8 nejčastějších otázek
10. **Final CTA:** Opakování hlavního CTA

---

## 📱 Správce sociálních sítí

### Platforma strategie

**Instagram (Priorita #1)**
- **Cílová skupina:** 18-35 let, hráči, tech enthusiasté
- **Hlavní formát:** Reels (90% dosahu)
- **Frekvence:** 1 Reel denně + 3-5 Stories
- **Best time to post:** 17:00-18:00

**Facebook (Priorita #2)**
- **Cílová skupina:** 30-50 let, rodiče, firmy
- **Hlavní formát:** Video + text
- **Frekvence:** 1 post denně + sdílení do skupin
- **Best time to post:** 12:00-13:00 nebo 19:00-20:00

**TikTok (Priorita #3)**
- **Cílová skupina:** 16-25 let, Gen Z
- **Hlavní formát:** Short videos, trendy
- **Frekvence:** 1-2 videa denně
- **Best time to post:** 17:00 nebo 21:00

### Social Media denní checklist

**Ráno (9:00-10:00)**
- [ ] Odpověz na všechny komentáře z noci (odpověď do 12h!)
- [ ] Zkontroluj a odpověz na DM (odpověď do 1h!)
- [ ] Sdílej 2-3 Stories (behind the scenes, produkty, tipy)
- [ ] Check trending topics v gaming komunitě

**Odpoledne (15:00-17:00)**
- [ ] Publikuj hlavní Reel (17:00 = prime time)
- [ ] Engage s konkurencí a komunitou
  - Likuj 20-30 postů z gaming komunitě
  - Komentuj 5-10 relevantních postů (hodnotně!)
  - Odpověz na nové komentáře
- [ ] Sdílej do FB skupin (hodnotu, ne spam!)

**Večer (20:00-21:00)**
- [ ] Stories update (2-3x)
- [ ] Odpověz na komentáře z odpoledne
- [ ] Quick analytics check (jak jde dnešní obsah?)
- [ ] Plán na zítra (jaké video, jaké téma)

### Content plánování

**Týdenní content mix:**
- 40% Edukační (tipy, how-to, vysvětlení)
- 30% Produktový (showcases, benchmarky)
- 20% Entertainment (memes, trendy, relatable)
- 10% Prodejní (akce, slevy, CTA)

**Content pilíře:**
1. **Edukace:** "Jak vybrat GPU", "5 chyb při stavbě PC"
2. **Showcase:** "Nová RTX 4070 v akci", "PC za 25k benchmark"
3. **Behind the scenes:** "Stavíme PC pro zákazníka"
4. **Community:** "Co vy hrajete?", "Tag kamaráda, co potřebuje nový PC"
5. **Trendy:** Aktuální herní novinky, hardware launches

### Engagement strategie

**Jak budovat komunitu:**

1. **Odpovídej rychle a autenticky**
   ```
   ❌ "Díky za komentář!"
   ✅ "Dobrá otázka! RTX 4060 Ti je lepší na 1080p, RTX 4070 na 1440p. Co plánuješ hrát?"
   ```

2. **Ptej se na konci postů**
   ```
   "Co vy hrajete teď?"
   "Jaký je váš budget na PC?"
   "RTX nebo Radeon? Proč?"
   ```

3. **Používej polls a quizy ve Stories**
   ```
   "Kolik FPS myslíš, že dá toto PC?"
   "AMD nebo Intel? Hlasuj!"
   "Quiz: Poznáš GPU podle vzhledu?"
   ```

4. **UGC (User Generated Content)**
   ```
   "Pošli foto svého setupu – nejlepší zveřejníme!"
   "Tag nás v tvém novém PC – repostneme!"
   ```

5. **Kolaborace s mikro-influencery**
   - Gaming komunita
   - Tech revieweři
   - Streamers (lokální)

### Hashtag strategie

**Instagram Hashtags (9-12 per post):**

Velké (100k+):
```
#gaming #gamingpc #pcgaming #gamingsetup #pcbuild
```

Střední (10k-100k):
```
#heřnípc #gamingczech #czechgaming #pcbuilder #gamingcommunity
```

Malé (<10k):
```
#hellocomp #prahapc #ceskegaming #pcstavba #hernipoč
```

**Tip:** Rotate hashtags, nepoužívej pořád stejné (Instagram shadowban)

### Analytics co sledovat

**Každý den:**
- Reach a impressions (rostou?)
- Engagement rate (likes + comments + shares / followers)
- Best performing post (co fungovalo?)

**Každý týden:**
- Follower growth (net new followers)
- Stories views trend
- Save rate (ukazatel kvality)

**Každý měsíc:**
- Audience demographics (jsou to naši lidé?)
- Best performing content types (double down)
- Conversion rate (social → web → prodej)

**KPIs (Key Performance Indicators):**
```
📊 Follower growth: +5-10% měsíčně
📊 Engagement rate: >3%
📊 Reach rate: >20% followers
📊 Click-through rate (link in bio): >2%
📊 Conversion rate (web → purchase): >1%
```

---

## 📅 Týdenní plán

### Pondělí - Research & Planning

**Dopoledne:**
- [ ] Keyword research pro nový obsah
- [ ] Konkurenční analýza (co dělají ostatní?)
- [ ] Content brainstorming (témata na tento týden)
- [ ] Social media trends check (co je teď hot?)

**Odpoledne:**
- [ ] Vytvoř content calendar na týden
- [ ] Připrav outlines pro blog články
- [ ] Naplánuj social media posty (scheduling tool)
- [ ] SEO audit 1-2 starších stránek

### Úterý - Content Creation Day 1

**Dopoledne:**
- [ ] Piš blog článek nebo SEO text (deep work)
- [ ] Validace pomocí `category_template_generator.py`

**Odpoledne:**
- [ ] Natoč Reel/video na dnes
- [ ] Připrav carousel pro Instagram
- [ ] Social media engagement

### Středa - Content Creation Day 2

**Dopoledne:**
- [ ] Dokonči a publikuj blog článek
- [ ] On-page SEO optimalizace nového obsahu
- [ ] Internal linking

**Odpoledne:**
- [ ] Natoč Reel/video
- [ ] Email newsletter draft
- [ ] Social media engagement

### Čtvrtek - SEO & Optimization Day

**Dopoledne:**
- [ ] Technické SEO úkoly (chyby, broken links)
- [ ] Aktualizace starých článků (content refresh)
- [ ] Meta descriptions/titles optimization

**Odpoledne:**
- [ ] Natoč Reel/video
- [ ] Dokonči email newsletter
- [ ] Social media engagement

### Pátek - Publishing & Analytics

**Dopoledne:**
- [ ] Publikuj newsletter
- [ ] Content wrap-up (publikuj co zbývá)
- [ ] Copywriting úkoly (product descriptions, landing pages)

**Odpoledne:**
- [ ] Týdenní analytics review
  - SEO: Pozice, traffic, conversions
  - Social: Reach, engagement, growth
  - Content: Best performers
- [ ] Natoč Reel/video
- [ ] Social media engagement

### Sobota & Neděle - Light Mode

**Sobota:**
- [ ] Lehčí social media content (fun, relatable)
- [ ] Stories (3-5x)
- [ ] Community engagement (odpověz, likuj)

**Neděle:**
- [ ] Plánování na příští týden
- [ ] Research nových trendů
- [ ] Batch vytvoř Stories na pondělí

---

## 📆 Měsíční checklist

### Na začátku měsíce

- [ ] **Analýza minulého měsíce**
  - SEO report (Search Console + Analytics)
  - Social media report (follower growth, reach, engagement)
  - Content performance (best articles, videos)
  - Co fungovalo? Co ne?

- [ ] **Strategie pro nový měsíc**
  - Hlavní cíle (např. "+500 followers", "5 nových článků")
  - Key themes (témata, která chceš pokrýt)
  - Content calendar (hrubý plán na měsíc)
  - SEO priorities (které stránky optimalizovat)

- [ ] **Content plán**
  - 8-12 blog článků (témata + keywords)
  - 20-30 Reels/videí (témata + skripty)
  - 4 newsletters (témata)
  - Social media campaigns (akce, soutěže)

### Každý týden v měsíci

- [ ] **Tracking progress**
  - Checklist: Co je hotovo, co zbývá?
  - Metrics: Jdu správným směrem?
  - Adjust: Co změnit?

### Na konci měsíce

- [ ] **Comprehensive review**
  - SEO: Ranking changes, traffic growth
  - Content: Views, shares, engagement
  - Social: Follower growth, best posts
  - Sales impact: Conversions, revenue

- [ ] **Backlinks audit**
  - Nové backlinky (Ahrefs, SEMrush)
  - Ztracené backlinky (recover?)
  - Konkurence backlinky (opportunities)

- [ ] **Technical SEO**
  - Site speed check (PageSpeed Insights)
  - Mobile usability (Google Mobile Test)
  - Security (SSL, HTTPS)
  - Broken links audit

- [ ] **Content refresh**
  - Aktualizuj 2-3 starší články
  - Přidej nové sekce podle "People also ask"
  - Aktualizuj statistiky a data
  - Re-publish a re-promote

---

## 📈 Jak se zlepšovat

### Kontinuální vzdělávání

**Denně (15-30 min):**
- [ ] Čti SEO/marketing blog (Moz, Ahrefs, Search Engine Land)
- [ ] Sleduj industry news (Gaming hardware, PC komponenty)
- [ ] Watch 1-2 YouTube tutorials (editing, SEO, marketing)

**Týdně (1-2 hod):**
- [ ] Online kurz (Udemy, Coursera, YouTube)
  - SEO advanced tactics
  - Video editing skills
  - Copywriting mastery
  - Social media algorithm updates

**Měsíčně:**
- [ ] Přečti marketing knihu nebo e-book
- [ ] Analyze konkurence (deep dive)
- [ ] Experiment s novou taktikou (A/B test něco)

### Skill development roadmap

**SEO Skills:**
1. **Základy** (máš) → **Pokročilé** (technical SEO, schema markup)
2. **Keyword research** → **Semantic SEO** (topic clusters)
3. **On-page** → **Programmatic SEO** (automatizace)

**Content Creation:**
1. **Psaní** → **Storytelling mastery**
2. **Video basics** → **Professional editing** (color grading, motion graphics)
3. **Static posts** → **Interactive content** (carousels, polls, AR filters)

**Copywriting:**
1. **Základy** → **Conversion copywriting**
2. **Product descriptions** → **Sales funnels**
3. **Email marketing** → **Marketing automation**

**Social Media:**
1. **Posting** → **Community management**
2. **Organic reach** → **Paid advertising** (FB Ads, IG Ads)
3. **Single platform** → **Multi-platform orchestration**

### Self-assessment (Každý měsíc)

**SEO:**
- [ ] Zlepšil jsem rankings? (o kolik pozic?)
- [ ] Roste organický traffic? (o kolik %?)
- [ ] Klesá bounce rate?
- [ ] Rostou konverze?

**Content:**
- [ ] Publikoval jsem dostatek obsahu? (cíl vs. realita)
- [ ] Kvalita obsahu? (engagement, shares)
- [ ] Time management? (kolik času per article?)

**Social Media:**
- [ ] Follower growth? (cíl vs. realita)
- [ ] Engagement rate? (roste?)
- [ ] Reach? (roste?)
- [ ] Conversions? (klikají na odkazy?)

**Areas for improvement:**
```
Co mi jde dobře?
1. _________________
2. _________________
3. _________________

Co potřebuji zlepšit?
1. _________________
2. _________________
3. _________________

Akční kroky na příští měsíc:
1. _________________
2. _________________
3. _________________
```

---

## 🚀 Maximalizace výkonu

### Time Management - Jak být produktivnější

**1. Time blocking**
```
Rozdělej den na bloky:
- Deep work (tvorba obsahu): 10:00-12:30
- Operativa (SEO tasks): 14:30-16:00
- Social media: 9:00-10:00, 17:00-18:00
- Admin: 17:00-18:00
```

**2. Pomodoro Technique**
```
- 25 minut práce (fokus!)
- 5 minut pauza
- Po 4 cyklech: 15-30 min dlouhá pauza
```

**3. Batch processing**
```
Dělej podobné úkoly najednou:
- Všechny sociální média posty najednou (pondělí)
- Všechny SEO checks najednou (čtvrtek)
- Všechny videa najednou (natáčení pak editace)
```

**4. Automation**
```
Automatizuj co se dá:
- Social media scheduling (Buffer, Later, Hootsuite)
- Email marketing (Mailchimp, SendGrid)
- Analytics reporting (Google Data Studio)
- Rank tracking (Ahrefs, SEMrush)
```

**5. Templates & Systems**
```
Vytvoř si šablony:
- Blog article template
- Video script template
- Social media caption templates
- Email templates
- SEO checklist template
```

### Produktivní nástroje

**Content Creation:**
- **Grammarly:** Gramatika a spelling
- **Hemingway Editor:** Readability
- **Canva:** Grafika, thumbnails
- **CapCut/Adobe Premiere Rush:** Video editing

**SEO:**
- **Google Search Console:** Free, must-have
- **Google Analytics:** Free, must-have
- **Ahrefs/SEMrush:** Paid, pokročilé (pokud máš budget)
- **Ubersuggest:** Free alternative

**Social Media:**
- **Buffer/Later:** Scheduling
- **Canva:** Grafika
- **CapCut:** Video editing
- **Unsplash/Pexels:** Free stock photos

**Organization:**
- **Notion/Trello:** Task management, content calendar
- **Google Calendar:** Time blocking
- **Google Drive:** File management
- **1Password:** Password management

### Prioritizace - Eisenhower Matrix

```
┌─────────────────────┬─────────────────────┐
│   URGENT + IMPORTANT│ NOT URGENT + IMPORTANT│
│   (DO IT NOW)       │   (SCHEDULE IT)     │
├─────────────────────┼─────────────────────┤
│ - Odpověz na DM     │ - Blog articles     │
│ - Fix critical SEO  │ - SEO optimization  │
│ - Post social media │ - Learning          │
│ - Customer issues   │ - Strategy planning │
├─────────────────────┼─────────────────────┤
│   URGENT + NOT IMP  │ NOT URGENT + NOT IMP│
│   (DELEGATE/AUTOMATE)│   (ELIMINATE)       │
├─────────────────────┼─────────────────────┤
│ - Some emails       │ - Mindless browsing │
│ - Some meetings     │ - Perfectionism     │
│ - Admin tasks       │ - Busy work         │
└─────────────────────┴─────────────────────┘
```

### Energy management

**Kdy máš nejvíc energie?**
- Ráno? → Deep work na dopoledne
- Odpoledne? → Deep work na odpoledne
- Večer? → Lehčí tasks ráno, heavy na večer

**High-energy tasks:**
- Psaní nového obsahu
- Kreativní brainstorming
- Natáčení videí
- Strategy thinking

**Low-energy tasks:**
- Email responses
- Social media engagement
- Admin work
- Data entry

### Jak být TOP v pozici

**1. Ownership mindset**
```
✅ Tohle je MOJE věc, beru zodpovědnost
✅ Proaktivní, ne reaktivní
✅ Přemýšlím o business impactu, ne jen o úkolech
```

**2. Data-driven decisions**
```
✅ Všechno měř
✅ Rozhoduj podle dat, ne podle pocitů
✅ Testuj, optimalizuj, iteruj
```

**3. Always learning**
```
✅ Investuj do sebe (kurzy, knihy, mentoring)
✅ Experimentuj s novými tactikami
✅ Sleduj industry leaders
```

**4. Kvalita > Kvantita**
```
✅ Raději 1 skvělý článek než 3 průměrné
✅ Raději 1 viral video než 10 průměrných
✅ Focus on impact, not activity
```

**5. Build systems**
```
✅ Vytvoř procesy pro opakované úkoly
✅ Dokumentuj co děláš (pro sebe i ostatní)
✅ Automatizuj kde se dá
```

**6. Communication**
```
✅ Sdílej výsledky (reporting)
✅ Komunikuj proaktivně (předejdi problémům)
✅ Přijímej feedback a uč se z něj
```

---

## 🛠️ Nástroje a zdroje

### Nástroje v tomto repo

**1. Category Template Generator**
```bash
# Validace SEO textu
python category_template_generator.py input.md --validate

# Generování nové kategorie
python category_template_generator.py --generate-sample "Herní počítače" -o output.md

# Převod Markdown → HTML
python category_template_generator.py input.md -o output.html -f html

# Převod HTML → Markdown
python category_template_generator.py input.html -o output.md -f markdown
```

**2. Content Utils**
```python
from content_utils import (
    validate_content_structure,
    convert_markdown_to_html,
    convert_html_to_markdown
)

# Validace
results = validate_content_structure(content, config)

# Konverze
html = convert_markdown_to_html(markdown_text)
markdown = convert_html_to_markdown(html_text)
```

### Dokumentace v repo

- **[QUICKSTART.md](QUICKSTART.md)** - Rychlý start
- **[README_GENERATOR.md](README_GENERATOR.md)** - Detailní API dokumentace
- **[NAVOD-K-POUZITI.md](NAVOD-K-POUZITI.md)** - Jak integrovat spodní sekce
- **[docs/facebook-instagram-strategie-2026.md](docs/facebook-instagram-strategie-2026.md)** - FB & IG strategie
- **[docs/social-media-quick-reference.md](docs/social-media-quick-reference.md)** - Social media checklist

### Externí zdroje

**SEO:**
- [Google Search Central](https://developers.google.com/search)
- [Moz Blog](https://moz.com/blog)
- [Ahrefs Blog](https://ahrefs.com/blog/)
- [Search Engine Land](https://searchengineland.com/)

**Content Marketing:**
- [Content Marketing Institute](https://contentmarketinginstitute.com/)
- [HubSpot Blog](https://blog.hubspot.com/)
- [Copyblogger](https://copyblogger.com/)

**Social Media:**
- [Social Media Examiner](https://www.socialmediaexaminer.com/)
- [Later Blog](https://later.com/blog/)
- [Hootsuite Blog](https://blog.hootsuite.com/)

**Video/Content Creation:**
- YouTube: Think Media, Video Influencers
- YouTube: Ali Abdaal (productivity)
- Skillshare, Udemy courses

---

## 🎯 Příklad ideálního dne

**8:00-8:30** - Káva, email check, planning  
**8:30-9:00** - Social media check & response  
**9:00-9:30** - Analytics & SEO monitoring  
**9:30-10:00** - Plánování dne, prioritizace  

**10:00-12:30** - DEEP WORK (psaní článku, flow state)  

**12:30-13:30** - Oběd & odpočinek  

**13:30-14:30** - Video creation (natáčení + editace)  
**14:30-15:00** - SEO technická práce  
**15:00-16:00** - Copywriting (product descriptions, emails)  
**16:00-17:00** - Social media engagement + publikace Reelu  

**17:00-17:30** - Admin & wrap-up  
**17:30-18:00** - Plánování na zítra + analytics check  

**Výsledek:**
- ✅ 1 blog článek napsán
- ✅ 1 Reel publikován
- ✅ 3-5 Stories sdíleno
- ✅ SEO úkoly hotovo
- ✅ Community engagement udržen
- ✅ Zítra naplánováno

---

## 💡 Závěrečné rady

**1. Neboj se experimentovat**
Zkus nové formáty, nové témata. Data ti řeknou, co funguje.

**2. Buď konzistentní**
Lepší průměrná kvalita každý den než perfekce jednou za měsíc.

**3. Poslouchej komunitu**
Co lidi zajímá? Co se ptají? O tom piš.

**4. Měř a optimalizuj**
Co neměříš, nemůžeš zlepšit.

**5. Péče o sebe**
Burnout neprospívá nikomu. Odpočinek je součást produktivity.

**6. Radost z práce**
Pokud tě to nebaví, nebude to dlouhodobě fungovat. Najdi způsob, jak si práci užít.

---

**Vytvořeno:** 2026-02-19  
**Verze:** 1.0  
**Pro:** HelloComp Multi-Role Position (SEO, Content, Copy, Social Media)

🚀 **Teď jdi a buď TOP člověk na svém místě!**
