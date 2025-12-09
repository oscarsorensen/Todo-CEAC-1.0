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
        "jpg", "jpeg", "png", "gif", "webp" => "Image",
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

function make_tree($h) {
    $tree = [];
    for ($i = 1; $i <= $h; $i++) {
        $stars  = str_repeat("*", $i*2 - 1);
        $spaces = str_repeat(" ", $h - $i);
        $tree[] = $spaces . "/" . $stars . "\\";
    }
    $tree[] = str_repeat(" ", $h-1) . "||";
    return implode("\n", $tree);
}

$tree_heights = [4,5,10,7,4];
$forest = [];
foreach ($tree_heights as $h) $forest[] = make_tree($h);
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
    color: #80CBC4;
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



/* Forest */
.forest {
    position: absolute;
    top: 50px;
    left: 800px;
    display: flex;
    gap: 35px;
    align-items: flex-end;
    font-family: monospace;
    white-space: pre;
    pointer-events: none;
    opacity: .90;
    font-size: 14px;
    line-height: 1.1;
}


</style>
</head>
<body>

<div class="forest">
<?php foreach ($forest as $tree): ?>
<pre><?php echo $tree; ?></pre>
<?php endforeach; ?>
</div>

<h1>Localhost</h1>
<div class="subtitle">Synced via GitHub</div>

<div class="breadcrumb">
    <a href="/">Home</a>
    <?php
    $acc = '';
    foreach ($parts as $p) {
        if (!$p || $p === 'index.php') continue;
        $acc .= "/$p";
        echo ' › <a href="'.$acc.'/">'.htmlspecialchars($p).'</a>';
    }
    ?>
</div>

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
            <div>-</div>
            <div><?php echo $modified; ?></div>
        </div>
    </div>

<?php else: ?>
    <!-- ARBEJDSFIL -->
    <?php $lang = file_language($path); ?>
    <div class="item work-file-item">
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
