import os


def gen_HTML_plot(header, IMG_PATH, subtxt = "", report_txt = ""):
    html_string = '''
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="utf-8">
    <title>Flask Tutorial</title>
</head>
<body>
    <h1> ''' + header + ''' </h1>
    <p> ''' + subtxt + ''' </p>
    <img src="'''+IMG_PATH+'''" alt="plot text" width ="20%" height="auto">
    <h2> Report summary </h2>
    <p> ''' + report_txt + ''' </p>
</body>
</html>
'''
    
    HTML_file = open(os.path.join('templates','report.html'),'w')
    HTML_file.write(html_string)
    HTML_file.close()
    
    print('HTML report generated')