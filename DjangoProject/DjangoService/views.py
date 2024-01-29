# views.py
from typing import Any, Dict
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from DjangoService.models import Item
from django.conf import settings
import stripe
from rest_framework.views import APIView

stripe.api_key = settings.STRIPE_SECRET_KEY

class BuyItemView(APIView):
    """
    API endpoint for purchasing an item.

    Parameters:
    - pk: The primary key of the item to be purchased.

    Returns:
    - Response: JSON response with the client secret and currency.
    """

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """
        Handles GET requests to create a PaymentIntent and return the client secret.

        Args:
        - request: The HTTP request object.
        - pk: The primary key of the item to be purchased.

        Returns:
        - Response: JSON response with the client secret and currency.
        """
        item = get_object_or_404(Item, pk=kwargs['pk'])

        # Создаем Payment Intent
        intent = stripe.PaymentIntent.create(
            amount=int(item.price * 100),  # Stripe requires amount in cents
            currency=item.currency,
            payment_method_types=['card'],
            description=f'Payment for {item.name}',
            statement_descriptor='Custom descriptor',
        )

        return JsonResponse({'client_secret': intent.client_secret, 'currency': item.currency})

class ItemDetailView(View):
    """
    View for displaying details of an item.

    Attributes:
    - template_name (str): The HTML template used for rendering the item details.
    """

    template_name = 'item_detail.html'

    def get(self, request, pk: int) -> render:
        """
        Handles GET requests to display the details of a specific item.

        Args:
        - request: The HTTP request object.
        - pk: The primary key of the item to be displayed.

        Returns:
        - render: HTML rendering of the item details.
        """
        item = get_object_or_404(Item, pk=pk)
        context: Dict[str, Any] = {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'price': str(item.price),
            'currency': item.currency,
            'stripe_price_id': item.stripe_price_id,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        }
        return render(request, self.template_name, context)