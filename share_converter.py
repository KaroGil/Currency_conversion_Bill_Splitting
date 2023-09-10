
#converts the percentage of your share of the bill to your currency (your bank's currency)
#useful for splitting bills while on vacation in another country that uses a different currency than yours
def convert_bill_share(total, your_share, money_from_bank):
    p = your_share / total
    amount = p * money_from_bank

    return amount


#If you have a series of bills to split you can input a list of payments
def split_several_bills(total_list, share_list, bank_statement_list):
    total_amount = 0
    l = len(total_list)
    if not (l == len(share_list) == len(bank_statement_list)):
        return 0
    for i in range(l):
       total_amount += convert_bill_share(total_list[i], share_list[i], bank_statement_list[i])

    return total_amount


# Examples
print("My KFC share", convert_bill_share(100,10,300))
print("Total amount for list of expenses", split_several_bills([100,1001,400],[70,100,40], [300,3003,1200]))
