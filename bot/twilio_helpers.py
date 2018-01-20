def parse_body(body):
    if body == '':
        return {}

    params_list = body.split('&')
    params_tuple = [param.split('=') for param in params_list]
    return {param[0]: param[1] for param in params_tuple}
