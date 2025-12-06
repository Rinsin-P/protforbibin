from django.shortcuts import render

# Create your views here.

def index(request):
    """Homepage view"""
    return render(request, 'bibiapp/index.html')

def about(request):
    """About page view"""
    return render(request, 'bibiapp/about.html')

def services(request):
    """Services page view"""
    return render(request, 'bibiapp/services.html')

def portfolio(request):
    """Portfolio page view"""
    return render(request, 'bibiapp/portfolio.html')

def testimonials(request):
    """Testimonials page view"""
    return render(request, 'bibiapp/testimonials.html')

def blog(request):
    """Blog page view"""
    return render(request, 'bibiapp/blog.html')

def contact(request):
    """Contact page view"""
    return render(request, 'bibiapp/contact.html')

def newsletter(request):
    """Newsletter subscription view"""
    if request.method == 'POST':
        # Handle newsletter subscription logic here
        email = request.POST.get('email')
        # Add your newsletter subscription logic
        return render(request, 'bibiapp/newsletter_success.html')
    return render(request, 'bibiapp/newsletter.html')

def generic(request):
    """Generic page view"""
    return render(request, 'bibiapp/generic.html')

def single(request):
    """Single post view"""
    return render(request, 'bibiapp/single.html')

def style_guide(request):
    """Style guide view"""
    return render(request, 'bibiapp/style.html')
