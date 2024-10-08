
# No Mouse

**No Mouse** یک ابزار کنترل صوتی برای تنظیم صدا، روشنایی، و انجام برخی از دستورات سیستم است. این پروژه به شما اجازه می‌دهد تا با استفاده از دستورات صوتی به راحتی تنظیمات سیستم خود را کنترل کنید، بدون نیاز به استفاده از موس.

## ویژگی‌ها

- **کنترل روشنایی**: افزایش، کاهش، و تنظیم درصد روشنایی صفحه نمایش.
- **کنترل صدا**: افزایش، کاهش، و قطع و وصل صدا.
- **دستورات سیستم**: خاموش کردن و راه‌اندازی مجدد سیستم، باز کردن برنامه‌ها و پنجره‌های مختلف، و مدیریت وای‌فای.

## پیش‌نیازها

برای استفاده از این پروژه، نیاز به نصب پیش‌نیازهای زیر است:

- Python 3.x
- `speech_recognition` برای شناسایی دستورات صوتی
- `pyautogui` برای شبیه‌سازی فعالیت‌های موس و کیبورد
- `screen_brightness_control` برای تنظیم روشنایی
- `pycaw` برای کنترل صدا
- `psutil` برای مدیریت فرآیندها

می‌توانید این پیش‌نیازها را با استفاده از pip نصب کنید:

```bash
pip install speech_recognition pyautogui screen_brightness_control pycaw psutil
```
نصب
برای نصب و استفاده از No Mouse، مراحل زیر را دنبال کنید:

این پروژه را از گیت‌هاب کلون کنید یا فایل‌های پروژه را دانلود کنید.

```bash
git clone https://github.com/shantiya401/no_mouse.git
```
به دایرکتوری پروژه بروید:

```bash
cd no_mouse
```
پیش‌نیازهای مورد نیاز را نصب کنید:

```bash
pip install -r requirements.txt
```
استفاده
برای اجرای No Mouse، فایل no_mouse.py را با استفاده از Python اجرا کنید:
```bash
python no_mouse.py
```


برنامه به طور مداوم به دستورات صوتی گوش می‌دهد و بسته به دستوراتی که دریافت می‌کند، عمل مربوطه را انجام می‌دهد. دستورات صوتی ممکن است شامل موارد زیر باشد:

نور کم برای کاهش روشنایی
نور زیاد برای افزایش روشنایی
روشنایی [درصد] برای تنظیم روشنایی به درصد مشخص شده
صدا کم برای کاهش صدا
صدا زیاد برای افزایش صدا
صدا قطع برای قطع صدا
صدا وصل برای وصل صدا
ویندوز خاموش برای خاموش کردن ویندوز
ویندوز ری استارت برای راه‌اندازی مجدد ویندوز
و سایر دستورات برای کنترل برنامه‌ها و پنجره‌های مختلف
مشارکت
اگر تمایل به مشارکت در این پروژه دارید، لطفاً یک درخواست کش (Pull Request) ارسال کنید. نظرات و پیشنهادات شما نیز خوشحال کننده است!

لایسنس
این پروژه تحت لایسنس MIT منتشر شده است. لطفاً برای اطلاعات بیشتر به فایل LICENSE مراجعه کنید.

تماس
برای هرگونه سوال یا مشکلی، لطفاً با من تماس بگیرید.

شما می‌توانید من را از طریق GitHub پیگیری کنید
