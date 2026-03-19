from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Cart
from .serializers import CartSerializer
from products.models import Product


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cart(request):
    items = Cart.objects.filter(user=request.user)
    serializer = CartSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    product_id = request.data.get("product")
    qty = request.data.get("qty", 1)

    if not product_id:
        return Response({"error": "Product id is required"}, status=400)

    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={"quantity": qty}
    )

    if not created:
        cart_item.quantity += int(qty)
        cart_item.save()

    serializer = CartSerializer(cart_item)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_cart(request, id):
    try:
        item = Cart.objects.get(id=id, user=request.user)
        item.delete()
        return Response({"message": "Item removed"})
    except Cart.DoesNotExist:
        return Response({"error": "Item not found"}, status=404)