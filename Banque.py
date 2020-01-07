
class Banque:
    _titulaires = 0
    _nomBanque  = ""
    
    def __init__(this, nomBanque):
        this_nomBanque = nomBanque

    def creerClient(this, nom, prenom, comptes = []):
        this._titulaires.append(Titulaire(nom, prenom, comptes))

    def supprimerClient(this, nClient):
        this._titulaires.remove(this._titulaire[nClient])

    def getTotalSoldes(this):
        total = 0
        for titulaire in this._titulaires:
            total += titulaire.getTotalSolde()
        return total


