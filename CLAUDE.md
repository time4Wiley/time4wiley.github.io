# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a GitHub Pages static website (time4wiley.github.io) that serves as an educational resource portal for Chinese middle school students. The site hosts PDF textbooks and study materials organized by subject, publisher, and grade level.

## Key Architecture

### Site Structure
- **Static HTML/CSS**: No JavaScript frameworks, build tools, or external dependencies
- **Content Organization**: `/{subject}/{publisher}/{grade}/` directory hierarchy
- **Inline Styles**: All CSS is embedded within HTML files (no external stylesheets)
- **Manual Updates**: HTML files are edited directly without templating

### Important Files
- `index.html`: Main library page displaying all available textbooks
- `add_content.py`: Python script for creating new content directories
- `6th-2nd-haidian-chinese-exam-review.html`: Example of specialized study guide page

## Development Commands

### Adding New Content
```bash
# Create directory structure for new subject/publisher/grade
python add_content.py --subject "数学" --publisher "人教版" --grade "八年级上册"

# Count statistics (subjects, publishers, grades, PDFs)
python add_content.py --count
```

### Deployment
```bash
# Commit and push to deploy (GitHub Pages auto-deploys from main branch)
git add .
git commit -m "Add new content"
git push origin main
```

## Content Management Workflow

1. **Add New Subject/Grade**:
   - Run `add_content.py` to create directory structure
   - Place PDF files in the created directory
   - Manually update `index.html` to add new module cards

2. **Update Existing Content**:
   - Add PDFs directly to existing directories
   - Update file links and sizes in `index.html`

3. **Create Specialized Pages**:
   - Copy existing HTML structure (e.g., exam review page)
   - Maintain inline CSS pattern
   - Include bilingual labels (Chinese/English)

## HTML/CSS Patterns

- **Module Cards**: Use `<div class="module">` with gradient backgrounds
- **File Links**: Include file size in parentheses: `<a href="path/to/file.pdf">Title (X.X MB)</a>`
- **Icons**: Use emoji icons for visual hierarchy
- **Responsive Design**: CSS Grid for layout, media queries for mobile
- **Print Styles**: Hidden elements marked with `@media print` rules

## Important Notes

- The `--update-index` flag in `add_content.py` is not implemented
- All content updates to `index.html` must be done manually
- Maintain bilingual labels throughout (Chinese primary, English in parentheses)
- File paths must match the GitHub Pages URL structure
- The `.nojekyll` file prevents Jekyll processing - do not remove