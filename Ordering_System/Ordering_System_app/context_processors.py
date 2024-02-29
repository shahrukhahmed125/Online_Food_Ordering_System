from .models import WebsiteInfo


def load_everywhere(request):
    # Define the string you want to display
    info = WebsiteInfo.objects.all()

    # Add it to the context
    return {'data': info}


# def login_logout_button(request):
#     if request.session.get('logged_in', False):
#         login_status = "Logout"
#     else:
#         login_status = "Login"
#
#     return {'login_status': login_status}
