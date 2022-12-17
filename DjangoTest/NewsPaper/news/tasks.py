from django.conf import settings

from celery import shared_task
import datetime
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from news.models import Post, Category

today = datetime.datetime.now()
last_week = today - datetime.timedelta(days=7)
posts = Post.objects.filter(date_creation__gte=last_week)
categories = set(posts.values_list('post_category__name', flat=True))
subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))


#############
# Еженедельная отправка писем#
#############
@shared_task
def weekly_newsletter():
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
#############


#############
# Отправка писем при создании поста#
#############
@shared_task
def send_notifications(preview, pk, title):
    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_context, 'text/html')
    msg.send()
#############
