# AI Model Karşılaştırma Matrisi

5 büyük provider'ın güncel modelleri: fiyat, bağlam penceresi, girdi/çıktı modaliteleri ve kabiliyet sınıflandırması.

> **Güncelleme: Eylül 2026.** Fiyatlar 1M token başına USD (girdi / çıktı). Kaynak: sağlayıcı fiyat sayfaları + Artificial Analysis, Eylül 2026 doğrulaması.

## Sütunların anlamı (sınıflandırma kalıbı)

Tam tanımlar ve ekleme kuralları için [SCHEMA.md](SCHEMA.md)'ye bak. Kısaca:

- **Girdi**: metin · görsel · ses · video · dosya
- **Çıktı**: metin · ses (TTS) · görsel · video
- **Etiketler**: 🧠 reasoning · 🤖 agent/tool-use · 💻 computer use · ⌨️ kod · 🔓 açık ağırlık (self-host)

### Lejant
✅ = yerleşik ve genel erişim · 🔶 = kısmi / önizleme / üst planda · — = yok

---

## OpenAI

| Model | Bağlam | $ girdi | $ çıktı | Girdi | Çıktı | Etiketler |
|---|---|---|---|---|---|---|
| **GPT-6 Astra** | 1.05M | 10.00 | 50.00 | metin, görsel, dosya | metin | 🧠🤖💻⌨️ |
| **GPT-6 Sol** | 1.05M | 2.00 | 10.00 | metin, görsel, dosya | metin | 🤖⌨️ |
| **GPT-6 Luna** | 1.05M | 0.10 | 0.50 | metin, görsel, dosya | metin | 🤖 (yüksek hacim, ucuz) |
| **GPT Image 2** | — | görüntü başına | görüntü başına | metin, görsel | görsel | En yüksek arena skoru (Elo ~1339) |
| **Whisper v4** | — | dk başına | — | ses | metin | Transkripsiyon standardı |
| **Sora 2** ⚠️ | — | sn başına | — | metin, görsel | video | ⚠️ API kapanışı: 24 Eylül 2026 |

*ChatGPT sesli konuşma (voice mode) metin modeli + ayrı ses katmanıyla çalışır; TTS API'si mevcuttur.*

## Anthropic

| Model | Bağlam | $ girdi | $ çıktı | Girdi | Çıktı | Etiketler |
|---|---|---|---|---|---|---|
| **Claude Fable 5.1** | 1M | 10.00 | 50.00 | metin, görsel, dosya | metin | 🧠🤖💻⌨️ |
| **Claude Opus 5.5** | 1M | 4.00 | 20.00 | metin, görsel, dosya | metin | 🤖💻⌨️ |
| **Claude Sonnet 5** | 1M | 2.00 | 10.00 | metin, görsel, dosya | metin | 🤖💻⌨️ |

*Görsel üretimi ve TTS yok. Cache okuma $0.25/1M (Fable) — uzun agent oturumlarında en ucuzu.*

## Google

| Model | Bağlam | $ girdi | $ çıktı | Girdi | Çıktı | Etiketler |
|---|---|---|---|---|---|---|
| **Gemini 3.1 Pro** | 200K+ (kademeli) | 2.00 | 12.00 | metin, görsel, ses, video, dosya | metin | 🧠🤖 |
| **Gemini 3.8 Flash** | 1M | 0.75 | 3.75 | metin, görsel, ses, video, dosya | metin | 🤖 (hacim işleri) |
| **Gemini 3.8 Live / ET** | oturum | 0.005/dk | 0.018/dk | ses | ses | 🎙️ S2S kalite endeksi #1 (82.6) |
| **Imagen (Nano Banana Pro)** | — | görüntü başına | — | metin, görsel | görsel | 4K çıktı, edit |
| **Veo 3.1** | — | sn başına | — | metin, görsel | video + ses | Kurumsal/SLA seçeneği |

## xAI

| Model | Bağlam | $ girdi | $ çıktı | Girdi | Çıktı | Etiketler |
|---|---|---|---|---|---|---|
| **Grok 4.7** | 500K | 2.00 | 6.00 | metin, görsel, dosya | metin | 🤖⌨️ (fiyat/performans) |
| **Grok Imagine** | — | görüntü/sn başına | — | metin, görsel | görsel, video | Görsel→video |

*Canlı X verisi erişimi. En açık içerik politikası frontier sınıfında.*

## Moonshot AI (Kimi)

| Model | Bağlam | $ girdi | $ çıktı | Girdi | Çıktı | Etiketler |
|---|---|---|---|---|---|---|
| **Kimi K3** | 1M | 2.20* | 8.00* | metin, görsel, video, dosya | metin | 🧠🤖⌨️🔓 2.8T MoE |
| **Kimi K2.8 Preview** | 1M | 0.60* | 2.50* | metin, görsel, video | metin | ⌨️🤖 (K3'e yakın, ucuz) |

*\*yaklaşık; cache girdi daha ucuz. K3 açık ağırlıklı (kendi lisansı, self-host mümkün).*

---

## Hızlı Karşılaştırma (amiral gemileri)

| Kabiliyet | En iyi seçenek |
|---|---|
| En zor akıl yürütme | GPT-6 Astra ≈ Claude Fable 5.1 |
| Uzun süreli agent / otonom iş | Claude Fable 5.1 (ucuz cache) |
| Kodlama (günlük) | Claude Sonnet 5 · Kimi K2.8 Preview |
| Kodlama (bütçe) | Grok 4.7 · DeepSeek V4.1 Flash |
| Sesli konuşma (S2S) | Gemini 3.8 Live — rakipsiz |
| Görsel üretim | GPT Image 2 (kalite) · Imagen (4K) |
| Video üretim | Kling 3.0 (fiyat) · Veo 3.1 (kurumsal) |
| Self-host / veri mahremiyeti | Kimi K3 (en güçlü açık model) |
| Hacimli ucuz iş | Gemini 3.8 Flash · GPT-6 Luna |

---

## Dosyalar

- [`models.yaml`](models.yaml) — aynı verinin makine okunur hali (agent'lar burayı tüketsin)
- [`SCHEMA.md`](SCHEMA.md) — sütun tanımları ve yeni model ekleme kuralı
