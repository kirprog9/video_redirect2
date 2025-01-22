from django.shortcuts import redirect, render
from .models import Video, RedirectSite

def video_page(request, user_id, video_id, redirect_id):
    try:
        video = Video.objects.get(id=video_id)
        print(f"{user_id}, {video_id}, {redirect_id}")
        return render(request, 'video.html', {'video_url': video.video_url})
    except Video.DoesNotExist:
        return redirect('/')

def about(request):
    return render(request, 'about.html')

def redirect_page(request):
    site = RedirectSite.objects.first()
    return redirect(site.destination_url)
