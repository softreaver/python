
class Transaction:
    CREDIT = 1
    DEBIT = 2

    _montant = 0
    _transactionType = 0

    def __init__(this, transactionType, montant):
        assert transactionType == this.CREDIT or transactionType == this.DEBIT
        this._montant = montant
        this._transactionType = transactionType

    def getMontant(this):
        return this._montant

    def getTransactionType(this):
        return this._transactionType

