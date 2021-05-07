from tkinter import *
# Variabler
transactions = []                   # En lista som loggar transaktioner
filename = "transaktioner.txt"      # Namnet på filen som transaktionerna lagras i

# Beräknar saldo på ditt konto
def saldo():
    saldo = 500 
    for t in transactions:
        saldo += t
    print(f"Ditt saldo är: {saldo} kr")

# Insättning
def insättning():
    print("<=>   Insättning   <=>")
    insättning = int(input("<=>  Ange Belopp:  <=>\n"))
    if insättning > 0:
            add_transaction(insättning, True)

# Skriver ned alla transaktioner
def print_transactions():   
    line = 0
    summa = 0
    output = ("\n<=>   Transaktioner   <=>"
              "\n{:>3} {:>12} {:>12}"
              "\n≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖≖").format("Nr", "Händelse", "Saldo")
    for t in transactions:
        line += 1
        summa += t
        output += ("\n{:>2}. {:>9} kr {:>9} kr".format(line, t, summa))
    
    print(output)

# Ta ut pengar
def uttag():
    print("<=>     Uttag     <=>")
    uttag = int(input("<=>  Ange Belopp:  <=>\n"))
    if uttag <= 500:
        add_transaction(-uttag, True)

# Avsluta programmet & töm transaktioner filen.
def quita():
    window.quit()
    open(filename, 'w').close()

# Den kollar så att filen är tillgänglig. Är den inte det skapas en ny
def check_file_exists():
    try:
        with open(filename, "x"):
            print("Filen har skapats")

        with open(filename, "a") as f:
            f.write("{}\n".format(500))
    except:
        return

# Den läser upp filens innerhåll
def read_file():
    check_file_exists()

    with open(filename) as f:
        for rad in f:
            if len(rad) > 0:
                add_transaction(int(rad))
            
# Lagrar transaktioner till en lista
def add_transaction(transaction, toFile = False):
    transactions.append(transaction)
    if toFile:
        write_transaction_to_file(transaction)

# Skriver transaktionen till filen
def write_transaction_to_file(transaction):
    with open(filename, "a") as f:
        f.write("{}\n".format(transaction))

read_file()

# Skapar ett fönster med titel och bakgrund

window = Tk()
window.title("Bank UI")
window.configure(bg="seashell2")

# Rubriken 

lbl1 = Label(window, text="▶ B͏a͏n͏k͏ o͏f͏ J͏a͏p͏a͏n͏ ◀", bg="seashell2", fg="sandy brown", font="Helvetica 18 bold")
lbl1.pack()

# Knapp för att visa saldo

saldobtn = Button(window, text="Saldo", bg="white", width=15, command=saldo)
saldobtn.pack()

# Knapp för att visa transaktioner

transaktioner = Button(window, text="Transaktioner", bg="white", width=15, command=print_transactions)
transaktioner.pack()

# Knapp för insättning

insättningbtn = Button(window, text="Insättning", bg="white", width=15, command=insättning)
insättningbtn.pack()

# Knapp för uttag

uttagbtn = Button(window, text="Uttag", bg="white", width=15, command=uttag)
uttagbtn.pack()

# Knapp för att avsluta programmet

stopbtn = Button(window, text="Avsluta Programmet", bg="white", width=15, command=quita)
stopbtn.pack()

# Fönstrets mainloop
window.mainloop()