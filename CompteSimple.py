
class CompteSimple:
    _solde = 0

    def __init__(this, initMnt = 0):
        this._solde = initMnt

    def credit(this, mnt):
        this._solde += mnt

    def debit(this, mnt):
        this._solde -= mnt

    def getSolde(this):
        return this._solde

