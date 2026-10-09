// CICADA 6845 // TEST 04 — pomocka 4/4
// Signál je zakódovaný. Prečítaj kód, nie len výstup.
// Toto je štvrtá zo 4 častí. Zvyšné: pomocka.js, signal1.py, signal2.py
using System;
using System.Linq;

class Pomocka {
    static void Main() {
        var data = new[]{85, 72, 81, 79, 83, 72, 90, 85, 76, 81, 90, 80, 76};
        // každý bajt je o 7 väčší, než má byť
        Console.WriteLine(new string(data.Select(b => (char)(b - 7)).ToArray()));
    }
}
