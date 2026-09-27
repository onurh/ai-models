# Sınıflandırma Şeması (SCHEMA)

Bu matrisin kalıpları. Yeni model eklerken bu dosyadaki tanımlara sadık kal.

## Alan tanımları

| Alan | Tip | Kural |
|---|---|---|
| `provider` | string | Şirket adı |
| `model` | string | Pazardaki tam ad |
| `released` | string | `YYYY-MM` veya `preview` |
| `context_tokens` | int \| null | Maksimum bağlam penceresi; yoksa `null` |
| `price_input` / `price_output` | float \| null | USD / 1M token; üretim modelleri için `null` + `billing_unit` |
| `billing_unit` | enum | `per_1m_tokens` (varsayılan) · `per_image` · `per_second` · `per_minute` |
| `input` | list | `text`, `image`, `audio`, `video`, `file` |
| `output` | list | `text`, `audio`, `image`, `video` |
| `tags` | list | Aşağıdaki etiket kümesinden |
| `open_weights` | bool | Ağırlıklar indirilebiliyor mu |
| `license` | string \| null | SPDX veya özel lisans adı |
| `status` | enum | `ga` (varsayılan) · `preview` · `sunset` (tarih `notes`'ta) |
| `best_for` | string | Tek cümlelik; pazarlama dili değil, kullanım dili |
| `notes` | string \| null | Uyarı, cache fiyatı, kapanış tarihi vb. |
| `source_date` | string | `YYYY-MM` — fiyatların doğrulandığı ay |

## Etiket kümesi (yenisini eklemeden önce burada tanımla)

| Etiket | Anlamı |
|---|---|
| `reasoning` 🧠 | Her zaman açık / yapılandırılmış derin akıl yürütme |
| `agent` 🤖 | Tool-use + çok adımlı agent işlerinde kanıtlanmış |
| `computer-use` 💻 | Ekran/terminal kontrolü (GUI agent) |
| `coding` ⌨️ | Kod üretimi ve repo-ölçekli işlerde güçlü |
| `voice` 🎙️ | Native speech-to-speech |
| `cheap-volume` | Fiyatının büyük kısmını hacim işlerine borçlu |
| `long-context` | 500K+ token bağlam |

## Doldurma kuralları

1. **Fiyat bilinmiyorsa `null` yaz, tahmin etme.** Yanlış fiyat, eksik fiyattan kötüdür.
2. **Modalite gerçekten destekleniyorsa ekle.** "Yakında geliyor" = listeye girmez.
3. **`status: sunset` modeller tabloda kalmaz** — sadece geçiş planı gerekenlere not düşülür.
4. Provider sayısı 5'i geçerse, `providers/` altına böl; tek dosya 5 provider'a kadar.
5. Her değişiklikte `source_date` güncelle.
