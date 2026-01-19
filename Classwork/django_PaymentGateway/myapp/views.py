from django.shortcuts import render
from django.http import JsonResponse
import razorpay
client = razorpay.Client(auth=("rzp_test_S3OBRdQwtxoAPZ", "NH6bN5d5RTccFvVmaWJEyEh8"))



# Create your views here.
def index(request):
    return render(request, "index.html")


def createOrder(request):
    value = request.GET["amount"]
    inPaisa = int(value)*100
    print(f"value received: {value} - converted to: {inPaisa}")

    # Create Order:
    data = { "amount": inPaisa, "currency": "INR", "receipt": "order_rcptid_11" } 
    payment = client.order.create(data=data) # Amount is in currency subunits. ie 500.00

    print(f"Order created: {payment} | Order Id to be sent to frontend: {payment["id"]}")
    return JsonResponse({"orderId":payment["id"]})