#Stock Purchase
#Declaring variables from available data
sharesBought = float(1000)
purchasePrice = float(32.87)
commission = 0.02
sharesSold = float(1000)
salePrice = 33.92

#calculating money spent and made with commission considerations
purchase = purchasePrice * sharesBought
purchaseComm = purchase * commission
sale = salePrice * sharesSold
saleComm = sale * commission
profit = purchase - sale - commission - commission

#Statements of information about transactions 
print('Joe paid ${:.2f} for the stock.'.format(purchase))
print('Joe paid ${:.2f} commission to his broker on purchase.'.format(purchaseComm))
print('Joe sold the stock for ${:.2f}.'.format(sale))
print('Joe paid ${:.2f} commission to his broker on sale.'.format(saleComm))

#Test 
if profit > 0:
    print('Joe profitted by ${:.2f}'.format(profit))
else:
    if profit < 0:
        print('Joe lost ${:.2f}'.format(profit))
    else:
        print('Joe broke even.')