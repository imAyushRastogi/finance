# urls.py
from django.urls import path
from. import views

urlpatterns = [
    path('track_expense/', views.track_expense, name='track_expense'),
    path('plan_budget/', views.plan_budget, name='plan_budget'),
    path('set_financial_goal/', views.set_financial_goal, name='set_financial_goal'),
    path('ai_insights/', views.get_ai_insights, name='ai_insights'),
]