
<?php
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
    if (!is_dir($dir)) return 0;
    if (basename($dir) === '.git') return 0;
    $count = 0;
    $items = array_diff(scandir($dir), ["..", "."]);
    foreach ($items as $item) {
        $path = $dir . "/" . $item;
        $count += is_dir($path) ? dir_count($path) : 1;
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

function total_project_size($folders) {
    $total = 0;
    foreach ($folders as $dir) {
        if (is_dir($dir)) {
            $total += dir_size($dir);
        }
    }
    return $total;
}



// --- Only these belong to Files (whitelist) ---
$special_files = [
    ".DS_Store",
    "browser.php",
    "index.php",
    "ting.md",
    ".git",
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

$path  = trim($_SERVER['REQUEST_URI'], '/');
$parts = $path ? explode('/', $path) : [];
?>



<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">

<title>Localhost · Project Browser</title>

<style>

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

/* core item layout */
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

/* SKRAMMEL-GRUPPEN: Files-sektion */
.file-item {
    opacity: .6;
}

/* ARBEJDSFILER: fuld opacity */
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

  display: flex;             /* center tekst */
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
  line-height: 0;        /* nul effekt */
  display: flex;
  align-items: center;   /* center inde i center */
  gap: 6px;              /* lille luft mellem elementer */
  font-size: 17px;
  font-weight: 500;
  color: #E1E5E7;
  white-space: nowrap;
}

.corner-gif {
  position: absolute;
  top: 40px;
  right: 50px;
  width: 120px;
  pointer-events: none; /* så den ikke blokerer klik */
  opacity: 0.9;         /* lidt diskret */
  z-index: 9999;
  width: 280px;

}

.breadcrumb-center {
  position: relative;
  z-index: 10;
}

.breadcrumb a:hover {
  color: #FAD000;          /* gul highlight */
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





</style>
</head>
<body>

<!--<img class="corner-gif" src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2Ewa3Y2eDk1NHVnYWttaHE1MzI3MGJvYTNiZmoyaXdkeGM4OXptZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MGaacoiAlAti0/giphy.gif">-->


<img class="corner-gif" src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOG9kM3U1Y2oxaGg3dGowenEzbWJ6czR6ZjBzMDV3NnZ2azhhdXpudyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13HgwGsXF0aiGY/giphy.gif"> 

<!--<img class="corner-gif" src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2xpZDlkYjI4Y2tzdXA2M3o4OHg1dm5rbWNhaXhsN2diajZrdG5odCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GghGKaZ8JeHJx0apQC/giphy.gif"> -->


<?php $totalSize = pretty_size(total_project_size($folders)); ?>


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
    Total Size: <?php echo $totalSize; ?>
</div>


<div class="subtitle">Synced via GitHub</div>

<input id="search" placeholder="Search…" autocomplete="off">


<!-- Folders -->

<h2 class="section">Folders</h2>

<?php foreach ($folders as $item):
    $path = $item;
    $modified = date("Y-m-d H:i", filemtime($path));
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
    $modified = date("Y-m-d H:i", filemtime($path));
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
