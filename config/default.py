# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2020 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import os

from blueapps.conf.default_settings import *  # noqa
from blueapps.conf.log import get_logging_config_dict
from config import get_env_or_raise

# 这里是默认的 INSTALLED_APPS，大部分情况下，不需要改动
# 如果你已经了解每个默认 APP 的作用，确实需要去掉某些 APP，请去掉下面的注释，然后修改
# INSTALLED_APPS = (
#     'bkoauth',
#     # 框架自定义命令
#     'blueapps.contrib.bk_commands',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.sites',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     # account app
#     'blueapps.account',
# )

# 请在这里加入你的自定义 APP
INSTALLED_APPS += (  # noqa
    "home_application",
    "mako_application",
)

# 这里是默认的中间件，大部分情况下，不需要改动
# 如果你已经了解每个默认 MIDDLEWARE 的作用，确实需要去掉某些 MIDDLEWARE，或者改动先后顺序，请去掉下面的注释，然后修改
# MIDDLEWARE = (
#     # request instance provider
#     'blueapps.middleware.request_provider.RequestProvider',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     # 跨域检测中间件， 默认关闭
#     # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     # 蓝鲸静态资源服务
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     # Auth middleware
#     'blueapps.account.middlewares.RioLoginRequiredMiddleware',
#     'blueapps.account.middlewares.WeixinLoginRequiredMiddleware',
#     'blueapps.account.middlewares.LoginRequiredMiddleware',
#     # exception middleware
#     'blueapps.core.exceptions.middleware.AppExceptionMiddleware',
#     # django国际化中间件
#     'django.middleware.locale.LocaleMiddleware',
# )

# 自定义中间件
MIDDLEWARE += (
    "blueapps.middleware.bkui.middlewares.BkuiPageMiddleware",
    "home_application.utils.middlewares.CSRFTokenExemptMiddleware",
)

# 添加首页搜索范围
TEMPLATES[0]["DIRS"] += (os.path.join(BASE_DIR, "static", "dist"),)
# 添加邮件模板搜索范围
TEMPLATES[0]["DIRS"] += (os.path.join(BASE_DIR, "home_application", "templates", "email_templates"),)

# 所有环境的日志级别可以在这里配置
# LOG_LEVEL = 'INFO'

# STATIC_VERSION_BEGIN
# 静态资源文件(js,css等）在APP上线更新后, 由于浏览器有缓存,
# 可能会造成没更新的情况. 所以在引用静态资源的地方，都把这个加上
# Django 模板中：<script src="/a.js?v={{ STATIC_VERSION }}"></script>
# mako 模板中：<script src="/a.js?v=${ STATIC_VERSION }"></script>
# 如果静态资源修改了以后，上线前改这个版本号即可
# STATIC_VERSION_END
STATIC_VERSION = "1.0"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  # noqa

# CELERY 开关，使用时请改为 True，修改项目目录下的 Procfile 文件，添加以下两行命令：
# worker: python manage.py celery worker -l info
# beat: python manage.py celery beat -l info
# 不使用时，请修改为 False，并删除项目目录下的 Procfile 文件中 celery 配置
IS_USE_CELERY = True

# 前后端分离开发配置开关，设置为True时dev和stag环境会自动加载允许跨域的相关选项
FRONTEND_BACKEND_SEPARATION = False

# CELERY 并发数，默认为 2，可以通过环境变量或者 Procfile 设置
CELERYD_CONCURRENCY = os.getenv("BK_CELERYD_CONCURRENCY", 2)  # noqa

# CELERY 配置，申明任务的文件路径，即包含有 @task 装饰器的函数文件
CELERY_IMPORTS = ("home_application.celery_task",)

# log level setting
LOG_LEVEL = "INFO"

# load logging settings
LOGGING = get_logging_config_dict(locals())

# 初始化管理员列表，列表中的人员将拥有预发布环境和正式环境的管理员权限
# 注意：请在首次提测和上线前修改，之后的修改将不会生效
super_user = os.getenv("BKAPP_INIT_SUPERUSER")
INIT_SUPERUSER = super_user.split(",") if super_user else []

# 使用mako模板时，默认打开的过滤器：h(过滤html)
MAKO_DEFAULT_FILTERS = ["h"]

# BKUI是否使用了history模式
IS_BKUI_HISTORY_MODE = True

# 是否需要对AJAX弹窗登录强行打开
IS_AJAX_PLAIN_MODE = True

# 国际化配置
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)  # noqa

# 调用API的用户名
API_INVOKE_USER = get_env_or_raise("BKAPP_API_INVOKE_USER")
# 日报网站url
BKAPP_FULL_SITE_URL = get_env_or_raise("BKAPP_FULL_SITE_URL")
# 权限中心会给注册的系统生成token https://bk.tencent.com/docs/document/6.0/160/8438?r=1
BKAPP_IAM_AUTH_TOKEN = os.environ.get("BKAPP_IAM_AUTH_TOKEN")
# 权限中心的网址
BKAPP_IAM_HOST = get_env_or_raise("BKAPP_IAM_HOST")
# 权限中心拉取资源时目标系统的system id
BKAPP_IAM_SYSTEM_ID = get_env_or_raise("BKAPP_IAM_SYSTEM_ID")
# 蓝鲸SaaS平台url
BKAPP_PAAS_URL = get_env_or_raise("BKAPP_PAAS_URL")

USE_TZ = False
TIME_ZONE = "Asia/Shanghai"
LANGUAGE_CODE = "zh-hans"

LANGUAGES = (
    ("en", "English"),
    ("zh-hans", "简体中文"),
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("MYSQL_NAME"),  # 数据库名
        "USER": os.getenv("MYSQL_USER"),  # 数据库用户
        "PASSWORD": os.getenv("MYSQL_PASSWORD"),  # 数据库密码
        "HOST": os.getenv("MYSQL_HOST"),  # 数据库主机
        "PORT": int(os.getenv("MYSQL_PORT", "3306")),  # 数据库端口
    },
}

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = int(os.environ.get("REDIS_PORT"))
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
BROKER_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0"

"""
以下为框架代码 请勿修改
"""
# celery settings
if IS_USE_CELERY:
    INSTALLED_APPS = locals().get("INSTALLED_APPS", [])
    INSTALLED_APPS += ("django_celery_beat", "django_celery_results")
    # 设置使用上海时区
    CELERY_TIMEZONE = "Asia/Shanghai"
    CELERYBEAT_SCHEDULER = "django_celery_beat.schedulers.DatabaseScheduler"
    # 避免时区的问题
    CELERY_ENABLE_UTC = False
    DJANGO_CELERY_BEAT_TZ_AWARE = False

# remove disabled apps
if locals().get("DISABLED_APPS"):
    INSTALLED_APPS = locals().get("INSTALLED_APPS", [])
    DISABLED_APPS = locals().get("DISABLED_APPS", [])

    INSTALLED_APPS = [_app for _app in INSTALLED_APPS if _app not in DISABLED_APPS]

    _keys = (
        "AUTHENTICATION_BACKENDS",
        "DATABASE_ROUTERS",
        "FILE_UPLOAD_HANDLERS",
        "MIDDLEWARE",
        "PASSWORD_HASHERS",
        "TEMPLATE_LOADERS",
        "STATICFILES_FINDERS",
        "TEMPLATE_CONTEXT_PROCESSORS",
    )

    import itertools

    for _app, _key in itertools.product(DISABLED_APPS, _keys):
        if locals().get(_key) is None:
            continue
        locals()[_key] = tuple([_item for _item in locals()[_key] if not _item.startswith(_app + ".")])
