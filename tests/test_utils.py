import requests

def get_rest_call_200(test, url, params = {}, get_header = {}, expected_code = 200):
    response = requests.get(url, params, headers = get_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

def get_rest_call_404(test, url, params = {}, get_header = {}, expected_code = 404):
    response = requests.get(url, params, headers = get_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

def post_rest_call_200(test, url, params = {}, post_header = {},expected_code = 200):
    response = requests.post(url, params, headers = post_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

def post_rest_call_404(test, url, params = {}, post_header = {},expected_code = 404):
    response = requests.post(url, params, headers = post_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

def put_rest_call_200(test, url, params = {}, put_header = {},expected_code = 200):
    response = requests.put(url, params, headers = put_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

def put_rest_call_404(test, url, params = {}, put_header = {},expected_code = 404):
    response = requests.put(url, params, headers = put_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

def delete_rest_call_200(test, url, delete_header={}, expected_code = 200):
    response = requests.delete(url, headers = delete_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

def delete_rest_call_404(test, url, delete_header={}, expected_code = 404):
    response = requests.delete(url, headers = delete_header)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()