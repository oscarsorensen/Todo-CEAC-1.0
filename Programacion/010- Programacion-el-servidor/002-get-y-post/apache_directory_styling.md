# Improving Apache Directory Listings on macOS  
### (How to style your localhost folders like your teacher)

## 1. What you want  
You already have Apache directory listing enabled on your Mac.  
That means when you visit a folder on localhost with no `index.php` or `index.html`, Apache shows a simple list of files like this:

```
Index of /some-folder/
• file1.php
• file2.php
• folder/
```

You want to improve the **design** of this listing:

- nicer layout  
- optional dark theme  
- cleaner typography  
- no bullets  
- maybe icons  
- same kind of look your teacher has  

Good news:  
**Apache supports this through mod_autoindex + custom CSS.**

---

## 2. Check that directory listing is enabled  
Find and open your Apache config (Homebrew version):

```
sudo nano /opt/homebrew/etc/httpd/httpd.conf
```

Look for:

```
Options Indexes FollowSymLinks
```

If “Indexes” is present, directory listing works.

---

## 3. Enable Fancy Indexing  
In the same `httpd.conf`, find the section:

```
<IfModule mod_autoindex.c>
```

Inside this block, add:

```
IndexOptions FancyIndexing HTMLTable VersionSort NameWidth=40 SuppressDescription
IndexStyleSheet "/style-index.css"
```

This activates:

- Fancy styling  
- Table layout  
- Sorted names  
- Your own CSS file  

---

## 4. Create your custom stylesheet  
Create this file in your Apache document root:

```
/opt/homebrew/var/www/style-index.css
```

Example dark theme:

```css
body {
    background: #121212;
    color: #e0e0e0;
    font-family: "Fira Code", monospace;
    padding: 30px;
}

h1 {
    font-size: 24px;
    color: #ffffff;
    margin-bottom: 20px;
}

ul {
    list-style: none;
    padding-left: 0;
}

li {
    margin: 6px 0;
}

a {
    color: #6aa6ff;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
```

You can modify the CSS at any time without restarting Apache.

---

## 5. Restart Apache  
Apply changes:

```
brew services restart httpd
```

Or if running manually:

```
apachectl restart
```

---

## 6. Done  
Now every directory without an index file will automatically use:

- Fancy directory listing  
- Your custom CSS theme  
- Clean layout  
- Improved readability  

This setup is almost identical to the one your teacher uses.
