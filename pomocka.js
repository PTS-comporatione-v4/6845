// CICADA 6845 // TEST 04 — pomocka 1/4
// Signál je zakódovaný. Prečítaj kód, nie len výstup.
// Toto je prvá zo 4 častí. Zvyšné: signal1.py, signal2.py, pomocka.cs

const signal = "TVVTUllU";  // base64, odzadu

const sprava = Buffer.from(
  signal.split("").reverse().join(""),
  "base64"
).toString("utf-8");

console.log(sprava);
