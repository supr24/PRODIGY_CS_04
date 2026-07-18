class KeyBuffer:
    def __init__(self, max_size=20):
        self.buffer = []
        self.max_size = max_size

    def add(self, character: str):
        if character:  # Only add non-empty strings
            self.buffer.append(character)

    def is_full(self) -> bool:
        return len(self.buffer) >= self.max_size

    def flush(self) -> str:
        data = "".join(self.buffer)
        self.buffer.clear()
        return data