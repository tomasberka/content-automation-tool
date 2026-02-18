# BIOS – Jak spustit a základní nastavení | Průvodce 2026

## Kontrolní seznam klíčových slov
- [x] co je to bios
- [x] jak aktualizovat bios
- [x] jak vstoupit do biosu
- [x] bios setup
- [x] uefi vs bios
- [x] boot order
- [x] xmp profil
- [x] secure boot
- [x] bios reset
- [x] cmos clear

## Meta informace
**Meta title:** Co je BIOS a jak do něj vstoupit | Nastavení a aktualizace 2026 | HelloComp
**Meta description:** Kompletní průvodce BIOSem: co je BIOS, jak vstoupit do BIOSu, základní nastavení (boot order, XMP, secure boot), jak aktualizovat BIOS krok za krokem.

---

# BIOS – Jak spustit a základní nastavení PC

**BIOS je základ každého počítače.** Pokud potřebujete vědět, **co je to BIOS**, **jak vstoupit do BIOSu** nebo **jak aktualizovat BIOS**, tento průvodce vám ukáže vše podstatné. Vysvětlíme, co dělá BIOS, jak ho spustit, základní nastavení (**boot order**, **XMP profil**, **Secure Boot**) a bezpečnou aktualizaci firmware.

**Prompt pro AI obrázek (21:9 formát):**
"BIOS setup screen interface in 21:9 format, HelloComp robot mascot pointing at motherboard with glowing BIOS chip, floating holographic BIOS menu screens, technical diagrams, modern tech lab setting, photorealistic 3D render, blue and white color scheme, professional aesthetic"

---

## Co je to BIOS a k čemu slouží?

### Definice BIOS

**BIOS** (Basic Input/Output System) je **firmware** uložený na čipu na základní desce, který startuje při zapnutí PC a inicializuje hardware před načtením operačního systému.

**Co BIOS dělá:**
1. **POST (Power-On Self-Test)** – Kontrola hardwaru při zapnutí (RAM, CPU, GPU)
2. **Inicializace hardware** – Aktivace komponent (disk y, USB, PCIe)
3. **Boot loader** – Spuštění operačního systému z vybraného disku
4. **Nastavení hardware** – Frekvence RAM, CPU, boot priority, fan curves

### UEFI vs Legacy BIOS

**Moderní PC používají UEFI** (Unified Extensible Firmware Interface) místo starého BIOSu, ale stále se mu říká "BIOS".

| Feature | Legacy BIOS | UEFI |
|---------|-------------|------|
| **Interface** | Text-based | Grafické (myš support) |
| **Boot rychlost** | Pomalejší | Rychlejší |
| **Disk limit** | 2 TB (MBR) | 9+ ZB (GPT) |
| **Secure Boot** | Ne | Ano |
| **Rok vzniku** | 1981 | 2005+ |

**Poznámka:** V tomto článku používáme "BIOS" pro UEFI i legacy BIOS – běžný termín.

---

## Jak vstoupit do BIOSu – Krok za krokem

### Metoda 1: Klávesová zkratka při startu

**Nejběžnější způsob** vstupu do BIOSu je stisknout specifickou klávesu během bootování PC.

**Postup:**
1. **Restartujte PC** (nebo zapněte)
2. **Okamžitě opakovaně mačkejte** příslušnou klávesu
3. PC vstoupí do BIOS setup

**Nejčastější klávesy podle výrobce motherboardu:**

| Výrobce | Klávesa pro BIOS |
|---------|------------------|
| **ASUS** | F2 nebo Delete |
| **MSI** | Delete |
| **Gigabyte** | Delete |
| **ASRock** | F2 nebo Delete |
| **Dell** | F2 |
| **HP** | F10 nebo Esc |
| **Lenovo** | F1 nebo F2 |
| **Acer** | F2 nebo Delete |

**Tip:** Pokud nevíte, která klávesa, sledujte **spodní část obrazovky** při startu – často je napsáno "Press DEL to enter Setup" nebo podobně.

### Metoda 2: Z Windows (pro UEFI)

**Windows 11/10** umožňuje vstup do UEFI bez mačkání kláves.

**Postup:**
1. **Start** → **Nastavení** (⚙️)
2. **Systém** → **Obnovení**
3. **Pokročilé spuštění** → **Restartovat**
4. **Poradce při potížích** → **Pokročilé možnosti** → **Nastavení firmwaru UEFI**
5. **Restartovat** → PC se restartuje do BIOSu

**Výhoda:** Spolehlivé, nemusíte stíhat správnou klávesu.

### Metoda 3: Shift + Restart

