from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import NewsUnit, Category, NewsComment

def news_item(request, news_id):
    news_item = get_object_or_404(NewsUnit, id=news_id)
    comments = NewsComment.objects.filter(news=news_item).order_by('-pub_date')

    # 點擊次數防止短時間重複計數
    session_key = f'viewed_news_{news_id}'
    last_view_time = request.session.get(session_key)

    current_time = timezone.now().timestamp()
    if not last_view_time or current_time - last_view_time > 300:  # 超過 5 分鐘 (300 秒)
        news_item.click_count += 1
        news_item.save()
        request.session[session_key] = current_time

    # 處理留言提交
    if request.method == 'POST':
        content = request.POST.get('content')
        if content and request.user.is_authenticated:
            NewsComment.objects.create(
                news=news_item,
                author=request.user.username,
                content=content,
                pub_date=timezone.now()
            )
            return redirect('NewsItem', news_id=news_id)  # 留言後重新載入頁面

    return render(request, 'news/news_item.html', locals())