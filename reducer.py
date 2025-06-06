#!/usr/bin/env python3
import sys

current_lang = None
count = 0
lang_totals = {}
total_count = 0

# Read all key-value pairs from stdin
for line in sys.stdin:
    lang, val = line.strip().split('\t')
    val = int(val)
    if lang in lang_totals:
        lang_totals[lang] += val
    else:
        lang_totals[lang] = val
    total_count += val

# Print the results with percentages
for lang in lang_totals:
    count = lang_totals[lang]
    percentage = (count / total_count) * 100
    print(f"{lang}\t{count}\t{percentage:.2f}%")