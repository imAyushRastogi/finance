# views.py
from django.shortcuts import render
from .models import User, Expense, Budget, FinancialGoal
from .ai_assistant import AIAssistant

def track_expense(request):
    user = request.user
    expenses = Expense.objects.filter(user=user)
    return render(request, 'track_expense.html', {'expenses': expenses})

def plan_budget(request):
    user = request.user
    budgets = Budget.objects.filter(user=user)
    return render(request, 'plan_budget.html', {'budgets': budgets})

def set_financial_goal(request):
    user = request.user
    goals = FinancialGoal.objects.filter(user=user)
    return render(request, 'set_financial_goal.html', {'goals': goals})

def get_ai_insights(request):
    user = request.user
    user_data = User.objects.get(id=user.id)
    ai_assistant = AIAssistant()
    insights = ai_assistant.get_insights(user_data)
    return render(request, 'ai_insights.html', {'insights': insights})