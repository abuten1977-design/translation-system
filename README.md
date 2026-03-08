# 🌐 Translation Quality System

Professional document translation system based on **MQM Framework** (Multidimensional Quality Metrics) and **LQA methodology** (Linguistic Quality Assurance) with complete formatting preservation.

## ✨ Key Features

- ✅ **6-stage quality checking** (MQM + LQA methodology)
- ✅ **Complete formatting preservation** (fonts, sizes, colors, styles)
- ✅ **Table translation** with structure preservation
- ✅ **Two modes**: precise and literary/artistic translation
- ✅ **Works through Kiro AI** - no API key needed!
- ✅ **Quality assessment** across 4 MQM categories

## 🎯 Translation Process (6 Stages)

1. **🔄 Initial Translation** - base translation (precise/literary mode)
2. **✍️ Spelling Check** - grammar and spelling verification
3. **🗣️ Fluency Check** - natural language flow assessment
4. **🔍 Accuracy Check** - meaning comparison with original
5. **🎭 Tone Check** - emotional tone preservation
6. **✨ Finalization** - final polishing

## 🚀 Quick Start

### Translate a document:

```bash
# 1. Prepare document for translation
python3 translate_with_kiro.py document.docx -s English -t Russian

# 2. AI translates all parts (just say "translate")

# 3. Assemble with structure preservation
python3 translate_with_structure.py document
```

### Or simply say:
```
"Translate document.docx"
```
And the AI will do everything automatically!

## 📊 Quality Metrics

### MQM Quality Assessment:
- **Accuracy** - meaning preservation
- **Fluency** - natural language flow
- **Spelling** - grammar correctness
- **Tone** - emotional coloring preservation

## 🔧 Technical Details

### Formatting Preservation:
- Fonts (name, size, color)
- Styles (bold, italic, underline)
- Alignment (left, center, right, justify)
- Indents and spacing
- Tables (structure, borders, column widths)
- Numbering and bullets

### Supported Formats:
- Microsoft Word (.docx)
- Markdown (.md)
- Plain text (.txt)

## 📁 Project Structure

```
translation-system/
├── 🎯 Core Scripts
│   ├── translate_with_kiro.py      # Translation preparation
│   ├── assemble_translation.py     # Parts assembly
│   ├── translate_with_structure.py # Assembly with formatting
│   ├── translator.py               # Core translation engine
│   └── cleanup.py                  # Cleanup utilities
│
├── 📚 Documentation
│   ├── README.md
│   ├── ARCHITECTURE.md
│   ├── KIRO_TRANSLATION_GUIDE.md
│   └── QUICKSTART.md
│
└── 🔧 Configuration
    └── .gitignore
```

## 📖 Scientific Foundation

- **MQM Framework** - EU QTLaunchPad project
- **LQA methodology** - Linguistic Quality Assurance
- **ISO 17100** - international translation quality standard
- **Multi-pass review** - multi-stage quality checking

## 🎓 References

- [MQM Framework Research](https://arxiv.org/html/2505.14848v2)
- [Translation Quality Standards](https://translated.com/resources/translation-quality-standards-iso-certification-best-practices)
- [Multi-Agent Translation Systems](https://arxiv.org/html/2505.14848v2)

## 💻 Installation

```bash
# Clone repository
git clone https://github.com/abuten1977-design/translation-system.git
cd translation-system

# Install dependencies
pip install python-docx
```

## 🔄 Usage Examples

### Basic Translation:
```bash
python3 translate_with_kiro.py document.docx -s English -t Russian
```

### With Custom Mode:
```bash
python3 translate_with_kiro.py document.docx -s English -t Russian --mode literary
```

### Assembly:
```bash
python3 assemble_translation.py document
```

## 🛠️ Technologies

- **Python 3.x**
- **python-docx** - Word document processing
- **Kiro AI** - translation engine
- **MQM Framework** - quality assessment
- **Git** - version control

## 🔄 Roadmap

- [x] Basic translation system
- [x] Formatting preservation
- [x] Table translation
- [x] Git version control
- [ ] Image caption translation
- [ ] Terminology databases
- [ ] Translation Memory integration
- [ ] Multi-language support expansion

## 📝 License

MIT License

Copyright (c) 2026 Andriy Butenko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 👥 Author

**Andriy Butenko**  
GitHub: [@abuten1977-design](https://github.com/abuten1977-design)  
Email: abuten1977@gmail.com

---

*Created with Kiro AI - translation system without API keys!*
