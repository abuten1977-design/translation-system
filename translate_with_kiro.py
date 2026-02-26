#!/usr/bin/env python3
"""
Перевод через Kiro - без API ключа
"""
import argparse
import json
from pathlib import Path
from docx import Document


def extract_text(filepath):
    doc = Document(filepath)
    return '\n\n'.join([p.text for p in doc.paragraphs if p.text.strip()])


def split_text(text, chunk_size=4000):
    """Разбивает текст на части"""
    parts = []
    current = ""
    
    for para in text.split('\n\n'):
        if len(current) + len(para) > chunk_size and current:
            parts.append(current)
            current = para
        else:
            current += '\n\n' + para if current else para
    
    if current:
        parts.append(current)
    
    return parts


def save_parts(parts, base_name):
    """Сохраняет части в файлы"""
    for i, part in enumerate(parts, 1):
        filename = f"{base_name}_part{i}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(part)
        print(f"✓ Часть {i}/{len(parts)} сохранена: {filename} ({len(part)} символов)")
    return len(parts)


def create_translation_request(part_num, total_parts, text, source, target, mode):
    """Создает запрос для перевода"""
    mode_desc = {
        "literary": "художественный - естественно и красиво",
        "precise": "точный - максимальная точность и правильная терминология"
    }
    
    return f"""Переведи часть {part_num}/{total_parts} документа с {source} на {target}.
Режим: {mode_desc[mode]}

Выполни 6-этапную проверку качества:
1. Начальный перевод
2. Орфография и грамматика
3. Естественность
4. Точность смысла
5. Эмоциональный тон
6. Финализация

ТЕКСТ:
{text}

Верни только JSON:
{{
  "translated_text": "перевод",
  "quality": {{"accuracy": "оценка", "fluency": "оценка", "spelling": "оценка", "tone": "оценка"}}
}}"""


def main():
    parser = argparse.ArgumentParser(description="Перевод через Kiro")
    parser.add_argument("input", help="Входной .docx файл")
    parser.add_argument("--source", "-s", default="English", help="Язык оригинала")
    parser.add_argument("--target", "-t", default="Russian", help="Целевой язык")
    parser.add_argument("--mode", "-m", choices=["literary", "precise"], default="precise")
    parser.add_argument("--chunk-size", type=int, default=4000, help="Размер части")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ Файл не найден: {args.input}")
        return 1
    
    base_name = input_path.stem
    
    print(f"\n{'='*60}")
    print(f"ПЕРЕВОД ЧЕРЕЗ KIRO")
    print(f"{'='*60}")
    print(f"Файл: {args.input}")
    print(f"Направление: {args.source} → {args.target}")
    print(f"Режим: {args.mode}")
    print(f"{'='*60}\n")
    
    # Извлечение текста
    print("📄 Извлечение текста...")
    text = extract_text(str(input_path))
    print(f"   Извлечено: {len(text)} символов\n")
    
    # Разбивка на части
    print("✂️  Разбивка на части...")
    parts = split_text(text, args.chunk_size)
    print(f"   Создано частей: {len(parts)}\n")
    
    # Сохранение частей
    print("💾 Сохранение частей...")
    save_parts(parts, base_name)
    
    # Создание запросов
    print(f"\n{'='*60}")
    print("📝 ЗАПРОСЫ ДЛЯ ПЕРЕВОДА")
    print(f"{'='*60}\n")
    
    requests_file = f"{base_name}_requests.txt"
    with open(requests_file, 'w', encoding='utf-8') as f:
        for i, part in enumerate(parts, 1):
            request = create_translation_request(i, len(parts), part, args.source, args.target, args.mode)
            f.write(f"\n{'='*60}\n")
            f.write(f"ЗАПРОС {i}/{len(parts)}\n")
            f.write(f"{'='*60}\n\n")
            f.write(request)
            f.write("\n\n")
    
    print(f"✅ Все запросы сохранены в: {requests_file}\n")
    print(f"{'='*60}")
    print("СЛЕДУЮЩИЕ ШАГИ:")
    print(f"{'='*60}")
    print(f"1. Открой файл: {requests_file}")
    print(f"2. Скопируй запрос для части 1/{len(parts)}")
    print(f"3. Отправь мне в чат")
    print(f"4. Сохрани мой ответ в: {base_name}_part1_translated.json")
    print(f"5. Повтори для всех {len(parts)} частей")
    print(f"6. Запусти: python3 assemble_translation.py {base_name}")
    print(f"{'='*60}\n")
    
    return 0


if __name__ == "__main__":
    exit(main())
