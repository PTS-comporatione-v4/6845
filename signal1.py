# CICADA 6845 // TEST 04 — pomocka 2/4
# Signál je zakódovaný. Prečítaj kód, nie len výstup.
# Toto je druhá zo 4 častí. Zvyšné: pomocka.js, signal2.py, pomocka.cs

signal = "56205449434845"  # šestnástková sústava

sprava = bytes.fromhex(signal).decode("utf-8")
print(sprava)
