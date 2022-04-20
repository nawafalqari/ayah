# azkar-api

## طريقة الإستخدام

### Python

```python
from requests import get

zekr = get('https://azkar-api.nawafhq.repl.co/zekr?json').json() # Type = dict
print(zekr['content'])
```

#### يمكن تحديد نوع الاذكار المراد رؤيتها

```
https://azkar-api.nawafhq.repl.co/zekr?[type]
```

|     نوع الذِكر     | الإختصار     |
|--------------|-----------|
| أذكار الصباح | m      |
| أذكار المساء      | e  |
| أذكار بعد السلام من الصلاة المفروضة      | as  |
| تسابيح و اذكار عشوائية      | t |
| أذكار قبل النوم      | bs |
| أذكار الاستيقاظ      | wu |
| أدعية قرآنية      | qd |
| أدعية الأنبياء      | pd |

## أمثلة
سيظهر ذكر من اذكار الصباح

```
https://azkar-api.nawafhq.repl.co/zekr?m
```
---
سيظهر دعاء من أدعية الأنبياء

```
https://azkar-api.nawafhq.repl.co/zekr?pd
```
---
يمكن ارجاع البيانات كـ JSON
```
https://azkar-api.nawafhq.repl.co/zekr?t&json
```

---
```
https://azkar-api.nawafhq.repl.co/zekr?t&json
```
سيرجع هذا المثال تسابيح عشوائية كـ كائن JSON

---

يمكن ارجاع ذكر عشوائي من نوعين او اكثر
```
https://azkar-api.nawafhq.repl.co/zekr?e&m&json
```
سيرجع هذا المثال ذكر من اذكار الصباح او المساء

---

[طريقة الاستعمال في لغات أخرى](https://github.com/nawafalqari/azkar-api/tree/main/examples "طريقة الاستعمال في لغات أخرى")