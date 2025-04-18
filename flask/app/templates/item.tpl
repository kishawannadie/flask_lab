{% if it.id is studentExist %}
    <div class="item-wrapper p-3 border rounded shadow-sm bg-white">
        <p><strong>Id:</strong> {{ it.id }}</p>
        <p><strong>Name:</strong> {{ it.name }}</p>
        <p><strong>Age:</strong> {{ it.age }}</p>
        <p><strong>Group:</strong> {{ it.groupnumber }}</p>
        <p><strong>Faculty:</strong> {{ it.faculty }}</p>

        {% if it is HeadStudent %}
            <p><strong>Phone:</strong> {{ it.phone }}</p>
        {% elif it is UnionOrganizer %}
            <p><strong>Salary:</strong> {{ it.salary }}</p>
        {% endif %}

        <a href="{{ url_for('.showform', id=it.id) }}" class="btn btn-outline-primary btn-sm">✏ Edit</a>
        <a href="{{ url_for('.deleteitem', id=it.id) }}" class="btn btn-outline-danger btn-sm">🗑 Delete</a>
    </div>
{% else %}
    <h2 class="text-muted text-center my-4"><u><i>Creating new student</i></u></h2>
{% endif %}
