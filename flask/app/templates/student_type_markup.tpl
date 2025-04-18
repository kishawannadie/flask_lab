<script>
    function toggleInputVisibility() {
        var selectElement = document.getElementById("studentTypeSelect");
        var inputElement = document.getElementById("additionalInput");
        var labelElement = document.getElementById("additionalFieldLabel");
        var blockElement = document.getElementById("additionalBlock");

        if (selectElement.value === "studentTypeOption_head" || selectElement.value === "studentTypeOption_organizer") {
            blockElement.style.display = "block";
            if (selectElement.value === "studentTypeOption_head") {
                labelElement.innerText = inputElement.placeholder = 'Phone number';
            } else {
                labelElement.innerText = inputElement.placeholder = 'Salary';
            }
        } else {
            blockElement.style.display = "none";
        }
    }
</script>

<div class="mb-3">
    <label for="studentTypeSelect" class="form-label">Choose student type:</label>
    <select id="studentTypeSelect" name="studentTypeSelect" class="form-select" onchange="toggleInputVisibility()">
        <option value="studentTypeOption_base">Base Student</option>
        <option value="studentTypeOption_head" {% if it is HeadStudent %}selected{% endif %}>Head Student</option>
        <option value="studentTypeOption_organizer" {% if it is UnionOrganizer %}selected{% endif %}>Union Organizer</option>
    </select>
</div>

<div id="additionalBlock" class="border p-3 rounded bg-light" style="display: {% if it is HeadStudent or it is UnionOrganizer %}block{% else %}none{% endif %};">
    <div class="mb-2">
        <label for="additionalInput" class="form-label" id="additionalFieldLabel">
            {% if it is HeadStudent %}Phone number{% elif it is UnionOrganizer %}Salary{% else %}Additional Info{% endif %}
        </label>
        <input type="text" id="additionalInput" name="additionalInput" class="form-control"
               placeholder="{% if it is HeadStudent %}Phone number{% elif it is UnionOrganizer %}Salary{% endif %}"
               value="{% if it is HeadStudent %}{{ it.phone }}{% elif it is UnionOrganizer %}{{ it.salary }}{% endif %}">
    </div>
</div>