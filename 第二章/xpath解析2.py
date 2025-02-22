from lxml import html

xml = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Website</title>
</head>
<body>
    <h1>Welcome to Sample Website</h1>
    <p>This is a sample webpage used for XPath practice.</p>
    
    <h2>Useful Links:</h2>
    <ul>
        <li><a href="http://www.example.com">Example</a></li>
        <li><a href="http://www.google.com">Google</a></li>
        <li><a href="http://www.bing.com">Bing</a></li>
    </ul>

    <h2>Important Articles:</h2>
    <ol>
        <li><a href="http://www.article1.com">Article 1</a></li>
        <li><a href="http://www.article2.com">Article 2</a></li>
        <li><a href="http://www.article3.com">Article 3</a></li>
    </ol>

    <h2>Contact Information:</h2>
    <p>If you have any questions, you can reach us at <a href="mailto:info@sample.com">info@sample.com</a></p>

    <div class="info">
        <h3>About Us</h3>
        <p>We are a sample company providing sample services.</p>
    </div>
    
    <div class="footer">
        <p>&copy; 2025 Sample Website</p>
    </div>
</body>
</html>
"""

# Use lxml.html for parsing HTML
tree = html.fromstring(xml)
result = tree.xpath('/html/body/ul/li/a/text()ieie')  # Corrected XPath
print(result)
