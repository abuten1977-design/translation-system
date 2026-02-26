#!/usr/bin/env python3
"""
CLI для системы качественного перевода
"""
import argparse
import sys
from pathlib import Path
from translator import QualityTranslator, extract_text_from_docx, save_translation


def main():
    parser = argparse.ArgumentParser(
        description="Система качественного перевода с многоэтапной проверкой"
    )
    parser.add_argument("input", help="Входной файл (.docx)")
    parser.add_argument("output", help="Выходной файл (.docx)")
    parser.add_argument("--source", "-s", required=True, help="Язык оригинала (например: English)")
    parser.add_argument("--target", "-t", required=True, help="Целевой язык (например: Russian)")
    parser.add_argument(
        "--mode", "-m",
        choices=["literary", "precise"],
        default="precise",
        help="Режим перевода: literary (художественный) или precise (точный)"
    )
    
    args = parser.parse_args()
    
    # Проверка входного файла
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ Ошибка: файл {args.input} не найден")
        sys.exit(1)
    
    if input_path.suffix != ".docx":
        print(f"❌ Ошибка: поддерживаются только .docx файлы")
        sys.exit(1)
    
    print(f"\n{'='*60}")
    print(f"СИСТЕМА КАЧЕСТВЕННОГО ПЕРЕВОДА")
    print(f"{'='*60}")
    print(f"Файл: {args.input}")
    print(f"Направление: {args.source} → {args.target}")
    print(f"Режим: {'Художественный' if args.mode == 'literary' else 'Точный'}")
    print(f"{'='*60}\n")
    
    # Извлечение текста
    print("📄 Извлечение текста из документа...")
    text = extract_text_from_docx(str(input_path))
    print(f"   Извлечено {len(text)} символов\n")
    
    # Перевод
    translator = QualityTranslator()
    result = translator.translate(text, args.source, args.target, args.mode)
    
    # Сохранение
    print(f"\n💾 Сохранение результата в {args.output}...")
    save_translation(result, args.output)
    
    # Итоговый отчет
    print(f"\n{'='*60}")
    print("✅ ПЕРЕВОД ЗАВЕРШЕН")
    print(f"{'='*60}")
    print("\nОценка качества (MQM):")
    print(f"  • Точность (Accuracy):  {result.final_score['accuracy']}")
    print(f"  • Беглость (Fluency):   {result.final_score['fluency']}")
    print(f"  • Орфография (Spelling): {result.final_score['spelling']}")
    print(f"  • Тон (Tone):           {result.final_score['tone']}")
    print(f"\nРезультат сохранен: {args.output}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
