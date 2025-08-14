import os
from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        User = get_user_model()
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        # Only run if env variables are set
        if username and email and password:
            try:
                if not User.objects.filter(username=username).exists():
                    User.objects.create_superuser(
                        username=username,
                        email=email,
                        password=password
                    )
                    print(f"✅ Superuser '{username}' created successfully.")
            except OperationalError:
                # This happens during migrate or before DB is ready — safe to ignore
                pass
