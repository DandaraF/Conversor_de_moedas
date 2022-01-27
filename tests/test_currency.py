from unittest.mock import MagicMock, patch, call

from currency_quotes.currency_quotes import \
    _get_currency, calculate_to_convert, construct_function, \
    get_information_coin, get_value_to_be_converted, show_conversion_result, \
    main

patch_root = 'currency_quotes.currency_quotes'


@patch(f'{patch_root}.requests')
def test_get_currency_quotes(mock_request):
    mock_url = MagicMock()

    result = _get_currency()

    assert result == mock_request.get(mock_url).json()


def test_calculate_to_convert():
    result = calculate_to_convert(2.543, 3.345)

    assert result == 8.51


@patch(f'{patch_root}.input', return_value='25.4')
def test_get_value_to_be_converted(mock_input):
    mock_symbol = MagicMock()

    result = get_value_to_be_converted(mock_symbol)

    assert result == 25.4


@patch(f'{patch_root}.print')
@patch(f'{patch_root}.tabulate')
def test_show_conversion_result(mock_tabulate,
                                mock_print):
    mock_name = MagicMock()
    mock_symbol = MagicMock()
    mock_value = MagicMock()
    mock_result = MagicMock()

    show_conversion_result(mock_name, mock_symbol, mock_value, mock_result)

    mock_print.assert_has_calls([
        call('\n'),
        call(mock_tabulate()),
    ])


@patch(f'{patch_root}.show_conversion_result')
@patch(f'{patch_root}.calculate_to_convert')
@patch(f'{patch_root}.get_value_to_be_converted')
def test_construct_function(mock_get_value,
                            mock_calculate,
                            mock_show):
    mock_symbol_coin = MagicMock()
    mock_currency_value = MagicMock()
    mock_name_coin = MagicMock()

    construct_function(mock_symbol_coin, mock_currency_value, mock_name_coin)


@patch(f'{patch_root}.construct_function')
@patch(f'{patch_root}._get_currency')
def test_get_information_coin(mock_currency,
                              mock_construct):
    mock_initials = MagicMock()
    mock_symbol = MagicMock()
    mock_name = MagicMock()

    get_information_coin(mock_initials, mock_symbol, mock_name)


@patch(f'{patch_root}.ConsoleMenu')
@patch(f'{patch_root}.FunctionItem')
def test_main(mock_function,
              mock_console_menu):
    main()
