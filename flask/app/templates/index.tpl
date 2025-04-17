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
            padding: 20px;
            background-color: #f8f9fa;
        }
        h3 {
            color: rgb(12, 35, 70);
            margin-bottom: 20px;
            text-align: center;
        }
        p {
            
            margin: 10px 0;
        }
        .main-card {
            position: relative;
            margin: 0 auto;
            display: flex;
            padding: 10px 10px;
            justify-content: center;
            width: 300px;
            height: 200px;
            border: 2px solid blue;
        }
        .title-wrapper{
         
        }
    </style>
</head>
<body>
    <div class="main-card">
        <div class="title-wrapper">
            <h3>Students:</h3>
            <div>
                <p>{{groups}}</p>
            </div>
        </div>
    </div>
</body>
</html>