from currency_codes.models import Currency


def get_fiat_currencies() -> list[Currency]:
    return _fiat_currencies


_fiat_currencies: list[Currency] = [
    Currency(name="Afghani", code="AFN", numeric_code="971", minor_units=2),
    Currency(name="Euro", code="EUR", numeric_code="978", minor_units=2),
    Currency(name="Lek", code="ALL", numeric_code="008", minor_units=2),
    Currency(name="Algerian Dinar", code="DZD", numeric_code="012", minor_units=2),
    Currency(name="US Dollar", code="USD", numeric_code="840", minor_units=2),
    Currency(name="Kwanza", code="AOA", numeric_code="973", minor_units=2),
    Currency(name="East Caribbean Dollar", code="XCD", numeric_code="951", minor_units=2),
    Currency(name="Argentine Peso", code="ARS", numeric_code="032", minor_units=2),
    Currency(name="Armenian Dram", code="AMD", numeric_code="051", minor_units=2),
    Currency(name="Aruban Florin", code="AWG", numeric_code="533", minor_units=2),
    Currency(name="Australian Dollar", code="AUD", numeric_code="036", minor_units=2),
    Currency(name="Azerbaijan Manat", code="AZN", numeric_code="944", minor_units=2),
    Currency(name="Bahamian Dollar", code="BSD", numeric_code="044", minor_units=2),
    Currency(name="Bahraini Dinar", code="BHD", numeric_code="048", minor_units=3),
    Currency(name="Taka", code="BDT", numeric_code="050", minor_units=2),
    Currency(name="Barbados Dollar", code="BBD", numeric_code="052", minor_units=2),
    Currency(name="Belarusian Ruble", code="BYN", numeric_code="933", minor_units=2),
    Currency(name="Belize Dollar", code="BZD", numeric_code="084", minor_units=2),
    Currency(name="Bermudian Dollar", code="BMD", numeric_code="060", minor_units=2),
    Currency(name="Indian Rupee", code="INR", numeric_code="356", minor_units=2),
    Currency(name="Ngultrum", code="BTN", numeric_code="064", minor_units=2),
    Currency(name="Boliviano", code="BOB", numeric_code="068", minor_units=2),
    Currency(name="Pula", code="BWP", numeric_code="072", minor_units=2),
    Currency(name="Norwegian Krone", code="NOK", numeric_code="578", minor_units=2),
    Currency(name="Brazilian Real", code="BRL", numeric_code="986", minor_units=2),
    Currency(name="Brunei Dollar", code="BND", numeric_code="096", minor_units=2),
    Currency(name="Bulgarian Lev", code="BGN", numeric_code="975", minor_units=2),
    Currency(name="Burundi Franc", code="BIF", numeric_code="108", minor_units=0),
    Currency(name="Cabo Verde Escudo", code="CVE", numeric_code="132", minor_units=2),
    Currency(name="Riel", code="KHR", numeric_code="116", minor_units=2),
    Currency(name="Canadian Dollar", code="CAD", numeric_code="124", minor_units=2),
    Currency(name="Cayman Islands Dollar", code="KYD", numeric_code="136", minor_units=2),
    Currency(name="Chilean Peso", code="CLP", numeric_code="152", minor_units=0),
    Currency(name="Yuan Renminbi", code="CNY", numeric_code="156", minor_units=2),
    Currency(name="Colombian Peso", code="COP", numeric_code="170", minor_units=2),
    Currency(name="Comorian Franc ", code="KMF", numeric_code="174", minor_units=0),
    Currency(name="Congolese Franc", code="CDF", numeric_code="976", minor_units=2),
    Currency(name="New Zealand Dollar", code="NZD", numeric_code="554", minor_units=2),
    Currency(name="Costa Rican Colon", code="CRC", numeric_code="188", minor_units=2),
    Currency(name="CFA Franc BCEAO", code="XOF", numeric_code="952", minor_units=0),
    Currency(name="Cuban Peso", code="CUP", numeric_code="192", minor_units=2),
    Currency(name="Netherlands Antillean Guilder", code="ANG", numeric_code="532", minor_units=2),
    Currency(name="Czech Koruna", code="CZK", numeric_code="203", minor_units=2),
    Currency(name="Danish Krone", code="DKK", numeric_code="208", minor_units=2),
    Currency(name="Djibouti Franc", code="DJF", numeric_code="262", minor_units=0),
    Currency(name="Dominican Peso", code="DOP", numeric_code="214", minor_units=2),
    Currency(name="Egyptian Pound", code="EGP", numeric_code="818", minor_units=2),
    Currency(name="El Salvador Colon", code="SVC", numeric_code="222", minor_units=2),
    Currency(name="Nakfa", code="ERN", numeric_code="232", minor_units=2),
    Currency(name="Lilangeni", code="SZL", numeric_code="748", minor_units=2),
    Currency(name="Ethiopian Birr", code="ETB", numeric_code="230", minor_units=2),
    Currency(name="Falkland Islands Pound", code="FKP", numeric_code="238", minor_units=2),
    Currency(name="Fiji Dollar", code="FJD", numeric_code="242", minor_units=2),
    Currency(name="Dalasi", code="GMD", numeric_code="270", minor_units=2),
    Currency(name="Lari", code="GEL", numeric_code="981", minor_units=2),
    Currency(name="Ghana Cedi", code="GHS", numeric_code="936", minor_units=2),
    Currency(name="Gibraltar Pound", code="GIP", numeric_code="292", minor_units=2),
    Currency(name="Quetzal", code="GTQ", numeric_code="320", minor_units=2),
    Currency(name="Pound Sterling", code="GBP", numeric_code="826", minor_units=2),
    Currency(name="Guinean Franc", code="GNF", numeric_code="324", minor_units=0),
    Currency(name="Guyana Dollar", code="GYD", numeric_code="328", minor_units=2),
    Currency(name="Gourde", code="HTG", numeric_code="332", minor_units=2),
    Currency(name="Lempira", code="HNL", numeric_code="340", minor_units=2),
    Currency(name="Hong Kong Dollar", code="HKD", numeric_code="344", minor_units=2),
    Currency(name="Forint", code="HUF", numeric_code="348", minor_units=2),
    Currency(name="Iceland Krona", code="ISK", numeric_code="352", minor_units=0),
    Currency(name="Rupiah", code="IDR", numeric_code="360", minor_units=2),
    Currency(name="Iranian Rial", code="IRR", numeric_code="364", minor_units=2),
    Currency(name="Iraqi Dinar", code="IQD", numeric_code="368", minor_units=3),
    Currency(name="New Israeli Sheqel", code="ILS", numeric_code="376", minor_units=2),
    Currency(name="Jamaican Dollar", code="JMD", numeric_code="388", minor_units=2),
    Currency(name="Yen", code="JPY", numeric_code="392", minor_units=0),
    Currency(name="Jordanian Dinar", code="JOD", numeric_code="400", minor_units=3),
    Currency(name="Tenge", code="KZT", numeric_code="398", minor_units=2),
    Currency(name="Kenyan Shilling", code="KES", numeric_code="404", minor_units=2),
    Currency(name="North Korean Won", code="KPW", numeric_code="408", minor_units=2),
    Currency(name="Won", code="KRW", numeric_code="410", minor_units=0),
    Currency(name="Kuwaiti Dinar", code="KWD", numeric_code="414", minor_units=3),
    Currency(name="Som", code="KGS", numeric_code="417", minor_units=2),
    Currency(name="Lao Kip", code="LAK", numeric_code="418", minor_units=2),
    Currency(name="Lebanese Pound", code="LBP", numeric_code="422", minor_units=2),
    Currency(name="Loti", code="LSL", numeric_code="426", minor_units=2),
    Currency(name="Rand", code="ZAR", numeric_code="710", minor_units=2),
    Currency(name="Liberian Dollar", code="LRD", numeric_code="430", minor_units=2),
    Currency(name="Libyan Dinar", code="LYD", numeric_code="434", minor_units=3),
    Currency(name="Swiss Franc", code="CHF", numeric_code="756", minor_units=2),
    Currency(name="Pataca", code="MOP", numeric_code="446", minor_units=2),
    Currency(name="Denar", code="MKD", numeric_code="807", minor_units=2),
    Currency(name="Malaysian Ringgit", code="MYR", numeric_code="458", minor_units=2),
    Currency(name="Rufiyaa", code="MVR", numeric_code="462", minor_units=2),
    Currency(name="Mauritius Rupee", code="MUR", numeric_code="480", minor_units=2),
    Currency(name="Mexican Peso", code="MXN", numeric_code="484", minor_units=2),
    Currency(name="Moldovan Leu", code="MDL", numeric_code="498", minor_units=2),
    Currency(name="Tugrik", code="MNT", numeric_code="496", minor_units=2),
    Currency(name="Moroccan Dirham", code="MAD", numeric_code="504", minor_units=2),
    Currency(name="Mozambique Metical", code="MZN", numeric_code="943", minor_units=2),
    Currency(name="Kyat", code="MMK", numeric_code="104", minor_units=2),
    Currency(name="Namibia Dollar", code="NAD", numeric_code="516", minor_units=2),
    Currency(name="Nepalese Rupee", code="NPR", numeric_code="524", minor_units=2),
    Currency(name="Rial Omani", code="OMR", numeric_code="512", minor_units=3),
    Currency(name="Pakistan Rupee", code="PKR", numeric_code="586", minor_units=2),
    Currency(name="Philippine Peso", code="PHP", numeric_code="608", minor_units=2),
    Currency(name="Zloty", code="PLN", numeric_code="985", minor_units=2),
    Currency(name="Qatari Rial", code="QAR", numeric_code="634", minor_units=2),
    Currency(name="Romanian Leu", code="RON", numeric_code="946", minor_units=2),
    Currency(name="Russian Ruble", code="RUB", numeric_code="643", minor_units=2),
    Currency(name="Rwanda Franc", code="RWF", numeric_code="646", minor_units=0),
    Currency(name="Saint Helena Pound", code="SHP", numeric_code="654", minor_units=2),
    Currency(name="Saudi Riyal", code="SAR", numeric_code="682", minor_units=2),
    Currency(name="Serbian Dinar", code="RSD", numeric_code="941", minor_units=2),
    Currency(name="Seychelles Rupee", code="SCR", numeric_code="690", minor_units=2),
    Currency(name="Leone", code="SLL", numeric_code="694", minor_units=2),
    Currency(name="Leone", code="SLE", numeric_code="925", minor_units=2),
    Currency(name="Singapore Dollar", code="SGD", numeric_code="702", minor_units=2),
    Currency(name="Solomon Islands Dollar", code="SBD", numeric_code="090", minor_units=2),
    Currency(name="Somali Shilling", code="SOS", numeric_code="706", minor_units=2),
    Currency(name="South Sudanese Pound", code="SSP", numeric_code="728", minor_units=2),
    Currency(name="Sri Lanka Rupee", code="LKR", numeric_code="144", minor_units=2),
    Currency(name="Sudanese Pound", code="SDG", numeric_code="938", minor_units=2),
    Currency(name="Surinam Dollar", code="SRD", numeric_code="968", minor_units=2),
    Currency(name="Swedish Krona", code="SEK", numeric_code="752", minor_units=2),
    Currency(name="Syrian Pound", code="SYP", numeric_code="760", minor_units=2),
    Currency(name="New Taiwan Dollar", code="TWD", numeric_code="901", minor_units=2),
    Currency(name="Somoni", code="TJS", numeric_code="972", minor_units=2),
    Currency(name="Tanzanian Shilling", code="TZS", numeric_code="834", minor_units=2),
    Currency(name="Baht", code="THB", numeric_code="764", minor_units=2),
    Currency(name="Trinidad and Tobago Dollar", code="TTD", numeric_code="780", minor_units=2),
    Currency(name="Tunisian Dinar", code="TND", numeric_code="788", minor_units=3),
    Currency(name="Turkish Lira", code="TRY", numeric_code="949", minor_units=2),
    Currency(name="Turkmenistan New Manat", code="TMT", numeric_code="934", minor_units=2),
    Currency(name="Uganda Shilling", code="UGX", numeric_code="800", minor_units=0),
    Currency(name="Hryvnia", code="UAH", numeric_code="980", minor_units=2),
    Currency(name="UAE Dirham", code="AED", numeric_code="784", minor_units=2),
    Currency(name="Uzbekistan Sum", code="UZS", numeric_code="860", minor_units=2),
    Currency(name="Bolívar Soberano", code="VES", numeric_code="928", minor_units=2),
    Currency(name="Bolívar Soberano", code="VED", numeric_code="926", minor_units=2),
    Currency(name="Yemeni Rial", code="YER", numeric_code="886", minor_units=2),
    Currency(name="Zambian Kwacha", code="ZMW", numeric_code="967", minor_units=2),
    Currency(name="Zimbabwe Dollar", code="ZWL", numeric_code="932", minor_units=2),
    Currency(name="Dong", code="VND", numeric_code="704", minor_units=0),
    Currency(name="Naira", code="NGN", numeric_code="566", minor_units=2),
    Currency(name="Vatu", code="VUV", numeric_code="548", minor_units=0),
    Currency(name="Balboa", code="PAB", numeric_code="590", minor_units=2),
    Currency(name="Kina", code="PGK", numeric_code="598", minor_units=2),
    Currency(name="Guarani", code="PYG", numeric_code="600", minor_units=0),
    Currency(name="Sol", code="PEN", numeric_code="604", minor_units=2),
    Currency(name="Tala", code="WST", numeric_code="882", minor_units=2),
    Currency(name="Dobra", code="STN", numeric_code="930", minor_units=2),
    Currency(name="Malagasy Ariary", code="MGA", numeric_code="969", minor_units=2),
    Currency(name="Malawi Kwacha", code="MWK", numeric_code="454", minor_units=2),
    Currency(name="Ouguiya", code="MRU", numeric_code="929", minor_units=2),
    Currency(name="Peso Uruguayo", code="UYU", numeric_code="858", minor_units=2),
    Currency(name="Pa'anga", code="TOP", numeric_code="776", minor_units=2),
    Currency(name="Nicaraguan Córdoba", code="NIO", numeric_code="558", minor_units=2),
    Currency(name="Peso Convertible", code="CUC", numeric_code="931", minor_units=2),
    Currency(name="Convertible Mark", code="BAM", numeric_code="977", minor_units=2),
]
