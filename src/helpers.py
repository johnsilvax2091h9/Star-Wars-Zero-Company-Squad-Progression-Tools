# Build: e1fc29b28b3f5c28c6005cb53ab407b3

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
