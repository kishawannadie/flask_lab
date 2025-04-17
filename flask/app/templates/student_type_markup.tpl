<script>
    function toggleInputVisibility() {
        var selectElement = document.getElementById("studentTypeSelect");
        var inputElement = document.getElementById("additionalInput");
        var labelElement = document.getElementById("additionalFieldLabel");
        var blockElement = document.getElementById("additionalBlock");

        if (selectElement.value === "studentTypeOption_head" || selectElement.value === "studentTypeOption_organizer")
        {
            blockElement.style.display = "block";
            if(selectElement.value == "studentTypeOption_head") labelElement.innerText = inputElement.placeholder = 'Phone number';
            else labelElement.innerText = inputElement.placeholder = 'Salary';
        }
        else blockElement.style.display = "none";

    }
</script>
<div>
<p style="font-size: 24px;">
<label>Choose student type:
    <select id="studentTypeSelect" name='studentTypeSelect' onchange="toggleInputVisibility()">
            <option value="studentTypeOption_base">Base Student</option>
            <option value="studentTypeOption_head" {% if it is HeadStudent %}selected{% endif %}>Head Student</option>
            <option value="studentTypeOption_organizer" {% if it is UnionOrganizer %}selected{% endif %}>Union Orginizer</option>
    </select>
</label>
</p>
</div>
<div id='additionalBlock' style="display: {% if it is HeadStudent or it is UnionOrganizer %} block {%else%} none {%endif%};">
<input value="{% if it is HeadStudent %} {{ it.phone }} {% elif it is UnionOrganizer %} {{ it.salary }} {% endif %}" type="text" id="additionalInput" name="additionalInput">
</div>


