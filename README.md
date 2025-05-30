# HexGuard - مشروع أمني لاختبار الاختراق الأخلاقي

## 🧠 الوصف:
HexGuard هو تطبيق أخلاقي لاختبار الثغرات الأمنية، مصمم بواجهة احترافية وميزات متعددة لفائدة الباحثين في الأمن السيبراني.

---

## 📁 مكونات المشروع:

```
HexGuard/

- main.py                 # نقطة تشغيل التطبيق
- login.py                # واجهة تسجيل الدخول
- dashboard_admin.py      # لوحة تحكم الأدمن
- dashboard_user.py       # لوحة تحكم المستخدم العادي
- tools/
  - port_scanner.py       # أداة فحص المنافذ
  - ping_tool.py          # أداة Ping
- users.db                # قاعدة بيانات المستخدمين (SQLite)
- assets/
  - logo.png              # شعار HexGuard (Placeholder)
- requirements.txt        # قائمة المكتبات المطلوبة
- README.md               # هذا الملف التعريفي
```

---

## ⚙️ طريقة التشغيل:

1. ثبت المكتبات:
```bash
pip install -r requirements.txt
```

2. شغل التطبيق:
```bash
python main.py
```

---

## 🧰 الميزات:
- تسجيل دخول آمن
- واجهة أدمن والمستخدم منفصلتين
- أدوات فحص البورتات وPing
- قاعدة بيانات مشفرة
- تصميم احترافي وسهل الاستعمال

---

## 📦 توليد .exe من المشروع:
1. ثبت PyInstaller:
```bash
pip install pyinstaller
```
2. أنشئ الملف التنفيذي:
```bash
pyinstaller --onefile main.py
```

---

## 📌 ملاحظات:
- لا تستعمل HexGuard إلا في السياق الأخلاقي والقانوني.
- هذا المشروع لأغراض تعليمية واختبارية فقط.

---


