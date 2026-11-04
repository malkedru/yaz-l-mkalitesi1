# Yapay Zekâ Destekli Kod İnceleme Asistanı

Streamlit ve Google Gemini API kullanan bu eğitim projesi, verilen kod parçaları için yapılandırılmış kalite incelemesi ve iyileştirme önerileri üretir.

## Başlangıç

Python 3.10 veya üzeri gerekir.

1. Sanal ortam oluşturup etkinleştirin.
2. Bağımlılıkları yükleyin: `python -m pip install -r requirements.txt`
3. `.env.example` dosyasını `.env` olarak kopyalayıp `GEMINI_API_KEY` değerini kendi Google AI Studio anahtarınızla değiştirin. Satır `GEMINI_API_KEY=...` biçiminde olmalıdır.
4. Uygulamayı başlatın: `streamlit run app.py`

Gerçek API anahtarını kaynak koda veya sürüm kontrolüne eklemeyin. Model seçimi isteğe bağlı olarak `GEMINI_MODEL` ortam değişkeninden yapılabilir.

## Kalite inceleme ölçütleri

İnceleme istemi ve uygulama arayüzü aşağıdaki kalite özelliklerini kapsar:

- **Doğruluk ve güvenilirlik:** hata yönetimi, sınır durumları ve doğrulanabilir davranış sorunları.
- **Güvenlik:** kodda görülen güvenlik açıkları ve hassas veri riskleri.
- **Bakım kolaylığı:** okunabilirlik, adlandırma, modülerlik ve tekrarın azaltılması.
- **Performans:** yalnızca anlamlı ve gerekçelendirilebilir performans sorunları.
- **Test edilebilirlik:** eksik senaryolar ve önerilen testler.

Bu ölçütler ISO/IEC 25010 kalite modeliyle ilişkili yazılım kalite özelliklerine dayanır. Yapay zekâ çıktısı otomatik bir sertifika veya kesin güvenlik denetimi değildir; bulgular kod ve testlerle doğrulanmalıdır.

## Tasarım ve kalite kararları

- Arayüz (`app.py`) ile Gemini entegrasyonu (`services/gemini_service.py`) ayrıdır.
- Anahtar ortam değişkeninden okunur; API hatalarının ayrıntıları kullanıcıya gösterilmez ve uygulama günlüğüne yazılır.
- Boş ve aşırı uzun girdiler API çağrısından önce reddedilir.
- Geçici servis hataları sınırlı sayıda üstel beklemeyle yeniden denenir.
- Model, `GEMINI_MODEL` ile yapılandırılabilir; varsayılan model `gemini-3.8-flash` değeridir.
- Python kodu PEP 8 biçimlendirme kurallarını izlemelidir; lint ayarları `pyproject.toml` içinde tanımlıdır.

## Proje yapısı

```text
app.py                    # Streamlit arayüzü
services/gemini_service.py # Gemini istemcisi ve inceleme iş mantığı
requirements.txt          # Uygulama bağımlılıkları
pyproject.toml            # Ruff lint yapılandırması
.env.example              # Güvenli yapılandırma örneği
```
