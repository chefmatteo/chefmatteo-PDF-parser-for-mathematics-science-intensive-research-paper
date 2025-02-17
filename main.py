<<<<<<< HEAD
import sys
from PyQt6.QtWidgets import QApplication
from src.ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and show the main window
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
from pathlib import Path
from src.parser import PDFParser

def main():
    parser = PDFParser(model_provider="local")
    
    # Set up paths - using raw string with r prefix
    pdf_path = Path(r"path to your document")
    
    
    output_dir = Path("extracted_content")
    output_dir.mkdir(exist_ok=True)
    
    # Process PDF
    result = parser.process_pdf(pdf_path, output_dir)
    
    # Save markdown content
    markdown_path = output_dir / "output.md"
    with open(markdown_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    # Print summary
    print(f"Processed PDF: {pdf_path}")
    print(f"Extracted {len(result['images'])} images")
    print(f"Found {len(result['equations'])} LaTeX equations")
    print(f"Output saved to: {output_dir}")

if __name__ == "__main__":
    main() 
