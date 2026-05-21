#!/usr/bin/env python
"""Test script for scientific name formatting"""

import sys
sys.path.insert(0, '.')

from utils.styling import format_scientific_name

# Test cases
test_names = [
    "Cyperus rotundus L.",
    "Imperata cylindrica (L.) Beauv.",
    "Eichhornia crassipes (Mart.) Solms",
    "Phyllanthus niruri L.",
    "Paspalum conjugatum Bergius",
    "Ageratum conyzoides (L.) L.",
    "Digitaria adscendens (H.B.K.) Henr.",
    "Mimosa pudica L.",
    "Portulaca oleracea L.",
    "Amaranthus spinosus L.",
    "Cyperus iria L.",
]

print("=" * 100)
print("TESTING format_scientific_name() - HTML Output")
print("=" * 100)
print()

for name in test_names:
    formatted = format_scientific_name(name)
    print(f"Input:   {name}")
    print(f"Output:  {formatted}")
    print()
    
    # Verify it contains HTML tags
    if "<i>" in formatted and "</i>" in formatted:
        print("✅ Correct: Contains HTML <i> tags")
    else:
        print("❌ Error: Missing HTML <i> tags")
    
    # Verify author is not in italic
    parts = name.split()
    if len(parts) > 2:
        author = parts[-1]
        if author not in formatted or f"<i>{author}</i>" not in formatted:
            print("✅ Correct: Author is not italicized")
        else:
            print("❌ Error: Author should not be italicized")
    
    print("-" * 100)
    print()

print("=" * 100)
print("TEST COMPLETE")
print("=" * 100)
