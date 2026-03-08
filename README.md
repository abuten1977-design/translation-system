# 🌐 Translation Quality System

![Status](https://img.shields.io/badge/status-research%20prototype-yellow)
![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**Professional translation quality assessment system based on MQM Framework (Multidimensional Quality Metrics) and LQA methodology (Linguistic Quality Assurance).**

---

## 🎯 Problem & Solution

### Problem
Manual translation quality assessment is:
- ⏱️ **Time-consuming** - days or weeks to review large documents
- 🤷 **Subjective** - different reviewers give different assessments
- 💸 **Expensive** - requires experienced translators to review everything
- 🐛 **Error-prone** - easy to miss issues in large texts

### Solution
Automated translation quality evaluation with:
- ⚡ **Fast** - minutes instead of days
- 📊 **Objective** - numerical metrics based on MQM standard
- 💰 **Cost-effective** - focus human reviewers only on problem areas
- 🎯 **Comprehensive** - systematic 6-stage quality checking

---

## 🚀 Quick Start

```bash
# 1. Clone repository
git clone https://github.com/abuten1977-design/translation-system.git
cd translation-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run demo
./demo.sh

# Or translate your own document
python3 translate_with_kiro.py your_document.txt -s English -t Russian
```

---

## 📊 How It Works

```
┌─────────────────────┐
│  Input Document     │
│  (DOCX / MD / TXT)  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Text Splitter      │
│  (by paragraphs)    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Translation Engine │
│  (Kiro AI)          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  6-Stage QA Process │
│  (MQM + LQA)        │
│                     │
│  1. Initial         │
│  2. Spelling ✓      │
│  3. Fluency ✓       │
│  4. Accuracy ✓      │
│  5. Tone ✓          │
│  6. Finalization ✓  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Output Document    │
│  + Quality Report   │
└─────────────────────┘
```

---

## 💡 Use Cases

### 1️⃣ **Startups translating apps**
Translate app to 5 languages via AI, then verify quality automatically before launch.

### 2️⃣ **Translation agencies**
Check freelancer translations automatically, focus human reviewers only on flagged issues.

### 3️⃣ **Companies with multilingual docs**
Maintain consistent quality across 10+ language versions of technical documentation.

### 4️⃣ **AI translation researchers**
Compare GPT vs DeepL vs Google Translate with objective MQM metrics.

### 5️⃣ **Translation educators**
Analyze student translations to identify common error patterns.

---

## 📸 Example Output

### Input (English):
```
The quick brown fox jumps over the lazy dog. 
This is a sample text to demonstrate the translation quality assessment system.
```

### Output (Russian):
```
Быстрая коричневая лиса перепрыгивает через ленивую собаку.
Это образец текста для демонстрации системы оценки качества перевода.
```

### Quality Report:
```json
{
  "overall_score": 94,
  "metrics": {
    "accuracy": 95,
    "fluency": 98,
    "spelling": 100,
    "tone": 92
  },
  "issues_found": 2,
  "processing_time": "2.3 seconds"
}
```

**Result:** 94/100 quality score with 2 minor issues identified.

---

## ✨ Key Features

- ✅ **6-stage quality checking** (MQM + LQA methodology)
- ✅ **Complete formatting preservation** (fonts, sizes, colors, styles)
- ✅ **Table translation** with structure preservation
- ✅ **Two modes**: precise and literary/artistic translation
- ✅ **Works through Kiro AI** - no API key needed!
- ✅ **Quality assessment** across 4 MQM categories

---

## 📁 Project Structure

```
translation-system/
├── 📄 Core Scripts
│   ├── translate_with_kiro.py      # Main entry point
│   ├── translator.py               # Translation engine with MQM
│   ├── assemble_translation.py     # Merge translated parts
│   ├── translate_with_structure.py # Preserve document formatting
│   └── cleanup.py                  # Clean temporary files
│
├── 📚 Documentation
│   ├── README.md                   # This file
│   ├── ARCHITECTURE.md             # System design details
│   ├── KIRO_TRANSLATION_GUIDE.md   # Usage guide
│   └── QUICKSTART.md               # Quick start guide
│
├── 📂 Examples
│   ├── sample_input.txt            # Example input document
│   ├── sample_output.txt           # Example translated output
│   └── quality_report.json         # Example quality metrics
│
└── 🔧 Configuration
    ├── requirements.txt            # Python dependencies
    ├── .gitignore                  # Git exclusions
    └── demo.sh                     # Quick demo script
```

---

## 🎯 Translation Process (6 Stages)

1. **🔄 Initial Translation** - Base translation (precise/literary mode)
2. **✍️ Spelling Check** - Grammar and spelling verification
3. **🗣️ Fluency Check** - Natural language flow assessment
4. **🔍 Accuracy Check** - Meaning comparison with original
5. **🎭 Tone Check** - Emotional tone preservation
6. **✨ Finalization** - Final polishing and quality report

---

## 📊 Quality Metrics (MQM Framework)

| Metric | Description | Weight |
|--------|-------------|--------|
| **Accuracy** | Meaning preservation, no mistranslations | 30% |
| **Fluency** | Natural language flow, readability | 30% |
| **Spelling** | Grammar correctness, no typos | 20% |
| **Tone** | Emotional coloring, style preservation | 20% |

**Overall Score** = Weighted average of all metrics

---

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

---

## 💻 Installation

```bash
# Clone repository
git clone https://github.com/abuten1977-design/translation-system.git
cd translation-system

# Install dependencies
pip install -r requirements.txt
```

**Requirements:**
- Python 3.x
- python-docx library
- Kiro AI (for translation engine)

---

## 🔄 Usage Examples

### Basic Translation:
```bash
python3 translate_with_kiro.py document.docx -s English -t Russian
```

### With Literary Mode:
```bash
python3 translate_with_kiro.py document.docx -s English -t Russian --mode literary
```

### Assemble Translation:
```bash
python3 assemble_translation.py document
```

### Run Demo:
```bash
./demo.sh
```

---

## 📖 Scientific Foundation

- **MQM Framework** - EU QTLaunchPad project standard
- **LQA methodology** - Linguistic Quality Assurance
- **ISO 17100** - International translation quality standard
- **Multi-pass review** - Multi-stage quality checking

---

## 🎓 References

- [MQM Framework Research](https://arxiv.org/html/2505.14848v2)
- [Translation Quality Standards](https://translated.com/resources/translation-quality-standards-iso-certification-best-practices)
- [Multi-Agent Translation Systems](https://arxiv.org/html/2505.14848v2)

---

## 🛠️ Technologies

- **Python 3.x** - Core language
- **python-docx** - Word document processing
- **Kiro AI** - Translation engine
- **MQM Framework** - Quality assessment
- **Git** - Version control

---

## 📈 Project Status

This is a **research prototype** exploring translation quality evaluation using MQM Framework. 

**Designed for:**
- Translation quality research
- Educational purposes
- Experimentation with QA pipelines
- Proof of concept demonstrations

**Not intended for production use** without further development and testing.

---

## 🔄 Roadmap

- [x] Basic translation system
- [x] Formatting preservation
- [x] Table translation
- [x] Git version control
- [x] MQM quality metrics
- [x] 6-stage QA process
- [ ] Image caption translation
- [ ] Terminology databases
- [ ] Translation Memory integration
- [ ] Multi-language support expansion
- [ ] Web interface
- [ ] API endpoints

---

## 🤝 Contributing

This is a research project. Contributions, suggestions, and feedback are welcome!

Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests
- Share your use cases
- Suggest improvements

---

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

---

## 👥 Author

**Andriy Butenko**  
GitHub: [@abuten1977-design](https://github.com/abuten1977-design)  
Email: abuten1977@gmail.com

---

## 💬 Support

If you have questions or need help:
- Open an issue on GitHub
- Check the documentation in `/docs`
- Review examples in `/examples`

---

*Created with Kiro AI - translation system without API keys!*
