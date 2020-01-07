from CompteSimple import CompteSimple
from Titulaire import Titulaire

personne = Titulaire("MILAZZO", "Christopher", [CompteSimple(1500), CompteSimple(200), CompteSimple()])

personne.speak()
print("compte numéro 1 : " + str(personne.getCompte(1).getSolde()) + " euros.")
print("ajout de 150 euros sur le compte numéro 1")
personne.getCompte(1).credit(150)
print("compte numéro 1 : " + str(personne.getCompte(1).getSolde()) + " euros.")

personne.speak()

