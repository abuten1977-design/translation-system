#!/bin/bash
# Пример использования системы перевода

# 1. Установи API ключ Anthropic (получи на https://console.anthropic.com/)
# export ANTHROPIC_API_KEY="your-api-key-here"

# 2. Примеры команд для перевода твоих документов:

# Точный перевод call_for_proposals.docx
python3 translate.py call_for_proposals.docx call_for_proposals_ru.docx \
  --source English --target Russian --mode precise

# Точный перевод appendix_i_-_application_form.docx
python3 translate.py appendix_i_-_application_form.docx appendix_i_ru.docx \
  --source English --target Russian --mode precise

# Художественный перевод (если нужен более свободный стиль)
# python3 translate.py call_for_proposals.docx call_for_proposals_ru_literary.docx \
#   --source English --target Russian --mode literary
