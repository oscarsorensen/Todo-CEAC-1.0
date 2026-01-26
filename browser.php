<?php
date_default_timezone_set("Europe/Madrid");
$items = array_diff(scandir("."), ["..", "."]);

function pretty_size($bytes) {
    if ($bytes < 1024) return $bytes . " B";
    if ($bytes < 1024*1024) return round($bytes/1024, 1) . " KB";
    return round($bytes/1024/1024, 1) . " MB";
}

function file_language($filename) {
    $ext = strtolower(pathinfo($filename, PATHINFO_EXTENSION));
    return match($ext) {
        "php" => "PHP",
        "html" => "HTML",
        "css" => "CSS",
        "js" => "JS",
        "py" => "Python",
        "sql" => "SQL",
        "json" => "JSON",
        "md" => "Markdown",
        "jpg", "jpeg", "png", "gif", "webp", "svg" => "Image",
        default => ""
    };
}

function dir_count($dir) {
    $count = 0;
    foreach (array_diff(scandir($dir), ['.', '..']) as $item) {
        $path = "$dir/$item";
        if (is_dir($path)) {
            $count += dir_count($path);
        } else {
            $count++;
        }
    }
    return $count;
}

function dir_size($dir) {
    $size = 0;
    foreach (array_diff(scandir($dir), ['.', '..']) as $file) {
        $path = "$dir/$file";
        if (is_file($path)) {
            $size += filesize($path);
        } elseif (is_dir($path)) {
            $size += dir_size($path);
        }
    }
    return $size;
}

function current_directory_total() {
    $total = 0;
    foreach (array_diff(scandir("."), ['.', '..']) as $item) {
        if ($item === '.git') continue;
        $path = "./$item";
        if (is_dir($path)) {
            $total += dir_size($path);
        } elseif (is_file($path)) {
            $total += filesize($path);
        }
    }
    return $total;
}

$totalSize = pretty_size(current_directory_total());

// --- Only these belong to Files (whitelist) ---
$special_files = [
    ".DS_Store",
    "browser.php",
    "index.php",
    "ting.md",
    ".git",
    ".gitignore",
];

// split using whitelist
$folders = [];
$files   = [];

foreach ($items as $item) {
    if (in_array($item, $special_files, true)) {
        $files[] = $item;
    } else {
        $folders[] = $item;
    }
}

sort($folders, SORT_NATURAL | SORT_FLAG_CASE);
sort($files, SORT_NATURAL | SORT_FLAG_CASE);

$requestPath = trim($_SERVER['REQUEST_URI'], '/');
$parts = $requestPath ? explode('/', $requestPath) : [];

?>



<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">

<title>Localhost · Project Browser</title>

<style>
:root{
    --bg: #111827;     /* lighter background */
--panel: #1f2937;  /* lighter cards */
--panel2: #263244; /* hover */
--border: #334155; /* clearer borders */


  --text: #e6edf3;
  --muted: #8b949e;

  --accent: #58a6ff;
  --link: #58a6ff;

  --radius: 14px;
  --shadow: 0 10px 26px rgba(0,0,0,0.45);
}

*{ box-sizing: border-box; }

html, body{ height: 100%; }

body{
  margin: 40px;
  color: var(--text);
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
-webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
  font-weight: 400;
  .left span:nth-child(2){
  font-weight: 600;
}
  /* IMPORTANT: solid base so “empty space” never becomes a color block */
  background: var(--bg);
}

/* Subtle ambient glow layer (safe, never looks like a big block) */
body::before{
  content:"";
  position: fixed;
  inset: 0;
  z-index: -1;
  pointer-events: none;

  background:
    radial-gradient(900px 520px at 15% 10%, rgba(88,166,255,0.10), transparent 60%),
    radial-gradient(900px 520px at 90% 15%, rgba(46,160,67,0.08), transparent 60%);
}

/* Title */
h1{
  margin: 0;
  font-size: 34px;
  font-weight: 800;
  letter-spacing: -0.6px;
  color: var(--text);
  margin-bottom: 6px;
}

.subtitle{
  font-size: 14px;
  color: var(--muted);
  margin-bottom: 28px;
}

/* Breadcrumb */
.breadcrumb-center{ position: relative; z-index: 10; }

