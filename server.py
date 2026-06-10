from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

genai.configure(api_key="API-Key")
model = genai.GenerativeModel('model')

@app.route('/')
def index():
    return send_from_directory('.', 'news_publisher.html')

@app.route('/classify', methods=['POST'])
def classify():
    try:
        text = request.json.get('text', '')
        print(f"دریافت شد: {text}")
        response = model.generate_content(
            f"فقط یک کلمه جواب بده. دسته‌بندی این خبر فارسی را از این گزینه‌ها انتخاب کن: سیاسی، ورزشی، اقتصادی، نظامی، امنیتی، اجتماعی، فناوری\n\nخبر: {text}"
        )
        result = response.text.strip()
        print(f"نتیجه: {result}")
        return jsonify({"category": result})
    except Exception as e:
        print(f"خطا: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
