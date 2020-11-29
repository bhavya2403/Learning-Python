def hurdleRace(k, height):
    need = max(height) - k
    if need > 0:
        return need
    else:
        return 0