import requests


def forex_rate(base_cur, dest_cur, multiplier):
    """
    :param base_cur: Первая валюта
    :param dest_cur: Вторая валюта
    :param multiplier: Множитель
    :return: Возвращает курс умноженный на multiplier или apidown
    Если в value было передано что-то кроме числа, value приравнивается к 1
    Если в запросе к currencyapi.com вернулся не код 200, возвращает json ошибки
    """
    source_url = "https://api.currencyapi.com/v3/latest"
    if base_cur.lower() == 'usd':
        payload = {'currencies': dest_cur,
                   'apikey': 'cur_live_vR4hSu88qzYLjyoKvFXGx03KQzyZbAJSV4p0fqVK'}
    else:
        payload = {'base_currency': base_cur, 'currencies': dest_cur, 'apikey': 'cur_live_vR4hSu88qzYLjyoKvFXGx03KQzyZbAJSV4p0fqVK'}

    response = requests.get(source_url, params=payload)

    if response.status_code == 200:
        rate = response.json().get('data')
        if not rate:
            return 'apidown'
        try:
            return float(rate[dest_cur]['value']) * float(multiplier)
        except ValueError:
            return rate[dest_cur]['value']

    return response.json()