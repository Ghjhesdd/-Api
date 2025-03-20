import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackContext

# مفاتيح الـ API
TELEGRAM_BOT_TOKEN = "7812532955:AAEGh2uQrEcv7lOv4PWtnidvQj5B5DRd4E4"
GOOGLE_API_KEY = "AIzaSyAjPdzvZWpxlzw7ShB0S6iLqA-UqkDWnWw"

# تهيئة Google AI باستخدام API Key
genai.configure(api_key=GOOGLE_API_KEY)

# اختيار النموذج الأحدث (Gemini 1.5 Pro) الذي يدعم generateContent
model = genai.GenerativeModel("models/gemini-1.5-pro")

# دالة للرد على الرسائل
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    try:
        # استخدام generate_content لتوليد الرد
        response = model.generate_content(user_message)
        if response and response.text:
            await update.message.reply_text(response.text)
        else:
            await update.message.reply_text("لم أتمكن من توليد رد.")
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ أثناء معالجة الرسالة: {str(e)}")

# إعداد وتشغيل البوت
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("البوت يعمل الآن...")
    app.run_polling()


main()