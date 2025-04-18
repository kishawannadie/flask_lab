{% extends "base.tpl" %}

{% block content %}

<div class="container py-4">
    {% if it.id != '0' %}
        <h2 class="text-center mb-4">Information about student</h2>
        <p class="lead text-center">{{ about }}</p>
    {% endif %}

    <h2 class="text-center mb-4">Fill in the following fields</h2>

    <form action='{{url_for('.add')}}' method="POST" class="border p-4 rounded bg-light shadow-sm">
        <input type="hidden" name="id" value="{{ it.id }}">

        <div class="mb-3">
            <label for="name" class="form-label">Name:</label>
            <input type="text" class="form-control" id="name" name="name" value="{{ it.name }}">
        </div>

        <div class="mb-3">
            <label for="age" class="form-label">Age:</label>
            <input type="text" class="form-control" id="age" name="age" value="{{ it.age }}">
        </div>

        <div class="mb-3">
            <label for="groupnumber" class="form-label">Group:</label>
            <input type="text" class="form-control" id="groupnumber" name="groupnumber" value="{{ it.groupnumber }}">
        </div>

        <div class="mb-3">
            <label for="faculty" class="form-label">Faculty:</label>
            <input type="text" class="form-control" id="faculty" name="faculty" value="{{ it.faculty }}">
        </div>

        {% include 'student_type_markup.tpl' ignore missing %}

        <button type="submit" class="btn btn-primary mt-3 w-100">Submit</button>
    </form>
</div>

{% endblock %}
