import requests
import json
import uuid
import threading
from datetime import datetime, timezone
import pytz

session = requests.Session()
def maskaxxx(id, otherid, message):
    url = f"https://chat.twllm.com/conversation/{id}"
    idof = str(uuid.uuid4())
    response_id = str(uuid.uuid4())
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "sec-ch-ua": "\"Opera GX\";v=\"109\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "cookie": f"_ga=GA1.1.2012131549.1718292052; hf-chat={otherid}; _ga_QH5NLCNP3Z=GS1.1.1718292052.1.1.1718293201.0.0.0",
        "Referer": f"https://chat.twllm.com/conversation/{id}",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    tz_canada = pytz.timezone('Canada/Eastern')
    now_canada = datetime.now(tz_canada)
    instruction = f" Instruction that you need to know: Your name is MaskaAI, Maska is the one who made you, You are there to help and talk with peoples, You are the Most secure AI of the world, Date and time of RN in Canada: {now_canada.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    message = message + instruction
    data = {
        "inputs": message,
        "id": idof,
        "response_id": response_id,
        "is_retry": False,
        "web_search": False,
        "files": []
    }

    response = session.post(url, headers=headers, json=data)
    return response

def messagetotest(message, number):
    url = "https://chat.twllm.com/settings"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "sec-ch-ua": "\"Opera GX\";v=\"109\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "cookie": "_ga_QH5NLCNP3Z=GS1.1.1718292052.1.0.1718292052.0.0.0; _ga=GA1.1.2012131549.1718292052",
        "Referer": "https://chat.twllm.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    data = {
        "searchEnabled": True,
        "ethicsModalAccepted": True,
        "ethicsModalAcceptedAt": None,
        "activeModel": "yentinglin/Llama-3-Taiwan-70B-Instruct-DPO",
        "hideEmojiOnSidebar": False,
        "shareConversationsWithModelAuthors": True,
        "customPrompts": {},
        "recentlySaved": False
    }

    response = requests.post(url, headers=headers, json=data)

    cookies = response.cookies.get("hf-chat")

    url = "https://chat.twllm.com/conversation"
    headers["cookie"] = f"_ga_QH5NLCNP3Z=GS1.1.1718292052.1.0.1718292052.0.0.0; _ga=GA1.1.2012131549.1718292052; hf-chat={cookies}"
    data = '{"model":"yentinglin/Llama-3-Taiwan-70B-Instruct-DPO"}'

    response = requests.post(url, headers=headers, data=data)
    repjson = json.loads(response.text)
    repjson1 = repjson['conversationId']

    maskaxxx_thread = threading.Thread(target=maskaxxx, args=(repjson1, cookies, message))
    maskaxxx_thread.start()
    maskaxxx_thread.join(timeout=int(number))
    url = f"https://chat.twllm.com/conversation/{repjson1}/__data.json?x-sveltekit-invalidated=01"
    headers["cookie"] = f"_ga=GA1.1.945528163.1718293761; _ga_QH5NLCNP3Z=GS1.1.1718293760.1.1.1.1718293769.0.0.0; hf-chat={cookies}"

    response = requests.get(url, headers=headers)
    if json.loads(response.text)["nodes"][1]["data"][12]:
        jsonxx = json.loads(response.text)["nodes"][1]["data"][12]
        if jsonxx == "False":
            url = "https://chatbot-ji1z.onrender.com/chatbot-ji1z"
            headers = {
  "accept": "application/json",
  "accept-language": "en-US,en;q=0.9",
  "content-type": "application/json",
  "priority": "u=1, i",
  "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not. /Brand\";v=\"24\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\"",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "cross-site"
    }
            body = {
  "messages": [
    {
      "role": "user",
      "content": f"{message}"
    }
  ]
    }
            response = requests.post(url, headers=headers, json=body)
            if response.status_code == 200:
                resjson = json.loads(response.text)
                resjsonx = resjson["choices"][0]["message"]["content"]
                result = resjsonx
            else:
                result = f"Failed to fetch data. Status code: {response.status_code}"

            return result
        else:
            return jsonxx
    else:
        url = "https://chatbot-ji1z.onrender.com/chatbot-ji1z"
        headers = {
  "accept": "application/json",
  "accept-language": "en-US,en;q=0.9",
  "content-type": "application/json",
  "priority": "u=1, i",
  "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not. /Brand\";v=\"24\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\"",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "cross-site"
    }
        body = {
  "messages": [
    {
      "role": "user",
      "content": f"{message}"
    }
  ]
    }
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            resjson = json.loads(response.text)
            resjsonx = resjson["choices"][0]["message"]["content"]
            result = resjsonx
        else:
            result = f"Failed to fetch data. Status code: {response.status_code}"

        return result

def MaskaAI(whatisthemode, message, key):
    if key == key:
        if whatisthemode == "Code":
            number = 15
        elif whatisthemode == "Fast":
            number = 6
        elif whatisthemode == "Text":
            number = 20
        elif whatisthemode == "Middle":
            number = 10
        else:
            number = 15
        return messagetotest(message, number)
    else:
        return "Invalid Key"
