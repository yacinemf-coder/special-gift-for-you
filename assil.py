import turtle
import math

# إعداد الشاشة نتاع الرسم
screen = turtle.Screen()
screen.title("💖 Special Gift 💖")
screen.bgcolor("#0d0d0d")  # خلفية سوداء داكنة وفخمة
screen.setup(width=700, height=700)

# إعداد القلم (الرسام)
pen = turtle.Turtle()
pen.speed(0)  # أسرع سرعة للرسم الفوري
pen.hideturtle()
pen.up()

# المعادلات الرياضية لشكل القلب الدقيق
def heart_x(t):
    return 16 * math.sin(t) ** 3

def heart_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

# دالة رسم القلب بحجم معين ولون معين
def draw_heart(scale, color):
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    
    first = True
    # حلقة ترسم المنحنى الرياضي كاملاً
    for i in range(0, 628):  # من 0 لـ 2*pi
        t = i / 100
        x = heart_x(t) * scale
        y = heart_y(t) * scale
        
        if first:
            pen.goto(x, y)
            pen.down()
            first = False
        else:
            pen.goto(x, y)
            
    pen.end_fill()
    pen.up()

# تأثير النبض (الأنيميشن)
print("جاري تشغيل هدية صديقتك...")

# 1. رسم تأثير التوهج الخلفي (النبضة الكبيرة الخفيفة)
draw_heart(16, "#3a0ca3")  # توهج بنفسجي خلفي
draw_heart(14, "#f72585")  # نبضة وردية ساطعة

# 2. رسم القلب الأساسي في المركز
draw_heart(12, "#d90429")  # قلب أحمر داكن ودافئ

# 3. كتابة الإهداء داخل القلب بشكل احترافي
pen.goto(0, -15)  # النزول لمركز القلب تقريباً
pen.color("#ffffff")  # كتابة باللون الأبيض الناصع عشان تبان

# 💡 نصيحة: تقدر تبدل الكلمة اللي بين علامتين الاقتباس باسم صديقتك بالإنجليزية أو العربية
pen.write("For You assil💖", align="center", font=("Arial", 24, "bold"))

# إضافة لمسة جمالية (نجوم صغيرة حول القلب)
stars = [(-200, 200), (200, 200), (-150, -150), (150, -150), (0, 250)]
pen.color("#ffb703") # لون النجوم ذهبي
for pos in stars:
    pen.goto(pos)
    pen.dot(8)

# إبقاء النافذة مفتوحة حتى تضغط عليها
screen.exitonclick()
