import speech_recognition as sr
import requests, random, time, os

class funcapsolver:
    def token(host, pkey):
            return requests.post(
                f"https://client-api.arkoselabs.com/fc/gt2/public_key/{pkey}",
                data={
                    "bda": "",
                    "public_key": pkey,
                    "site": host,
                    "userbrowser": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
                    "rnd": f'0.{random.choice("12334565789")}',
                },
            ).json()["token"]
        

    def recog(audiofilename):
        r = sr.Recognizer()
        with sr.AudioFile(audiofilename) as s:
            r.adjust_for_ambient_noise(s)
            audio = r.record(s)
            response = r.recognize_google(audio, language="en")
            return response

    def solvecap(token):
        session_token = token.split("|")[0]
        getcaptchaAudio = requests.get(
                f"https://client-api.arkoselabs.com/fc/get_audio/?session_token={session_token}&analytics_tier=40&r=us-east-1&game=1&language=en"
            )
        
        open(rf"{os.getcwd()}\audios\captcha" + ".wav", "wb+").write(
            getcaptchaAudio.content
        )

        solve_res = requests.post(
            "https://client-api.arkoselabs.com/fc/audio/",
            headers={
                "authority": "client-api.arkoselabs.com",
                "accept": "*/*",
                "cache-control": "no-cache",
                "x-newrelic-timestamp": str(round(time.time())),
                "x-requested-with": "XMLHttpRequest",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://client-api.arkoselabs.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "accept-language": "en-US,en;q=0.9",
            },
            data = {
                "session_token": session_token,
                "language": "en",
                "r": "us-east-1",
                "audio_type": "2",
                "response": funcapsolver.recog(
                    rf"{os.getcwd()}\audios\captcha.wav"
                ),
                "analytics_tier": "40",
            },
        )

        # success = f'{Fore.GREEN}[captcha solved] {token}'
        if solve_res.json()["response"] == "correct":
            return token
        else:
            return "Captcha Failed Keep Trying!"
