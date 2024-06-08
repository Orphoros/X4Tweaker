def not_empty(value: str) -> str:
    if not None and len(value.strip()) > 0:
        return None
    return "Must not be empty"
