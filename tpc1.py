def parser(path):
    ua = set()
    trues = 0.0
    falses = 0.0
    nlines = 0
    ages = {f"{i}-{i+4}": 0 for i in range(0, 100, 5)}

    with open(path, 'r') as file:
        next(file)

        for line in file:
            nlines +=1
            row = line.strip().split(',')

            if row[-1] == "true":
                trues += 1
            else:
                falses += 1

            sport = row[8].strip()
            ua.add(sport)

            try:
                age = int(row[5].strip())
                if age < 100:
                    escalao = "{}-{}".format(age // 5 * 5, age // 5 * 5 + 4)
                    ages[escalao] += 1
            except ValueError:
                pass
        
        trues = (trues/nlines)*100
        falses = (falses/nlines)*100

    return sorted(ua), ages, trues, falses

def main():
    file = input("Introduza o caminho para o csv:\n")
    ua, ages, trues, falses = parser(file)
    inp = 0
    while(inp!= 4):
        print("\nSelecione a opção pretendida:\n")
        print("1 - Lista de atividades\n")
        print("2 - Percentagem de aptos e inaptos\n")
        print("3 - Distribuição de idades\n")
        print("4 - Sair\n")
        inp = int(input())
        if inp == 1:
            print(ua)
        elif inp == 2:
            print("Percentagem de aptos: ", trues)
            print("Percentagem de inaptos: ", falses)
        elif inp == 3:
            for age in ages:
                print(age, ":", ages[age])

if __name__ == "__main__":
    main()