<!doctype html>
<html>
	<head>
    <style>
  :root{
    --bg: #0b1020;
    --card: rgba(255,255,255,0.06);
    --border: rgba(255,255,255,0.12);
    --text: rgba(255,255,255,0.92);
    --muted: rgba(255,255,255,0.65);
    --accent: #7c3aed;
    --shadow: 0 18px 60px rgba(0,0,0,0.55);
    --radius: 22px;
  }

  *{ box-sizing:border-box; }
  html,body{ height:100%; }
  body{
    margin:0;
    font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
    color: var(--text);
    background:
      radial-gradient(900px 600px at 15% 10%, rgba(124,58,237,0.35), transparent 60%),
      radial-gradient(900px 600px at 85% 90%, rgba(59,130,246,0.22), transparent 60%),
      var(--bg);
    display:flex;
    justify-content:center;
    align-items:center;
    padding:24px;
  }

  main{
    width:min(560px, 100%);
    min-height:520px;
    padding:18px;
    border:1px solid var(--border);
    border-radius: var(--radius);
    background: var(--card);
    box-shadow: var(--shadow);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    display:flex;
    flex-direction:column;
    gap:14px;
  }

  section{
    flex:1;
    display:flex;
    overflow:hidden;
    border-radius: 18px;
    border:1px solid rgba(255,255,255,0.08);
    background: rgba(0,0,0,0.18);
  }

  article{
    width:100%;
    padding:18px 18px;
    margin:0;
    overflow:auto;
    line-height:1.55;
    font-size:15px;
    color: var(--text);
  }

  /* Chat bubble look */
  article{
    position:relative;
  }
  article::before{
    content:"AI";
    display:inline-flex;
    align-items:center;
    justify-content:center;
    width:28px;
    height:28px;
    border-radius:999px;
    background: rgba(124,58,237,0.22);
    border:1px solid rgba(124,58,237,0.35);
    color: rgba(255,255,255,0.85);
    font-size:12px;
    margin-right:10px;
    flex:0 0 auto;
  }

  form{
    display:flex;
    gap:10px;
    padding:10px;
    border-radius: 18px;
    border:1px solid rgba(255,255,255,0.10);
    background: rgba(0,0,0,0.22);
  }

  input{
    width:100%;
    padding:14px 14px;
    border-radius: 14px;
    border:1px solid rgba(255,255,255,0.10);
    background: rgba(255,255,255,0.06);
    color: var(--text);
    outline:none;
    font-size:15px;
    transition: border-color .2s ease, box-shadow .2s ease, transform .08s ease;
  }

  input::placeholder{
    color: var(--muted);
  }

  input:focus{
    border-color: rgba(124,58,237,0.55);
    box-shadow: 0 0 0 4px rgba(124,58,237,0.22);
  }

  input:active{
    transform: translateY(1px);
  }

  /* Scrollbar (nice on Chrome) */
  article::-webkit-scrollbar{ width:10px; }
  article::-webkit-scrollbar-track{ background: transparent; }
  article::-webkit-scrollbar-thumb{
    background: rgba(255,255,255,0.14);
    border-radius: 999px;
  }
  article::-webkit-scrollbar-thumb:hover{
    background: rgba(255,255,255,0.22);
  }
</style>

  </head>
  <body>
  	<main>
    	<section>
      	<article>
          <?php
            $OLLAMA_URL = "http://localhost:11434/api/generate";
            $MODEL = "qwen2.5:7b-instruct";

            $mensaje = trim($_POST['mensaje'] ?? '');

            if ($mensaje === '') {
            echo "Write a question below.";
            } else {

            $prompt = "You are here to help in my studies. Im studying a Grado Superior in Desarollo Aplicationes Web. Answer in clear, simple English. Keep it direct.\n\nQuestion: ".$mensaje;

            $data = [
                "model" => $MODEL,
                "prompt" => $prompt,
                "stream" => false
            ];

            $ch = curl_init($OLLAMA_URL);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_HTTPHEADER, ["Content-Type: application/json"]);
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));

            $response = curl_exec($ch);
            if ($response === false) {
                die("cURL error: " . curl_error($ch));
            }

            $result = json_decode($response, true);
            echo $result["response"] ?? "No response";
            }
            ?>

        </article>
      </section>
      <form action="?" method="POST">
      <input type="text" name="mensaje">
      </form>
    </main>
  </body>
</html>