# Akıllı Finansal Analiz ve Tahmin Sistemi

Bu proje, şirketlerin finansal verilerini (gelir, gider, nakit akışı) analiz edip geleceğe dönük tahminler üreten **portföy seviyesinde** bir örnek uygulamadır.

## İçerik
- `backend/` : .NET 8 Web API örnek iskeleti (başlangıç noktası)
- `database/create_tables.sql` : Veritabanı şeması ve örnek veri ekleme scripti
- `analytics/` : Python tabanlı analiz ve tahmin scriptleri (örnek ARIMA ve LSTM şablonları)
- `sample_data/` : Örnek finansal zaman serisi CSV dosyası
- `README.md` : Bu dosya

## Hızlı Başlangıç

### 1) Veritabanı
SQL Server veya PostgreSQL kullanabilirsiniz. Aşağıdaki SQL script'i örnek tablo yapısını ve örnek veriyi oluşturur.

```
psql -U <user> -d <db> -f database/create_tables.sql
```
ya da SQL Server Management Studio üzerinden çalıştırın.

### 2) Backend (.NET 8 Web API)
`backend/` dizininde basit bir .NET Web API iskeleti bulunuyor.

```bash
cd backend
dotnet restore
dotnet run
```

### 3) Analitik (Python)
Python ortamı gerektirir (3.9+ önerilir). Gerekli paketleri kurup örnek tahminleri çalıştırabilirsiniz.

```bash
cd analytics
pip install -r requirements.txt
python analyze_arima.py
python analyze_lstm.py
```

### 4) Sample Data
`sample_data/finance_timeseries.csv` dosyası aylık gelir verisi içerir. Bu dosyayı analiz scriptlerinde kullanabilirsiniz.

## Ne Bulacaksınız?

- Çalıştırılabilir .NET API iskeleti (örnek controller ve model)
- SQL tablo ve sample insert örnekleri
- Python ile ARIMA ve LSTM için hazır şablon scriptleri
- Power BI ile kullanılabilecek CSV veri örneği

## Lisans
MIT © 2025 — Olcayto Akbudak

