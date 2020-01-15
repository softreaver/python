from CompteSimple import CompteSimple
from Transaction import Transaction

class CompteCourant(CompteSimple):
    _historique = []
    
    def __init__(this, initMnt = 0):
        CompteSimple.__init__(this, initMnt)

    def afficherHistorique(this):
        for transaction in this._historique:
            message = ''
            montant = transaction.getMontant()
            if transaction.getTransactionType() == Transaction.CREDIT:
                message = "--CREDIT-- d'un montant de " + str(montant) + " euros"
            else:
		montant = montant * -1
                message = "--DEBIT-- d'un montant de " + str(montant) + " euros"
                
            print(message)

        print("SOLDE TOTAL = " + str(CompteSimple.getSolde(this)))

    # mask
    def credit(this, montant):
        this._historique.append(Transaction(Transaction.CREDIT, montant))
        CompteSimple.credit(this, montant)

    # mask
    def debit(this, montant):
        this._historique.append(Transaction(Transaction.DEBIT, montant))
        CompteSimple.debit(this, montant)

