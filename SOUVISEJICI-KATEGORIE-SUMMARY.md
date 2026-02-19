# Související kategorie (Related Categories) - Implementation Summary

## Overview
This document summarizes the implementation of "Související kategorie" (Related Categories) sections for all HelloComp.cz category pages. These sections provide internal linking for SEO and help customers discover related products.

## Created Files

### Gaming PC Category Files (Price-based)
All gaming PC category files follow a consistent format and link to adjacent price tiers without linking to themselves:

1. **herni-pocitac-do-15000-spodni-sekce.md** - Gaming PCs up to 15,000 CZK
   - Links to: 20k, 30k (adjacent higher tiers)
   - Context: Entry-level, e-sports, basic Full HD

2. **herni-pocitac-do-20000-spodni-sekce.md** - Gaming PCs up to 20,000 CZK
   - Links to: 15k, 30k (adjacent tiers)
   - Context: Mid-range, solid Full HD

3. **herni-pocitac-do-30000-spodni-sekce.md** - Gaming PCs up to 30,000 CZK
   - Links to: 20k, 40k (adjacent tiers)
   - Context: Solid 1440p, modern AAA games

4. **herni-pocitac-do-40000-spodni-sekce.md** - Gaming PCs up to 40,000 CZK
   - Links to: 30k, 60k (adjacent tiers)
   - Context: High-end 1440p, streaming

5. **herni-pocitac-do-60000-spodni-sekce.md** - Gaming PCs up to 60,000 CZK
   - Links to: 40k (adjacent lower tier)
   - Context: 4K gaming, high-end, ultimate

### General Category Files

7. **herni-pocitace-obecna-spodni-sekce.md** - General Gaming PCs category
   - Links to: ALL price categories (15k, 20k, 30k, 40k, 60k)
   - Links to: Key subcategories

### Modified Existing Files

8. **kancelarske-pocitace.md** - Office Computers
   - Added Související kategorie section at the end
   - Cross-sells to: Workstations, Gaming PCs, Components, Monitors

9. **pracovni-stanice.md** - Workstations
   - Added Související kategorie section at the end
   - Cross-sells to: Office PCs, Gaming PCs, Components, Monitors

## Format and Structure

All sections follow this consistent format:

```markdown
## Související kategorie

* [Category Name](URL)
* [Category Name](URL)
...
```

## Key Rules Followed

✅ **No Self-Links**: Each category does NOT link to itself
✅ **Adjacent Price Tiers**: Gaming categories link to neighboring price levels (min 1 lower, 1 higher if exists)
✅ **Standard Cross-sells**: All gaming categories include:
   - General gaming PC category
   - How to choose gaming PC
   - Gaming PC on installments
   - Custom gaming PC
   - Intel/AMD gaming PCs
   - Graphics cards
   - Processors
   - Monitors

✅ **Professional Style**: Czech language, consistent with HelloComp brand
✅ **Valid URLs**: All URLs match the real hellocomp.cz structure

## SEO Benefits

1. **Internal Linking**: Distributes link juice across category pages
2. **User Navigation**: Helps customers find related products easily
3. **Reduced Bounce Rate**: Provides clear paths to explore more categories
4. **Price Tier Discovery**: Customers can see all available price options

## Usage Instructions

These files contain the bottom sections (footer text) that should be appended to their respective category pages on the HelloComp.cz e-shop.

### Integration Steps:
1. Open the corresponding category page in your CMS
2. Scroll to the bottom of the main content
3. Add a separator line (`---`)
4. Copy and paste the "Související kategorie" section from the appropriate file
5. Save and publish

### Example:
For the "Gaming PC up to 15,000 CZK" category page:
- Use content from `herni-pocitac-do-15000-spodni-sekce.md`
- Append it to the end of the main category description
- The section will appear below the main content, before the footer

## Files Overview Table

| File Name | Category | Self-Link Check | Adjacent Links | Status |
|-----------|----------|----------------|----------------|---------|
| herni-pocitac-do-15000-spodni-sekce.md | Gaming PC ≤15k CZK | ✅ No self-link | 20k, 30k | ✅ Complete |
| herni-pocitac-do-20000-spodni-sekce.md | Gaming PC ≤20k CZK | ✅ No self-link | 15k, 30k | ✅ Complete |
| herni-pocitac-do-30000-spodni-sekce.md | Gaming PC ≤30k CZK | ✅ No self-link | 20k, 40k | ✅ Complete |
| herni-pocitac-do-40000-spodni-sekce.md | Gaming PC ≤40k CZK | ✅ No self-link | 30k, 60k | ✅ Complete |
| herni-pocitac-do-60000-spodni-sekce.md | Gaming PC ≤60k CZK | ✅ No self-link | 40k | ✅ Complete |
| herni-pocitace-obecna-spodni-sekce.md | Gaming PCs (General) | ✅ No self-link | All price tiers | ✅ Complete |
| kancelarske-pocitace.md | Office Computers | ✅ No self-link | Cross-sell | ✅ Complete |
| pracovni-stanice.md | Workstations | ✅ No self-link | Cross-sell | ✅ Complete |

## Maintenance

When adding new categories or price tiers:
1. Create a new section file following the same format
2. Ensure no self-links
3. Update adjacent categories to include the new tier
4. Add standard cross-sell links
5. Maintain Czech language and HelloComp style

## Notes

- All URLs use the actual hellocomp.cz domain structure
- The format is consistent with the reference provided in the original requirements
- Each file can be used independently for its respective category
- The sections support SEO by creating a strong internal linking structure
