from django.shortcuts import render
import stripe


def index(request):
    amount = 2000

    if request.method == 'POST':
        stripe.api_key = "sk_test_wDcAjWQXevsyIZRGWurwlaTy"

        # Get the credit card details submitted by the form
        token = request.POST['stripeToken']

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency="usd",
                source=token,
                description="Example charge"
            )
        except stripe.error.CardError, e:
            # The card has been declined
            pass

    return render(request, 'index.html', {
        'body': 'Test',
        'amount': amount,
    })
