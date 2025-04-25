from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from .forms import CheckoutForm
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('signup')
    
        user = User.objects.create(
            username=email,  
            email=email,
            password=make_password(password),  
            first_name=name
        )
        
        messages.success(request, 'Account created successfully!')
        return redirect('gallery')
    
    return render(request, 'signup.html')



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        
        if user is not None:
            auth_login(request, user)  
            return redirect('gallery')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
            
    return render(request, 'signup.html')  

def index(request):
    return render(request, 'index.html')


def home_page(request):
    return render(request, 'home.html')


def gallery(request):
    username = "Guest"
    email = "guest@example.com"
    if request.user.is_authenticated:
        username = request.user.first_name or request.user.username
        email = request.user.email
    
    context = {
        'username': username,
        'email': email,
    }
    
    return render(request, 'main.html', context)

def blog_view(request):
    username = "Guest"
    email = "guest@example.com"
    if request.user.is_authenticated:
        username = request.user.first_name or request.user.username
        email = request.user.email
    
    context = {
        'username': username,
        'email': email,
    }
    
    return render(request, 'blog.html', context)

def auction(request):
    username = "Guest"
    email = "guest@example.com"
    if request.user.is_authenticated:
        username = request.user.first_name or request.user.username
        email = request.user.email
    
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
        {
        'id': 4,
        'title': 'Silver Car Crash (Double Disaster)',
        'artist': 'Andy Warhol',
        'price': '1800',
        'img': 'https://www.sothebysinstitute.com/wp-content/uploads/2015/10/warhol-cc-144_banner.jpg',
        'description': 'A stark silkscreen of a car crash in silver and black, exploring themes of mortality and media.',
        'year': '1963',
        'dimensions': '267.3 cm × 416.9 cm',
        'medium': 'Silkscreen ink on canvas',
        'url': 'https://en.wikipedia.org/wiki/Silver_Car_Crash_(Double_Disaster)',
    },
    {
        'id': 5,
        'title': 'Dreamscape',
        'artist': 'Sofia Petrov',
        'price': '2750',
        'img': 'https://i.pinimg.com/736x/ac/aa/13/acaa13b229b4b9c4c149378abd99f0dc.jpg',
        'description': 'An ethereal abstract work with flowing colors that evoke a dreamlike state.',
        'year': '2020',
        'dimensions': '80 cm × 100 cm',
        'medium': 'Acrylic on Canvas',
        'url': 'https://www.saatchiart.com/abstract',
    },
    {
        'id': 6,
        'title': 'Color Fields',
        'artist': 'David Kim',
        'price': '1950',
        'img': 'https://artpostgallery.com/wp-content/uploads/2014/10/david-kim-fall-41-x-41.jpg',
        'description': 'A bold exploration of color and form, with overlapping hues creating depth and movement.',
        'year': '2014',
        'dimensions': '104 cm × 104 cm',
        'medium': 'Mixed Media on Canvas',
        'url': 'https://artpostgallery.com/david-kim/',
    },
    {
        'id': 7,
        'title': 'Abstract Composition',
        'artist': 'Elena Petrova',
        'price': '1850',
        'img': 'https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5',
        'description': 'Vibrant abstract work with bold brushstrokes and dynamic color interplay.',
        'year': '2021',
        'dimensions': '90 cm × 120 cm',
        'medium': 'Acrylic on Canvas',
        'url': 'https://www.elenavasquez.com/about',
    },
    {
        'id': 8,
        'title': 'Urban Landscape',
        'artist': 'Marcus Chen',
        'price': '2200',
        'img': 'https://images.unsplash.com/photo-1578926375605-eaf7559b1458',
        'description': 'Contemporary cityscape capturing the energy of modern metropolitan life.',
        'year': '2020',
        'dimensions': '80 cm × 100 cm',
        'medium': 'Oil on Canvas',
        'url': '#',
    },
    {
        'id': 9,
        'title': 'Botanical Study',
        'artist': 'Sophie Laurent',
        'price': '1650',
        'img': 'https://images.unsplash.com/photo-1531913764164-f85c52e6e654',
        'description': 'Detailed floral study with delicate watercolor techniques.',
        'year': '2019',
        'dimensions': '50 cm × 70 cm',
        'medium': 'Watercolor on Paper',
        'url': 'https://www.artmajeur.com/sophie-laurent/en',
    },
    {
        'id': 10,
        'title': 'Coastal Memories',
        'artist': 'James Wilson',
        'price': '1950',
        'img': 'https://images.unsplash.com/photo-1547036967-23d11aacaee0',
        'description': 'Impressionistic seascape with textured palette knife work.',
        'year': '2022',
        'dimensions': '60 cm × 90 cm',
        'medium': 'Oil on Board',
        'url': 'https://artvee.com/dl/coastal-village/',
    },
    {
        'id': 11,
        'title': 'Lodge on Lake Como',
        'artist': 'Carl Frederic Aagaard', 
        'price': '2750',
        'img': 'https://artevenue.com/static/image_data/POD/images/49_2AA4370_lowres.jpg',
        'description': 'Serene lakeside landscape capturing the golden light of dusk on Lake Como\'s historic villa.',
        'year': '1892',
        'dimensions': '60 cm × 90 cm',
        'medium': 'Oil on canvas',
        'url': 'https://en.wikipedia.org/wiki/Lake_Como',
    },
    {
    'id': 12,
    'title': 'Minimalist Forms',
    'artist': 'Carlos Mendez',
    'price': '1750',
    'img': 'https://images.unsplash.com/photo-1578926375605-eaf7559b1458',
    'description': 'Clean geometric composition exploring space and balance.',
    'year': '2020',
    'dimensions': '70 cm × 70 cm',
    'medium': 'Acrylic on Wood Panel',
    'url': 'https://en.wikipedia.org/wiki/Carlos_M%C3%A9ndez',
}
    ]
    if request.user.is_authenticated:
        username = request.user.first_name or request.user.username
        email = request.user.email
    
    context = {
        'products': products,
        'username': username,
        'email': email,
    }
    return render(request, 'auction.html', context)
def checkout(request):
    form = CheckoutForm()  
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            messages.success(request, "Order placed successfully!")
            return render(request, 'checkout.html', {
                'form': form,
                'order_success': True
            })
    
    return render(request, 'checkout.html', {
        'form': form,
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
def logout_view(request):
    logout(request)
    return redirect('home') 
def empty_view(request):
    return HttpResponse("")
