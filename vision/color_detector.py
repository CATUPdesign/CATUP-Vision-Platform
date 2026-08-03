def detect_color(h, s, v):

    # Black
    if v < 40:
        return "BLACK"

    # White / Gray
    if s < 40:
        if v > 180:
            return "WHITE"
        else:
            return "GRAY"

    # Hue Classification
    if h <= 10 or h >= 170:
        return "RED"

    elif h < 20:
        return "ORANGE"

    elif h < 35:
        return "YELLOW"

    elif h < 85:
        return "GREEN"

    elif h < 100:
        return "CYAN"

    elif h < 130:
        return "BLUE"

    elif h < 155:
        return "PURPLE"

    else:
        return "PINK"