#!/usr/bin/env python3

import json
import requests

model = "hyppchoipus"
server = "http://0.0.0.0:11434/api/chat"


def chat(messages, model=model, server=server):
    """
    Chat with the model using the given messages.

    Parameters:
        - messages (list): The list of messages to send to the model.
        - model (str): The model to chat with. Default is "hyppchoipus".
        - server (str): The URL of the server. Default is
         "http://0.0.0.0:11434/api/chat".

    Returns:
        dict: The response from the model.
    """

    if not isinstance(messages, list) or not messages:
        raise ValueError("chat: messages must be a list")
    if not isinstance(model, str) or model == "":
        raise ValueError("chat: model must be a non-empty string")
    if not isinstance(server, str) or server == "":
        raise ValueError("chat: server must be a non-empty string")

    try:
        r = requests.post(
                        server,
                        json={
                            "model": model,
                            "messages": messages,
                            "stream": True},
                        stream=True
                        )
        r.raise_for_status()
    except Exception as e:
        print(e)
        return

    output = ""
    for line in r.iter_lines():
        body = json.loads(line)
        if "error" in body:
            raise Exception(body["error"])
        if body.get("done") is False:
            message = body.get("message", "")
            content = message.get("content", "")
            output += content
            print(content, end="", flush=True)

        if body.get("done", False):
            message["content"] = output
            return message


if __name__ == "__main__":
    print(chat([], model, server))
