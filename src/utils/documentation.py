def rtl(text: str):
   return f"<p style='direction: rtl'>{text}</p>"

DEKR = {
   "name": "مسار الاذكار",
   "summary": "مسار الاذكار",
   "tags": ["adkar"],
   "description": f'''
استخدم الاختصار في متغير

`types`

مثال:
```
https://ayah.nawafdev.com/api/dekr?types=m
```

ولاختيار نوع عشوائي افصل الانواع بفاصلة

`,`

مثال:
```
https://ayah.nawafdev.com/api/dekr?types=m,e
```

|     نوع الذِكر     |                         الإختصار     |
|--------------------------------------|--------------------|
| أذكار الصباح                        | m                  |
| أذكار المساء                        | e                  |
| أذكار بعد السلام من الصلاة المفروضة | as                 |
| تسابيح و اذكار عشوائية             | t                  |
| أذكار قبل النوم                     | bs                 |
| أذكار الاستيقاظ                     | wu                  |
| أدعية قرآنية                       | qd                  |
| أدعية الأنبياء                      | pd                  |
| ذكر عشوائي                         | random                  |
'''
}

QURAN = {
   "name": "مسار القرآن",
   "summary": "مسار القرآن",
   "tags": ["quran"],
   "deprecated": True,
   "description": '''

جلب معلومات من القرآن عن `سورة` او `جزء` او `صفحة محددة`.

<br>

- `sura`: اسم السورة كامل بدون اضافات (`string`)
- `jozz`: رقم الجزء 1-30 (`int`)
- `page`: رقم الصفحة 1-604 (`int`)

يجب تحديد واحد منهم على الاقل
'''
}

QURAN_SURA = {
   "name": "مسار القرآن من اسم السورة",
   "summary": "مسار القرآن من اسم السورة",
   "tags": ["quran"],
   "description": '''

جلب معلومات عن سورة محددة   
   
'''
}

QURAN_JOZZ = {
   "name": "مسار القرآن من رقم الجزء",
   "name": "مسار القرآن من رقم الجزء",
   "tags": ["quran"],
   "description": '''

جلب معلومات من جزء محدد   
   
'''
}

QURAN_PAGE = {
   "name": "مسار القرآن من رقم الصفحة",
   "summary": "مسار القرآن من رقم الصفحة",
   "tags": ["quran"],
   "description": '''

جلب معلومات من صفحة محددة   
   
'''
}

QURAN_IMAGES = {
   "name": "مسار صور القرآن",
   "summary": "مسار صور القرآن",
   "tags": ["quran"],
   "description": '''

اخذ صورة صفحة من القرآن
   
'''
}

QURAN_SURAS = {
   "name": "مسار سور القرآن",
   "summary": "مسار سور القرآن",
   "tags": ["quran"],
   "description": '''
   
جلب اسماء جميع سور القرآن (114)

'''
}

QURAN_PREVIOUS_SURA = {
   "name": "مسار السورة التي قبل",
   "summary": "مسار السورة التي قبل",
   "tags": ["quran"],
   "description": '''
   
جلب اسم السورة اللي قبل سورة محددة

مثال:
```
https://ayah.nawafdev.com/api/quran/previous_sura?sura=البقرة
```
النتيجة:
```
{"sura":"الفَاتِحة","first":false,"last":false}
```

<br>

واذا كانت السورة هي السورة الأولى (الفاتحة)

سيكون
`"first": true` و `"sura": null`

مثال:
```
https://ayah.nawafdev.com/api/quran/previous_sura?sura=الفاتحة
```

النتيجة
```
{"sura":null,"first":true,"last":false}
```
   
'''
}

QURAN_NEXT_SURA = {
   "name": "مسار السورة التي تلي",
   "summary": "مسار السورة التي تلي",
   "tags": ["quran"],
   "description": '''
   
جلب اسم السورة اللي تلي (تأتي بعد) سورة محددة

مثال:
```
https://ayah.nawafdev.com/api/quran/next_sura?sura=الفاتحة
```
النتيجة:
```
{"sura":"البَقَرَة","first":false,"last":false}
```

<br>

واذا كانت السورة هي السورة الاخيرة (الناس)

سيكون
`"last": true` و `"sura": null`

مثال:
```
https://ayah.nawafdev.com/api/quran/next_sura?sura=الناس
```

النتيجة
```
{"sura":null,"first":false,"last":true}
```
   
'''
}

ADKAR_JSON = {
   "name": "مسار ملف الاذكار",
   "summary": "مسار ملف الاذكار",
   "tags": ["files"],
   "description": '''

ملف يحتوي على الاذكار المستخدمة في الـ `API`

يرجى عدم تجربة المسار هنا لانه من الممكن توقف المتصفح لديك بسبب حجم الملف الكبير

'''
}

QURAN_JSON = {
   "name": "مسار ملف القرآن",
   "summary": "مسار ملف القرآن",
   "tags": ["files"],
   "description": '''

ملف يحتوي على جميع الآيات القرآنية المستخدمة في الـ `API`

يرجى عدم تجربة المسار هنا لانه من الممكن توقف المتصفح لديك بسبب حجم الملف الكبير
   
'''
}