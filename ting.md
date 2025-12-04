<?php
$items = array_diff(scandir("."), ["..", "."]);

// sort: folders first, alpha, .git forced to files and bottom
usort($items, function($a, $b) {
    if ($a === '.git') return 1;
    if ($b === '.git') return -1;
    return (is_dir($b) <=> is_dir($a)) ?: strcasecmp($a, $b);
});

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

// split into folders/files (but .git forced into files)
$folders = [];
$files   = [];
foreach ($items as $item) {
    if ($item === '.git') {
        $files[] = $item;
        continue;
    }
    if (is_dir($item)) $folders[] = $item;
    else $files[] = $item;
}

// breadcrumb path
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
        opacity: 0;
        transition: opacity 1s ease;
    }
    body.loaded { opacity: 1; }

    h1 {
        margin: 0;
        font-size: 32px;
        color: #FAD000;
        letter-spacing: 1px;
        font-weight: bold;
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
    .breadcrumb a:hover { color: #A8FFFF; }

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
    #search:focus {
        outline: none;
        border-color: #FAD000;
    }

    .section {
        margin-top: 35px;
        margin-bottom: 12px;
        font-size: 14px;
        color: #C1C0C0;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-weight: bold;
        opacity: .7;
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
    }

    /* folders bounce */
    .folder-item:hover {
        background: #4A484B;
        border-color: #FAD000;
        transform: translateY(-2px) scale(1.01);
    }

    /* files faded always (also on hover) */
    .file-item {
        opacity: .6;
    }
    .file-item:hover {
        opacity: .6;
        background: #4A484B;
        border-color: #514F52;
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

    .faded {
        opacity: 0.35;
        font-style: italic;
        transition: opacity 2s ease;
    }

    a {
        color: #80CBC4;
        text-decoration: none;
        font-weight: normal;
    }
    a:hover { color: #A8FFFF; }

    .right {
        color: #C1C0C0;
        font-size: 13px;
        text-align: right;
    }
</style>
</head>
<body>

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
    $count = dir_count($path);

    // irrelevant in folders: index & .DS_Store
    $is_irrelevant = ($item === ".DS_Store" || $item === "index.php");
?>
<div class="item folder-item <?php echo $is_irrelevant ? "faded" : "" ?>">
    <div class="left">
        <span class="icon">📁</span>
        <a href="<?php echo $item; ?>"
           title="Modified: <?php echo $modified ?>&#10;Files: <?php echo $count ?>">
           <?php echo $item; ?>
        </a>
        <span class="tag folder"><?php echo $count ?> files</span>
    </div>
    <div class="right">
        <div>-</div>
        <div><?php echo $modified; ?></div>
    </div>
</div>
<?php endforeach; ?>

<!-- Files -->
<h2 class="section">Files</h2>
<?php foreach ($files as $item):
    $path = $item;
    $size = pretty_size(filesize($path));
    $modified = date("Y-m-d H:i", filemtime($path));
    $lang = file_language($path);
?>
<div class="item file-item">
    <div class="left">
        <span class="icon">📄</span>
        <a href="<?php echo $item; ?>"
           title="Modified: <?php echo $modified ?>&#10;Size: <?php echo $size ?><?php if($lang) echo '&#10;Type: ' . $lang; ?>">
           <?php echo $item; ?>
        </a>

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


<script>
// fade-in page load
window.addEventListener("load", () => {
    document.body.classList.add("loaded");
});

// live search
document.getElementById("search").addEventListener("input", e => {
    const term = e.target.value.toLowerCase();
    document.querySelectorAll(".item").forEach(el => {
        const name = el.querySelector("a").textContent.toLowerCase();
        el.style.display = name.includes(term) ? "" : "none";
    });
});
</script>

</body>
</html>
