# Pronote-Shell

Le projet "Pronote-Shell" permet aux utilisateurs d'accéder à leurs devoirs et notes directement depuis un terminal (shell) en se connectant à la plateforme Pronote. Ce script Python simplifie la gestion des devoirs et des notes en fournissant des informations actualisées sur les tâches à faire et les évaluations récentes.

## Fonctionnalités

- **Affichage des devoirs** : Récupère et affiche les devoirs pour aujourd'hui et pour les jours suivants.
- **Affichage des notes** : Récupère et affiche les notes des 5 derniers jours.
- **Vérification des vacances** : Indique si l'élève est en période de vacances basée sur les dates définies.

## Prérequis

- Python 3.x
- La bibliothèque `pronotepy` (installez-la avec `pip install pronotepy`)

## Installation

Clonez ce dépôt :

```bash
git clone https://github.com/lecodeetmoi/pronote-helper.git
```
Allez dans le dossier

```bash
cd pronote-shell
```

Allez dans 

```bash
cd le-chemin-pour-allez-dans-le-dossier
```
Avant d'executer le fichier vous devez modifier la partie client modifier donc le mot de passe et username . Puis executer le scripte 

```bash
python script.py
```
## Configuration

Vous pouvez ajuster les dates de début et de fin des vacances dans le script à l'aide des variables date_debut et date_fin.

## Bonus 

Si vous avez le shell [Fish](https://fishshell.com/) vous pouvez faire en sorte que des que vous lancer votre shell le scripte s'execute . 

```bash
cd ~/.config/fish/

```

```bash
nano config.fish
```

Puis ajouter la ligne à la suite 

```bash
python shell.py
```

Attention votre script shell.py doit doit être à la racine **~**



## Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez contribuer au projet, veuillez soumettre une demande de tirage (pull request) avec les modifications que vous proposez.

## Licence

Ce projet est sous licence MIT.