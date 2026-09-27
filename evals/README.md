# Benchmark — deneme tahtası

Ürün değil, oyun alanı. Amaç: aynı prompt'u farklı modellere atıp **hangi yöntemin hangi modelde daha iyi işlediğini** görmek. Çıktılar burada durur, gözlemler `results.md`'de birikir, zamanla ana matristeki tag'lere yansır.

## Nasıl yapılır

1. `prompts/` içinden bir prompt seç.
2. Modelin sohbet arayüzüne (veya API'sine) yapıştır, çıktıyı al.
3. Çıktıyı `outputs/<model-id>/<prompt-id>.md` olarak kaydet. Örn: `outputs/kimi-k3/tr-register.md`
4. Bir cümlelik gözlemi `results.md`'ye ekle: ne işe yaradı, ne patladı.

Hepsi bu. Koşturucu, jüri, anahtar yok — çıktıyı sen üretiyorsun, karşılaştırmayı da sen yapıyorsun.

## İlkeler

- **Çıktılar her zaman kaydedilir.** Karşılaştırma ancak ham çıktı durduğunda adildir.
- **Gözlem dili net olsun:** "kısıt 2'yi sessizce bozdu" > "kötüymüş".
- **Her prompt'un altında HTML yorumu var** — neye bakacağını hatırlatır, modele gitmez.
- **Yeni prompt eklemek serbest:** kafana göre `prompts/` altına dosya at, üstüne `id` + `capability` yaz.
