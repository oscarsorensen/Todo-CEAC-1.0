<?php
$items = array_diff(scandir("."), ["..", "."]);

usort($items, function($a, $b) {
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

?>

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Localhost Lenguajes de Marcas</title>

<style>
    body {
        background: #2D2A2E;
        color: #FCFCFA;
        font-family: Helvetica, Arial, sans-serif;
        margin: 40px;
    }

    h1 {
        margin-bottom: 25px;
        color: #FAD000;
        letter-spacing: 1px;
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
    }

    .item:hover {
        background: #4A484B;
        border-color: #FAD000;
    }

    .left { display: flex; gap: 12px; align-items: center; }

    .icon { width: 22px; text-align: center; }

    /* TAG DESIGN */
    .tag {
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: bold;
        color: black;
    }

    .folder   { background: #80CBC4; }
    .PHP      { background: #FF6188; }
    .HTML     { background: #FAD000; }
    .CSS      { background: #A9DC76; }
    .JS       { background: #FFD866; }
    .Python   { background: #78DCE8; }
    .SQL      { background: #AB9DF2; }
    .JSON     { background: #FC9867; }
    .Image    { background: #AE81FF; }

    /* Irrelevant files */
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

<h1>Lenguajes de Marcas</h1>

<?php foreach ($items as $item): ?>
    <?php
        $path = $item;
        $is_dir = is_dir($path);
        $icon = $is_dir ? "📁" : "📄";
        $size = $is_dir ? "-" : pretty_size(filesize($path));
        $modified = date("Y-m-d H:i", filemtime($path));
        $lang = $is_dir ? "" : file_language($path);
        $count = $is_dir ? dir_count($path) : null;

        $is_irrelevant = ($item === ".DS_Store" || $item === "index.php");
    ?>

    <div class="item <?php echo $is_irrelevant ? "faded" : "" ?>">
        <div class="left">
            <span class="icon"><?php echo $icon; ?></span>
            <a href="<?php echo $item; ?>"><?php echo $item; ?></a>

            <?php if ($lang): ?>
                <span class="tag <?php echo $lang; ?>"><?php echo $lang; ?></span>
            <?php endif; ?>

            <?php if ($is_dir): ?>
                <span class="tag folder"><?php echo $count ?> files</span>
            <?php endif; ?>
        </div>

        <div class="right">
            <div><?php echo $size; ?></div>
            <div><?php echo $modified; ?></div>
        </div>
    </div>

<?php endforeach; ?>

</body>
</html>
