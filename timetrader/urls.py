from django.conf.urls import include, url
from django.contrib import admin

import pages.urls


urlpatterns = [
  url(r'', include(pages.urls)),
  # url(r'^admin/', include(admin.site.urls)),
]
