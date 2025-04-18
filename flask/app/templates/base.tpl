{% include "/header.tpl" ignore missing %}

<div class="container py-4">
    {% block content %} {% endblock %}
</div>

<div class="p-3 fs-5 bg-secondary text-white border rounded w-25 text-center m-3 shadow-sm mx-auto">
    <a href="/" class="text-white text-decoration-none">🔙 Return</a>
</div>

{% include "/footer.tpl" ignore missing %}