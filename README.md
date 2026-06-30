# SmartPOS-AI-Dataset
SmartPOS with AI-based stock prediction, automatic restock recommendation, supervisor approval, and distributor notification.
# 🛒 SmartPOS AI Dataset

SmartPOS AI Dataset adalah project pendukung aplikasi **Smart Point of Sale (POS)** berbasis **Android Java** yang dilengkapi Artificial Intelligence (AI) untuk membantu proses analisis penjualan, prediksi stok, dan rekomendasi restock secara otomatis.

---

# 📌 Features

- 📦 Generate Dummy Dataset
- 📈 Sales Analytics
- 🤖 AI Stock Prediction
- 📊 Daily Sales Summary
- 📉 Slow Moving Product Detection
- 🔥 Best Selling Product Detection
- 📧 Distributor Email Recommendation
- 👨‍💼 Supervisor Approval
- 📱 Android Java Ready
- 🗄 MySQL Ready
- 📚 Google Colab Ready

---

# 🧠 AI Workflow

Kasir melakukan transaksi

↓

Data Penjualan

↓

AI Menganalisis Penjualan

↓

Prediksi Stok Habis

↓

Rekomendasi Restock

↓

Supervisor Approval

↓

Distributor Menerima Email

---

# 📂 Project Structure

```
SmartPOS-AI-Dataset

│
├── dataset/
│
│ ├── products.csv
│ ├── distributors.csv
│ ├── sales.csv
│ ├── stock_history.csv
│ ├── daily_summary.csv
│ ├── ai_recommendation.csv
│ ├── popup_supervisor.csv
│ └── email_distributor.csv
│
├── notebooks/
│ └── SmartPOS_AI.ipynb
│
├── api/
│ └── app.py
│
├── model/
│ └── linear_regression.pkl
│
├── generate_dataset.py
│
├── requirements.txt
│
└── README.md
```

---

# 📊 Dataset

Dataset dibuat secara otomatis menggunakan Python.

Dataset berisi:

- 30 Produk
- 3 Distributor
- 30 Hari Penjualan
- ±1000 Transaksi
- Fast Moving Product
- Medium Moving Product
- Slow Moving Product
- Daily Summary
- Stock History
- AI Recommendation

---

# 🤖 AI Model

Model AI yang digunakan adalah

- Linear Regression

Digunakan untuk:

- Prediksi penjualan
- Prediksi stok habis
- Rekomendasi jumlah restock

---

# 📱 Android SmartPOS

Role pada aplikasi

### Kasir

- Login
- Melakukan transaksi
- Melihat stok

### Supervisor

- Melihat dashboard
- Melihat rekomendasi AI
- Approve restock

### Distributor

- Menerima email
- Mengirim barang

---

# 🚀 Technology

- Python
- Pandas
- NumPy
- Scikit Learn
- Google Colab
- MySQL
- Android Java
- GitHub

---

# 📄 License

MIT License

---

© 2026 SmartPOS AI Dataset
