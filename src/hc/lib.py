import requests


def get_state():
    resp = requests.get("http://10.1.1.40/?m=1")
    assert resp.status_code == 200
    is_off = "OFF" in resp.text
    is_on = "ON" in resp.text
    assert is_off != is_on
    return is_on


def toggle():
    resp = requests.get("http://10.1.1.40/?m=1&o=1")
    assert resp.status_code == 200


def set_on():
    state = get_state()
    if not state:
        toggle()
        return True
    else:
        return False


def set_off():
    state = get_state()
    if state:
        toggle()
        return True
    else:
        return False
