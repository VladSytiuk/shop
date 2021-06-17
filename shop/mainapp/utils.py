from PIL import Image
from django.forms import ValidationError
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin
from .models import Product, Category, Customer, Cart1


class ImageValidationMixin:
    def validate_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('The size of the uploaded image is more than 3 MB')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('The resolution of the uploaded image is less than the minimum allowed')
        return image


class CartMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = Customer.objects.filter(user=request.user).first()
            if not customer:
                customer = Customer.objects.create(user=request.user)
            cart = Cart1.objects.filter(owner=customer, in_order=False).first()
            if not cart:
                cart = Cart1.objects.create(owner=customer)
        else:
            cart = Cart1.objects.filter(for_anonymous_user=True).first()
            if not cart:
                cart = Cart1.objects.create(for_anonymous_user=True)
        self.cart = cart
        return super().dispatch(request, *args, **kwargs)


class CategoryDetailMixin(SingleObjectMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.get_categories_for_left_sidebar()
        return context




