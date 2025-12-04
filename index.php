<?php
$items = array_diff(scandir("."), ["..", "."]);

// mapper først, alfabetisk, .git nederst
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

    // stop recursion on .git folder
    if (basename($dir) === '.git') return 0;

    $count = 0;
    $items = array_diff(scandir($dir), ["..", "."]);

    foreach ($items as $item) {
        $path = $dir . "/" . $item;

        if (is_dir($path)) {
            $count += dir_count($path);  // tæller undermapper rekursivt
        } else {
            $count++;
        }
    }

    return $count;
}

// split i folders/files
$folders = [];
$files   = [];
foreach ($items as $item) {
    if (is_dir($item)) $folders[] = $item;
    else $files[] = $item;
}

// breadcrumb
$path  = trim($_SERVER['REQUEST_URI'], '/');
$parts = $path ? explode('/', $path) : [];
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>PHP Project Browser</title>

<style>
    body {
        background: #2D2A2E;
        color: #FCFCFA;
        font-family: Helvetica, Arial, sans-serif;
        margin: 40px;
        transition: .15s;
    }

    h1 {
        margin-bottom: 25px;
        color: #FAD000;
        letter-spacing: 1px;
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
        padding: 8px 12px;
        border-radius: 6px;
        color: #FCFCFA;
        margin-bottom: 20px;
        width: 240px;
    }
    #search:focus {
        outline: none;
        border-color: #FAD000;
    }

    .section {
        margin-top: 30px;
        margin-bottom: 10px;
        font-size: 15px;
        color: #C1C0C0;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-weight: bold;
        opacity: .7;
    }

    .item {
        display: flex;
        justify-content: space-between;
        padding: 12px 18px;
        background: #403E41;
        margin-bottom: 10px;
        border-radius: 6px;
        transition: 0.15s;
        border: 1px solid #514F52;
        box-shadow: 0 2px 4px rgba(0,0,0,0.25);
        opacity: 0;
        transform: translateY(6px);
        animation: fadeIn 1s ease forwards;
    }

    /* lille stagger så man kan se det, men ikke langsomt */
    .item:nth-child(1) { animation-delay: .05s; }
    .item:nth-child(2) { animation-delay: .10s; }
    .item:nth-child(3) { animation-delay: .15s; }
    .item:nth-child(4) { animation-delay: .20s; }
    .item:nth-child(5) { animation-delay: .25s; }

    @keyframes fadeIn {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* slide-out når man klikker */
    body.slideOut .item {
        opacity: 0;
        transform: translateX(-10px);
        transition: .15s ease;
    }

    .item:hover {
        background: #4A484B;
        border-color: #FAD000;
    }

    .left { display: flex; gap: 12px; align-items: center; }

    .icon { width: 22px; text-align: center; }

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

<h1>PHP Project Browser</h1>

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

<h2 class="section">Folders</h2>

<?php foreach ($folders as $item): ?>
    <?php
        $path = $item;
        $modified = date("Y-m-d H:i", filemtime($path));
        $count = dir_count($path);

        $is_irrelevant = (
            $item === ".DS_Store" ||
            $item === "index.php" ||
            $item === ".git"
        );
    ?>

    <div class="item <?php echo $is_irrelevant ? "faded" : "" ?>">
        <div class="left">
            <span class="icon">📁</span>
            <a href="<?php echo $item; ?>"
               title="Modified: <?php echo $modified ?>&#10;Files: <?php echo $count ?>">
               <?php echo $item; ?>
            </a>

            <?php if ($item === '.git'): ?>
                <span class="tag Git">Git repo</span>
            <?php else: ?>
                <span class="tag folder"><?php echo $count ?> files</span>
            <?php endif; ?>
        </div>

        <div class="right">
            <div>-</div>
            <div><?php echo $modified; ?></div>
        </div>
    </div>
<?php endforeach; ?>


<h2 class="section">Files</h2>

<?php foreach ($files as $item): ?>
    <?php
        $path = $item;
        $is_dir = false;
        $icon = "📄";
        $size = pretty_size(filesize($path));
        $modified = date("Y-m-d H:i", filemtime($path));
        $lang = file_language($path);

        $is_irrelevant = (
            $item === ".DS_Store" ||
            $item === "index.php" ||
            $item === ".git"
        );
    ?>

    <div class="item <?php echo $is_irrelevant ? "faded" : "" ?>">
        <div class="left">
            <span class="icon"><?php echo $icon; ?></span>
            <a href="<?php echo $item; ?>"
               title="Modified: <?php echo $modified ?>&#10;Size: <?php echo $size ?><?php if($lang) echo '&#10;Type: ' . $lang; ?>">
               <?php echo $item; ?>
            </a>

            <?php if ($lang): ?>
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
// slide-out ved klik
document.querySelectorAll(".item a").forEach(a => {
    a.addEventListener("click", () => {
        document.body.classList.add("slideOut");
    });
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
