import os

# Template for generating the report in the web browser
def gen_HTML_plot(header, IMG_PATH, subtxt = "", report_txt = ""):
    html_string = '''
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <link rel="stylesheet" href="static/style.css">
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



def gen_HTML_report(header, IMG_PATH, sub_header = "" , subtxt = "", report_txt = ""):
    html_string = '''
<!DOCTYPE html>
<html lang="no" dir="ltr">
<head>
    <meta charset="utf-8">
    <title>Flask Tutorial</title>
</head>
<body style="
    align-items: center;
    font-family: sans-serif;
    text-align: -webkit-center;
    background-color: white;
    ">
    <h1 style="
        font-size: 50px;
    "> ''' + header + ''' </h1>
    <p style="
        font-size: xx-large;
        font-family: sans-serif;
    ">''' + subtxt + '''</p>
    <img src="'''+IMG_PATH+'''" alt="plot text" width="20%" height="auto" style="width: fit-content;height: auto;">
    <h2 style="
        font-size: xx-large;
    "> ''' + sub_header + ''' </h2>
    <p style="
        font-size: x-large;
    ">''' + report_txt + '''</p>
    
    <object id="__symantecPKIClientMessenger" data-supports-flavor-configuration="true" data-extension-version="0.5.0.109" style="display: none;"></object>
    <span id="__symantecPKIClientDetector" style="display: none;">__PRESENT</span>
</body>
</html>
    '''
    HTML_file = open(os.path.join('templates','report.html'),'w',encoding='utf8')
    HTML_file.write(html_string)
    HTML_file.close()
    
    print('HTML report generated new')
