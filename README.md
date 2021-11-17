# azkar-api

## طريقة الإستخدام
### Python
```python
from requests import get

zekr = get('https://azkar.ml/zekr?json=true').json() # Type = dict
print(zekr['content'])
```
#### يمكن تحديد نوع الاذكار المراد رؤيتها
```
https://azkar.ml/zekr?[type]=true
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
https://azkar.ml/zekr?m=true
```
سيظهر دعاء من أدعية الأنبياء
```
https://azkar.ml/zekr?pd=true
```
يمكن ارجاع البيانات كـ JSON
```
https://azkar.ml/zekr?t=true&json=true
```
سيرجع هذا المثال تسابيح عشوائية كـ كائن JSON
