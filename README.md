# django-real-time logging

Useful and simple real-time logging middleware for django projects.

```no-highlight
https://github.com/Speccy-Rom/django-real-time-logging
```

# How to use it

To install run:
```no-highlight
pip install django-rt-logging
```


Add the following lines at the end of **settings.py** file:
```python
INSTALLED_APPS = INSTALLED_APPS + ('django-rt-logging',)
MIDDLEWARE = ( MIDDLEWARE + ('django_watch.middleware.LoggingMiddleware',) )  
```


Open your development console and see the result:
```python
""" START /my_project/posts/views.py => news_list: Line number 15 """
kwargs: {'posts_id': '3'}
request.GET: <QueryDict: {'published_at': ['today']}>

""" END /my_project/posts/views.py => news_list: Line number 15 """
sql queries time: 0.13
total time: 4.23
```
