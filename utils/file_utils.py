from pathlib import Path
import uuid


ALLOW_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif"]
MAX_FILE_SIZE = 5 * 1024 * 1024


def is_allowed_file(filename: Path) -> bool:
    """Проверяем, есть ли расширение в списке разрешенных."""
    ext = filename.suffix.lower()
    print(ext)
    return ext in ALLOW_EXTENSIONS


def get_unique_name(filename: Path) -> str:
    ext = filename.suffix.lower()
    unique_name = f"{uuid.uuid4().hex}{ext}"
    print(f"Новое имя файла {unique_name}")
    return unique_name


if __name__ == '__main__':
    print(is_allowed_file(Path('test.jpg')))
    print(get_unique_name(Path('test.jpg')))