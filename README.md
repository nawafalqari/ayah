# azkar-api

## طريقة الإستخدام
### Python
```python
from requests import get

zekr = get('https://azkar-api.nawafhq.repl.co/zekr?json=true').json() # Type = dict
print(zekr['content'])
```
#### يمكن تحديد نوع الاذكار المراد رؤيتها
```
https://azkar.nawaf.cf/zekr?[type]=true
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

##### أمثلة
سيظهر ذكر من اذكار الصباح
```
https://azkar.nawaf.cf/zekr?m=true
```
سيظهر دعاء من أدعية الأنبياء
```
https://azkar.nawaf.cf/zekr?pd=true
```
يمكن ارجاع البيانات كـ JSON
```
https://azkar.nawaf.cf/zekr?t=true&json=true
```
سيرجع هذا المثال تسابيح عشوائية كـ كائن JSON

#### إذا لم يعمل `https://azkar.nawaf.cf/`
استخدم:
```
https://azkar-api.nawafhq.repl.co/zekr
```
