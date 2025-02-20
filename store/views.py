from django.shortcuts import render

def home(request):
    # Hard-coded list of products for the MVP
    products = [
        {
            "name": "Product 1",
            "description": "A wonderful item for your store.",
            "price": "$19.99",
            "image_url": "https://via.placeholder.com/150"
        },
        {
            "name": "Product 2",
            "description": "Another great product to enhance your collection.",
            "price": "$29.99",
            "image_url": "https://via.placeholder.com/150"
        },
        {
            "name": "Product 3",
            "description": "The best product for your e-commerce site.",
            "price": "$39.99",
            "image_url": "https://via.placeholder.com/150"
        },
    ]
    return render(request, 'store/home.html', {'products': products})