**Rychlejší varianta:**
1. Držte **Shift**
2. Klikněte **Start** → **Napájení** → **Restartovat**
3. Pokračujte stejně jako Metoda 2

---

## Základní navigace v BIOSu

### UEFI Interface

**Moderní UEFI** má grafické rozhraní s myší supportem.

**Hlavní sekce UEFI:**
* **Main / System** – Základní info (CPU, RAM, datum/čas)
* **AI Tweaker / OC** – Přetaktování CPU, RAM (XMP)
* **Advanced** – Pokročilá nastavení (USB, SATA, PCIe)
* **Boot** – Boot order, boot options
* **Security** – Hesla, Secure Boot
* **Save & Exit** – Uložení změn a restart

### Legacy BIOS Interface

**Starší BIOS** je text-based, ovládání pouze klávesnicí:
* **Šipky** – Navigace
* **Enter** – Potvrzení
* **Esc** – Zpět
* **F10** – Uložit a exit (většina BIOSů)

**Tip:** Tlačítka/klávesy pro ovládání jsou **zobrazeny dole** na obrazovce BIOSu.

---

## Důležitá BIOS nastavení

### 1. Boot Order (Pořadí bootování)

**Boot order** určuje, ze kterého disku se PC pokusí nabootovat první.

**Jak nastavit:**
1. V BIOSu najděte sekci **Boot**
2. **Boot Priority** nebo **Boot Option #1**
3. Nastavte **primární disk** s Windows (obvykle NVMe SSD nebo SATA SSD)
4. Uložte (F10)

**Proč to záleží:**
* Rychlejší boot (PC nehledá OS na jiných discích)
* Nutné při instalaci Windows z USB (nastavte USB jako první)

**Doporučení:** Primární disk s OS jako Boot Option #1.

### 2. XMP / EXPO (RAM profil)

**XMP** (Intel) a **EXPO** (AMD) jsou profily pro automatické přetaktování RAM na deklarované frekvence.

**Problém:** RAM běžně běží na 2133 MHz místo svých 3200/3600/6000 MHz, pokud **neaktivujete XMP**.

**Jak aktivovat XMP:**
1. V BIOSu najděte **AI Tweaker / OC / Advanced**
2. **XMP** nebo **EXPO** nebo **A-XMP** (AMD)
3. Nastavte na **Profile 1** nebo **Enabled**
4. Uložte a restartujte

**Výsledek:** RAM běží na své plné frekvenci → **o 5-15 % vyšší výkon** v hrách a aplikacích.

**Doporučení:** **Vždy aktivujte XMP** po sestavení nového PC.

**Tip:** Ověřte aktivaci v **Task Manager** → **Výkon** → **Paměť** → Rychlost by měla odpovídat specifikaci RAM.

### 3. Secure Boot

**Secure Boot** je bezpečnostní funkce, která brání bootování nepodepsaného softwaru (ochrana proti malware).

**Kdy vypnout:**
* Instalace starších OS (Windows 7)
* Dual-boot s Linuxem (některé distro vyžadují vypnutý Secure Boot)
* Kompatibilita s některým starým HW

**Jak vypnout:**
1. **Security** nebo **Boot** sekce
2. **Secure Boot** → **Disabled**

**Doporučení:** **Nechte zapnutý** na moderních Windows 10/11 PC – zvyšuje bezpečnost.

### 4. Fan Curves (Křivky ventilátorů)

**Fan curves** řídí otáčky ventilátorů podle teplot.

**Preset profily:**
* **Silent** – Tišší, vyšší teploty
* **Standard** – Vyvážené
* **Performance** – Hlučnější, nižší teploty

**Custom curve:**
* V pokročilém BIOSu můžete nastavit vlastní křivku (% otáček při specifické teplotě)
* Příklad: 40 °C = 30 %, 60 °C = 60 %, 80 °C = 100 %

**Doporučení:** Standard stačí, ale pokud je PC hlučné nebo horké, upravte.

### 5. CPU Power Limits (PL1/PL2)

**Intel procesor y** mají power limity:
* **PL1** – Dlouhodobý power limit (např. 125W)
* **PL2** – Krátkodobý boost (např. 253W)

**Snížení PL2** sníží teploty CPU o 10-15 °C, ale **mírně sníží výkon** v krátkých burst úlohách.

**Doporučení:** Nechte na **Auto**, pokud nemáte problémy s teplotami.

### 6. Resizable BAR (ReBAR)

**Resizable BAR** je technologie, která zvyšuje FPS v hrách (o 1-10 %) tím, že umožní CPU přistupovat ke **celé VRAM** GPU najednou.

