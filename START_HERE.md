# 🎯 Инструкция для запуска

## Шаг 1: Получи API ключ Anthropic

1. Зайди на https://console.anthropic.com/
2. Зарегистрируйся или войди
3. Создай API ключ
4. Скопируй его

## Шаг 2: Установи API ключ

```bash
export ANTHROPIC_API_KEY="sk-ant-api03-твой-ключ-здесь"
```

Чтобы ключ сохранился между сессиями, добавь в ~/.bashrc:
```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-твой-ключ-здесь"' >> ~/.bashrc
source ~/.bashrc
```

## Шаг 3: Проверь установку

```bash
# Проверь что ключ установлен
echo $ANTHROPIC_API_KEY

# Проверь что библиотеки установлены
python3 -c "import docx, anthropic; print('✅ Все готово!')"
```

## Шаг 4: Запусти перевод

### Вариант 1: Точный перевод (рекомендуется для документов)
```bash
python3 translate.py call_for_proposals.docx call_for_proposals_ru.docx \
  --source English --target Russian --mode precise
```

### Вариант 2: Художественный перевод (для креативных текстов)
```bash
python3 translate.py call_for_proposals.docx call_for_proposals_ru.docx \
  --source English --target Russian --mode literary
```

### Вариант 3: Второй документ
```bash
python3 translate.py appendix_i_-_application_form.docx appendix_i_ru.docx \
  --source English --target Russian --mode precise
```

## Что произойдет?

Система выполнит 6 этапов проверки:
1. 🔄 Начальный перевод
2. ✍️ Проверка орфографии и грамматики
3. 🗣️ Проверка естественности
4. 🔍 Сравнение смысла
5. 🎭 Сравнение эмоционального тона
6. ✨ Финализация

## Результат

Ты получишь .docx файл с:
- Переведенным текстом
- Отчетом о качестве (MQM оценки)

## Если что-то не работает

### Ошибка: "No module named 'docx'"
```bash
pip install --user python-docx anthropic
```

### Ошибка: "ANTHROPIC_API_KEY not found"
```bash
export ANTHROPIC_API_KEY="твой-ключ"
```

### Ошибка: "File not found"
Проверь что ты в правильной директории:
```bash
cd /home/butenhome/translation
ls -la *.docx
```

## Дополнительные опции

### Помощь
```bash
python3 translate.py --help
```

### Короткие флаги
```bash
python3 translate.py input.docx output.docx -s English -t Russian -m precise
```

## Примеры для разных языков

### Английский → Русский
```bash
python3 translate.py doc.docx doc_ru.docx -s English -t Russian -m precise
```

### Русский → Английский
```bash
python3 translate.py doc.docx doc_en.docx -s Russian -t English -m precise
```

### Английский → Немецкий
```bash
python3 translate.py doc.docx doc_de.docx -s English -t German -m precise
```

## Советы

1. **Для официальных документов** используй режим `precise`
2. **Для маркетинговых текстов** попробуй режим `literary`
3. **Большие документы** могут занять несколько минут
4. **Проверяй результат** - система хороша, но не идеальна
5. **Сохраняй оригиналы** - всегда держи backup

## Стоимость

Anthropic Claude API платный. Примерная стоимость:
- Документ на 1000 слов ≈ $0.10-0.30
- Проверяй актуальные цены на https://www.anthropic.com/pricing

## Следующие шаги

1. Протестируй на своих документах
2. Сравни качество с другими переводчиками
3. Дай обратную связь для улучшения
4. Смотри ROADMAP.md для будущих функций

---

**Готов начать? Запускай команду выше! 🚀**
