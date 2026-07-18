def append_to_log(data: str, filename="log.txt"):
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(data)
    except IOError as e:
        print(f"Error writing to storage file: {e}")