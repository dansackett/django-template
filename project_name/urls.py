from django.conf.urls import patterns, include

urlpatterns = patterns('',
    (r'^$', '', {}, 'home'),
    # (r'^account/', include('account.urls')),
)
