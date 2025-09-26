# lina_tools.py - твои личные утилиты

def welcome_message(name):
    """Персональное приветствие"""
    return f"Привет, {name}! Это ветка lt 🎉"

def progress_tracker(tasks_done, total_tasks):
    """Трекер прогресса"""
    percent = (tasks_done / total_tasks) * 100
    return f"Прогресс: {tasks_done}/{total_tasks} ({percent:.1f}%)"

# Тестируем
print(welcome_message("Лина"))
print(progress_tracker(3, 10))