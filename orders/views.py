from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, OrderItem
from cart.models import Cart

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, OrderItem

@api_view(['POST'])
def create_order(request):

    user = request.user
    cart_items = Cart.objects.filter(user=user)

    if not cart_items:
        return Response({"error":"cart empty"},status=400)

    total = sum(i.product.price * i.quantity for i in cart_items)

    order = Order.objects.create(
        user=user,
        total_price=total
    )

    for item in cart_items:

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )

    cart_items.delete()

    return Response({"message":"order placed"})


@api_view(['GET'])
def user_orders(request):

    user = request.user

    orders = Order.objects.filter(user=user).order_by("-created_at")

    data = []

    for order in orders:

        items = OrderItem.objects.filter(order=order)

        order_items = []

        for i in items:
            order_items.append({
                "product": i.product.name,
                "price": i.product.price,
                "qty": i.quantity
            })

        data.append({
            "id": order.id,
            "total": order.total_price,
            "date": order.created_at,
            "items": order_items
        })

    return Response(data)