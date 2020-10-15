from django.urls import path

from .views import api, users, dealers, patterns, plotters


app_name = 'accounts'

urlpatterns = [
    path('', api.API.as_view(), name='api'),
    path('signup/', users.UsersCreateView.as_view(), name='signup'),
    path('login/', users.UsersLoginView.as_view(), name='login'),
    path('users/', users.UsersListView.as_view(), name='users-list'),
    path('users/<pk>/', users.UsersDetailView.as_view(), name='users-detail'),
    # path('users/<pk>/stat/', views.UserStatView.as_view(), name='user-stat'),
    # path('users/<pk>/manage/', views.UserAddView.as_view(),
    # name='user-manage'),
    path('dealers/', dealers.DealersListView.as_view(), name='dealers-list'),
    path('dealers/<pk>/', dealers.DealersDetailView.as_view(),
         name='dealers-detail'),
    # path('dealers/<pk>/stat/', views.DealerStatView.as_view(),
    # name='dealer-stat'),
    path('plotters/', plotters.PlottersListView.as_view(),
         name='plotters-list'),
    path('plotters/<pk>/', plotters.PlottersDetailView.as_view(),
         name='plotters-detail'),
    # path('plotters/<pk>/stat/', views.PlotterStatView.as_view(),
    #      name='plotter-stat'),
    # path('plotters/<pk>/manage/', views.PlotterAddView.as_view(),
    #      name='plotter-manage'),
    path('plotters/<pk>/patterns/', patterns.PatternsListView.as_view(),
         name='patterns-list'),
    path('plotters/<pk>/patterns/<pattern_id>/',
         patterns.PatternsDetailView.as_view(),
         name='patterns-detail'),
    # path('plotters/<pk>/patterns/<pattern_id>/use', name='pattern-use'),
    # path('plotters/<pk>/patterns/<pattern_id>/stat/',
    #      views.PatternStatView.as_view(), name='pattern-stat'),
    # path('plotters/<pk>/patterns/<pattern_id>/manage/',
    #      views.PatternStatView.as_view(), name='pattern-manage'),
]
