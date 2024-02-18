import re
import os

class Parser:
    md = {
        "h1" : re.compile(r'^(?<!#)#(?!#) (.+)'),
        "h2" : re.compile(r'^(?<!\s#)##(?!#) (.+)'),
        "h3" : re.compile(r'^(?<!#)###(?!#) (.+)'),
        "b" : re.compile(r'(?<!\*)[*][*](?![*\s])([^*]*[^*\s])?[*][*](?!\*)'),
        "it" : re.compile(r'(?<!\*)\*(?![*\s])([^*]*[^*\s])?\*(?!\*)'),
        "bq" : re.compile(r'(?<!.)>\s([^ ]+)$'),
        "ol" : re.compile(r'(?:\d+[.] (.+))'),
        "ul" : re.compile(r'(?:- (.+)\n)'),
        "code" : re.compile(r'`([^`]*)`'),
        "brk" : re.compile(r'^---(?=(?:\n|$))'), #contabilizar bsp's antes?
        "link" : re.compile(r'[[](.+)[]][(]((https?://)?www[.][a-z0-9]+([.].+)+)[)]'),
        "image" : re.compile(r'[!][[](.*)[]][(](.+[.].+)[)]')
    }

    def md2html(string, types, ltypes):
        text=string
        text = re.sub(Parser.md["h1"],r"<h1>\1</h1>",text)
        text = re.sub(Parser.md["h2"],r"<h2>\1</h2>",text)
        text = re.sub(Parser.md["h3"],r"<h3>\1</h3>",text)
        text = re.sub(Parser.md["b"],r"<b>\1</b>",text)
        text = re.sub(Parser.md["it"],r"<it>\1</it>",text)
        text = re.sub(Parser.md["bq"],r"<blockquote>\1</blockquote>",text)
        text = re.sub(Parser.md["code"],r"<code>\1</code>",text)
        text = re.sub(Parser.md["brk"],r"<br>",text)
        text = re.sub(Parser.md["link"],r'<a href="\2">\1</a>',text)
        text = re.sub(Parser.md["image"],r'<img src="\2" alt="\1"/>',text)

        rol=re.match(Parser.md["ol"], text)
        rul=re.match(Parser.md["ul"], text)
        if rol:
            if types!="ol":
                if ltypes=="ul":
                    text = '</ul>\n<ol>\n' + text
                
                text = '<ol>\n' + text

                ltypes=types
                types='ol'

        elif rul:

            if types!="ul":

                if ltypes=="ol":
                    text = '</ol>\n<ul>\n' + text
                else:
                    text = '<ul>\n' + text
                ltypes=types
                types='ul'

        else:
            if ltypes=="ol":
                text = '\n</ol>\n' + text

            elif ltypes=="ul":
                text = '\n</ul>\n' + text

            ltypes=types
            types=None
            
        text = re.sub(Parser.md["ol"],r"<li>\1</li>",text)
        text = re.sub(Parser.md["ul"],r"<li>\1</li>",text)

        return text, types, ltypes

def main():
    path = input("Escolha o ficheiro (markdown) na mesma diretoria:\n")
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, path)

    try:
        with open(filename,'r') as files, open("html_"+path, 'w') as out:
            ltypes=None
            types=None
            for line in files:
                outline, types, ltypes = Parser.md2html(line, types, ltypes)
                if outline:
                    out.write(outline)
            
    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    main()