# Telegram bot — Data Analytics platformasi

Veb-sayt va Telegram **bitta Django akkaunt** va **bitta baza**dan foydalanadi.

## Nima sinxron?

- Foydalanuvchi (email/parol)
- Kurslar, darslar, mashqlar
- Dars tugallanishi
- SQL natijalari va ballar
- Uy vazifasi
- Progress
- Profil, e’lonlar, o‘qituvchi xabarlari

Telegramda dars/mashq qilsangiz, vebda ham ko‘rinadi. Aksincha ham.

## Sozlash

1. [@BotFather](https://t.me/BotFather) dan token oling.
2. Loyiha ildizidagi `.env` ga qo‘ying:

```
TELEGRAM_BOT_TOKEN=123456:ABC...
DJANGO_SETTINGS_MODULE=config.settings.local
```

3. Migratsiya:

```
python manage.py migrate
```

4. Bog‘liqlik (loyiha venv ichida):

```
pip install -r telegram_bot/requirements.txt
```

5. Ishga tushirish (loyiha ildizidan):

```
python -m telegram_bot.bot
```

## Kirish

- **Ro‘yxatdan o‘tish** — yangi Django `User` (talaba). Shu email/parol bilan vebga kirasiz.
- **Kirish** — mavjud veb akkauntni Telegramga bog‘lash.

Chiqish faqat Telegram bog‘lanishini uzadi, veb akkaunt o‘chmaydi.

## O‘qituvchi

`teacher` / `admin` roli bilan kirilsa **O‘qituvchi paneli** ochiladi: talabalar, uy vazifasi tekshiruvi, xabar, e’lon.

Yordam: `/support`
