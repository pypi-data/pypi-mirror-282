#!/usr/bin/env python3
"""
Chatbot script to interact with OpenAI's API from the terminal.
"""

import os
import logging
import argparse
import sys

from openai import OpenAI
from chat import Chatbot, Speaker

logging.basicConfig(encoding="utf-8", format="%(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)
logging.getLogger("httpx").setLevel(logging.WARNING)

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    logger.error("OPENAI_API_KEY environment variable not set.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(prog="chat", description="Chat from the comfort of your terminal")
    parser.add_argument("-s", "--system", type=str, help="Set the system message for the chatbot.")
    parser.add_argument("-m", "--messages", nargs="+", type=str, help="Write a message for the chatbot.")
    parser.add_argument("-c", "--conversation", action="store_true", help="Flag for conversation mode.")
    parser.add_argument("--save-audio", type=str, help="Path to save the audio response.")
    parser.add_argument("--model", type=str, help="Specify the model to use.")
    parser.add_argument("--available-models-gpt", action='store_true', help="List available ChatGPT models.")
    parser.add_argument("--available-models", action='store_true', help="List available OpenAI models.")
    parser.add_argument("-t", "--temperature", type=float, help="Set the temperature for the model.")
    return parser.parse_args()

def main():
    args = parse_arguments()
    chatbot = Chatbot(".chatconfig.json", client)

    if args.available_models:
        print(chatbot.get_openai_model_list())
        sys.exit(0)
    if args.available_models_gpt:
        print(chatbot.get_chatgpt_model_list())
        sys.exit(0)

    chatbot.system_message = args.system or chatbot.system_message
    chatbot.model = args.model or chatbot.model
    chatbot.temperature = args.temperature or chatbot.temperature

    if args.messages:
        if args.conversation:
            for message in args.messages:
                chatbot.append_user_message(message)
        else:
            chatbot.user_messages = args.messages
    elif args.conversation:
        chatbot.user_messages = []
        print(
            "New conversation started.\n"
            "Continue chatting with: chat -c -m \"Your message.\"\n"
            "Current settings:\n"
            f"\tmodel: {chatbot.model:<10}\n"
            f"\ttemperature: {chatbot.temperature}\n"
            f"\tsystem message: {chatbot.system_message}"
        )
        sys.exit(0)

    logger.info(
        f"Chat\nModel: {chatbot.model}, Temperature: {chatbot.temperature}\n"
        f"System: {chatbot.system_message}\nMessage: {chatbot.user_messages[-1]}\n"
    )
    content = chatbot.chat(chatbot.system_message, chatbot.user_messages, chatbot.model, chatbot.temperature)

    if args.save_audio:
        Speaker(client).create_audio(text=content, audio_save=True, audio_file_path=args.save_audio)

    if args.conversation:
        chatbot.append_user_message(content)
    else:
        chatbot.user_messages = []

if __name__ == "__main__":
    main()