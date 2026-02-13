<?php
session_start();

if (!isset($_SESSION["chat"]) || !is_array($_SESSION["chat"])) {
    $_SESSION["chat"] = [];
}

$error = "";

function ask_ollama(string $message): array
{
    $url = "http://localhost:11434/api/generate";
    $model = "qwen2.5-coder:7b";

    $instruction = "You are a helpful assistant. Reply only in English. Keep the answer to one concise sentence unless the user explicitly asks for more detail.";

    $payload = [
        "model" => $model,
        "prompt" => $instruction . "\n\nUser message:\n" . $message,
        "stream" => false
    ];

    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ["Content-Type: application/json"]);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
    curl_setopt($ch, CURLOPT_TIMEOUT, 60);

    $response = curl_exec($ch);
    $curlError = curl_error($ch);

    if ($response === false) {
        return [false, "Error de conexion con Ollama: " . $curlError];
    }

    $decoded = json_decode($response, true);
    if (!is_array($decoded) || !isset($decoded["response"])) {
        return [false, "Respuesta invalida desde Ollama."];
    }

    return [true, trim((string) $decoded["response"])];
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    if (isset($_POST["reset_chat"])) {
        $_SESSION["chat"] = [];
        header("Location: " . strtok($_SERVER["REQUEST_URI"], "?"));
        exit;
    }

    $mensaje = trim((string) ($_POST["mensaje"] ?? ""));

    if ($mensaje === "") {
        $error = "Please write a message before sending.";
    } else {
        $_SESSION["chat"][] = ["role" => "user", "text" => $mensaje];
        [$ok, $result] = ask_ollama($mensaje);

        if ($ok) {
            $_SESSION["chat"][] = ["role" => "assistant", "text" => $result];
        } else {
            $error = $result;
        }
    }
}
?>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>005 AI Chat</title>
  <style>
    :root {
      --bg1: #0a0f1c;
      --bg2: #121c33;
      --card: #ffffff;
      --muted: #5f6b7a;
      --border: #dde3ec;
      --user: #ffe9b8;
      --ai: #d9f3d2;
      --primary: #173b8f;
      --danger: #b42318;
    }

    * { box-sizing: border-box; }

    html, body {
      margin: 0;
      min-height: 100%;
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
      color: #0d1b2a;
      background:
        radial-gradient(circle at 10% 20%, rgba(255,255,255,0.08) 0%, transparent 35%),
        radial-gradient(circle at 90% 80%, rgba(255,255,255,0.06) 0%, transparent 40%),
        linear-gradient(145deg, var(--bg1), var(--bg2));
    }

    .wrap {
      width: min(980px, 94vw);
      margin: 28px auto;
    }

    .app {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 18px;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0,0,0,0.25);
    }

    .head {
      padding: 16px 20px;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      background: linear-gradient(90deg, #f6f8fc, #edf2fb);
    }

    .title {
      margin: 0;
      font-size: 1.1rem;
      color: var(--primary);
    }

    .subtitle {
      margin: 4px 0 0;
      font-size: 0.88rem;
      color: var(--muted);
    }

    .reset-btn {
      border: 1px solid #f0c0c0;
      background: #fff5f5;
      color: #7a1f1f;
      border-radius: 10px;
      padding: 8px 12px;
      font-weight: 600;
      cursor: pointer;
    }

    .chat {
      height: min(60vh, 620px);
      overflow: auto;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: linear-gradient(180deg, #ffffff, #fbfcfe);
    }

    .empty {
      margin: auto;
      text-align: center;
      color: var(--muted);
      max-width: 500px;
      line-height: 1.45;
    }

    .msg {
      max-width: 80%;
      padding: 11px 14px;
      border-radius: 12px;
      line-height: 1.4;
      white-space: pre-wrap;
      word-wrap: break-word;
      border: 1px solid var(--border);
    }

    .msg.user {
      align-self: flex-end;
      background: var(--user);
      border-bottom-right-radius: 4px;
    }

    .msg.assistant {
      align-self: flex-start;
      background: var(--ai);
      border-bottom-left-radius: 4px;
    }

    .composer {
      border-top: 1px solid var(--border);
      padding: 14px;
      background: #f9fbff;
    }

    .composer form {
      display: flex;
      gap: 10px;
    }

    .composer input[type="text"] {
      flex: 1;
      border: 1px solid #c8d4e6;
      border-radius: 10px;
      padding: 12px;
      font-size: 0.95rem;
      outline: none;
    }

    .composer input[type="text"]:focus {
      border-color: #6b93e6;
      box-shadow: 0 0 0 4px rgba(53, 100, 205, 0.15);
    }

    .composer button[type="submit"] {
      border: 0;
      background: var(--primary);
      color: #fff;
      border-radius: 10px;
      padding: 12px 18px;
      font-weight: 700;
      cursor: pointer;
    }

    .error {
      margin: 10px 0 0;
      color: var(--danger);
      font-size: 0.9rem;
      font-weight: 600;
    }

    @media (max-width: 720px) {
      .msg { max-width: 92%; }
      .head { flex-direction: column; align-items: flex-start; }
    }
  </style>
</head>
<body>
  <div class="wrap">
    <section class="app">
      <header class="head">
        <div>
          <h1 class="title">AI Chat (005)</h1>
          <p class="subtitle">Improved version of 004: better UI + stable input/API handling</p>
        </div>
        <form method="post" action="">
          <button class="reset-btn" type="submit" name="reset_chat" value="1">Clear chat</button>
        </form>
      </header>

      <main class="chat" id="chat">
        <?php if (count($_SESSION["chat"]) === 0): ?>
          <p class="empty">Write your first message below. The chat history is stored in your session.</p>
        <?php else: ?>
          <?php foreach ($_SESSION["chat"] as $entry): ?>
            <?php
              $role = ($entry["role"] ?? "") === "user" ? "user" : "assistant";
              $text = htmlspecialchars((string) ($entry["text"] ?? ""), ENT_QUOTES, "UTF-8");
            ?>
            <div class="msg <?php echo $role; ?>"><?php echo $text; ?></div>
          <?php endforeach; ?>
        <?php endif; ?>
      </main>

      <footer class="composer">
        <form method="post" action="">
          <input
            type="text"
            name="mensaje"
            placeholder="Write your question..."
            autocomplete="off"
          >
          <button type="submit">Send</button>
        </form>
        <?php if ($error !== ""): ?>
          <div class="error"><?php echo htmlspecialchars($error, ENT_QUOTES, "UTF-8"); ?></div>
        <?php endif; ?>
      </footer>
    </section>
  </div>

  <script>
    const chat = document.getElementById("chat");
    chat.scrollTop = chat.scrollHeight;
  </script>
</body>
</html>
