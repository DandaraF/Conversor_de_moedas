import requests
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
from tabulate import tabulate


def _get_currency():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    return requests.get(url).json()


def calculate_to_convert(value, currency_quote):
    return round(value * float(currency_quote), 2)


def get_value_to_be_converted(symbol_coin):
    return float(
        input(f'Digite o valor que deseja converter:{symbol_coin} '))


def show_conversion_result(name, symbol, value, result):
    datas = [[name, f'{symbol} {value}', 'Real Brasileiro', f'R$ {result}']]
    headers = ['Conversão de:', 'Valor a converter:', 'Para:',
               'Resultado da conversão:']
    print('\n')
    print(tabulate(datas, headers=headers, tablefmt="psql",
                   stralign="center"))


def construct_function(symbol_coin, currency_unit_value, name_coin):
    value = get_value_to_be_converted(symbol_coin)
    conversion_value = calculate_to_convert(value,
                                            currency_unit_value)
    show_conversion_result(name_coin, symbol_coin, value,
                           conversion_value)


def get_information_coin(initials, symbol, name):
    construct_function(symbol, _get_currency()[initials]['bid'], name)


def main():
    menu = ConsoleMenu(clear_screen=False, title='CONVERSOR DE MOEDA',
                       subtitle="Selecione a moeda abaixo que gostaria"
                                " de converter para Real.",
                       exit_option_text="SAIR", )

    options = [

        FunctionItem('USD (Dolar Americano)',
                     get_information_coin,
                     args=('USDBRL', 'US$', 'Dolar Americano')),
        FunctionItem('EUR (Euro)', get_information_coin,
                     args=('EURBRL', '€', 'Euro')),
        FunctionItem('BTC (Bitcoin)', get_information_coin,
                     args=('BTCBRL', '₿', 'Bitcoin')),
    ]

    for option in options:
        menu.append_item(option)

    menu.show()


if __name__ == '__main__':
    main()
