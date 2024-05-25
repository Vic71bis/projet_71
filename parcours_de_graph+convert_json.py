# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:50:37 2024

@author: ifyes
"""

# all_countries = {"AF": [["China", "CN"], ["Iran", "IR"], ["Pakistan", "PK"], ["Tajikistan", "TJ"], ["Turkmenistan", "TM"], ["Uzbekistan", "UZ"]], 
# "AL": [["Greece", "GR"], ["Kosovo", "XK"], ["Montenegro", "ME"], ["North Macedonia", "MK"], ["Serbia", "RS"]], 
# "DZ": [["Libya", "LY"], ["Mali", "ML"], ["Mauritania", "MR"], ["Morocco", "MA"], ["Niger", "NE"], ["Tunisia", "TN"], ["Western Sahara", "EH"]], 
# "AD": [["France", "FR"], ["Spain", "ES"]], 
# "AO": [["Congo Republic", "CG"], ["DR Congo", "CD"], ["Namibia", "NA"], ["Zambia", "ZM"]], 
# "AG": [], 
# "AR": [["Bolivia", "BO"], ["Brazil", "BR"], ["Chile", "CL"], ["Paraguay", "PY"], ["Uruguay", "UY"]], 
# "AM": [["Azerbaijan", "AZ"], ["Georgia", "GE"], ["Iran", "IR"], ["Turkey", "TR"]], 
# "AU": [], 
# "AT": [["Czechia", "CZ"], ["Germany", "DE"], ["Hungary", "HU"], ["Italy", "IT"], ["Liechtenstein", "LI"], ["Slovakia", "SK"], ["Slovenia", "SI"], ["Switzerland", "CH"]], 
# "AZ": [["Armenia", "AM"], ["Georgia", "GE"], ["Iran", "IR"], ["Russia", "RU"], ["Turkey", "TR"]], 
# "BS": [], 
# "BH": [], 
# "BD": [["India", "IN"], ["Myanmar", "MM"]], 
# "BB": [], 
# "BY": [["Latvia", "LV"], ["Lithuania", "LT"], ["Poland", "PL"], ["Russia", "RU"], ["Ukraine", "UA"]], 
# "BE": [["France", "FR"], ["Germany", "DE"], ["Luxembourg", "LU"], ["Netherlands", "NL"]], 
# "BZ": [["Guatemala", "GT"], ["Mexico", "MX"]], 
# "BJ": [["Burkina Faso", "BF"], ["Niger", "NE"], ["Nigeria", "NG"], ["Togo", "TG"]], 
# "BT": [["China", "CN"], ["India", "IN"]], 
# "BO": [["Argentina", "AR"], ["Brazil", "BR"], ["Chile", "CL"], ["Paraguay", "PY"], ["Peru", "PE"]], 
# "BA": [["Croatia", "HR"], ["Montenegro", "ME"], ["Serbia", "RS"]], 
# "BW": [["Namibia", "NA"], ["South Africa", "ZA"], ["Zimbabwe", "ZW"]], 
# "BR": [["Argentina", "AR"], ["Bolivia", "BO"], ["Colombia", "CO"], ["French Guiana", "GF"], ["Guyana", "GY"], ["Paraguay", "PY"], ["Peru", "PE"], ["Suriname", "SR"], ["Uruguay", "UY"], ["Venezuela", "VE"]], 
# "BN": [["Malaysia", "MY"]], 
# "BG": [["Greece", "GR"], ["North Macedonia", "MK"], ["Romania", "RO"], ["Serbia", "RS"], ["Turkey", "TR"]], 
# "BF": [["Benin", "BJ"], ["Ghana", "GH"], ["Ivory Coast", "CI"], ["Mali", "ML"], ["Niger", "NE"], ["Togo", "TG"]], 
# "BI": [["DR Congo", "CD"], ["Rwanda", "RW"], ["Tanzania", "TZ"]], 
# "KH": [["Laos", "LA"], ["Thailand", "TH"], ["Vietnam", "VN"]], 
# "CM": [["Central African Republic", "CF"], ["Chad", "TD"], ["Congo Republic", "CG"], ["Equatorial Guinea", "GQ"], ["Gabon", "GA"], ["Nigeria", "NG"]], 
# "CA": [["United States", "US"]], 
# "CV": [], "cf": [["Cameroon", "CM"], ["Chad", "TD"], ["Congo Republic", "CG"], ["DR Congo", "CD"], ["South Sudan", "SS"], ["Sudan", "SD"]], 
# "TD": [["Cameroon", "CM"], ["Central African Republic", "CF"], ["Libya", "LY"], ["Niger", "NE"], ["Nigeria", "NG"], ["Sudan", "SD"]], 
# "CL": [["Argentina", "AR"], ["Bolivia", "BO"], ["Peru", "PE"]], 
# "CN": [["Afghanistan", "AF"], ["Bhutan", "BT"], ["India", "IN"], ["Kazakhstan", "KZ"], ["Kyrgyzstan", "KG"], ["Laos", "LA"], ["Mongolia", "MN"], ["Myanmar", "MM"], ["Nepal", "NP"], ["North Korea", "KP"], ["Pakistan", "PK"], ["Russia", "RU"], ["Tajikistan", "TJ"], ["Vietnam", "VN"]], 
# "CO": [["Brazil", "BR"], ["Ecuador", "EC"], ["Panama", "PA"], ["Peru", "PE"], ["Venezuela", "VE"]], 
# "KM": [], 
# "CG": [["Angola", "AO"], ["Cameroon", "CM"], ["Central African Republic", "CF"], ["DR Congo", "CD"], ["Gabon", "GA"]], 
# "CR": [["Nicaragua", "NI"], ["Panama", "PA"]], 
# "CI": [["Burkina Faso", "BF"], ["Ghana", "GH"], ["Guinea", "GN"], ["Liberia", "LR"], ["Mali", "ML"]], 
# "HR": [["Bosnia and Herzegovina", "BA"], ["Hungary", "HU"], ["Montenegro", "ME"], ["Serbia", "RS"], ["Slovenia", "SI"]], 
# "CU": [["United States", "US"]], 
# "CY": [], 
# "CZ": [["Austria", "AT"], ["Germany", "DE"], ["Poland", "PL"], ["Slovakia", "SK"]], 
# "KP": [["China", "CN"], ["Russia", "RU"], ["South Korea", "KR"]], 
# "CD": [["Angola", "AO"], ["Burundi", "BI"], ["Central African Republic", "CF"], ["Congo Republic", "CG"], ["Rwanda", "RW"], ["South Sudan", "SS"], ["Tanzania", "TZ"], ["Uganda", "UG"], ["Zambia", "ZM"]], 
# "DK": [["Germany", "DE"]], 
# "DJ": [["Eritrea", "ER"], ["Ethiopia", "ET"], ["Somalia", "SO"]], 
# "DM": [], 
# "DO": [["Haiti", "HT"]], "ec": [["Colombia", "CO"], ["Peru", "PE"]], 
# "EG": [["Israel", "IL"], ["Libya", "LY"], ["Palestine", "PS"], ["Sudan", "SD"]], 
# "SV": [["Guatemala", "GT"], ["Honduras", "HN"]], 
# "GQ": [["Cameroon", "CM"], ["Gabon", "GA"]], 
# "ER": [["Djibouti", "DJ"], ["Ethiopia", "ET"], ["Sudan", "SD"]], 
# "EE": [["Latvia", "LV"], ["Russia", "RU"]], 
# "ET": [["Djibouti", "DJ"], ["Eritrea", "ER"], ["Kenya", "KE"], ["Somalia", "SO"], ["South Sudan", "SS"], ["Sudan", "SD"]], 
# "FJ": [], 
# "FI": [["Norway", "NO"], ["Russia", "RU"], ["Sweden", "SE"]], 
# "FR": [["Andorra", "AD"], ["Belgium", "BE"], ["Germany", "DE"], ["Italy", "IT"], ["Luxembourg", "LU"], ["Monaco", "MC"], ["Spain", "ES"], ["Switzerland", "CH"]], 
# "GA": [["Cameroon", "CM"], ["Congo Republic", "CG"], ["Equatorial Guinea", "GQ"]], 
# "GM": [["Senegal", "SN"]], 
# "GE": [["Armenia", "AM"], ["Azerbaijan", "AZ"], ["Russia", "RU"], ["Turkey", "TR"]], 
# "DE": [["Austria", "AT"], ["Belgium", "BE"], ["Czechia", "CZ"], ["Denmark", "DK"], ["France", "FR"], ["Luxembourg", "LU"], ["Netherlands", "NL"], ["Poland", "PL"], ["Switzerland", "CH"]], 
# "GH": [["Burkina Faso", "BF"], ["Ivory Coast", "CI"], ["Togo", "TG"]], 
# "GR": [["Albania", "AL"], ["Bulgaria", "BG"], ["North Macedonia", "MK"], ["Turkey", "TR"]], 
# "GL": [], 
# "GD": [], 
# "GT": [["Belize", "BZ"], ["El Salvador", "SV"], ["Honduras", "HN"], ["Mexico", "MX"]], 
# "GN": [["Guinea-Bissau", "GW"], ["Ivory Coast", "CI"], ["Liberia", "LR"], ["Mali", "ML"], ["Senegal", "SN"], ["Sierra Leone", "SL"]], 
# "GW": [["Guinea", "GN"], ["Senegal", "SN"]], 
# "GY": [["Brazil", "BR"], ["Suriname", "SR"], ["Venezuela", "VE"]], 
# "HT": [["Dominican Republic", "DO"]], 
# "HN": [["El Salvador", "SV"], ["Guatemala", "GT"], ["Nicaragua", "NI"]], 
# "HU": [["Austria", "AT"], ["Croatia", "HR"], ["Romania", "RO"], ["Serbia", "RS"], ["Slovakia", "SK"], ["Slovenia", "SI"], ["Ukraine", "UA"]], 
# "IS": [], 
# "IN": [["Bangladesh", "BD"], ["Bhutan", "BT"], ["China", "CN"], ["Myanmar", "MM"], ["Nepal", "NP"], ["Pakistan", "PK"]], 
# "ID": [["Malaysia", "MY"], ["Papua New Guinea", "PG"], ["Timor-Leste", "TL"]], 
# "IR": [["Afghanistan", "AF"], ["Armenia", "AM"], ["Azerbaijan", "AZ"], ["Iraq", "IQ"], ["Pakistan", "PK"], ["Turkey", "TR"], ["Turkmenistan", "TM"]], 
# "IQ": [["Iran", "IR"], ["Jordan", "JO"], ["Kuwait", "KW"], ["Saudi Arabia", "SA"], ["Syria", "SY"], ["Turkey", "TR"]], 
# "IE": [["United Kingdom", "GB"]], 
# "IL": [["Egypt", "EG"], ["Jordan", "JO"], ["Lebanon", "LB"], ["Palestine", "PS"], ["Syria", "SY"]], 
# "IT": [["Austria", "AT"], ["France", "FR"], ["San Marino", "SM"], ["Slovenia", "SI"], ["Switzerland", "CH"], ["Vatican City", "VA"]], 
# "JM": [], 
# "JP": [], 
# "JO": [["Iraq", "IQ"], ["Israel", "IL"], ["Palestine", "PS"], ["Saudi Arabia", "SA"], ["Syria", "SY"]], 
# "KZ": [["China", "CN"], ["Kyrgyzstan", "KG"], ["Russia", "RU"], ["Turkmenistan", "TM"], ["Uzbekistan", "UZ"]], 
# "KE": [["Ethiopia", "ET"], ["Somalia", "SO"], ["South Sudan", "SS"], ["Tanzania", "TZ"], ["Uganda", "UG"]], 
# "KI": [], 
# "KW": [["Iraq", "IQ"], ["Saudi Arabia", "SA"]], 
# "KG": [["China", "CN"], ["Kazakhstan", "KZ"], ["Tajikistan", "TJ"], ["Uzbekistan", "UZ"]], 
# "LA": [["Cambodia", "KH"], ["China", "CN"], ["Myanmar", "MM"], ["Thailand", "TH"], ["Vietnam", "VN"]], 
# "LV": [["Belarus", "BY"], ["Estonia", "EE"], ["Lithuania", "LT"], ["Russia", "RU"]], 
# "LB": [["Israel", "IL"], ["Syria", "SY"]], 
# "LS": [["South Africa", "ZA"]], 
# "LR": [["Guinea", "GN"], ["Ivory Coast", "CI"], ["Sierra Leone", "SL"]], 
# "LY": [["Algeria", "DZ"], ["Chad", "TD"], ["Egypt", "EG"], ["Niger", "NE"], ["Sudan", "SD"], ["Tunisia", "TN"]], 
# "LI": [["Austria", "AT"], ["Switzerland", "CH"]], 
# "LT": [["Belarus", "BY"], ["Latvia", "LV"], ["Poland", "PL"], ["Russia", "RU"]], 
# "LU": [["Belgium", "BE"], ["France", "FR"], ["Germany", "DE"]], 
# "MK": [["Albania", "AL"], ["Bulgaria", "BG"], ["Greece", "GR"], ["Kosovo", "XK"], ["Serbia", "RS"]], 
# "MG": [], "mw": [["Mozambique", "MZ"], ["Tanzania", "TZ"], ["Zambia", "ZM"]], 
# "MY": [["Brunei", "BN"], ["Indonesia", "ID"], ["Thailand", "TH"]], 
# "MV": [], 
# "ML": [["Algeria", "DZ"], ["Burkina Faso", "BF"], ["Guinea", "GN"], ["Ivory Coast", "CI"], ["Mauritania", "MR"], ["Niger", "NE"], ["Senegal", "SN"]], 
# "MT": [], 
# "MH": [], 
# "MR": [["Algeria", "DZ"], ["Mali", "ML"], ["Senegal", "SN"], ["Western Sahara", "EH"]], 
# "MU": [], 
# "MX": [["Belize", "BZ"], ["Guatemala", "GT"], ["United States", "US"]], 
# "FM": [], 
# "MC": [["France", "FR"]], 
# "MN": [["China", "CN"], ["Russia", "RU"]], 
# "ME": [["Albania", "AL"], ["Bosnia and Herzegovina", "BA"], ["Croatia", "HR"], ["Kosovo", "XK"], ["Serbia", "RS"]], 
# "MA": [["Algeria", "DZ"], ["Spain", "ES"], ["Western Sahara", "EH"]], 
# "MZ": [["Eswatini", "SZ"], ["Malawi", "MW"], ["South Africa", "ZA"], ["Tanzania", "TZ"], ["Zambia", "ZM"], ["Zimbabwe", "ZW"]], 
# "MM": [["Bangladesh", "BD"], ["China", "CN"], ["India", "IN"], ["Laos", "LA"], ["Thailand", "TH"]], 
# "NA": [["Angola", "AO"], ["Botswana", "BW"], ["South Africa", "ZA"], ["Zambia", "ZM"]], 
# "NR": [], 
# "NP": [["China", "CN"], ["India", "IN"]], 
# "NL": [["Belgium", "BE"], ["Germany", "DE"]], 
# "NZ": [], 
# "NI": [["Costa Rica", "CR"], ["Honduras", "HN"]], 
# "NE": [["Algeria", "DZ"], ["Benin", "BJ"], ["Burkina Faso", "BF"], ["Chad", "TD"], ["Libya", "LY"], ["Mali", "ML"], ["Nigeria", "NG"]], 
# "NG": [["Benin", "BJ"], ["Cameroon", "CM"], ["Chad", "TD"], ["Niger", "NE"]], 
# "NO": [["Finland", "FI"], ["Russia", "RU"], ["Sweden", "SE"]], 
# "OM": [["Saudi Arabia", "SA"], ["United Arab Emirates", "AE"], ["Yemen", "YE"]], 
# "PK": [["Afghanistan", "AF"], ["China", "CN"], ["India", "IN"], ["Iran", "IR"]], 
# "PW": [], 
# "PA": [["Colombia", "CO"], ["Costa Rica", "CR"]], 
# "PG": [["Indonesia", "ID"]], 
# "PY": [["Argentina", "AR"], ["Bolivia", "BO"], ["Brazil", "BR"]], 
# "PE": [["Bolivia", "BO"], ["Brazil", "BR"], ["Chile", "CL"], ["Colombia", "CO"], ["Ecuador", "EC"]], 
# "PH": [], 
# "PL": [["Belarus", "BY"], ["Czechia", "CZ"], ["Germany", "DE"], ["Lithuania", "LT"], ["Russia", "RU"], ["Slovakia", "SK"], ["Ukraine", "UA"]], 
# "PT": [["Spain", "ES"]], 
# "QA": [["Saudi Arabia", "SA"]], 
# "RO": [["Bulgaria", "BG"], ["Hungary", "HU"], ["Moldova", "MD"], ["Serbia", "RS"], ["Ukraine", "UA"]], 
# "RU": [["Azerbaijan", "AZ"], ["Belarus", "BY"], ["China", "CN"], ["Estonia", "EE"], ["Finland", "FI"], ["Georgia", "GE"], ["Kazakhstan", "KZ"], ["Latvia", "LV"], ["Lithuania", "LT"], ["Mongolia", "MN"], ["North Korea", "KP"], ["Norway", "NO"], ["Poland", "PL"], ["Ukraine", "UA"]], 
# "RW": [["Burundi", "BI"], ["DR Congo", "CD"], ["Tanzania", "TZ"], ["Uganda", "UG"]], 
# "KN": [], 
# "LC": [], 
# "VC": [], 
# "WS": [], 
# "SM": [["Italy", "IT"]], 
# "ST": [], 
# "SA": [["Iraq", "IQ"], ["Jordan", "JO"], ["Kuwait", "KW"], ["Oman", "OM"], ["Qatar", "QA"], ["United Arab Emirates", "AE"], ["Yemen", "YE"]], 
# "SN": [["Guinea", "GN"], ["Guinea-Bissau", "GW"], ["Mali", "ML"], ["Mauritania", "MR"], ["The Gambia", "GM"]], 
# "RS": [["Albania", "AL"], ["Bosnia and Herzegovina", "BA"], ["Bulgaria", "BG"], ["Croatia", "HR"], ["Hungary", "HU"], ["Kosovo", "XK"], ["Montenegro", "ME"], ["North Macedonia", "MK"], ["Romania", "RO"]], 
# "SC": [], 
# "SL": [["Guinea", "GN"], ["Liberia", "LR"]], 
# "SG": [], 
# "SK": [["Austria", "AT"], ["Czechia", "CZ"], ["Hungary", "HU"], ["Poland", "PL"], ["Ukraine", "UA"]], 
# "SI": [["Austria", "AT"], ["Croatia", "HR"], ["Hungary", "HU"], ["Italy", "IT"]], 
# "SB": [], 
# "SO": [["Djibouti", "DJ"], ["Ethiopia", "ET"], ["Kenya", "KE"]], 
# "ZA": [["Botswana", "BW"], ["Eswatini", "SZ"], ["Lesotho", "LS"], ["Mozambique", "MZ"], ["Namibia", "NA"], ["Zimbabwe", "ZW"]], 
# "SS": [["Central African Republic", "CF"], ["DR Congo", "CD"], ["Ethiopia", "ET"], ["Kenya", "KE"], ["Sudan", "SD"], ["Uganda", "UG"]], 
# "ES": [["Andorra", "AD"], ["France", "FR"], ["Gibraltar", "GI"], ["Morocco", "MA"], ["Portugal", "PT"]], 
# "LK": [], 
# "SD": [["Central African Republic", "CF"], ["Chad", "TD"], ["Egypt", "EG"], ["Eritrea", "ER"], ["Ethiopia", "ET"], ["Libya", "LY"], ["South Sudan", "SS"]], 
# "SR": [["Brazil", "BR"], ["French Guiana", "GF"], ["Guyana", "GY"]], 
# "SZ": [["Mozambique", "MZ"], ["South Africa", "ZA"]], 
# "SE": [["Finland", "FI"], ["Norway", "NO"]], 
# "CH": [["Austria", "AT"], ["France", "FR"], ["Germany", "DE"], ["Italy", "IT"], ["Liechtenstein", "LI"]], 
# "SY": [["Iraq", "IQ"], ["Israel", "IL"], ["Jordan", "JO"], ["Lebanon", "LB"], ["Turkey", "TR"]], 
# "TW": [], 
# "TJ": [["Afghanistan", "AF"], ["China", "CN"], ["Kyrgyzstan", "KG"], ["Uzbekistan", "UZ"]], 
# "TZ": [["Burundi", "BI"], ["DR Congo", "CD"], ["Kenya", "KE"], ["Malawi", "MW"], ["Mozambique", "MZ"], ["Rwanda", "RW"], ["Uganda", "UG"], ["Zambia", "ZM"]], 
# "TH": [["Cambodia", "KH"], ["Laos", "LA"], ["Malaysia", "MY"], ["Myanmar", "MM"]], 
# "TL": [["Indonesia", "ID"]], 
# "TG": [["Benin", "BJ"], ["Burkina Faso", "BF"], ["Ghana", "GH"]], 
# "TO": [], 
# "TT": [], 
# "TN": [["Algeria", "DZ"], ["Libya", "LY"]], 
# "TR": [["Armenia", "AM"], ["Azerbaijan", "AZ"], ["Bulgaria", "BG"], ["Georgia", "GE"], ["Greece", "GR"], ["Iran", "IR"], ["Iraq", "IQ"], ["Syria", "SY"]], 
# "TM": [["Afghanistan", "AF"], ["Iran", "IR"], ["Kazakhstan", "KZ"], ["Uzbekistan", "UZ"]], 
# "TC": [], 
# "TV": [], 
# "UG": [["DR Congo", "CD"], ["Kenya", "KE"], ["Rwanda", "RW"], ["South Sudan", "SS"], ["Tanzania", "TZ"]], 
# "UA": [["Belarus", "BY"], ["Hungary", "HU"], ["Moldova", "MD"], ["Poland", "PL"], ["Romania", "RO"], ["Russia", "RU"], ["Slovakia", "SK"]], 
# "AE": [["Oman", "OM"], ["Saudi Arabia", "SA"]], 
# "GB": [["Ireland", "IE"]], 
# "US": [["Canada", "CA"], ["Cuba", "CU"], ["Mexico", "MX"]], 
# "UY": [["Argentina", "AR"], ["Brazil", "BR"]], 
# "UZ": [["Afghanistan", "AF"], ["Kazakhstan", "KZ"], ["Kyrgyzstan", "KG"], ["Tajikistan", "TJ"], ["Turkmenistan", "TM"]], 
# "VU": [], 
# "VE": [["Brazil", "BR"], ["Colombia", "CO"], ["Guyana", "GY"]], 
# "VN": [["Cambodia", "KH"], ["China", "CN"], ["Laos", "LA"]], 
# "YE": [["Oman", "OM"], ["Saudi Arabia", "SA"]], 
# "ZM": [["Angola", "AO"], ["DR Congo", "CD"], ["Malawi", "MW"], ["Mozambique", "MZ"], ["Namibia", "NA"], ["Tanzania", "TZ"], ["Zimbabwe", "ZW"]], 
# "ZW": [["Botswana", "BW"], ["Mozambique", "MZ"], ["South Africa", "ZA"], ["Zambia", "ZM"]]}

import json

with open(country_neighbours.json, 'r') as file:
    all_countries = json.load(file)


def create_bfs (start, all_countries):
    """
    Parameters
    ----------
    start : string (pays de depart)
        
    all_countries: dico avec neighbours
    

    Returns : dico_prec (tree des pays qu'on peut atteindre à partir du start)
    
    """
    a_traiter = [start]
    dico_prec = {}
    dico_prec[start] = None
    treated = []
    
    while len(a_traiter) > 0:
        s = a_traiter.pop(0)
        treated.append(s)
        if s in all_countries:
            for si in all_countries[s]:
                if si != []:
                    s_abrev = si[1]
                    if s_abrev not in treated and s_abrev not in a_traiter:
                        a_traiter.append(s_abrev)
                        dico_prec[s_abrev] = s
                    
    return dico_prec

def is_reachable_by_car (start, end, all_countries):
    ans = 10
    tree = create_bfs(start, all_countries)
    if end in tree:
        ans = True
    else:
        ans = False
    return ans, tree
    
def shortest_path(v, parents):
    path = []
    while v is not None:
        path.append(v)
        v = parents[v]
    return path[::-1]

        
def get_path_btw_countries (start, end, all_countries):
    reachable, tree = is_reachable_by_car(start, end, all_countries)
    if reachable:
        path = shortest_path(end, tree)
        return path
    else:
        return False

# Get the path from Canada (CA) to Mexico (MX)
path = get_path_btw_countries("FI", "FR", all_countries)
print("Path from CA to MX :", path)