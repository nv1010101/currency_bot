telegram_token = '5945363327:AAGHSRWD_bXVOirqcodZF212kgc4uf562mc'

public_currency_keys = {
    'биткоин': 'BTC',
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB',
    'драм': 'AMD'
}

keys = {
    'биткоин': 'BTC',
    'доллар': 'USD',
    '$': 'USD',
    'евро': 'EUR',
    '€': 'EUR',
    'рубль': 'RUB',
    'руб': 'RUB',
    '₽': 'RUB',
    'драм': 'AMD'
}


# openexchangerates.org/
openexchangerates_token = 'a864cc1edda0423383ddd5298e8ca43e'
url = f"https://openexchangerates.org/api/latest.json?app_id={openexchangerates_token}"

# пример приходящих данных от openexchangerates.org
# {'disclaimer': 'Usage subject to terms: https://openexchangerates.org/terms', 'license':
# 'https://openexchangerates.org/license', 'timestamp': 1681855200, 'base': 'USD', 'rates':
# {'AED': 3.67235, 'AFN': 91.499996, 'ALL': 102.575557, 'AMD': 388.3982, 'ANG': 1.802907,
# 'AOA': 506.516333, 'ARS': 216.9054, 'AUD': 1.48639, 'AWG': 1.80235, 'AZN': 1.7, 'BAM': 1.782326,
# 'BBD': 2, 'BDT': 106.227195, 'BGN': 1.782565, 'BHD': 0.376977, 'BIF': 2080.946757, 'BMD': 1,
# 'BND': 1.332507, 'BOB': 6.912388, 'BRL': 4.9858, 'BSD': 1, 'BTC': 3.2919275e-05, 'BTN': 82.048669,
# 'BWP': 13.146036, 'BYN': 2.525311, 'BZD': 2.016622, 'CAD': 1.339147, 'CDF': 2066.486194, 'CHF': 0.896339,
# 'CLF': 0.028807, 'CLP': 794.88, 'CNH': 6.88121, 'CNY': 6.876, 'COP': 4437.517561, 'CRC': 534.876334, 'CUC': 1,
# 'CUP': 25.75, 'CVE': 100.68733, 'CZK': 21.366984, 'DJF': 178.172377, 'DKK': 6.790656, 'DOP': 54.735049,
# 'DZD': 135.543585, 'EGP': 30.8952, 'ERN': 15, 'ETB': 54.304037, 'EUR': 0.911386, 'FJD': 2.20805,
# 'FKP': 0.804719, 'GBP': 0.804719, 'GEL': 2.51, 'GGP': 0.804719, 'GHS': 12.042584, 'GIP': 0.804719,
# 'GMD': 62.25, 'GNF': 8621.154416, 'GTQ': 7.802633, 'GYD': 211.581414, 'HKD': 7.849082, 'HNL': 24.616056,
# 'HRK': 6.867377, 'HTG': 156.069682, 'HUF': 338.046107, 'IDR': 14888.65, 'ILS': 3.646605, 'IMP': 0.804719,
# 'INR': 82.1138, 'IQD': 1460, 'IRR': 42275, 'ISK': 136.26, 'JEP': 0.804719, 'JMD': 152.470118,
# 'JOD': 0.7094, 'JPY': 134.08466667, 'KES': 135, 'KGS': 87.5136, 'KHR': 4065.511483, 'KMF': 449.300118,
# 'KPW': 900, 'KRW': 1317.619646, 'KWD': 0.306421, 'KYD': 0.833732, 'KZT': 452.169974, 'LAK': 17205.586287,
# 'LBP': 15077.12967, 'LKR': 322.163819, 'LRD': 163.049979, 'LSL': 18.177227, 'LYD': 4.758844,
# 'MAD': 10.144399, 'MDL': 17.908133, 'MGA': 4395.934612, 'MKD': 56.165287, 'MMK': 2100.96331,
# 'MNT': 3519, 'MOP': 8.088751, 'MRU': 34.310772, 'MUR': 45.060003, 'MVR': 15.35, 'MWK': 1026.900393,
# 'MXN': 18.045168, 'MYR': 4.4345, 'MZN': 63.899991, 'NAD': 18.19, 'NGN': 462.041639, 'NIO': 36.553286,
# 'NOK': 10.471796, 'NPR': 131.293498, 'NZD': 1.610519, 'OMR': 0.385003, 'PAB': 1, 'PEN': 3.782903,
# 'PGK': 3.526045, 'PHP': 56.290999, 'PKR': 283.947255, 'PLN': 4.213474, 'PYG': 7131.974811,
# 'QAR': 3.6405, 'RON': 4.49955, 'RSD': 106.868531, 'RUB': 81.837175, 'RWF': 1109.669943,
# 'SAR': 3.750644, 'SBD': 8.265733, 'SCR': 13.132151, 'SDG': 600, 'SEK': 10.309284,
# 'SGD': 1.332659, 'SHP': 0.804719, 'SLL': 17665, 'SOS': 569.009163, 'SRD': 36.7715,
# 'SSP': 130.26, 'STD': 22823.990504, 'STN': 22.508974, 'SVC': 8.753856, 'SYP': 2512.53,
# 'SZL': 18.165705, 'THB': 34.285, 'TJS': 10.929918, 'TMT': 3.5, 'TND': 3.115, 'TOP': 2.357826,
# 'TRY': 19.400518, 'TTD': 6.792109, 'TWD': 30.509201, 'TZS': 2346, 'UAH': 36.768045,
# 'UGX': 3744.429717, 'USD': 1, 'UYU': 38.980488, 'UZS': 11448.683459, 'VES': 24.530512,
# 'VND': 23510.232799, 'VUV': 118.979, 'WST': 2.72551, 'XAF': 597.829736, 'XAG': 0.03969856,
# 'XAU': 0.00049869, 'XCD': 2.70255, 'XDR': 0.741436, 'XOF': 597.829736, 'XPD': 0.00061265,
# 'XPF': 108.757226, 'XPT': 0.00091769, 'YER': 250.350023, 'ZAR': 18.183925, 'ZMW': 17.706501, 'ZWL': 322}}