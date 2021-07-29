"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import datetime
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+o%czit6&vc!8+e8*4q)gd&1dyb0gdro5gxorpio*$h35w6dc2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

'''
ALLOWED_HOSTS = [
    '127.0.0.1',
    '192.168.0.11',
    'localhost',
    # '192.168.0.17'
]
'''
'''
# APPEND_SLASH = False
CORS_ORIGIN_WHITELIST = [
    "https://127.0.0.1:3000",
    "https://192.168.0.11:3000",
    "https://localhost:3000",
]
'''
ALLOWED_HOSTS = ['*']
#CORS_ORIGIN_WHITELIST = ['*']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [  # 기본 Permission 설정
        'rest_framework.permissions.AllowAny',  # 모든 계정 액세스 허용
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (  # Authenticationt 설정
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # API 실행 시 인증할 클래스 정의
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': [  # api 결과 전달 방식
        'rest_framework.renderers.JSONRenderer',  # Json 방식
    ],
    'DEFAULT_PARSER_CLASSES': [  # 요청 받을 때 body 형태
        'rest_framework.parsers.JSONParser',
        # 'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ],
    'EXCEPTION_HANDLER': 'user.utils.custom_exception_handler'
}
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'user.serializers.UserRegisterSerializer',
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1),  # Access 토큰 유효 기간
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=7),  # Refresh 토큰 유효 기간
    'ROTATE_REFRESH_TOKENS': True,  # Refresh 토큰 사용 여부
    # 블랙리스트 사용 여부, Refresh 토큰 사용 시 Refresh 토큰이 블랙리스트로 추가됨
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,  # auth_user 테이블의 last_login 필드 업데이트 사용 여부
    'ALGORITHM': 'HS256',  # 암호화 알고리즘
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,  # 토큰 확인 시 사용되는 확인키
    'AUDIENCE': None,  # 생성자 토큰 포함
    'ISSUER': None,  # 발급자 토큰 포함
    'AUTH_HEADER_TYPES': ('Bearer',),  # 인증 헤더 유형
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',  # 인증 헤더 명칭
    'USER_ID_FIELD': 'username',  # 사용자 식별을 위한 토큰에 포함할 사용자 모델의 DB 필드명
    'USER_ID_CLAIM': 'user_id',  # 사용자 식별을 저장하는 데 사용할 생성된 토큰의 클레임
    # 토큰 유형 지정 클레스
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken', 'rest_framework_simplejwt.tokens.RefreshToken'),
    'TOKEN_TYPE_CLAIM': 'token_type',  # 토큰 유형 저장하는 데 사용되는 클레임 명칭
    'JTI_CLAIM': 'jti',  # 토큰 고유 식별자 저장 클레임 명칭, 블랙리스트 앱에서 해지된 토큰 식별
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=1),
}
REST_USE_JWT = False  # 로그인 전 토큰 사용 여부
ACCOUNT_LOGOUT_ON_GET = False  # 로그아웃 설정, 로그아웃 시 GET 방식 사용

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'sslserver',
    'user',
    'dataset'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SITE_ID = 1
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend', 'build'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
AUTH_USER_MODEL = 'user.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'build', 'static')
]
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ROOT_PATH = BASE_DIR
MEDIA_URL = '/data/'
MEDIA_ROOT = f"{ROOT_PATH}/catdog/ai/data"
