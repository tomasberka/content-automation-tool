# Návod k použití souvisejících kategorií / Usage Guide

## Jak integrovat spodní sekce do kategoriií HelloComp.cz

### Přehled
Každý soubor `*-spodni-sekce.md` obsahuje sekci "Související kategorie", kterou je potřeba přidat na konec příslušné kategorie na webu HelloComp.cz.

### Krok za krokem

#### 1. Herní počítače do 15 000 Kč
**Soubor:** `herni-pocitac-do-15000-spodni-sekce.md`  
**Cílová stránka:** https://www.hellocomp.cz/herni-pocitace-do-15000/

**Postup:**
```
1. Otevřete kategorii "Herní PC do 15 000 Kč" v CMS
2. Přejděte na konec hlavního textu kategorie
3. Přidejte oddělovač: ---
4. Zkopírujte celý obsah ze souboru herni-pocitac-do-15000-spodni-sekce.md
5. Vložte pod oddělovač
6. Uložte a publikujte
```

**Výsledek:**
```markdown
[... hlavní text kategorie ...]

---

## Související kategorie

* [Herní počítače](https://www.hellocomp.cz/herni-pocitace--gaming/)
* [Jak vybrat herní PC](https://www.hellocomp.cz/jak-si-vybrat-herni-pc/)
* [Herní PC do 20 000 Kč](https://www.hellocomp.cz/herni-pocitace-do-20000/)
* [Herní PC do 30 000 Kč](https://www.hellocomp.cz/herni-pocitace-do-30000/)
[... další odkazy ...]
```

#### 2. Herní počítače do 20 000 Kč
**Soubor:** `herni-pocitac-do-20000-spodni-sekce.md`  
**Cílová stránka:** https://www.hellocomp.cz/herni-pocitace-do-20000/

Stejný postup jako výše.

#### 3. Herní počítače do 30 000 Kč
**Soubor:** `herni-pocitac-do-30000-spodni-sekce.md`  
**Cílová stránka:** https://www.hellocomp.cz/herni-pocitace-do-30000/

Stejný postup jako výše.

#### 4. Herní počítače do 40 000 Kč
**Soubor:** `herni-pocitac-do-40000-spodni-sekce.md`  
**Cílová stránka:** https://www.hellocomp.cz/herni-pocitace-do-40000/

Stejný postup jako výše.

#### 6. Herní počítače do 60 000 Kč
**Soubor:** `herni-pocitac-do-60000-spodni-sekce.md`  
**Cílová stránka:** https://www.hellocomp.cz/herni-pocitace-do-60000/

Stejný postup jako výše.

#### 7. Herní počítače (obecná kategorie)
**Soubor:** `herni-pocitace-obecna-spodni-sekce.md`  
**Cílová stránka:** https://www.hellocomp.cz/herni-pocitace--gaming/

Stejný postup jako výše.

#### 8. Kancelářské počítače
**Soubor:** `kancelarskе-pocitace.md` (již obsahuje sekci na konci)  
**Cílová stránka:** https://www.hellocomp.cz/kancelarske-pocitace/

Sekce je již přidána v souboru, stačí zkopírovat poslední část (od "## Související kategorie").

#### 9. Pracovní stanice
**Soubor:** `pracovni-stanice.md` (již obsahuje sekci na konci)  
**Cílová stránka:** https://www.hellocomp.cz/pracovni-stanice--workstation-pc/

Sekce je již přidána v souboru, stačí zkopírovat poslední část (od "## Související kategorie").

---

## Kontrolní seznam před publikací

Před publikací každé kategorie ověřte:

- [ ] Sekce "Související kategorie" je na konci stránky
- [ ] Je přidán oddělovač (---) před sekcí
- [ ] Všechny odkazy fungují (otevřete 2-3 náhodné)
- [ ] Kategorie NEODKAZUJE sama na sebe
- [ ] Formátování odpovídá zbytku stránky
- [ ] Text je v češtině a odpovídá stylu HelloComp

---

## Časté dotazy (FAQ)

**Q: Můžu upravit pořadí odkazů?**  
A: Ano, ale doporučujeme zachovat stávající strukturu pro konzistenci napříč kategoriemi.

**Q: Co když chci přidat další kategorii?**  
A: Použijte některý existující soubor jako šablonu a dodržte stejný formát a pravidla (zejména: žádné self-linky, odkazy na sousední cenové hladiny).

**Q: Kategorie už má nějakou spodní sekci. Co s ní?**  
A: Pokud je relevantní, ponechte ji nad sekcí "Související kategorie". Pokud ne, nahraďte ji novou sekcí.

**Q: Můžu změnit texty odkazů?**  
A: Texty odkazů jsou optimalizované pro SEO. Změny doporučujeme konzultovat s SEO specialistou.

---

## Kontakt

V případě dotazů nebo problémů při implementaci kontaktujte odpovědnou osobu za HelloComp.cz obsah.
