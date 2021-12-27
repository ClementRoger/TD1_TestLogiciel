# Commandes git

## Créer une branche

* _git checkout -b nom_branche_

## Basculer sur une branche

* _git checkout nom_branche_

## Ajouter un fichier sur le dépôt distant

* _git pull_ (ou _git fetch origin nom_branche_ puis _git merge origin nom_branche_)
* _git add nom_fichier_
* _git commit -m "changements effectués"_
* _git push -u origin nom_branche_

## Autres commandes utiles

* Créer un nouveau dépôt &#8594; _git init_
* Cloner un dépôt &#8594; _git clone URL_
* Si on veut "annuler" un git add &#8594; _git reset_
* Savoir les actions qu'on a faites (add, commit ou push) &#8594; _git status_
* Voir les conflits &#8594; _git diff_
* Afficher les fichiers qui sont sur le dépôt distant &#8594; _git ls-tree HEAD_
