import requests


def forex_rate(base_cur, dest_cur):
    """
    :param base_cur: Первая валюта
    :param dest_cur: Вторая валюта
    :param multiplier: Множитель
    :return: Возвращает курс умноженный на multiplier или apidown

    """
    source_url = "https://api.currencyapi.com/v3/latest"
    if base_cur.lower() == 'usd':
        payload = {'currencies': dest_cur,
                   'apikey': 'cur_live_vR4hSu88qzYLjyoKvFXGx03KQzyZbAJSV4p0fqVK'}
    else:
        payload = {'base_currency': base_cur, 'currencies': dest_cur,
                   'apikey': 'cur_live_vR4hSu88qzYLjyoKvFXGx03KQzyZbAJSV4p0fqVK'}

    response = requests.get(source_url, params=payload)

    return response
