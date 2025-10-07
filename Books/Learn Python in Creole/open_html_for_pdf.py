#!/usr/bin/env python3
"""
Script pou louvri HTML nan navigatè pou jenere PDF
"""

import webbrowser
import os
from pathlib import Path

def open_html_for_pdf():
    """Louvri HTML nan navigatè pou jenere PDF"""
    
    html_file = "Python_Essential_Training_Kreyol_Professional.html"
    
    if os.path.exists(html_file):
        # Jwenn chemin absoli
        html_path = os.path.abspath(html_file)
        
        print(f"🚀 Lansi navigatè w...")
        print(f"📄 Fichier: {html_path}")
        
        # Louvri nan navigatè
        webbrowser.open(f"file://{html_path}")
        
        print("\n✅ HTML louvri nan navigatè w!")
        print("\n📋 Enstriksyon pou jenere PDF:")
        print("1. ⏳ Tann navigatè a fini chaje paj la")
        print("2. ⌨️  Klike Cmd+P (Mac) oswa Ctrl+P (Windows)")
        print("3. 📄 Chwazi 'Save as PDF' nan meni Print")
        print("4. ⚙️  Konfigirasyon rekòmande:")
        print("   - Paper size: A4")
        print("   - Margins: Normal")
        print("   - Background graphics: ✅ (Check this)")
        print("   - Scale: 100%")
        print("5. 💾 Chwazi kote pou sove PDF a")
        print("6. 🎉 Klike 'Save'")
        
        print(f"\n💡 Konsèy:")
        print("- Si paj la long, navigatè a ka pran tan pou chaje")
        print("- Asire w ke 'Background graphics' check pou gen koulè")
        print("- Ou ka adjust margins si nesesè")
        
    else:
        print(f"❌ Fichier {html_file} pa jwenn!")
        print("💡 Kouri 'python3 generate_simple_pdf.py' premye")

if __name__ == "__main__":
    open_html_for_pdf()
