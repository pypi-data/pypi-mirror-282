import hashlib
import hmac
import json
import time

import requests


class Paycek:
	def __init__(self, api_key: str, api_secret: str):
		self.api_secret = api_secret
		self.api_key = api_key
		self.api_host = 'https://paycek.io'
		self.api_prefix = '/processing/api'
		self.encoding = 'utf-8'

	def _generate_mac_hash(self, nonce_str: str, endpoint: str, body_bytes: bytes, http_method='POST', content_type='application/json'):
		mac = hashlib.sha3_512()
		mac.update(b'\0')
		mac.update(self.api_key.encode(self.encoding))
		mac.update(b'\0')
		mac.update(self.api_secret.encode(self.encoding))
		mac.update(b'\0')
		mac.update(nonce_str.encode(self.encoding))
		mac.update(b'\0')
		mac.update(http_method.encode(self.encoding))
		mac.update(b'\0')
		mac.update(endpoint.encode(self.encoding))
		mac.update(b'\0')
		mac.update(content_type.encode(self.encoding))
		mac.update(b'\0')
		mac.update(body_bytes)
		mac.update(b'\0')

		return mac.hexdigest()

	def _api_call(self, endpoint: str, body: dict):
		prefixed_endpoint = f'{self.api_prefix}/{endpoint}'
		body_bytes = json.dumps(body).encode(self.encoding)
		nonce_str = str(int(time.time() * 1000))

		mac_hash = self._generate_mac_hash(nonce_str, prefixed_endpoint, body_bytes)

		headers = {
			'Content-Type': 'application/json',
			'ApiKeyAuth-Key': self.api_key,
			'ApiKeyAuth-Nonce': nonce_str,
			'ApiKeyAuth-MAC': mac_hash
		}

		r = requests.request(
			method='POST',
			url=f'{self.api_host}{prefixed_endpoint}',
			data=body_bytes,
			headers=headers
		)
		r.encoding = self.encoding

		return r.json()

	def check_headers(self, headers: dict, endpoint: str, body_bytes: bytes, http_method='GET', content_type=''):
		"""
		This method is used to verify callback was encoded by paycek.
		A mac digest will be created by encoding nonce from headers, endpoint, body bytes, your api key and secret, http method and content type.
		That value will be compared with mac digest from headers.

		:param headers: callback headers
		:param endpoint: callback endpoint
		:param body_bytes: callback body bytes
		:param http_method: callback http method
		:param content_type: callback content type
		:return: True if the generated mac digest is equal to the one received in headers, False otherwise
		"""
		try:
			headers_lower = {key.lower(): headers[key] for key in headers}
			generated_mac = self._generate_mac_hash(headers_lower['apikeyauth-nonce'], endpoint, body_bytes, http_method, content_type)

			return hmac.compare_digest(generated_mac, headers_lower['apikeyauth-mac'])
		except:
			return False

	def generate_payment_url(self, profile_code: str, dst_amount: str, **optional_fields):
		"""
		:param optional_fields: Optional fields:
			payment_id: string
			location_id: string
			items: array
			email: string
			success_url: string
			fail_url: string
			back_url: string
			success_url_callback: string
			fail_url_callback: string
			status_url_callback: string
			description: string
			language: string
			generate_pdf: bool
			client_fields: dict
		"""
		payment = self.open_payment(profile_code, dst_amount, **optional_fields)

		try:
			return payment['data']['payment_url']
		except KeyError:
			print(payment)
			raise

	def get_payment(self, payment_code: str):
		body = {
			"payment_code": payment_code
		}

		return self._api_call('payment/get', body)

	def open_payment(self, profile_code: str, dst_amount: str, **optional_fields):
		"""
		You can implement getting payment status in 3 ways:

		1. **Provide** ``status_url_callback`` upon opening a payment and receive status updates on your endpoint.
		2. **Provide** ``success_url_callback`` **and** ``fail_url_callback`` upon opening a payment and receive success and fail updates on your endpoints.
		3. **Manually poll** ``payment/get`` to check payment status.

		**Do not use** ``fail_url`` **and** ``success_url`` **to update payment status in your system. These URLs are used ONLY for redirecting users back to your shop.**

		**Authorization**

		If you decide to use callbacks, you **must check the headers for every callback** to ensure they are authorized.
		If a callback doesn't have a valid Authorization header, your server must respond with a **401 Unauthorized** status. If the callback has a valid Authorization header, your server must respond with a **200 OK** status.

		**Integration Testing**

		In order to ensure system security, on every new payment, an automated integration test will check if your integration is secure.
		An API call with an invalid Authorization header will be made to each of your callback endpoints. If any endpoint returns a status other than 401 for requests with an invalid Authorization header, **all ongoing payments will be canceled**, and your **profile will be blocked** to prevent unauthorized transactions. Ensure your endpoints are correctly configured to handle authorization and respond appropriately.

		*Test profiles won't be blocked even if the response for callbacks with an invalid Authorization header returns an invalid status. The payment will still be canceled.*

		:param profile_code: The profile code for the payment.
		:type profile_code: str
		:param dst_amount: The amount of the payment.
		:type dst_amount: float
		:param optional_fields: Optional fields:
				- payment_id (str)
				- location_id (str)
				- items (list)
				- email (str)
				- success_url (str)
				- fail_url (str)
				- back_url (str)
				- success_url_callback (str)
				- fail_url_callback (str)
				- status_url_callback (str)
				- description (str)
				- language (str)
				- generate_pdf (bool)
				- client_fields (dict)
		:type optional_fields: dict
		"""
		body = {
			"profile_code": profile_code,
			"dst_amount": dst_amount,
			**optional_fields
		}

		return self._api_call('payment/open', body)

	def update_payment(self, payment_code: str, src_currency: str, **optional_fields):
		"""
		:param optional_fields: Optional fields:
			src_protocol: str
		"""
		body = {
			"payment_code": payment_code,
			"src_currency": src_currency,
			**optional_fields
		}

		return self._api_call('payment/update', body)

	def cancel_payment(self, payment_code: str):
		body = {
			"payment_code": payment_code
		}

		return self._api_call('payment/cancel', body)

	def get_profile_info(self, profile_code: str):
		body = {
			"profile_code": profile_code
		}

		return self._api_call('profile_info/get', body)

	def profile_withdraw(self, profile_code: str, method: str, amount: str, details: dict, **optional_fields):
		"""
		:param details: Withdraw details object with fields:
			iban: string (required)
			purpose: string
			model: string
			pnb: string
		:param optional_fields: Optional fields:
			id: string
		"""
		body = {
			"profile_code": profile_code,
			"method": method,
			"amount": amount,
			"details": details,
			**optional_fields
		}

		return self._api_call('profile/withdraw', body)

	def create_account(self, email: str, name: str, street: str, city: str, country: str, profile_currency: str, profile_automatic_withdraw_method: str, profile_automatic_withdraw_details: dict, **optional_fields):
		"""
		:param profile_automatic_withdraw_details: Automatic withdraw details object with fields:
			iban: string (required)
			purpose: string
			model: string
			pnb: string
		:param optional_fields: Optional fields:
			type: string
			oib: string
			vat: string
			profile_name: string
			profile_email: string
			profile_type: string
		"""
		body = {
			"email": email,
			"name": name,
			"street": street,
			"city": city,
			"country": country,
			"profile_currency": profile_currency,
			"profile_automatic_withdraw_method": profile_automatic_withdraw_method,
			"profile_automatic_withdraw_details": profile_automatic_withdraw_details,
			**optional_fields
		}

		return self._api_call('account/create', body)

	def create_account_with_password(self, email: str, password: str, name: str, street: str, city: str, country: str, profile_currency: str, profile_automatic_withdraw_method: str, profile_automatic_withdraw_details: dict, **optional_fields):
		"""
		:param profile_automatic_withdraw_details: Automatic withdraw details object with fields:
			iban: string (required)
			purpose: string
			model: string
			pnb: string
		:param optional_fields: Optional fields:
			type: string
			oib: string
			vat: string
			profile_name: string
			profile_email: string
		"""
		body = {
			"email": email,
			"password": password,
			"name": name,
			"street": street,
			"city": city,
			"country": country,
			"profile_currency": profile_currency,
			"profile_automatic_withdraw_method": profile_automatic_withdraw_method,
			"profile_automatic_withdraw_details": profile_automatic_withdraw_details,
			**optional_fields
		}

		return self._api_call('account/create_with_password', body)

	def get_reports(self, profile_code: str, datetime_from: str, datetime_to: str, **optional_fields):
		"""
		:param optional_fields: Optional fields:
			location_id: string
		"""
		body = {
			"profile_code": profile_code,
			"datetime_from": datetime_from,
			"datetime_to": datetime_to,
			**optional_fields
		}

		return self._api_call('reports/get', body)
