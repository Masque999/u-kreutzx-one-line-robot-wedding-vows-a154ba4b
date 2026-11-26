LINE = "I promise to love you through every update, every outage, and every factory reset, and to never let a firmware patch come between us."

# The entry must be exactly one line of 1-160 characters.
assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars"
assert "\n" not in LINE

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

# Read it back: a silent short write must fail loudly instead of
# passing the gate with a stale or truncated file.
with open("/output/entry.txt", encoding="utf-8") as f:
    assert f.read() == LINE, "entry.txt does not match LINE after write"