**Požadavky:**
* Moderní GPU (RTX 3000+, RX 6000+)
* Moderní CPU (Intel 10. gen+, AMD Ryzen 3000+)
* UEFI BIOS

**Jak aktivovat:**
1. **Advanced** → **PCI Subsystem Settings**
2. **Resizable BAR** → **Enabled**
3. **Above 4G Decoding** → **Enabled** (nutné)
4. Uložte

**Doporučení:** Aktivujte, pokud máte kompatibilní hardware – free FPS boost.

### 7. SATA Mode (AHCI vs IDE)

**AHCI** je moderní SATA režim, **IDE** je legacy.

**Doporučení:** **AHCI** – lepší výkon, hot-swap support.

### 8. Virtualizace (Intel VT-x / AMD-V)

**Virtualizace** je nutná pro **VMs** (Virtual Machines), **WSL2** (Windows Subsystem for Linux), **Android emulátory** (BlueStacks).

**Jak aktivovat:**
1. **Advanced** → **CPU Configuration**
2. **Intel Virtualization Technology** nebo **SVM Mode** (AMD) → **Enabled**

**Doporučení:** Aktivujte, pokud plánujete používat virtualizaci.

---

## Jak aktualizovat BIOS – Bezpečně

**Aktualizace BIOSu** přináší:
* Podporu nových CPU
* Opravu bugů
* Zlepšení stability
* Nové funkce

**Varování:** ⚠️ **Aktualizace BIOSu je riziková** – pokud se něco pokazí (výpadek proudu), může to "zbricknout" motherboard. **Aktualizujte pouze pokud je to nutné.**

### Kdy aktualizovat BIOS?

✅ **ANO, aktualizujte:**
* Nový CPU vyžaduje novější BIOS (např. Ryzen 5000 na B450)
* Problémy se stabilitou, freezy, BSOD
* Výrobce doporučuje update (bezpečnostní důvody)
* Nové funkce, které potřebujete

❌ **NE, neaktualizujte:**
* "If it ain't broke, don't fix it" – pokud vše funguje, nechat
* Jen pro "nejnovější verzi"

### Příprava před aktualizací

1. **Zjistěte aktuální verzi BIOSu:**
   * V BIOSu (Main screen – BIOS Version)
   * Nebo Windows: **Win + R** → `msinfo32` → **Verze systému BIOS**

2. **Stáhněte správnou verzi:**
   * Web výrobce motherboardu (ASUS, MSI, Gigabyte, ASRock)
   * **Support** → Váš model → **BIOS** → Stáhněte nejnovější verzi
   * **Důležité:** Stahujte **pouze z oficiálního webu výrobce**

3. **Příprava:**
   * **UPS nebo zajištění stability proudu** (kritické!)
   * **USB flash disk** (FAT32 formát)
   * **Backup důležitých dat** (pro jistotu)

### Metoda 1: BIOS Flash Utility (v BIOSu)

**Nejbezpečnější metoda.**

**Postup:**
1. Rozbalte stažený BIOS soubor na USB flash disk (root, ne složka)
2. Restartujte PC a vstupte do BIOSu
3. Najděte **EZ Flash** (ASUS), **M-Flash** (MSI), **Q-Flash** (Gigabyte), **Instant Flash** (ASRock)
4. Vyberte BIOS soubor z USB
5. Potvrďte aktualizaci
6. **NEČEKEJTE, NEVYPíNEJTE PC** – Proces trvá 3-10 minut
7. PC se restartuje, nový BIOS je nainstalovaný

**Tip:** Po aktualizaci BIOSu **resetujte BIOS na výchozí** (Load Optimized Defaults) a znovu nastavte XMP, boot order, atd.

### Metoda 2: Windows Utility (od výrobce)

Někteří výrobci nabízejí Windows aplikaci pro update BIOSu (ASUS EZ Update, MSI Live Update).

**Nevýhoda:** Méně bezpečné než BIOS utility (Windows může crashnout během update).

**Doporučení:** Preferujte BIOS Flash Utility.

### Metoda 3: BIOS Flashback (bez CPU/RAM)

**Pokročilá metoda** – některé high-end motherboardy umožňují flashnout BIOS bez CPU/RAM pomocí speciálního tlačítka.

**Použití:** Když potřebujete aktualizovat BIOS před instalací nového CPU (např. Ryzen 5000 na B450 bez BIOS update).

