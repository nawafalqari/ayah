
// install http package (flutter pub add http / dart pub add http )
// NOTE : you should have a pubspec.yaml file 
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() async {
  http.Response response =
      await http.get(Uri.parse("https://azkar-api.nawafhq.repl.co/zekr?json=true"));
  print(jsonDecode(response.body)["content"]);
}