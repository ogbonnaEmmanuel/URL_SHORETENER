import secrets

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from HomePage.models import Link
from .forms import ProfileUpdateForm


# Create your views here.
@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def get_all_user_data(request):
    user = request.user
    username = user.username
    links_count = Link.objects.filter(creator=user).count()
    active_links = Link.objects.filter(creator=user).filter(is_active=True).count()
    link_visits = request.user.link_set.all()
    total_visitors = 0
    user_link_data = []
    for link_id, link_visitors in enumerate(link_visits):
        total_visitors += link_visitors.visitors
        object_data = {
            'link_id': link_id,
            'url': link_visitors.alias,
            'visitors': link_visitors.visitors,
            'is_active': link_visitors.is_active
        }
        user_link_data.append(object_data)
    response = JsonResponse({
        'Aggregate': {
            'username': username,
            'links_count': links_count,
            'active_links': active_links,
            'total_visitors': total_visitors,
        },
        'unit': {
            'user_link_data': user_link_data
        }
    })
    return response


@login_required
def settings(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'settings.html', {'form': form})


@csrf_exempt
def create_link(request):
    url = request.POST['url']
    alias = request.POST['alias']
    if validate_url(url)['status'] == 'success':
        if request.user.is_authenticated:
            user = request.user
            create_known_user_link(url, user, alias)
        else:
            create_unknown_user_link(url, alias)
        return JsonResponse({
            'success': 'url created'
        })
    else:
        return JsonResponse({
            'error': 'invalid url'
        })


def validate_url(user_url):
    message = {
        'status': None
    }
    try:
        validate = URLValidator()
        validate(user_url)
        message['status'] = 'success'
    except ValidationError:
        message['status'] = 'error'
    return message


def create_known_user_link(user_url, user, alias):
    Link.objects.create(
        url=user_url,
        creator=user,
        alias=alias
    )


def create_unknown_user_link(user_url, alias):
    user = User.objects.create(
        username=secrets.token_hex(8),
        password=secrets.token_hex(8),
        email=f'{secrets.token_hex(5)}@gmail.com'
    )
    Link.objects.create(
        creator=user,
        url=user_url,
        alias=alias
    )
