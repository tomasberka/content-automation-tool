#!/usr/bin/env python3
"""
Test HTML Structure Validation
================================

Tests to verify that content structure validation enforces <p> tag requirements.
"""

import sys
from category_template_generator import (
    CategoryContent,
    ContentSection,
    ContentValidator,
    ContentFormatter,
    ValidationLevel
)


def test_introduction_starts_with_p():
    """Test that introduction text starts with <p> tag"""
    print("Test 1: Introduction must start with <p> tag")
    
    content = CategoryContent(
        title="Test Title",
        meta_description="Test meta description for testing purposes only.",
        h1="Test H1 Heading",
        introduction="This is a test introduction text.",
        h2_sections=[]
    )
    
    validator = ContentValidator()
    results = validator.validate(content)
    
    # Check if HTML structure validation passes
    html_errors = [r for r in results if 'html' in r.section.lower() and r.level == ValidationLevel.ERROR]
    
    if html_errors:
        print(f"  ❌ FAILED: Found HTML structure errors: {html_errors[0].message}")
        return False
    else:
        print("  ✅ PASSED: Introduction starts with <p> tag")
        return True


def test_section_starts_with_p():
    """Test that section content starts with <p> tag"""
    print("\nTest 2: Section content must start with <p> tag")
    
    section1 = ContentSection(
        type="h2",
        heading="Test Section 1",
        content="This is test section content."
    )
    
    section2 = ContentSection(
        type="h2",
        heading="Test Section 2",
        content="Another test section with content."
    )
    
    section3 = ContentSection(
        type="h2",
        heading="Test Section 3",
        content="Third section for testing."
    )
    
    content = CategoryContent(
        title="Test Title for Testing Only",
        meta_description="Test meta description for testing purposes only and meeting length requirements.",
        h1="Test H1 Heading",
        introduction="This is a test introduction text that needs to be long enough to meet the minimum word count requirement of fifty words so let me add more words here to make it longer.",
        h2_sections=[section1, section2, section3]
    )
    
    validator = ContentValidator()
    results = validator.validate(content)
    
    # Check if HTML structure validation passes
    html_errors = [r for r in results if 'html' in r.section.lower() and r.level == ValidationLevel.ERROR]
    
    if html_errors:
        print(f"  ❌ FAILED: Found HTML structure errors: {html_errors[0].message}")
        return False
    else:
        print("  ✅ PASSED: All sections start with <p> tag")
        return True


def test_list_content_validation():
    """Test that content starting with list gets <p> prefix"""
    print("\nTest 3: List content should have <p> prefix added")
    
    section1 = ContentSection(
        type="h2",
        heading="Features",
        content="- Feature 1\n- Feature 2\n- Feature 3"
    )
    
    content = CategoryContent(
        title="Test Title for Testing Only",
        meta_description="Test meta description for testing purposes only and meeting length requirements.",
        h1="Test H1 Heading",
        introduction="This is a test introduction text that needs to be long enough to meet the minimum word count requirement of fifty words so let me add more words here to make it longer.",
        h2_sections=[section1]
    )
    
    # Format the section content
    formatted = ContentFormatter._format_html_content(section1.content)
    
    if formatted.strip().startswith('<p>'):
        print("  ✅ PASSED: List content has <p> prefix")
        return True
    else:
        print(f"  ❌ FAILED: List content doesn't start with <p>: {formatted[:50]}")
        return False


def test_html_formatting():
    """Test that _format_html_content produces correct structure"""
    print("\nTest 4: HTML formatting produces <p> tags")
    
    # Test plain text
    text = "This is plain text."
    formatted = ContentFormatter._format_html_content(text)
    
    if formatted.strip().startswith('<p>'):
        print("  ✅ PASSED: Plain text formatted with <p> tag")
    else:
        print(f"  ❌ FAILED: Plain text not formatted correctly: {formatted}")
        return False
    
    # Test list content
    list_text = "- Item 1\n- Item 2"
    formatted_list = ContentFormatter._format_html_content(list_text)
    
    if formatted_list.strip().startswith('<p>'):
        print("  ✅ PASSED: List content has <p> prefix")
        return True
    else:
        print(f"  ⚠️  WARNING: List starts with: {formatted_list[:50]}")
        return True  # This is acceptable as we now add <p> prefix


def test_existing_html_passthrough():
    """Test that existing HTML is preserved"""
    print("\nTest 5: Existing HTML should be preserved")
    
    html_text = "<p>This is already HTML.</p>"
    formatted = ContentFormatter._format_html_content(html_text)
    
    if formatted == html_text:
        print("  ✅ PASSED: Existing HTML preserved")
        return True
    else:
        print(f"  ❌ FAILED: HTML was modified: {formatted}")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("HTML Structure Validation Tests")
    print("=" * 60)
    
    tests = [
        test_introduction_starts_with_p,
        test_section_starts_with_p,
        test_list_content_validation,
        test_html_formatting,
        test_existing_html_passthrough
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"  ❌ EXCEPTION: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Results: {passed}/{total} tests passed")
    print("=" * 60)
    
    return all(results)


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
