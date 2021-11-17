<?php 

// header('Content-Type: text/html; charset=utf-8');
// $zekr = json_decode(file_get_contents('https://azkar.ml/zekr?json=true'));
$zekr = json_encode('{"category": "أذكار الاستيقاظ", "count": "01", "description": "", "reference": "", "content": "الحَمْـدُ لِلّهِ الّذي أَحْـيانا بَعْـدَ ما أَماتَـنا وَإليه النُّـشور."}');
echo $zekr;
?>