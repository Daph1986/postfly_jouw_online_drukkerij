from django.http import HttpResponse


class StripeWebHookHandler:
	""" Handles Stripe webhooks """

	def __init__(self, request):
		self.request = request

	def handle_event(self, event):
		""" Handels a generic, unknown or unexpected webhook event """
		return HttpResponse(
			content=f'Unhandled webhook received: {event["type"]}',
			status = 200)

	def handle_payment_intent_succeeded(self, event):
		""" Handels the payment_intent.succeeded webhook from Stripe """
		intent = event.data.object
		print(intent)
		return HttpResponse(
			content=f'Webhook received: {event["type"]}',
			status = 200)

	def handle_payment_intent_payment_failed(self, event):
		""" Handels the payment_intent.payment_failed webhook from Stripe """
		return HttpResponse(
			content=f'Webhook received: {event["type"]}',
			status = 200)