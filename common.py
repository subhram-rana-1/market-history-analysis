from kiteconnect import KiteConnect


API_KEY = 'p7qy2u03ev8e45pm'
API_SECRETE = '4pamm45xsirewovl8smza5t1qvft0t92'
ACCESS_TOKEN = None


def new_kite_connect_client() -> KiteConnect:
    kc: KiteConnect = KiteConnect(
        api_key=API_KEY,
    )

    print("Please login with here and fetch the 'request_token' from redirected "
          "url after successful login : ", kc.login_url())

    request_token: str = input("enter 'request_token': ")

    session_data: dict = kc.generate_session(
        request_token=request_token,
        api_secret=API_SECRETE,
    )

    ACCESS_TOKEN = session_data['access_token']
    kc.set_access_token(ACCESS_TOKEN)

    print('\nkite connect client creation successful !!! ')

    return kc
