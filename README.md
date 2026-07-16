# E-Bazar Marketplace

Django asosida yozilgan ko'p funksiyali marketplace loyihasi. Loyiha xaridor va sotuvchi rollarini qo'llab-quvvatlaydi: mahsulot qo'shish, mahsulotlarni ko'rish, saqlash, buyurtma berish, karta/hisob boshqaruvi va profil sozlamalari mavjud.

https://marketplace-g37t.onrender.com/

## Asosiy imkoniyatlar

- Foydalanuvchi ro'yxatdan o'tishi va tizimga kirishi
- Xaridor va sotuvchi rollari
- Mahsulotlar katalogi
- Mahsulot qidirish va kategoriyalar bo'yicha filtrlash
- Mahsulotni saqlash/saqlanganlarga qo'shish
- Buyurtma yaratish va buyurtmalarni boshqarish
- Sotuvchi dashboardi
- Karta/hisob qo'shish, tahrirlash va o'chirish
- Profilni tahrirlash
- Kommentariya va mahsulot ko'rish statistikasi

## Texnologiyalar

- Python 3.x
- Django 6.x
- SQLite
- Bootstrap 5
- Pillow
- django-credit-cards / creditcard

## Loyiha tuzilmasi

- `config/` — asosiy Django settings va URL konfiguratsiyasi
- `main/` — bosh sahifa
- `users/` — autentifikatsiya, profil va signup
- `products/` — mahsulotlar, kategoriyalar, saqlangan mahsulotlar
- `orders/` — buyurtmalar
- `wallets/` — karta/hisob boshqaruvi
- `templates/` — umumiy template fayllar
- `static/` — statik fayllar
- `media/` — yuklangan fayllar

## O'rnatish

### 1. Virtual muhit yaratish

```bash
python -m venv .venv
```

### 2. Virtual muhitni faollashtirish

Windows:

```bash
.venv\Scripts\activate
```

### 3. Kerakli paketlarni o'rnatish

```bash
pip install -r requirements.txt
```

### 4. Migratsiyalarni bajarish

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Superuser yaratish

```bash
python manage.py createsuperuser
```

### 6. Serverni ishga tushirish

```bash
python manage.py runserver
```

So'ng brauzerda quyidagi manzilni oching:

```bash
http://127.0.0.1:8000/
```

## Muhim sozlamalar

`config/settings.py` ichida quyidagilar mavjud:

- `AUTH_USER_MODEL = "users.CustomUser"`
- `STATICFILES_DIRS`
- `MEDIA_ROOT`
- `MEDIA_URL`
- `ALLOWED_HOSTS = ["*"]`
- `DEBUG = True`

## Litsenziya

Ushbu loyiha o'rganish uchun tayyorlangan.
