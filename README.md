# 🗝️ Skeleton Key

**Skeleton Key** is a comprehensive encryption and decryption desktop application built with Python. It offers a wide range of cryptographic tools, from historical ciphers to modern industry-standard algorithms, all wrapped in a highly customizable user interface.

---

## 🚀 Features

- **Multi-Algorithm Support:** Encrypt and decrypt data using historical, bitwise, and modern symmetric methods.
- **Secure Authentication:** Integrated login system to protect access to the tool.
- **Database Logging:** Every successful operation is automatically logged to a **PostgreSQL** database (running via **Docker**).
- **Advanced History Tracking:** Query past operations with custom date range filters.
- **Reporting:** View results on a dedicated screen and export your operations to **PDF** files.
- **Dynamic UI:**
  - 🌓 Dark and Light mode support.
  - 🎨 Customizable font colors and sizes for better accessibility.

---

## 🛠️ Supported Algorithms

Skeleton Key categorizes its tools for ease of use:

### 📜 Historical & Classic Ciphers

- **Caesar:** The classic substitution cipher.
- **Vigenère:** Polyalphabetic substitution.
- **ROT13:** Simple letter substitution.
- **Atbash:** A monoalphabetic substitution cipher.

### ⚙️ Bitwise & Logic Ciphers

- **XOR:** Fundamental bitwise logic encryption.

### 🔐 Modern Symmetric Encryption

- **AES-256:** Advanced Encryption Standard (high security).
- **DES:** Data Encryption Standard.
- **Blowfish:** Fast symmetric-key block cipher.

### 🧮 Encoding & Hashing

- **Base64:** Binary-to-text encoding.
- **SHA-256:** Secure Hash Algorithm for data integrity.

---

## 🏗️ Tech Stack

- **Language:** Python
- **Database:** PostgreSQL
- **Containerization:** Docker
- **GUI Framework:** PyQt6
- **Reporting:** fpdf
