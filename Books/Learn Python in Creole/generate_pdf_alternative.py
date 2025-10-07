#!/usr/bin/env python3
"""
Script alternatif pou jenere PDF nan liv Python Essential Training nan Kreyòl Ayisyen
Sèvi ak weasyprint oswa reportlab
"""

import markdown
import os
from pathlib import Path

def markdown_to_pdf_alternative():
    """Konvèti Markdown nan PDF ak weasyprint"""
    
    try:
        from weasyprint import HTML, CSS
        from weasyprint.text.fonts import FontConfiguration
        
        print("✅ WeasyPrint jwenn - jenere PDF...")
        
        # Chemin fichier yo
        markdown_file = "Python_Essential_Training_Kreyol_Professional.md"
        output_pdf = "Python_Essential_Training_Kreyol_Professional.pdf"
        
        # Li fichier Markdown
        with open(markdown_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # CSS pou PDF
        css_content = """
        @page {
            size: A4;
            margin: 2cm;
            @top-center {
                content: "Python Essential Training nan Kreyòl Ayisyen";
                font-size: 10pt;
                color: #666;
            }
            @bottom-center {
                content: counter(page);
                font-size: 10pt;
                color: #666;
            }
        }
        
        body {
            font-family: 'Times New Roman', serif;
            font-size: 11pt;
            line-height: 1.4;
            color: #333;
        }
        
        h1 {
            color: #2c3e50;
            font-size: 20pt;
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
            font-size: 16pt;
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
            font-size: 9pt;
        }
        
        pre {
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 5px;
            padding: 10px;
            overflow-x: auto;
            font-size: 9pt;
            line-height: 1.3;
            page-break-inside: avoid;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 10px 0;
            font-size: 9pt;
            page-break-inside: avoid;
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
        
        blockquote {
            border-left: 4px solid #3498db;
            margin: 0;
            padding-left: 20px;
            color: #555;
            font-style: italic;
        }
        """
        
        # Konvèti Markdown nan HTML
        html_content = markdown.markdown(
            markdown_content,
            extensions=[
                'codehilite',
                'fenced_code',
                'tables',
                'toc',
                'attr_list'
            ]
        )
        
        # Kreye HTML konplè
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Python Essential Training nan Kreyòl Ayisyen</title>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Jenere PDF
        font_config = FontConfiguration()
        html_doc = HTML(string=full_html)
        css_doc = CSS(string=css_content, font_config=font_config)
        
        html_doc.write_pdf(output_pdf, stylesheets=[css_doc], font_config=font_config)
        
        print(f"✅ PDF jenere ak siksè: {output_pdf}")
        print(f"📄 Gwosè fichier: {os.path.getsize(output_pdf) / 1024 / 1024:.1f} MB")
        
    except ImportError:
        print("❌ WeasyPrint pa enstale")
        print("💡 Pou enstale WeasyPrint:")
        print("   pip3 install weasyprint")
        print("\n🔄 Sèvi ak HTML version la pou jenere PDF:")
        print("   1. Ouvri Python_Essential_Training_Kreyol_Professional.html nan navigatè")
        print("   2. Klike Cmd+P (Mac) oswa Ctrl+P (Windows)")
        print("   3. Chwazi 'Save as PDF'")
        
    except Exception as e:
        print(f"❌ Erè nan jenere PDF: {e}")
        print("\n🔄 Sèvi ak HTML version la pou jenere PDF:")
        print("   1. Ouvri Python_Essential_Training_Kreyol_Professional.html nan navigatè")
        print("   2. Klike Cmd+P (Mac) oswa Ctrl+P (Windows)")
        print("   3. Chwazi 'Save as PDF'")

if __name__ == "__main__":
    print("🚀 Kòmanse jenere PDF ak WeasyPrint...")
    markdown_to_pdf_alternative()
    print("✨ Fini!")
