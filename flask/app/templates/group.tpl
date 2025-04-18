{% extends "/base.tpl" %}

{% block content %}
<div class="container py-4">
    <div class="row g-3">
        {% for it in items %}
            {% include "/item.tpl" ignore missing %}
        {% else %}
            <p class="text-muted text-center">Student List is empty</p>
        {% endfor %}
    </div>
</div>

{% include "/add.tpl" ignore missing %}
{% endblock %}
