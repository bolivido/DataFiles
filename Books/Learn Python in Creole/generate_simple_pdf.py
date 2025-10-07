#!/usr/bin/env python3
"""
Script senp pou jenere HTML nan liv Python Essential Training nan Kreyòl Ayisyen
Pou konvèti nan PDF, sèvi ak navigatè w oswa zouti online
"""

import markdown
import os
from pathlib import Path

def markdown_to_html():
    """Konvèti Markdown nan HTML"""
    
    # Chemin fichier yo
    markdown_file = "Python_Essential_Training_Kreyol_Professional.md"
    output_html = "Python_Essential_Training_Kreyol_Professional.html"
    
    # Li fichier Markdown
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # CSS pou styling
    css = """
    <style>
    body {
        font-family: 'Times New Roman', serif;
        font-size: 12pt;
        line-height: 1.6;
        color: #333;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }
    
    h1 {
        color: #2c3e50;
        font-size: 28pt;
        border-bottom: 3px solid #3498db;
        padding-bottom: 10px;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    
    h1:first-child {
        margin-top: 0;
    }
    
    h2 {
        color: #34495e;
        font-size: 22pt;
        margin-top: 25px;
        margin-bottom: 15px;
        border-left: 4px solid #3498db;
        padding-left: 15px;
    }
    
    h3 {
        color: #2c3e50;
        font-size: 18pt;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    
    h4 {
        color: #34495e;
        font-size: 14pt;
        margin-top: 15px;
        margin-bottom: 8px;
    }
    
    h5 {
        color: #2c3e50;
        font-size: 12pt;
        margin-top: 12px;
        margin-bottom: 6px;
    }
    
    code {
        font-family: 'Courier New', monospace;
        background-color: #f8f9fa;
        padding: 3px 6px;
        border-radius: 4px;
        font-size: 11pt;
        border: 1px solid #e9ecef;
    }
    
    pre {
        background-color: #f8f9fa;
        border: 2px solid #e9ecef;
        border-radius: 8px;
        padding: 20px;
        overflow-x: auto;
        font-size: 11pt;
        line-height: 1.4;
        margin: 15px 0;
    }
    
    pre code {
        background-color: transparent;
        padding: 0;
        border: none;
        font-size: 11pt;
    }
    
    blockquote {
        border-left: 5px solid #3498db;
        margin: 15px 0;
        padding-left: 20px;
        color: #555;
        font-style: italic;
        background-color: #f8f9fa;
        padding: 15px 20px;
        border-radius: 5px;
    }
    
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 15px 0;
        font-size: 11pt;
    }
    
    th, td {
        border: 1px solid #ddd;
        padding: 12px;
        text-align: left;
    }
    
    th {
        background-color: #f2f2f2;
        font-weight: bold;
        color: #2c3e50;
    }
    
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    
    ul, ol {
        margin: 15px 0;
        padding-left: 30px;
    }
    
    li {
        margin: 8px 0;
        line-height: 1.5;
    }
    
    .emoji {
        font-size: 16pt;
    }
    
    /* Pou evite page break nan mitan kòd */
    pre, code {
        page-break-inside: avoid;
    }
    
    /* Pou evite page break nan mitan tablo */
    table {
        page-break-inside: avoid;
    }
    
    /* Styling pou list ak checklist */
    input[type="checkbox"] {
        margin-right: 8px;
    }
    
    /* Styling pou quote ak citation */
    .quote {
        background-color: #e8f4fd;
        border-left: 4px solid #3498db;
        padding: 15px;
        margin: 15px 0;
        border-radius: 5px;
    }
    
    /* Styling pou note ak tip */
    .tip {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 15px;
        margin: 15px 0;
        border-radius: 5px;
    }
    
    .warning {
        background-color: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: 15px;
        margin: 15px 0;
        border-radius: 5px;
    }
    
    /* Styling pou separator */
    hr {
        border: none;
        height: 2px;
        background-color: #3498db;
        margin: 30px 0;
    }
    
    /* Styling pou imaj */
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 10px auto;
    }
    
    /* Styling espesyal pou logo */
    img[alt*="Logo"], img[alt*="logo"] {
        max-width: 200px;
        height: auto;
        margin: 20px auto;
    }
    
    /* Print styles */
    @media print {
        body {
            font-size: 11pt;
            line-height: 1.4;
        }
        
        h1 {
            page-break-before: always;
            font-size: 24pt;
        }
        
        h1:first-child {
            page-break-before: avoid;
        }
        
        h2 {
            font-size: 18pt;
        }
        
        h3 {
            font-size: 14pt;
        }
        
        pre {
            font-size: 9pt;
        }
        
        table {
            font-size: 9pt;
        }
    }
    </style>
    """
    
    # Konvèti Markdown nan HTML
    html = markdown.markdown(
        markdown_content,
        extensions=[
            'codehilite',
            'fenced_code',
            'tables',
            'toc',
            'attr_list',
            'md_in_html'
        ]
    )
    
    # Ajoute CSS ak HTML wrapper
    full_html = f"""
    <!DOCTYPE html>
    <html lang="ht">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python Essential Training nan Kreyòl Ayisyen</title>
        <meta name="description" content="Kou konplè pou aprann Python nan lang Kreyòl Ayisyen">
        <meta name="author" content="Jamhson Boliva">
        {css}
    </head>
    <body>
        {html}
    </body>
    </html>
    """
    
    # Ekri HTML nan fichier
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"✅ HTML jenere ak siksè: {output_html}")
    print(f"📄 Gwosè fichier: {os.path.getsize(output_html) / 1024:.1f} KB")
    print("\n💡 Pou jenere PDF:")
    print("1. Ouvri fichier HTML nan navigatè w")
    print("2. Klike Ctrl+P (Windows) oswa Cmd+P (Mac)")
    print("3. Chwazi 'Save as PDF'")
    print("4. Oswa sèvi ak zouti online tankou:")
    print("   - https://www.ilovepdf.com/html-to-pdf")
    print("   - https://smallpdf.com/html-to-pdf")

if __name__ == "__main__":
    print("🚀 Kòmanse jenere HTML...")
    markdown_to_html()
    print("✨ Fini!")