.breadcrumb-box{
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  top: 0px;

  height: 42px;
  padding: 0 18px;

  display: flex;
  align-items: center;
  justify-content: center;

  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}

.breadcrumb{
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  font-weight: 650;
  color: var(--muted);
  white-space: nowrap;
}

.breadcrumb a{
  color: var(--link);
  text-decoration: none;
}

.breadcrumb a:hover{
  color: var(--text);
  text-decoration: underline;
  text-underline-offset: 3px;
}

/* Total size */
.total-box{
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  top: 155px;

  height: 42px;
  padding: 0 18px;

  display: flex;
  align-items: center;
  justify-content: center;

  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);

  font-size: 14px;
  font-weight: 750;
  color: var(--accent);
}

/* Search */
#search{
  width: 300px;
  background: var(--panel);
  border: 1px solid var(--border);
  padding: 11px 14px;
  border-radius: var(--radius);
  color: var(--text);
  margin-bottom: 22px;
  font-size: 14px;
  outline: none;
  transition: 0.15s ease;
}

#search::placeholder{
  color: rgba(230,237,243,0.35);
}

#search:focus{
  border-color: rgba(88,166,255,0.55);
  box-shadow: 0 0 0 3px rgba(88,166,255,0.18);
  background: var(--panel2);
}

/* Section headers */
.section{
  margin-top: 34px;
  margin-bottom: 12px;

  font-size: 12px;
  letter-spacing: 0.14em;
  color: rgba(230,237,243,0.40);
  text-transform: uppercase;
  font-weight: 800;

  display: flex;
  align-items: center;
  gap: 10px;

  background: transparent;
  border: none;
  padding: 0;
}

.chevron{
  width: 14px;
  display: inline-block;
  transition: .15s;
  transform: rotate(0deg);
  opacity: .85;
}
.chevron.open{ transform: rotate(90deg); }

/* Cards */
.item{
  position: relative;
  display: flex;
  justify-content: space-between;
  gap: 18px;

  padding: 16px 18px;
  margin-bottom: 12px;

  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);

  transition: 0.15s ease;
}

.folder-item:hover,
.work-file-item:hover{
  background: var(--panel2);
  border-color: rgba(88,166,255,0.40);
  transform: translateY(-2px);
}

/* Dim files section */
.file-item{
  opacity: 0.62;
}

/* Layout inside cards */
.left{
  display: flex;
  gap: 14px;
  align-items: center;
  min-width: 0;
}

.icon{
  width: 26px;
  text-align: center;
  opacity: 0.95;
}

.left span:nth-child(2){
  font-weight: 700;
  letter-spacing: -0.2px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 52vw;
}

.right{
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 4px;

  font-size: 13px;
  color: var(--muted);
}

/* Tags */
.tag{
  padding: 3px 10px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 850;
  color: rgba(0,0,0,0.85);
}

