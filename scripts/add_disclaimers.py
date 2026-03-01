#!/usr/bin/env python3
"""
Add disclaimer to all PRACTICE-QUESTIONS.md files
"""

import os
from pathlib import Path

DISCLAIMER = """
> **⚠️ DISCLAIMER:** These are **original practice questions** created for educational purposes based on AWS documentation. They are **NOT actual exam questions** from the AWS certification exam.

"""

def add_disclaimer_to_file(file_path):
    """Add disclaimer after the first heading if not already present"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if disclaimer already exists
        if '⚠️ DISCLAIMER:' in content or 'DISCLAIMER' in content[:500]:
            print(f"✓ Disclaimer already exists in {file_path}")
            return False

        # Find the first heading and add disclaimer after it
        lines = content.split('\n')
        new_lines = []
        disclaimer_added = False

        for i, line in enumerate(lines):
            new_lines.append(line)

            # Add disclaimer after first # heading
            if not disclaimer_added and line.startswith('# ') and i < 5:
                new_lines.append('')
                new_lines.append(DISCLAIMER.strip())
                disclaimer_added = True

        if disclaimer_added:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))
            print(f"✓ Added disclaimer to {file_path}")
            return True
        else:
            print(f"⚠ Could not find suitable location in {file_path}")
            return False

    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False

def main():
    """Process all PRACTICE-QUESTIONS.md files"""
    base_dir = Path(__file__).parent.parent

    # Find all PRACTICE-QUESTIONS.md files
    practice_files = list(base_dir.glob('**/PRACTICE-QUESTIONS.md'))

    print(f"Found {len(practice_files)} PRACTICE-QUESTIONS.md files\n")

    modified_count = 0
    for file_path in sorted(practice_files):
        if add_disclaimer_to_file(file_path):
            modified_count += 1

    print(f"\n✓ Modified {modified_count} files")
    print(f"✓ Skipped {len(practice_files) - modified_count} files (already have disclaimer)")

if __name__ == '__main__':
    main()

