import asyncio
import requests
import json
import time
import uuid
from loguru import logger
import os
import sys

# Script'in bulunduğu dizini belirle
script_dir = os.path.dirname(os.path.abspath(__file__))

# Tek satırlık token'ı dosyaya yazma fonksiyonu
def write_single_line_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

# Tek satırlık token'ı dosyadan okuma fonksiyonu
def read_single_line_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return f.read().strip()
    return None

# Dosyadan yapılandırma değerlerini oku
token_file_path = os.path.join(script_dir, 'token.txt')
NP_TOKEN = read_single_line_file(token_file_path)

# Sabitler
HTTPS_URL = "https://nw2.nodepay.ai/api/network/ping"
RETRY_INTERVAL = 60  # Başarısız proxy'ler için yeniden deneme aralığı (saniye cinsinden)
EXTENSION_VERSION = "2.2.3"

async def call_api_info(token):
    logger.info("UserID alınıyor")
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = f'Bearer {token}'

    response = requests.post(
        "https://api.nodepay.ai/api/auth/session",
        headers=headers,
        json={}
    )
    response.raise_for_status()
    return response.json()

async def send_ping(user_id, token):
    logger.info("Ping gönderiliyor")
    browser_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, user_id))
    logger.info(browser_id)
    while True:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                'Content-Type': 'application/json'
            }
            headers['Authorization'] = f'Bearer {token}'
            payload = {
                "user_id": user_id,
                "browser_id": browser_id,
                "time
