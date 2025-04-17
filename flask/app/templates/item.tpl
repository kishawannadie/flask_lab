{% if it.id is studentExist %}
    <div class="item-wrapper">
    Id: {{it.id}}<br>
    Name: {{it.name}}<br>
    Age: {{it.age}} <br>
    Group: {{it.groupnumber}} <br>
    Faculty: {{it.faculty}} <br>

    {% if it is HeadStudent %}
        Phone: {{it.phone}}<br>
    {% elif it is UnionOrganizer %}
        Salary: {{it.salary}}<br>
    {% endif %}

    <a href="{{url_for('.showform', id=it.id)}}">Edit</a>
    <a href="{{url_for('.deleteitem', id=it.id)}}">Delete</a>
    </div>
    <br><hr><br>
{% else %}
    <h2><u><i>Creating new student</i></u></h2>
{% endif %}
