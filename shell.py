import pronotepy
from datetime import date, time, datetime, timedelta
import locale

client = pronotepy.Client(
    "https://0383069e.index-education.net/pronote/eleve.html?login=true",
    username="username",
    password="password",
)

locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")


# Obtenir l'année actuelle
def convertir_date(date_str):
    # Convertir la chaîne de caractères en objet datetime
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    # Convertir l'objet datetime en chaîne formatée
    formatted_date = date_obj.strftime("%A %d %Y")

    return formatted_date.capitalize()


# Obtenir la date du jour sous forme de chaîne de caractères
date_du_jours_str = datetime.today().strftime("%Y-%m-%d")
date_du_jours = datetime.strptime(date_du_jours_str, "%Y-%m-%d").date()

# Obtenir l'année actuelle
annee_actuelle = datetime.today().year

# Définir les dates de vacances
date_debut = date(year=annee_actuelle, month=6, day=10)
date_fin = date(year=annee_actuelle, month=9, day=1)
vacances = [date_debut, date_fin]


if client.logged_in:
    # Récupérer les données JSON de l'étudiant
    # Obtenir toutes les périodes
    if date_debut <= date_du_jours <= date_fin:
        print("")
        print("Vacances")
        print("")
    else:

        def Devoir():
            print("\n")
            today = (
                datetime.today().date()
            )  # store today's date using datetime built-in library
            homework = client.homework(
                today
            )  # get list of homework for today and later
            print(
                "_______ Voici les devoirs, penses à les faire :) ___________________________________"
            )
            for hw in homework:  # iterate through the list
                print(
                    f"({hw.subject.name}): {hw.description} pour le {convertir_date(str(hw.date))}"
                )  # print the homework's subject, title, and description
            print(
                "___________________________________________________________________________________"
            )
            print("\n")

        def Notes():
            listeNote = []
            today = datetime.today().date()
            ten_days_ago = today - timedelta(days=5)
            # listeNoteRenverse = []
            # print only the grades from the current period
            # print all the grades the user had in this school year
            periods = client.periods
            print("_______ Voici les dernières notes  _______")
            for period in periods:
                for grade in period.grades:
                    if ten_days_ago <= grade.date <= today:
                        listeNote.append(
                            [grade.subject.name, f"{grade.grade}/{grade.out_of}"]
                        )
            # listeNoteRenverse = listeNote[::-1]
            if len(listeNote) == 0:
                print("\n", "Il y a pas de note pour le moment")
            else:
                for i in range(5):
                    print("\n", listeNote[i])
            print("__________________________________________")

        Devoir()
        Notes()


else:
    print("Erreur lors de la conextion")

## Pensé a choque pour prinf quelque chose quand il y a pas internet
