from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import request, FileResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact_msg, Restaurant, category, dish, WebsiteInfo, CustomUserCreationForm, CartItem, CustomOwnerCreationForm


# from .models import WebsiteInfo
# var = WebsiteInfo.objects.all().values()
# request.session['add'] = var
# Create your views here.


def index(request):
    one_res = Restaurant.objects.all().order_by('-Res_id')[:3]
    cate = category.objects.all()
    dishlist = dish.objects.all().order_by('-Dish_id')[:4]
    context = {
        'cate': cate,
        'dishlist': dishlist,
        'one_res': one_res
    }
    return render(request, "index.html", context)


def restaurant(request):
    cate = category.objects.all()
    res = Restaurant.objects.all()
    context = {
        'cate': cate,
        'res': res,
    }

    return render(request, "restaurant.html", context)


def dishes(request):
    cate = category.objects.all()
    dishlist = dish.objects.all()
    context = {
        'dishlist': dishlist,
        'cate': cate,
    }

    return render(request, "dishes.html", context)


def dishCategory(request, id):
    cate = category.objects.all()
    dishlist = dish.objects.all().filter(cate_id=id)
    context = {
        'cate': cate,
        'dishlist': dishlist,
    }

    return render(request, "dishes.html", context)


def resCategory(request, id):
    cate = category.objects.all()
    res = Restaurant.objects.all().filter(cate_id=id)
    context = {
        'cate': cate,
        'res': res,
    }

    return render(request, "restaurant.html", context)


def shop(request):
    one_res = Restaurant.objects.all().order_by('-Res_id')[:3]
    cate = category.objects.all()
    dishlist_discount = dish.objects.all().order_by('-Dish_id')[:4]
    dishlist = dish.objects.all().order_by('-Dish_id')[:6]
    context = {
        'cate': cate,
        'dishlist': dishlist,
        'dishlist_discount': dishlist_discount,
        'one_res': one_res
    }
    return render(request, "shop-grid.html", context)


def contact(request):
    info = WebsiteInfo.objects.all()
    context = {
        'info': info,
    }

    if request.method == "POST":
        name = request.POST["con_name"]
        email = request.POST["con_email"]
        message = request.POST["con_msg"]

        Contact_msg.objects.create(Con_Name=name, Con_Email=email, Con_msg=message)

        alert_msg = "Message sent successfully!"
        return render(request, "contact.html", {"m": alert_msg})

    return render(request, "contact.html", context)


def add_to_cart(request, dish_id):
    dish_item = get_object_or_404(dish, Dish_id=dish_id)

    # Check if the cart already exists in the session
    if 'cart' not in request.session:
        request.session['cart'] = {}

    cart = request.session['cart']

    if str(dish_item.Dish_id) in cart:
        cart[str(dish_item.Dish_id)] += 1
    else:
        cart[str(dish_item.Dish_id)] = 1

    request.session['cart'] = cart
    return redirect('/shoping-cart')


def remove_from_cart(request, dish_id):
    cart = request.session.get('cart', {})

    if str(dish_id) in cart:
        if cart[str(dish_id)] > 1:
            cart[str(dish_id)] -= 1
        else:
            del cart[str(dish_id)]

    request.session['cart'] = cart
    return redirect('/shoping-cart')  # You can change the redirect URL as needed.


def shop_details(request, id):
    dishlist = dish.objects.get(Dish_id=id)
    context = {
        'dishlist': dishlist,
    }

    return render(request, "shop-details.html", context)


@login_required
def shoping_cart(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total_price = 0

    for dish_id, quantity in cart.items():
        dish_item = get_object_or_404(dish, Dish_id=dish_id)
        item_total = dish_item.Dish_Price * quantity
        total_price += item_total

        cart_items.append({
            'dish_item': dish_item,
            'quantity': quantity,
            'item_total': item_total
        })

    return render(request, 'shoping-cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

def checkout(request):
    return render(request, "checkout.html")


def searchbar_dish(request):
    if request.method == 'GET':
        query = request.GET.get("search_query")
        if query:
            cate = category.objects.all()
            dishlist = dish.objects.all().filter(Dish_Name__icontains=query)

            return render(request, 'search_dish.html', {'dishlist': dishlist, 'cate': cate})
        else:

            return render(request, 'search_dish.html')


def searchbar_res(request):
    if request.method == 'GET':
        query = request.GET.get("search_query")
        if query:
            cate = category.objects.all()
            reslist = Restaurant.objects.all().filter(Res_Name__icontains=query)

            return render(request, 'search_res.html', {'reslist': reslist, 'cate': cate})
        else:

            return render(request, 'search_res.html')


def restaurant_details(request, id):
    res = Restaurant.objects.get(Res_id=id)
    context = {
        'res': res,
    }
    return render(request, "restaurant-details.html", context)


# def download_file(request, file_id):
#     try:
#         restaurant = Restaurant.objects.get(Res_id=file_id)
#         if restaurant.Res_MenuFile:
#             file_path = restaurant.Res_MenuFile.path
#             with open(file_path, 'rb') as file:
#                 response = FileResponse(file)
#                 response['Content-Disposition'] = f'attachment; filename="{restaurant.Res_MenuFile.name}"'
#                 return response
#         else:
#             raise Http404("File does not exist")
#     except Restaurant.DoesNotExist:
#         raise Http404("Restaurant does not exist")


def user_login(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            msg = "Invalid Credentials"
            form = AuthenticationForm(request.POST)
            return render(request, "user-login.html", {"form": form, "msg": msg})
    else:
        form = AuthenticationForm()
        return render(request, "user-login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("/")


def sign_up(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get("username")
            # password = form.cleaned_data.get("password")
            # user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
        else:
            return render(request, "user-signup.html", {"form": form})
    else:
        form = CustomUserCreationForm()
        return render(request, "user-signup.html", {"form": form})


def create_restaurant(request):
    if request.method == 'POST':
        form = CustomOwnerCreationForm(request.POST)
        if form.is_valid():
            # Create and save the user
            user = form.save()
            user.set_password(request.POST['password1'])  # Set the user's password
            user.save()

            # Create and associate the restaurant with the user
            restaurant = Restaurant(
                Res_Name=request.POST['Res_Name'],
                Res_Email=request.POST['Res_Email'],
                Res_Phone=request.POST['Res_Phone'],
                Res_Address=request.POST['Res_Address'],
            )
            restaurant.save()
            restaurant.user = user  # Associate the restaurant with the user
            restaurant.save()

            return redirect('/admin')
    else:
        form = CustomOwnerCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'restaurant-register.html', context)
