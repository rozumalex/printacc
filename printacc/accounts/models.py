from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from .managers import AccountManager


class Account(AbstractUser):
    objects = AccountManager()

    is_admin = models.BooleanField(default=False, verbose_name='Admin')
    is_dealer = models.BooleanField(default=False, verbose_name='Dealer')

    def last_used_time(self):
        return 'n/a'

    def total_usages(self):
        return 'n/a'

    def daily_usage(self):
        return 'n/a'

    def usages_for_last_week(self):
        return 'n/a'

    class Meta:
        ordering = ['username']
        unique_together = ('email',)


class User(Account):

    class Meta:
        proxy = True

    def last_used_time(self):
        last_usage = self.statistics_set.filter(
            user=self.id).order_by('-date_used').first()
        if not last_usage:
            return 'never'
        return self.statistics_set.filter(
            user=self.id).order_by('-date_used').first()

    def total_usages(self):
        return self.statistics_set.filter(
            user=self.id).all().count()

    def daily_usage(self):
        delta = timezone.now() - self.date_joined + timezone.timedelta(days=1)
        return int(self.total_usages() / delta.days)

    def usages_for_last_week(self):
        period = timezone.now() - timezone.timedelta(days=7)
        return self.statistics_set.filter(user=self.id,
                                          date_used__gte=period).count()


class Dealer(Account):

    class Meta:
        proxy = True

    def last_used_time(self):
        return self.statistics_set.filter(
            plotter__dealer__id=self.id).order_by('-date_used').first()

    def total_usages(self):
        return self.statistics_set.filter(
            plotter__dealer__id=self.id).count()

    def daily_usage(self):
        delta = timezone.now() - self.date_joined + timezone.timedelta(days=1)
        return int(self.total_usages() / delta.days)

    def usages_for_last_week(self):
        period = timezone.now() - timezone.timedelta(days=7)
        return self.statistics_set.filter(plotter__dealer__id=self.id,
                                          date_used__gte=period).count()


class Plotter(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE,
                               related_name='owner')
    model = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField(default=timezone.now)
    users = models.ManyToManyField(User, blank=True)

    def last_used_time(self):
        return self.statistics_set.filter(
            plotter=self.id).order_by('-date_used').first()

    def total_usages(self):
        return self.statistics_set.filter(
            plotter=self.id).all().count()

    def daily_usage(self):
        delta = timezone.now() - self.date_added + timezone.timedelta(days=1)
        return int(self.total_usages() / delta.days)

    def usages_for_last_week(self):
        period = timezone.now() - timezone.timedelta(days=7)
        return self.statistics_set.filter(plotter__id=self.id,
                                          date_used__gte=period).count()

    def dealers_email(self):
        return self.dealer.email

    def __str__(self):
        return self.model


class Pattern(models.Model):
    name = models.CharField(max_length=255)
    plotter = models.ForeignKey(Plotter, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField(default=timezone.now)

    def last_used_time(self):
        return self.statistics_set.filter(
            pattern=self.id).order_by('-date_used').first()

    def total_usages(self):
        return self.statistics_set.filter(pattern=self.id).all().count()

    def daily_usage(self):
        delta = timezone.now() - self.date_added + timezone.timedelta(days=1)
        return int(self.total_usages() / delta.days)

    def usages_for_last_week(self):
        period = timezone.now() - timezone.timedelta(days=7)
        return self.statistics_set.filter(pattern__id=self.id,
                                          date_used__gte=period).count()

    def __str__(self):
        return self.name


class Clients(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE,
                               related_name='dealer')
    limit = models.IntegerField()

    def last_used_time(self):
        return self.statistics_set.filter(
            plotter=self.id).order_by('-date_used').first()

    def total_usages(self):
        return self.statistics_set.filter(
            plotter=self.id).all().count()

    def daily_usage(self):
        delta = timezone.now() - self.date_joined
        return self.total_usages() / delta.days()

    def usages_in_period(self, days):
        period = timezone.now() - timezone.timedelta(days=days)
        return self.statistics_set.filter(user=self.id,
                                          date_used__gte=period)


class Admin(Account):
    is_admin = True
    is_dealer = False

    class Meta:
        proxy = True


class Statistics(models.Model):
    plotter = models.ForeignKey(Plotter, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    date_used = models.DateTimeField(default=timezone.now)
