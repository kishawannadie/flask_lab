{% extends "/base.tpl" %}

{% block content %}
<div class="wrapper">
    {% for it in items %}
{% include "/item.tpl" ignore missing %}
    {% else %}

Student List is empty
    {% endfor %}
</div>
{% include "/add.tpl" ignore missing %}
{% endblock %}