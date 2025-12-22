<?php
session_start();

$message = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $username = $_POST['usuario'] ?? "";
    $password = $_POST['contrasena'] ?? "";

    // ---- Username test ----
    if ($username === "") {
        $message = "Empty username → Rejected";
    } elseif (strlen($username) < 5) {
        $message = "Username too short (<5) → Rejected";
    } elseif (strlen($username) > 20) {
        $message = "Username too long (>20) → Rejected";
    } elseif (!preg_match('/^[a-zA-Z0-9]+$/', $username)) {
        $message = "Username contains invalid characters → Rejected";
    }

    // ---- Password checking within parametres ----
    elseif ($password === "") {
        $message = "Empty password → Rejected";
    } elseif (strlen($password) < 8) {
        $message = "Password too short (<8) → Rejected";
    } elseif (strlen($password) > 16) {
        $message = "Password too long (>16) → Rejected";
    } elseif (
        !preg_match('/[a-zA-Z]/', $password) ||
        !preg_match('/[0-9]/', $password)
    ) {
        $message = "Password without required letter/number combination → Rejected";
    }

    // ---- If everything works: ----
    else {
        $_SESSION['usuario'] = $username;
        $message = "Login accepted";
    }
}
?>


<!doctype html>
<html lang="es">
<head>
  <title>Pruebas Clases y valores</title>
  <meta charset="utf-8">
</head>
<body>
<!-- Showing different messages depending on outcome-->
<?php if ($message): ?>
<p style="color:red"><?= $message ?></p>
<?php endif; ?>

<form method="POST">
  <input type="text" name="usuario" placeholder="usuario">
  <input type="password" name="contrasena" placeholder="contraseña">
  <input type="submit">
</form>

</body>
</html>
