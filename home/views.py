from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages



def index(request):
    return render(request, 'index.html')


def home_page(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        messages.success(request, 'Account created successfully!')
        return redirect('gallery')
    return render(request, 'signup.html')


def login_view(request):  # Renamed from 'login' to avoid conflict
    if request.method == 'POST':
        return redirect('gallery')
    return render(request, 'login.html')  # Changed from 'signup.html'


def gallery(request):
    return render(request, 'main.html')


def blog_view(request):
    return render(request, 'blog.html')


def auction(request):
    # Hardcoded product data
    products = [
        {
            'id': 1,
            'title': 'The Starry Night',
            'artist': 'Vincent van Gogh',
            'price': '1250',
            'img': 'https://m.media-amazon.com/images/I/91PeFpf5NNL._AC_UF894,1000_QL80_.jpg',
            'description': 'The painting is dominated by a swirling, turbulent sky with deep blues and vibrant yellows, evoking both awe and restlessness.',
            'year': '1889',
            'dimensions': '73.7 cm × 92.1 cm',
            'medium': 'Oil on Canvas',
            'url': 'https://en.wikipedia.org/wiki/The_Starry_Night',
        },
        {
            'id': 2,
            'title': 'Les Femmes d’Alger (Version O)',
            'artist': 'Pablo Picasso',
            'price': '2400',
            'img': 'https://images.saatchiart.com/saatchi/247461/art/3717192/2787076-HSC00001-7.jpg',
            'description': 'A vibrant composition featuring abstracted figures in rich colors, inspired by Delacroix’s work.',
            'year': '1955',
            'dimensions': '114 cm × 146.4 cm',
            'medium': 'Oil on Canvas',
            'url': 'https://en.wikipedia.org/wiki/Les_Femmes_d%27Alger',
        },
        {
            'id': 3,
            'title': 'Impression, Sunrise',
            'artist': 'Claude Monet',
            'price': '3150',
            'img': 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSp0KWxnySgyOcD7s2fSWVIUhozVuUzTfyZxMyc0minGIR9iITyU3rAxfjuh3f2udbfaOTqC7im2A7e1JACoWTMj90uyoHQFI0zGHq2YuIPyKyLE0iSLMGIy9Ji5b3LzAl6XBwdkOvPLHU/w1200-h630-p-k-no-nu/sunrise.jpg',
            'description': 'A serene depiction of a harbor at sunrise, with soft oranges and blues blending into a misty atmosphere.',
            'year': '1872',
            'dimensions': '48 cm × 63 cm',
            'medium': 'Oil on Canvas',
            'url': 'https://en.wikipedia.org/wiki/Impression,_Sunrise',
        },
        # ... (products 4 to 12 as originally listed)
    ]

    context = {
        'products': products,
        'username': 'John Doe',
        'email': 'john@example.com',
    }

    return render(request, 'auction.html', context)


from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def home_page(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        messages.success(request, 'Account created successfully!')
        return redirect('gallery')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        return redirect('gallery')
    return render(request, 'signup.html') 

def gallery(request):
    return render(request, 'main.html')

def blog_view(request):
    return render(request, 'blog.html')

def auction(request):
    products = [  # Sample product data
        {
            'id': 1,
            'title': 'The Starry Night',
            'artist': 'Vincent van Gogh',
            'price': '1250',
            'img': 'https://m.media-amazon.com/images/I/91PeFpf5NNL._AC_UF894,1000_QL80_.jpg',
            'description': 'The painting is dominated by a swirling, turbulent sky with deep blues and vibrant yellows, evoking both awe and restlessness.',
            'year': '1889',
            'dimensions': '73.7 cm × 92.1 cm',
            'medium': 'Oil on Canvas',
            'url': 'https://en.wikipedia.org/wiki/The_Starry_Night',
        },
        # Add other product dictionaries...
    ]
    context = {
        'products': products,
        'username': 'John Doe',
        'email': 'john@example.com',
    }
    return render(request, 'auction.html', context)

def checkout(request):
    if request.method == 'POST':
        # Handle basic POST data or mock processing here
        messages.success(request, "Order placed successfully!")
        return render(request, 'checkout.html', {
            'order_success': True
        })

    cart_items = request.session.get('cart_items', [])
    subtotal = sum(float(item['price']) * item['quantity'] for item in cart_items)
    tax = subtotal * 0.1
    total = subtotal + tax

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'tax': tax,
        'total': total,
        'order_success': False
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        inquiry_type = request.POST.get('inquiry-type')
        message = request.POST.get('message')

        print(f"Name: {name}, Email: {email}, Type: {inquiry_type}, Message: {message}")

        messages.success(request, "Your message has been sent!")
        return redirect('contact')

    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def empty_view(request):
    return HttpResponse("")



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        inquiry_type = request.POST.get('inquiry-type')
        message = request.POST.get('message')

        print(f"Name: {name}, Email: {email}, Type: {inquiry_type}, Message: {message}")

        messages.success(request, "Your message has been sent!")
        return redirect('contact')

    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def empty_view(request):
    return HttpResponse("")
