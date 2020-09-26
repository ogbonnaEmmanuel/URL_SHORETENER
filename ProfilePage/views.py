from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from HomePage.models import Link


# Create your views here.
@login_required
def profile(request):
    return render(request, 'profile.html')


def get_all_user_data(request):
    user = request.user
    username = user.username
    links_count = Link.objects.filter(creator=user).count()
    active_links = Link.objects.filter(creator=user).filter(is_active=True).count()
    link_visits = request.user.link_set.all()
    total_visitors = 0
    user_link_data = [

    ]
    for link_id, link_visitors in enumerate(link_visits):
        total_visitors += link_visitors.visitors
        object_data = {
            'link_id': link_id,
            'url': link_visitors.url,
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
