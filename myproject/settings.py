import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env
load_dotenv(BASE_DIR / ".env")

# ========================
# SECURITY
# ========================
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "unsafe-secret-key")
DEBUG = False
ALLOWED_HOSTS = ["*"]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# ========================
# INSTALLED APPS
# ========================
INSTALLED_APPS = [
    "corsheaders",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",

    "users",
    "resume",
]

# ========================
# MIDDLEWARE (ORDER MATTERS)
# ========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ========================
# CORS / CSRF
# ========================
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = False

CSRF_TRUSTED_ORIGINS = [
    "https://resumeanalysisbackend-production.up.railway.app",
    "http://localhost:3000",
]

# ========================
# URLS / WSGI
# ========================
ROOT_URLCONF = "myproject.urls"
WSGI_APPLICATION = "myproject.wsgi.application"

# ========================
# TEMPLATES
# ========================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ========================
# DATABASE (SQLite OK FOR MVP)
# ========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ========================
# DJANGO REST FRAMEWORK
# ========================
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny",
    ),
}

# ========================
# STATIC FILES (RAILWAY FIX)
# ========================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# ========================
# DEFAULT PRIMARY KEY
# ========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ========================
# GEMINI
# ========================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
