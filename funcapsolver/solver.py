import speech_recognition as sr
import requests, random, string, time, os


# funcap solver
# github/acierp
# fixed by github/accusables

class funcapsolver():
	def get_token(host, pkey, proxy=None):
		if proxy == None:
			return requests.post(f'https://client-api.arkoselabs.com/fc/gt2/public_key/{pkey}', data={'bda': '','public_key': pkey,'site': host,'userbrowser': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36','rnd': f'0.{random.choice("12334565789")}'}).json()['token']
		else:
			return requests.post(f'https://client-api.arkoselabs.com/fc/gt2/public_key/{pkey}', proxies={'all://': proxy}, data={'bda': '','public_key': pkey,'site': host,'userbrowser': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36','rnd': f'0.{random.choice("12334565789")}'}).json()['token']

	def recognizeAudio(audiofilename):
		r = sr.Recognizer()
		with sr.WavFile(audiofilename) as s:
			audio = r.record(s)
			response = r.recognize(audio)
			return response

	def solveCaptcha(token, proxy=None):
		session_token = token.split('|')[0]
		if proxy == None:
			getcaptchaAudio = requests.get(f'https://client-api.arkoselabs.com/fc/get_audio/?session_token={session_token}&analytics_tier=40&r=us-east-1&game=1&language=en')
		else:
			getcaptchaAudio = requests.get(f'https://client-api.arkoselabs.com/fc/get_audio/?session_token={session_token}&analytics_tier=40&r=us-east-1&game=1&language=en', proxies={"all://": proxy})
		audiornd = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7)) 
		open(rf"{os.getcwd()}\audios\captcha" + '.wav', 'wb+').write(getcaptchaAudio.content)

		attemptSolve = requests.post('https://client-api.arkoselabs.com/fc/audio/', proxies=proxy,
		headers = {
			'authority': 'client-api.arkoselabs.com',
			'accept': '*/*',
			'cache-control': 'no-cache',
			'x-newrelic-timestamp': str(round(time.time())),
			'x-requested-with': 'XMLHttpRequest',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://client-api.arkoselabs.com',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'cors',
			'sec-fetch-dest': 'empty',
			'accept-language': 'en-US,en;q=0.9'
		},
		data = {
			'session_token': session_token,
			'language': 'en',
			'r': 'us-east-1',
			'audio_type': '2',
			'response': funcapsolver.recognizeAudio(rf"{os.getcwd()}\audios\captcha.wav"),
			'analytics_tier': '40'
		})
		
		# success = f'{Fore.GREEN}[captcha solved] {token}'
		if attemptSolve.json()['response'] == 'correct':
			return token
		else:
			return 'Captcha Failed Keep Trying!'

