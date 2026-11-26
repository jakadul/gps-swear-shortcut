"""make.fun entry: u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9

Emits one judged text line into the output file. Offline, deterministic.
"""
import os

ENTRY_TEXT = "I was not lost. I was checking whether you were. You are."
GATE_LIMIT = 200


def emit() -> int:
    value = ENTRY_TEXT
    n = len(value)
    assert value.strip(), "entry text is empty"
    assert 1 <= n <= GATE_LIMIT, f"{n} code points outside 1..{GATE_LIMIT}"
    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target, exist_ok=True)
    handle = open(os.path.join(target, "entry.txt"), "w", encoding="utf-8")
    try:
        handle.write(value)
    finally:
        handle.close()
    return n


if __name__ == "__main__":
    count = emit()
    print(f"entry.txt written with {count} code points")