<style>
.custom-add-btn {
    background-color: #4a90e2; /* мягкий синий */
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 6px;
    transition: background-color 0.3s ease;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
.custom-add-btn:hover {
    background-color: #357ab8;
    text-decoration: none;
    color: white;
}
</style>

<div class="text-center mt-4">
    <a href="{{ url_for('.showform', id=0) }}" class="custom-add-btn">
        ➕ Add a student
    </a>
</div>