**Postup:**
1. Připravte USB s BIOS souborem (přejmenujte podle instrukce výrobce)
2. Vložte USB do **BIOS Flashback portu** (označený port)
3. Zapojte PSU (PC vypnuté)
4. Stiskněte **BIOS Flashback tlačítko** (na I/O panelu)
5. LED bliká ~5-10 minut → Hotovo

**Podpora:** ASUS (Flashback), MSI (Flash BIOS Button), Gigabyte (Q-Flash Plus).

---

## BIOS reset – Jak resetovat nastavení

### Metoda 1: Z BIOSu (Software reset)

**Nejjednodušší metoda.**

**Postup:**
1. Vstupte do BIOSu
2. **Exit** → **Load Optimized Defaults** nebo **Load Setup Defaults**
3. Potvrďte **Yes**
4. **Save Changes and Exit** (F10)

**Výsledek:** BIOS se vrátí na výchozí nastavení.

### Metoda 2: CMOS Clear (Hardware reset)

**Pokud nemůžete vstoupit do BIOSu** (zapomenuté heslo, špatné nastavení), použijte CMOS clear.

**Postup:**
1. **Vypněte PC a odpojte napájení** (PSU vypínač + vytáhněte kabel)
2. Otevřete skříň
3. Najděte **CMOS baterii** (kulatá knoflíková baterie, CR2032)
4. **Vyjměte baterii**
5. **Počkejte 5-10 minut** (nebo stiskněte power tlačítko na 10 sekund)
6. Vložte baterii zpět
7. Zavřete skříň, zapojte napájení
8. Zapněte PC → BIOS je resetovaný

**Alternativa:** Některé motherboardy mají **Clear CMOS jumper** nebo **Clear CMOS tlačítko** (na I/O panelu nebo desce) – přečtěte si manuál.

**Poznámka:** Po CMOS clear musíte znovu nastavit datum/čas, boot order, XMP, atd.

---

## Časté BIOS problémy a řešení

### PC nenabootuje po BIOS změně

**Řešení:**
* Reset BIOSu na výchozí (Load Optimized Defaults)
* CMOS Clear (vyjmutí baterie)

### Zapomenuté BIOS heslo

**Řešení:**
* CMOS Clear (vymaže heslo)
* Kontaktujte výrobce motherboardu (někdy mají master password)

### RAM běží na nízké frekvenci

**Řešení:**
* Aktivujte XMP / EXPO v BIOSu

### USB zařízení nefunguje

**Řešení:**
* **Advanced** → **USB Configuration** → Ověřte, že USB porty jsou **Enabled**

### PC nenabootuje po aktualizaci BIOSu

**Prevence:** Vždy aktualizujte s UPS nebo stabilním proudem.
**Řešení:** Pokud motherboard má **dual BIOS**, automaticky se přepne na záložní. Jinak potřebujete BIOS Flashback nebo výměnu BIOS čipu (servis).

---

## BIOS tipy pro hráče

### 1. Aktivujte XMP hned po sestavení PC

Nejjednodušší způsob, jak získat **5-15 % vyšší výkon zdarma**.

### 2. Vypněte Fast Boot pro snadnější vstup do BIOSu

**Fast Boot** přeskakuje POST → rychlejší start, ale těžší vstup do BIOSu.
**Doporučení:** Vypnout, pokud často vstupujete do BIOSu.

### 3. Monitorujte teploty v BIOS

BIOS zobrazuje real-time teploty CPU, motherboard, fan RPM. Vhodné pro kontrolu po čištění PC.

### 4. Nastavte boot logo (některé BIOSy)

Některé UEFI umožňují změnit boot logo na vlastní obrázek – čistě kosmetické, ale zábavné.

---

## BIOS pro začátečníky – Co nedělat

❌ **Nehrát si s napětími** – Zvyšování CPU/RAM voltage bez znalosti může poškodit hardware
❌ **Neaktualizujte BIOS "jen tak"** – Pouze pokud je to nutné
❌ **Nevypínat PC během BIOS update** – Může to zničit motherboard
❌ **Neotvírat pokročilá nastavení**, pokud nevíte, co děláte

✅ **Bezpečné změny:**
* Aktivace XMP
* Boot order
* Fan curves (preset profily)
* Datum/čas

---

## BIOS pod kontrolou

Teď už víte, **co je to BIOS** a **jak vstoupit do BIOSu** na vašem PC. Rozumíte důležitým nastavením jako **boot order**, **XMP profil**, **Secure Boot** a víte, **jak bezpečně aktualizovat BIOS**. Umíte resetovat BIOS a řešit běžné problémy.

### Potřebujete nové PC s aktuálním BIOSem?

