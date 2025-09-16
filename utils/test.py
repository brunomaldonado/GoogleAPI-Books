
prices = [
  {'country': 'US', 'saleability': 'FOR_SALE', 'isEbook': True, 'listPrice': {'amount': 9.99, 'currencyCode': 'USD'}},
  {'country': 'US', 'saleability': 'FOR_SALE', 'isEbook': True, 'listPrice': {'amount': 11.99, 'currencyCode': 'USD'}}, 
  {'country': 'US', 'saleability': 'NOT_FOR_SALE', 'isEbook': False}, 
  {'country': 'US', 'saleability': 'FOR_SALE', 'isEbook': True, 'listPrice': {'amount': 11.99, 'currencyCode': 'USD'}}, 
  {'country': 'US', 'saleability': 'NOT_FOR_SALE', 'isEbook': False}, 
  {'country': 'US', 'saleability': 'FOR_SALE', 'isEbook': True, 'listPrice': {'amount': 11.99, 'currencyCode': 'USD'}}, 
  {'country': 'US', 'saleability': 'NOT_FOR_SALE', 'isEbook': False}, 
  {'country': 'US', 'saleability': 'NOT_FOR_SALE', 'isEbook': False}, 
  {'country': 'US', 'saleability': 'NOT_FOR_SALE', 'isEbook': False}, 
  {'country': 'US', 'saleability': 'FOR_SALE', 'isEbook': True, 'listPrice': {'amount': 11.99, 'currencyCode': 'USD'}}]

# print(type(prices))
# for_sale = ['amount']
# currency_code = prices[0]['listPrice']['currencyCode']
# print(for_sale, currency_code)

# print(f"Price: {prices[0]['listPrice']['amount']} {prices[0]['listPrice']['currencyCode']}")

def select_index(selection):
  if 1 <= selection <= len(prices):
    return selection - 1
  else:
    return None
selection = int(input("\nEnter option: "))
option = select_index(selection)
# print(option)

# if prices[option]['listPrice']:
#   for_sale = f"{prices[option]['listPrice']['amount']} {prices[option]['listPrice']['currencyCode']}"
# else:
#   for_sale = " Not For Sale"

# print(for_sale)

if option is not None:
  if 'listPrice' in prices[option]:
    for_sale = f"{prices[option]['listPrice']['amount']} {prices[option]['listPrice']['currencyCode']}"
  else:
    for_sale = "NOT FOR SALE"
  print(for_sale)
else:
  print("Invalid selection")