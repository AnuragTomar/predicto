#import nsetools
from nsetools import Nse
nse = Nse()
print(nse)

q = nse.get_quote('infy') # it's ok to use both upper or lower case for codes.
from pprint import pprint # just for neatness of display
pprint(q)

nifty_quote = nse.get_index_quote('cnx nifty') # code can be provided in upper|lower case.
banknifty_quote = nse.get_index_quote('banknifty') # code can be provided in upper|lower case.
pprint(nifty_quote)

pprint(banknifty_quote)

all_stock_codes = nse.get_stock_codes()
pprint(all_stock_codes)

index_codes = nse.get_index_list()
pprint(index_codes)

adv_dec = nse.get_advances_declines()
pprint(adv_dec)

top_gainers = nse.get_top_gainers()
pprint(top_gainers)

nse.is_valid_code('infy') # this should return True
