def encrypt(text, key):
    key_indices = sorted(range(len(key)), key=lambda k: key[k])
    rows, extra = divmod(len(text), len(key))
    if extra > 0:
        rows += 1
    grid = [['' for _ in key] for _ in range(rows)]
    for idx, char in enumerate(text):
        grid[idx // len(key)][idx % len(key)] = char
    return ''.join(''.join(grid[r][c] for r in range(rows)) for c in key_indices)

def decrypt(text, key):
    key_indices = sorted(range(len(key)), key=lambda k: key[k])
    rows, extra = divmod(len(text), len(key))
    if extra > 0:
        rows += 1
    grid = [['' for _ in key] for _ in range(rows)]
    text_index = 0
    for idx in key_indices:
        for r in range(rows):
            if text_index < len(text):
                grid[r][idx] = text[text_index]
                text_index += 1
    return ''.join(''.join(grid[r]) for r in range(rows)).strip()
