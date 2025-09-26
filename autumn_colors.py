# autumn_colors.py - осенние цвета
autumn_palette = {
    "рыжий": "#FF7F50",
    "золотой": "#FFD700", 
    "бордовый": "#800000",
    "оливковый": "#808000",
    "коричневый": "#8B4513"
}

def get_autumn_color(name):
    """Возвращает осенний цвет по названию"""
    return autumn_palette.get(name, "#000000")

def generate_autumn_gradient():
    """Генерирует осенний градиент"""
    return ["#FF7F50", "#FF8C00", "#FFA500", "#FFD700"]