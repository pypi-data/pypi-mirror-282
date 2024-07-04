import requests
from django.conf import settings

CRETA_AUTH_BASE_URL = settings.CRETA_AUTH_BASE_URL


def register_user(email, password, name, is_two_factor, email_verified_at):
    url = f"{CRETA_AUTH_BASE_URL}/credential/register"
    payload = {
        "email": email,
        "password": password,
        "name": name,
        "isTwoFactor": is_two_factor,
        "emailVerifiedAt": email_verified_at
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json(), response.status_code


def login_user(email, password):
    url = f"{CRETA_AUTH_BASE_URL}/credential/login"
    payload = {
        "email": email,
        "password": password,
        "authProvider": "credential"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json(), response.status_code


def reset_password(email, key, password):
    url = f"{CRETA_AUTH_BASE_URL}/credential/reset-password"
    payload = {
        "email": email,
        "key": key,
        "password": password
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json(), response.status_code


def update_password(session_token, old_password, new_password):
    url = f"{CRETA_AUTH_BASE_URL}/credential/update-password"
    payload = {
        "oldPassword": old_password,
        "newPassword": new_password
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {session_token}'
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json(), response.status_code


def send_verification_key(email, call_back_url):
    url = f"{CRETA_AUTH_BASE_URL}/validate/send-verification-key"
    payload = {
        "email": email,
        "callBackUrl": call_back_url
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json(), response.status_code


def verify_key(email, key):
    url = f"{CRETA_AUTH_BASE_URL}/validate/verify-key"
    params = {
        "email": email,
        "key": key
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, params=params, headers=headers)
    return response.json(), response.status_code


def find_existing_user(email):
    url = f"{CRETA_AUTH_BASE_URL}/validate/find-existing-user"
    params = {"email": email}
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, params=params, headers=headers)
    return response.json(), response.status_code


def send_password_reset(email, call_back_url):
    url = f"{CRETA_AUTH_BASE_URL}/validate/send-password-reset"
    payload = {
        "email": email,
        "callBackUrl": call_back_url
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json(), response.status_code


def verify_password_reset(email, key):
    url = f"{CRETA_AUTH_BASE_URL}/validate/verify-password-reset"
    params = {
        "email": email,
        "key": key
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, params=params, headers=headers)
    return response.json(), response.status_code


def validate_session(session_token):
    url = f"{CRETA_AUTH_BASE_URL}/session/validate"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {session_token}'
    }
    response = requests.get(url, headers=headers)
    return response.json(), response.status_code


def refresh_session(refresh_token):
    url = f"{CRETA_AUTH_BASE_URL}/session/refresh"
    payload = {"refreshToken": refresh_token}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json(), response.status_code


def logout_user(session_token):
    url = f"{CRETA_AUTH_BASE_URL}/session/logout"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {session_token}'
    }
    response = requests.post(url, headers=headers)
    return response.json(), response.status_code


def google_oauth_login(origin_url):
    url = f"{CRETA_AUTH_BASE_URL}/oauth/google"
    params = {"originUrl": origin_url}
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, params=params, headers=headers)
    return response.json(), response.status_code


def apple_oauth_login(origin_url):
    url = f"{CRETA_AUTH_BASE_URL}/oauth/apple"
    params = {"originUrl": origin_url}
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, params=params, headers=headers)
    return response.json(), response.status_code


def upsert_oauth_user(provider, provider_user_id, access_token, refresh_token, name, picture_url, email):
    url = f"{CRETA_AUTH_BASE_URL}/oauth/upsertUser"
    payload = {
        "provider": provider,
        "providerUserId": provider_user_id,
        "accessToken": access_token,
        "refreshToken": refresh_token,
        "name": name,
        "pictureUrl": picture_url,
        "email": email
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json(), response.status_code
