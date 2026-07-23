from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_order_status_email(order_id, new_status):
    """
    Buyurtma statusi o'zgarganda foydalanuvchiga email yuborish.
    
    Nima uchun kerak:
    - Foydalanuvchilarga buyurtma holati haqida avtomatik xabar berish
    - Asosiy jarayonni sekinlamasdi (email yuborish uzoq vaqt olishi mumkin)
    - Backgroundda ishlaydi, foydalanuvchi kutmaydi
    
    Qanday ishlaydi:
    1. Task RabbitMQ ga yuboriladi
    2. Celery worker taskni qabul qiladi
    3. Backgroundda email yuboriladi
    4. Xatolik bo'lsa qayta urinadi
    """
    from orders.models import Order
    
    try:
        order = Order.objects.get(id=order_id)
        
        status_messages = {
            'new': 'Buyurtmangiz qabul qilindi',
            'accepted': 'Sotuvchi buyurtmangizni qabul qildi',
            'completed': 'Buyurtmangiz yakunlandi',
            'canceled': 'Buyurtmangiz bekor qilindi'
        }
        
        message = status_messages.get(new_status, 'Buyurtma statusi o\'zgardi')
        
        send_mail(
            f'Buyurtma #{order.id} statusi',
            f'Salom {order.buyer.username},\n\n{message}\n\nMahsulot: {order.product.title}',
            settings.DEFAULT_FROM_EMAIL,
            [order.buyer.email],
            fail_silently=False,
        )
        
        return f"Email sent to {order.buyer.email}"
        
    except Order.DoesNotExist:
        return f"Order {order_id} not found"
    except Exception as e:
        return f"Error: {str(e)}"
