# 🚀 Быстрый старт

## 1. Установи API ключ

Получи ключ на https://console.anthropic.com/ и установи:

```bash
export ANTHROPIC_API_KEY="твой-ключ-здесь"
```

## 2. Запусти перевод

```bash
# Точный перевод
python3 translate.py call_for_proposals.docx call_for_proposals_ru.docx \
  -s English -t Russian -m precise

# Художественный перевод
python3 translate.py call_for_proposals.docx call_for_proposals_ru.docx \
  -s English -t Russian -m literary
```

## 3. Получи результат

Система создаст .docx файл с:
- Переведенным текстом
- Отчетом о качестве (MQM оценки)

---

Подробная документация в [README.md](README.md)
