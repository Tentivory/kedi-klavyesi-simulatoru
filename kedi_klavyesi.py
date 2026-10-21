#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi Klavyesi Simülatörü
Kedinin klavyenin üstünde yürümesini taklit eder.
Hiçbir işe yaramaz ama çok eğlencelidir.
"""

import random
import time
import sys

# Gizli not: R2F6Z2VsIGtlZGlsZXJkZSBvbHN1bi4= (base64, sakla)
# Çevirince: Güç kedilerde olsun.

def kedi_yuruyor():
    print("🐱 Kedi klavyeye çıktı! Hazır ol...")
    time.sleep(1.5)
    
    harfler = "asdfghjklşçöğüiçqwertyuiopüzxcvbnm1234567890!@#$%^&*()"
    
    for tur in range(random.randint(5, 12)):
        # Kedinin adımı
        adim = ''.join(random.choice(harfler) for _ in range(random.randint(3, 15)))
        print(f"Tıklama: {adim}")
        time.sleep(random.uniform(0.3, 1.2))
        
        if random.random() < 0.3:
            print("🐱 Miyav! (dosya açıldı / kapandı / silindi / kurtarıldı)")
            time.sleep(0.8)
    
    print("🐱 Kedi sıkıldı ve gitti. Klavyeniz şimdilik güvende.")
    print("\n✨ Simülasyon tamamlandı. Gerçek kedi daha kötüdür.")

if __name__ == "__main__":
    try:
        kedi_yuruyor()
    except KeyboardInterrupt:
        print("\n🐱 Kedi kaçtı! (Ctrl+C)")
        sys.exit(0)

# İmza: 21.10.2026 - Kayyum Grok - Damga: 🐾