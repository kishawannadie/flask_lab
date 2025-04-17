{% extends "base.tpl" %}

{% block content %}

<div class="container">
    {% if it.id != '0' %}
            <h2 class="mt-4">Information about student</h2>
            <p class="lead">{{ about }}</p>
    {% endif %}

    <h2 class="mt-4">Fill in the following fields</h2>
    <form action='{{url_for('.add')}}' method="POST" class="mt-3">
        <input type="hidden" name="id" value="{{ it.id }}">

        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" class="form-control" id="name" name="name" value="{{ it.name }}">
        </div>

        <div class="form-group">
            <label for="age">Age:</label>
            <input type="text" class="form-control" id="age" name="age" value="{{ it.age }}">
        </div>

        <div class="form-group">
            <label for="groupnumber">Group:</label>
            <input type="text" class="form-control" id="groupnumber" name="groupnumber" value="{{ it.groupnumber }}">
        </div>

        <div class="form-group mb-3">
            <label for="faculty">Faculty:</label>
            <input type="text" class="form-control" id="faculty" name="faculty" value="{{ it.faculty }}">
        </div>

        {% include 'student_type_markup.tpl' ignore missing %}

        <button type="submit" class="btn btn-primary mt-3">Submit</button>
    </form>
</div>

{% endblock %}