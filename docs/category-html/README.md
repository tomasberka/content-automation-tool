# Category HTML for Shoptet E-shop

This directory contains ready-to-use HTML category descriptions for the HelloComp.cz e-shop running on Shoptet platform.

## Overview

These HTML files are designed to be directly inserted into Shoptet category pages. They include:

- **Complete CSS styling** - Embedded styles for consistent presentation
- **Responsive design** - Mobile-optimized layouts (breakpoint at 768px)
- **Expandable content** - "Read more" functionality to keep pages clean
- **SEO-optimized** - Internal links, proper heading structure, and keyword-rich content
- **Shoptet-ready** - No external dependencies, direct copy-paste integration

## File Structure

### herni-pocitace-kategorie-shoptet.html
**Category:** Gaming Computers (Herní počítače)

Complete category description with:
- Introduction paragraph with CTA link
- Expandable content section (hidden by default)
- Multiple H2 and H3 sections covering:
  - Gaming PC builds for maximum performance
  - Different player types (beginners, advanced, hardcore)
  - Hardware specifications and compatibility
  - Gaming PC setup components
  - FPS calculator information
  - Upgrade options
- Internal links to related HelloComp categories
- Responsive CSS for mobile devices

## Usage

### To add to Shoptet:

1. Copy the entire HTML content from the desired file
2. Navigate to your Shoptet admin panel
3. Go to the category edit page (e.g., Gaming Computers category)
4. Paste the HTML into the category description field
5. Save the changes

### Key Features:

**CSS Styling:**
- `.category-content` - Main container class
- H2 headings with blue underline border
- H3 headings with gray underline
- Proper link styling with hover effects
- Responsive adjustments for mobile devices

**Interactive Elements:**
- `#readMore` - Link to expand hidden content
- `#hiddenContent` - Hidden content section
- `#hideDescription` - Link to collapse content back

**Note:** The expand/collapse functionality requires JavaScript to be implemented on the Shoptet side. The IDs are provided for easy integration.

## Style Guide

All category HTML files follow these design principles:

- **Color Scheme:**
  - Primary text: #2c3e50 (dark blue-gray)
  - Links: #2980b9 (blue)
  - Borders: #2980b9 (blue for H2), #ccc (gray for H3)
  
- **Typography:**
  - Base font-size: 1em
  - Line-height: 1.6 (1.5 on mobile)
  - H2: 1.5em (1.3em on mobile)
  - H3: 1.2em (1.1em on mobile)

- **Spacing:**
  - Generous margins and padding for readability
  - Clear visual hierarchy with consistent spacing

## Internal Linking Strategy

Each category page includes contextual internal links to related HelloComp categories:
- PC components (processors, RAM, graphics cards, storage)
- Peripherals (monitors, keyboards, mice, headsets)
- Related product categories
- Guide articles

This creates a strong internal link structure for SEO and user navigation.

## Maintenance

When adding new category HTML files:
1. Follow the established structure and styling
2. Use the `.category-content` container class
3. Maintain responsive design patterns
4. Include relevant internal links
5. Keep content between 600-900 words
6. Update this README with new file information

## Technical Specifications

- **Format:** HTML with embedded CSS
- **Platform:** Shoptet e-commerce
- **Compatibility:** Modern browsers (Chrome, Firefox, Safari, Edge)
- **Responsive breakpoint:** 768px
- **External dependencies:** None
- **JavaScript required:** Optional (for expand/collapse functionality)

---

**Created:** 2026-02-04  
**Status:** ✅ Initial version with Gaming Computers category
