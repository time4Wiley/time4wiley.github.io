#!/usr/bin/env python3
"""
Content Management Script for Study Materials Library
用于学习资料库的内容管理脚本

This script helps you add new subjects, publishers, and grades to your GitHub Pages site
while maintaining the existing URL structure and automatically updating the index.html file.

Usage:
    python add_content.py --subject "数学" --publisher "人教版" --grade "八年级上册"

Directory structure will be created as:
    {subject}/{publisher}/{grade}/
"""

import os
import sys
import argparse
from pathlib import Path

def create_directory_structure(subject, publisher, grade):
    """Create the directory structure for new content"""
    base_path = Path(subject) / publisher / grade
    base_path.mkdir(parents=True, exist_ok=True)
    print(f"✅ Created directory: {base_path}")
    return base_path

def get_subject_icon(subject):
    """Return appropriate icon for subject"""
    icons = {
        "中国历史": "🏛️",
        "数学": "🔢",
        "语文": "📖",
        "英语": "🌍",
        "物理": "⚗️",
        "化学": "🧪",
        "生物": "🧬",
        "地理": "🌏",
        "政治": "🏛️",
        "历史": "📜"
    }
    return icons.get(subject, "📚")

def get_publisher_display_name(publisher):
    """Return display name for publisher"""
    names = {
        "人教版": "人教版 (People's Education Press)",
        "北师大版": "北师大版 (Beijing Normal University Press)",
        "苏教版": "苏教版 (Jiangsu Education Press)",
        "岳麓版": "岳麓版 (Yuelu Press)",
        "华东师大版": "华东师大版 (East China Normal University Press)"
    }
    return names.get(publisher, f"{publisher} (Publisher)")

def scan_existing_content():
    """Scan the existing directory structure to understand current content"""
    content_structure = {}
    
    # Look for existing content directories
    for subject_dir in Path('.').iterdir():
        if subject_dir.is_dir() and not subject_dir.name.startswith('.'):
            # Skip non-content directories
            if subject_dir.name in ['__pycache__', 'node_modules', '.git']:
                continue
                
            content_structure[subject_dir.name] = {}
            
            for publisher_dir in subject_dir.iterdir():
                if publisher_dir.is_dir():
                    content_structure[subject_dir.name][publisher_dir.name] = []
                    
                    for grade_dir in publisher_dir.iterdir():
                        if grade_dir.is_dir():
                            content_structure[subject_dir.name][publisher_dir.name].append(grade_dir.name)
    
    return content_structure

def count_pdf_files(base_path):
    """Count PDF files in a directory recursively"""
    return len(list(base_path.rglob("*.pdf")))

def generate_readme(subject, publisher, grade, base_path):
    """Generate a README file for the new content directory"""
    readme_content = f"""# {subject} - {publisher} - {grade}

This directory contains study materials for:
- **Subject**: {subject}
- **Publisher**: {publisher} 
- **Grade**: {grade}

## Adding Files

To add PDF files to this directory:

1. Upload your PDF files to this directory
2. Run the content management script to update the index page:
   ```bash
   python add_content.py --update-index
   ```

## Directory Structure

```
{base_path}/
├── *.pdf (your PDF files)
└── README.md (this file)
```

## Access URLs

Files in this directory will be accessible at:
- `https://time4wiley.github.io/{base_path}/filename.pdf`

For example:
- `https://time4wiley.github.io/{base_path}/textbook.pdf`
"""
    
    readme_path = base_path / "README.md"
    readme_path.write_text(readme_content, encoding='utf-8')
    print(f"✅ Created README: {readme_path}")

def main():
    parser = argparse.ArgumentParser(description='Manage content for Study Materials Library')
    parser.add_argument('--subject', required=True, help='Subject name (e.g., 数学, 中国历史)')
    parser.add_argument('--publisher', required=True, help='Publisher name (e.g., 人教版, 北师大版)')
    parser.add_argument('--grade', required=True, help='Grade level (e.g., 七年级下册, 八年级上册)')
    parser.add_argument('--update-index', action='store_true', help='Update the index.html file')
    
    args = parser.parse_args()
    
    # Create directory structure
    base_path = create_directory_structure(args.subject, args.publisher, args.grade)
    
    # Generate README
    generate_readme(args.subject, args.publisher, args.grade, base_path)
    
    # Scan existing content
    content_structure = scan_existing_content()
    
    # Calculate statistics
    total_subjects = len(content_structure)
    total_publishers = len(set(pub for subj in content_structure.values() for pub in subj.keys()))
    total_grades = sum(len(grades) for subj in content_structure.values() for grades in subj.values())
    total_pdfs = sum(count_pdf_files(Path(subj) / pub / grade) 
                    for subj, publishers in content_structure.items()
                    for pub, grades in publishers.items()
                    for grade in grades)
    
    print(f"""
📊 Content Summary:
- Subjects: {total_subjects}
- Publishers: {total_publishers}  
- Grades: {total_grades}
- PDF Files: {total_pdfs}

📁 Directory created: {base_path}
🌐 Access URL: https://time4wiley.github.io/{base_path}/

Next steps:
1. Add your PDF files to the {base_path} directory
2. Run: python add_content.py --update-index (to update the website)
3. Commit and push to GitHub
""")

if __name__ == "__main__":
    main() 