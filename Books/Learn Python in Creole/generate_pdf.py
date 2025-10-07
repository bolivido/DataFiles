#!/usr/bin/env python3
"""
Script pou jenere PDF nan liv Python Essential Training nan Kreyòl Ayisyen
"""

import markdown
import pdfkit
from pathlib import Path
import os

def markdown_to_pdf():
    """Konvèti Markdown nan PDF"""
    
    # Chemin fichier yo
    markdown_file = "Python_Essential_Training_Kreyol_Professional.md"
    output_pdf = "Python_Essential_Training_Kreyol_Professional.pdf"
    
    # Li fichier Markdown
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Konfigirasyon PDF
    options = {
        'page-size': 'A4',
        'margin-top': '1in',
        'margin-right': '1in',
        'margin-bottom': '1in',
        'margin-left': '1in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': None,
        'print-media-type': None,
        'disable-smart-shrinking': None,
        'zoom': '1.2',
        'footer-center': '[page]',
        'footer-font-size': '10',
        'footer-spacing': '10',
        'header-center': 'Python Essential Training nan Kreyòl Ayisyen',
        'header-font-size': '10',
        'header-spacing': '10'
    }
    
    # CSS pou styling
    css = """
    <style>
    @page {
        size: A4;
        margin: 1in;
    }
    
    body {
        font-family: 'Times New Roman', serif;
        font-size: 11pt;
        line-height: 1.4;
        color: #333;
    }
    
    h1 {
        color: #2c3e50;
        font-size: 24pt;
        page-break-before: always;
        margin-top: 0;
        border-bottom: 2px solid #3498db;
        padding-bottom: 10px;
    }
    
    h1:first-child {
        page-break-before: avoid;
    }
    
    h2 {
        color: #34495e;
        font-size: 18pt;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    
    h3 {
        color: #2c3e50;
        font-size: 14pt;
        margin-top: 15px;
        margin-bottom: 8px;
    }
    
    h4 {
        color: #34495e;
        font-size: 12pt;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    
    code {
        font-family: 'Courier New', monospace;
        background-color: #f8f9fa;
        padding: 2px 4px;
        border-radius: 3px;
        font-size: 10pt;
    }
    
    pre {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 5px;
        padding: 15px;
        overflow-x: auto;
        font-size: 10pt;
        line-height: 1.3;
    }
    
    pre code {
        background-color: transparent;
        padding: 0;
    }
    
    blockquote {
        border-left: 4px solid #3498db;
        margin: 0;
        padding-left: 20px;
        color: #555;
        font-style: italic;
    }
    
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 10px 0;
    }
    
    th, td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }
    
    th {
        background-color: #f2f2f2;
        font-weight: bold;
    }
    
    ul, ol {
        margin: 10px 0;
        padding-left: 20px;
    }
    
    li {
        margin: 5px 0;
    }
    
    .emoji {
        font-size: 14pt;
    }
    
    /* Pou evite page break nan mitan kòd */
    pre, code {
        page-break-inside: avoid;
    }
    
    /* Pou evite page break nan mitan tablo */
    table {
        page-break-inside: avoid;
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
            'attr_list'
        ]
    )
    
    # Ajoute CSS ak HTML wrapper
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Python Essential Training nan Kreyòl Ayisyen</title>
        {css}
    </head>
    <body>
        {html}
    </body>
    </html>
    """
    
    try:
        # Jenere PDF
        pdfkit.from_string(full_html, output_pdf, options=options)
        print(f"✅ PDF jenere ak siksè: {output_pdf}")
        print(f"📄 Gwosè fichier: {os.path.getsize(output_pdf) / 1024 / 1024:.1f} MB")
        
    except Exception as e:
        print(f"❌ Erè nan jenere PDF: {e}")
        print("💡 Asire w ke wkhtmltopdf enstale sou sistèm ou")

if __name__ == "__main__":
    print("🚀 Kòmanse jenere PDF...")
    markdown_to_pdf()
    print("✨ Fini!")
