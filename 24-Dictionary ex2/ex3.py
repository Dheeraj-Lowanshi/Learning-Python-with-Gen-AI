


accounts={101:45000,102:500000,103:55000}
acct_id=int(input("Enter the account id:"))
amt=int(input("Enter the amount:"))
balance=accounts.get(acct_id)
if balance is None:
    accounts[acct_id]=amt
    print("Account created")
else:
    accounts[acct_id]=balance+amt
    print("Amount added")

print("After Changes:")
print(accounts)