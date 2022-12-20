INSTALLED_APPS = [
    # core Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local Apps
    'apps.products.apps.AppProductsConfig',
    'apps.accounts.apps.AppAccountsConfig',
    'apps.orders.apps.AppOrdersConfig',
    'apps.siteviews.apps.AppSiteviewsConfig',
    # third-party Apps
    'easy_thumbnails',
    'image_cropping',
    'rest_framework',
    'mathfilters',
    'widget_tweaks',
]
