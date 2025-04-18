<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Groups</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="container py-5">
        <div class="card shadow-sm mx-auto" style="max-width: 400px;">
            <div class="card-body text-center">
                <h3 class="card-title text-primary">Student Groups</h3>
                <p class="card-text">{{ groups }}</p>
            </div>
        </div>
    </div>
</body>
</html>
