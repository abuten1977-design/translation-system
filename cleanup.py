#!/usr/bin/env python3
"""
Очистка промежуточных файлов после перевода
"""
import os
import glob
from pathlib import Path

def cleanup_translation_files(base_name=None):
    """Удаляет промежуточные файлы перевода"""
    
    patterns = [
        "*_part*.txt",              # Части текста
        "*_part*_translated.json",  # Переведенные части
        "*_requests.txt",           # Запросы для перевода
        "*_full_text.txt",          # Полный извлеченный текст
        "*_ru.docx",                # Промежуточные версии (не FINAL)
        "*_ru_structured.docx",     # Промежуточные версии
    ]
    
    if base_name:
        # Очистка для конкретного документа
        patterns = [f"{base_name}{p[1:]}" for p in patterns]
    
    deleted = []
    for pattern in patterns:
        for file in glob.glob(pattern):
            # Не удаляем FINAL версии
            if "FINAL" not in file:
                try:
                    os.remove(file)
                    deleted.append(file)
                    print(f"✓ Удален: {file}")
                except Exception as e:
                    print(f"✗ Ошибка при удалении {file}: {e}")
    
    return deleted

if __name__ == "__main__":
    import sys
    
    print("="*60)
    print("ОЧИСТКА ПРОМЕЖУТОЧНЫХ ФАЙЛОВ")
    print("="*60)
    
    if len(sys.argv) > 1:
        base_name = sys.argv[1]
        print(f"\nОчистка для: {base_name}")
        deleted = cleanup_translation_files(base_name)
    else:
        print("\nОчистка всех промежуточных файлов")
        deleted = cleanup_translation_files()
    
    print(f"\n{'='*60}")
    print(f"Удалено файлов: {len(deleted)}")
    print("="*60)
