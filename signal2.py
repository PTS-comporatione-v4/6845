# CICADA 6845 // TEST 04 — pomocka 3/4
# Signál je zakódovaný. Prečítaj kód, nie len výstup.
# Toto je tretia zo 4 častí. Zvyšné: pomocka.js, signal1.py, pomocka.cs

signal = "KRYRUL"  # každé písmeno je posunuté o 3 dopredu

sprava = "".join(chr((ord(c) - 65 - 3) % 26 + 65) for c in signal)
print(sprava)
