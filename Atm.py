class Atm(object):
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber
    def CashWithdrawl(self):
        print("cashwithdrawling")
    def BalanceEnquiry(self):
        print("BalanceEnquiry")
    def Money(self):
        print("Money to be Withdrawled")
    def Remove(self):
        print("Removethecard")
ATMCARD=Atm("1234567890","1122334455")
ATMCARD.CashWithdrawl()
ATMCARD.BalanceEnquiry()
ATMCARD.Money()
ATMCARD.Remove()