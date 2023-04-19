import matplotlib.pyplot as plt
import csv


def main():
    mesi_n = []
    ore_studio = []
    voti = []
    data_file = open("./voti_studio.csv")
    data_reader = csv.reader(data_file, delimiter=',')
    next(data_reader)
    for row in data_reader:
        mesi_n.append(int(row[1]))
        ore_studio.append(float(row[2]))
        voti.append(float(row[3]))
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle('Media dei voti di tutte le materie e ore di studio giornaliere medie nel periodo Gennaio-Giugno')

    ax1.plot(mesi_n, voti, 'o-g')
    ax1.set_xlabel('Mese')
    ax1.set_ylabel('Voto medio di tutte le materie')

    ax2.plot(mesi_n, ore_studio, 'o-r')
    ax2.set_xlabel('Mese')
    ax2.set_ylabel('Ore di studio medie al giorno (h)')

    plt.show()


if __name__ == "__main__":
    main()
