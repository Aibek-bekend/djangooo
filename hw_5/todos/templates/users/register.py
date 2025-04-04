{% extends 'base.html' %}

{% block content %}
<div class="container mt-5">
    <h2>📝 Регистрация</h2>
    <form method="posts">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">✅ Зарегистрироваться</button>
    </form>
    <a href="{% url 'login' %}" class="btn btn-secondary">🔙 Уже есть аккаунт? Войти</a>
</div>
{% endblock %}