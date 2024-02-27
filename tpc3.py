import os
import re

class Sum:
    keyword = re.compile(r'([Oo][Nn])|([Oo][Ff][Ff])|([=])|(\d)')

def main():
    path = input("Escolha o ficheiro (na mesma diretoria):\n")
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, path)
    try:
        with open(filename,'r') as files:
            Count = False
            Res = 0
            for line in files:
                spot = re.findall(Sum.keyword,line)
                for match in spot:
                    if(match[0]!=''):
                        Count = True
                    elif(match[1]!=''):
                        Count = False
                    elif(match[2]!=''):
                        print(Res)
                    elif(Count):
                        Res += 1
                   
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    main()