/* Keep your original tag colors */
.folder   { background: #80CBC4; }
.Git      { background: #FF1744; }
.PHP      { background: #FF6188; }
.HTML     { background: #FAD000; }
.CSS      { background: #A9DC76; }
.JS       { background: #FFD866; }
.Python   { background: #78DCE8; }
.SQL      { background: #AB9DF2; }
.JSON     { background: #FC9867; }
.Image    { background: #AE81FF; }
.Markdown { background: #FFCA80; }

/* Files wrapper hidden by default */
#files-wrapper{ display:none; }

/* Overlay link */
.overlay-link{
  position: absolute;
  inset: 0;
  z-index: 1;
}

/* Corner gif stays */
.corner-gif{
  position: absolute;
  top: 40px;
  right: 50px;
  pointer-events: none;
  opacity: 0.9;
  z-index: 9999;
  width: 180px;
}


/*
body {
    background: #2D2A2E;
    color: #FCFCFA;
    font-family: Helvetica, Arial, sans-serif;
    margin: 40px;
}

h1 {
    margin: 0;
    font-size: 32px;
    color: #FAD000;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 15px;
    color: #C1C0C0;
    opacity: .7;
    margin-bottom: 30px;
}

.breadcrumb {
    margin-bottom: 15px;
    color: #C1C0C0;
    font-size: 14px;
}
.breadcrumb a {
    color: #8FE8DB;
    text-decoration: none;
}


#search {
    background: #403E41;
    border: 1px solid #514F52;
    padding: 10px 14px;
    border-radius: 8px;
    color: #FCFCFA;
    margin-bottom: 24px;
    width: 260px;
    font-size: 14px;
}

.section {
    margin-top: 35px;
    margin-bottom: 12px;
    font-size: 14px;
    color: #C1C0C0;
    text-transform: uppercase;
    font-weight: bold;
    opacity: .7;
    display: flex;
    align-items: center;
    gap: 8px;
}

.chevron {
    width: 14px;
    display: inline-block;
    transition: .15s;
    transform: rotate(0deg);
}
.chevron.open {
    transform: rotate(90deg);
}

.item {
    display: flex;
    justify-content: space-between;
    padding: 16px 22px;
    background: #403E41;
    margin-bottom: 12px;
    border-radius: 8px;
    border: 1px solid #514F52;
    box-shadow: 0 2px 4px rgba(0,0,0,0.25);
    transition: 0.2s ease;
    position: relative;
}

.folder-item:hover {
    background: #4A484B;
    border-color: #FAD000;
    transform: translateY(-2px) scale(1.01);
}


.file-item {
    opacity: .6;
}


.work-file-item {
    opacity: 1;
}

.image-item {
    opacity: .6;
}


.work-file-item:hover {
    background: #4A484B;
    border-color: #FAD000;
    transform: translateY(-2px) scale(1.01);
}

.left { display: flex; gap: 16px; align-items: center; }
.icon { width: 24px; text-align: center; }

.tag {
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: bold;
    color: black;
}

.folder   { background: #80CBC4; }
.Git      { background: #FF1744; }
.PHP      { background: #FF6188; }
.HTML     { background: #FAD000; }
.CSS      { background: #A9DC76; }
.JS       { background: #FFD866; }
.Python   { background: #78DCE8; }
.SQL      { background: #AB9DF2; }
.JSON     { background: #FC9867; }
.Image    { background: #AE81FF; }

.files-wrap {
    display:none;
}


.overlay-link {
    position: absolute;
    inset: 0;
    z-index: 1;
}

.breadcrumb-box {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  top: 0px;

  display: flex;            
  align-items: center;
  justify-content: center;

  height: 40px;
  padding: 0 25px;

  background: #3B4B53;
  border-radius: 10px;
  border: 1px solid #495A61;
  box-shadow: 0 2px 5px rgba(0,0,0,0.35);
  backdrop-filter: blur(6px);
}

.breadcrumb {
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;  
  gap: 6px;            
  font-size: 17px;
  font-weight: 500;
  color: #E1E5E7;
  white-space: nowrap;
}

.corner-gif {
  position: absolute;
  top: 40px;
  right: 50px;
  pointer-events: none;
  opacity: 0.9;        
  z-index: 9999;
  width: 180px;

}

.breadcrumb-center {
  position: relative;
  z-index: 10;
}

.breadcrumb a:hover {
  color: #FAD000;     
  text-decoration: underline;
  text-underline-offset: 3px;
  text-decoration-thickness: 1px;
}

.total-box {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  top: 155px;

  display: flex;
  align-items: center;
  justify-content: center;

  height: 40px;
  padding: 0 25px;

  background: #3B4B53;
  border-radius: 10px;
  border: 1px solid #495A61;
  box-shadow: 0 2px 5px rgba(0,0,0,0.35);
  backdrop-filter: blur(6px);

  font-size: 17px;
  font-weight: 500;
  color: #80CBC4;
}

.Markdown { background: #FFCA80; }
*/



</style>
</head>
<body>


<img class="corner-gif" src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2ZvcTN3eG5zMnp5N2NycHBqZXNoeWN3djFoMGI3eGNycmgwcjV2ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/66M6ZwJkTLYikvhrqZ/giphy.gif"> 

<!--<img class="corner-gif" src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOG9kM3U1Y2oxaGg3dGowenEzbWJ6czR6ZjBzMDV3NnZ2azhhdXpudyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13HgwGsXF0aiGY/giphy.gif"> -->
<!--<img class="corner-gif" src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2xpZDlkYjI4Y2tzdXA2M3o4OHg1dm5rbWNhaXhsN2diajZrdG5odCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GghGKaZ8JeHJx0apQC/giphy.gif"> -->




<h1 class="title">Localhost</h1>
<div class="breadcrumb-center">
  <div class="breadcrumb-box">
    <div class="breadcrumb">
      <a href="/">Home</a>
      <?php
      $acc = '';
      foreach ($parts as $p) {
        if (!$p || $p === 'index.php') continue;
        $acc .= "/$p";
        echo ' › <a href="'.$acc.'/">'.$p.'</a>';
      }
      ?>
    </div>
  </div>
</div>

<div class="total-box">
    Total Size: <?= $totalSize ?>
</div>



<div class="subtitle">Synced via GitHub</div>

<input id="search" placeholder="Search…" autocomplete="off">


<!-- Folders -->

<h2 class="section">Folders</h2>

<?php foreach ($folders as $item):
    $path = $item;
    $modified = date("d/m/Y H:i", filemtime($path));
?>

<?php if (is_dir($path)): ?>
    <!-- MAPPE -->
    <div class="item folder-item">
        <a class="overlay-link" href="<?php echo $item; ?>"></a>
        <div class="left">
            <span class="icon">📁</span>
            <span><?php echo $item; ?></span>
            <span class="tag folder"><?php echo dir_count($path) ?> files</span>
        </div>
        <div class="right">
    <div><?php echo pretty_size(dir_size($path)); ?></div>
    <div><?php echo $modified; ?></div>
</div>

    </div>

<?php else: ?>
    <!-- ARBEJDSFIL -->
    <?php $lang = file_language($path); ?>
    <div class="item work-file-item <?php echo ($lang === 'Image') ? 'image-item' : ''; ?>">
        <a class="overlay-link" href="<?php echo $item; ?>"></a>
        <div class="left">
            <span class="icon">📄</span>
            <span><?php echo $item; ?></span>
            <?php if ($lang): ?>
                <span class="tag <?php echo $lang; ?>"><?php echo $lang; ?></span>
            <?php endif; ?>
        </div>
        <div class="right">
            <div><?php echo pretty_size(filesize($path)); ?></div>
            <div><?php echo $modified; ?></div>
        </div>
    </div>
<?php endif; ?>

<?php endforeach; ?>

<!-- Files -->
<h2 class="section" id="files-toggle" style="cursor:pointer;">
    <span class="chevron">▶</span> Files
</h2>

<div class="files-wrap" id="files-wrapper">
<?php foreach ($files as $item):
    $path = $item;
    $size = pretty_size(filesize($path));
    $modified = date("d/m/Y H:i", filemtime($path));
    $lang = file_language($path);
?>
<div class="item file-item">
    <a class="overlay-link" href="<?php echo $item; ?>"></a>
    <div class="left">
        <span class="icon">📄</span>
        <span><?php echo $item; ?></span>

        <?php if ($item === '.git'): ?>
            <span class="tag Git">Git repo</span>
        <?php elseif ($lang): ?>
            <span class="tag <?php echo $lang; ?>"><?php echo $lang; ?></span>
        <?php endif; ?>
    </div>
    <div class="right">
        <div><?php echo $size; ?></div>
        <div><?php echo $modified; ?></div>
    </div>
</div>
<?php endforeach; ?>
</div>

<script>
document.getElementById("search").addEventListener("input", e => {
    const term = e.target.value.toLowerCase();
    document.querySelectorAll(".item").forEach(el => {
        const nameEl = el.querySelector(".left span:nth-child(2)");
        if (!nameEl) return;
        const name = nameEl.textContent.toLowerCase();
        el.style.display = name.includes(term) ? "" : "none";
    });
});

const toggleBtn = document.getElementById("files-toggle");
const wrap = document.getElementById("files-wrapper");
const chev = toggleBtn.querySelector(".chevron");

toggleBtn.addEventListener("click", () => {
    const visible = wrap.style.display === "block";
    if (visible) {
        wrap.style.display = "none";
        chev.classList.remove("open");
    } else {
        wrap.style.display = "block";
        chev.classList.add("open");
    }
});
</script>



</body>
</html>
