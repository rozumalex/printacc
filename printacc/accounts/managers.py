from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('Username is a required field.')
        if not email:
            raise ValueError('Email is a required field.')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)

    def create_admin(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Admin must have is_admin=True.')

        return self._create_user(username, email, password, **extra_fields)

    def create_dealer(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_dealer', True)

        if extra_fields.get('is_dealer') is not True:
            raise ValueError('Dealer must have is_dealer=True.')

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        user_obj = self.create_admin(username, email, password, **extra_fields)
        return user_obj

    def admins(self):
        return self.filter(is_admin=True)

    def dealers(self):
        return self.filter(is_dealer=True)

    def users(self):
        return self.filter(is_dealer=False, is_admin=False)