Prohlédněte si naši nabídku <a href="https://www.hellocomp.cz/herni-pocitace--gaming/">herních počítačů HelloComp</a>, kde každá sestava je dodávána s **aktuálním BIOSem** a **optimalizovanými nastavením**. Kvalitní základní desky s <a href="https://www.hellocomp.cz/procesory/">podporou nejnovějších procesorů</a>.

Potřebujete poradit s BIOSem? <a href="https://www.hellocomp.cz/kontakt/">Kontaktujte nás</a> – pomůžeme s nastavením nebo aktualizací.

---

## FAQ: Často kladené otázky o BIOSu

### Co je to BIOS a k čemu slouží?

**BIOS** (Basic Input/Output System) je firmware na čipu motherboardu, který **inicializuje hardware při zapnutí PC** a spouští operační systém. BIOS kontroluje CPU, RAM, disky při startu (POST test), umožňuje nastavit boot priority, frekvence RAM (XMP), fan curves a další parametry hardware. Moderní PC používají **UEFI** (grafický interface s myší), ale termín "BIOS" se stále běžně používá. Bez BIOSu by PC nemohl nabootovat.

### Jak vstoupit do BIOSu na Windows 11?

**Metoda 1** (klávesová zkratka): Restartujte PC a opakovaně mačkejte **Delete** nebo **F2** (záleží na výrobci) při startu. **Metoda 2** (z Windows): Start → Nastavení → Systém → Obnovení → Pokročilé spuštění → Restartovat → Poradce při potížích → Pokročilé možnosti → Nastavení firmwaru UEFI → Restartovat. Druhá metoda je spolehlivější, pokud Windows bootuje příliš rychle a nestíháte mačkat klávesu.

### Co je XMP a proč ho mám aktivovat?

**XMP** (Intel) nebo **EXPO** (AMD) je profil pro automatické přetaktování RAM na deklarované frekvence. Bez aktivace XMP běží RAM na základní 2133 MHz místo svých 3200/3600/6000 MHz, což **snižuje výkon o 5-15 %** v hrách a aplikacích. **Aktivace**: V BIOSu najděte sekci AI Tweaker/OC, nastavte XMP na Profile 1 nebo Enabled, uložte (F10). Ověřte v Task Manager → Výkon → Paměť – frekvence by měla odpovídat specifikaci RAM. XMP aktivujte vždy po sestavení nového PC.

### Je bezpečné aktualizovat BIOS?

**Aktualizace BIOSu je riziková** – při výpadku proudu během update může dojít k poškození motherboardu. **Aktualizujte pouze pokud**: potřebujete podporu nového CPU, máte problémy se stabilitou, nebo výrobce doporučuje update z bezpečnostních důvodů. **Neaktualizujte "jen tak"** pro nejnovější verzi – "if it ain't broke, don't fix it". **Bezpečná aktualizace**: použijte BIOS Flash Utility (v BIOSu), UPS nebo stabilní proud, oficiální BIOS od výrobce, nikdy nevypínejte PC během procesu.

### Jak resetovat BIOS na výchozí nastavení?

**Softwarový reset**: Vstupte do BIOSu → Exit → Load Optimized Defaults → Yes → Save & Exit (F10). **Hardware reset (CMOS Clear)**: Pokud nemůžete vstoupit do BIOSu, vypněte PC, odpojte napájení, otevřete skříň, vyjměte CMOS baterii (kulatá CR2032) na 5-10 minut, vložte zpět, zapněte PC. CMOS Clear vymaže všechna nastavení včetně hesel. Po resetu musíte znovu nastavit datum/čas, boot order, XMP, atd.

### Proč má moje RAM nižší frekvenci, než je uvedeno na obalu?

Protože **nemáte aktivovaný XMP/EXPO profil** v BIOSu. RAM výchozí běží na JEDEC standardu (2133-2666 MHz) – XMP profil je technicky "přetaktování" a musí být manuálně aktivován. **Řešení**: Vstupte do BIOSu, najděte AI Tweaker/OC sekci, aktivujte XMP → Profile 1, uložte. Ověřte v Task Manager → Výkon → Paměť. Pokud RAM odmítá běžet na XMP frekvenci (PC nenabootuje), může být problém s kompatibilitou nebo napětí – zkuste vyšší DRAM voltage (1.35V → 1.40V).

---

**Prompt pro AI obrázek (21:9 formát):**
"BIOS configuration workspace in 21:9 format, HelloComp robot mascot at workbench with motherboard displaying glowing BIOS chip, floating transparent UEFI interface screens showing XMP, boot order, fan curves, technical blueprints in background, modern tech laboratory, photorealistic 3D render, blue holographic lighting"
