import requests
from colorama import Fore, init
import os
import time
import asyncio
import aiohttp
import random
from datetime import datetime, timedelta
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)

def format_time(seconds):
    if seconds == float('inf'):
        return "Unknown"
    return str(timedelta(seconds=int(seconds)))

class RateLimiter:
    def __init__(self):
        self.reset_time = time.time()
        self.success_count = 0
        self.fail_count = 0
        self.delay = 0.1
        self.last_success = time.time()
        self.consecutive_fails = 0

    async def should_send(self):
    
        success_ratio = self.success_count / (self.success_count + self.fail_count + 1)
        if success_ratio < 0.5:
            self.delay = min(2.0, self.delay * 1.2)
        elif success_ratio > 0.8:
            self.delay = max(0.1, self.delay * 0.8)
        
        await asyncio.sleep(self.delay)
        return True

    def update_stats(self, success):
        if success:
            self.success_count += 1
            self.consecutive_fails = 0
            self.last_success = time.time()
        else:
            self.fail_count += 1
            self.consecutive_fails += 1

class MessageQueue:
    def __init__(self, total_messages):
        self.queue = asyncio.Queue()
        self.failed_queue = asyncio.Queue()
        self.total = total_messages
        self.sent = 0
        self.retries = 0
        self.start_time = time.time()

    async def add_failed(self, message_id):
        await self.failed_queue.put(message_id)
        self.retries += 1

    def get_stats(self):
        elapsed = time.time() - self.start_time
        rate = self.sent / elapsed if elapsed > 0 else 0
        remaining = self.total - self.sent
        eta = remaining / rate if rate > 0 else float('inf')
        return rate, eta, remaining

def extract_webhooks(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"{Fore.RED}[!] File not found: {file_path}")
            return []
        
        with open(file_path, 'r') as file:
            for _ in range(2):
                next(file)
    
            webhooks = [line.strip() for line in file if line.strip()]
        return webhooks
    except Exception as e:
        print(f"{Fore.RED}[!] Error reading webhooks file: {e}")
        return []

def display_webhooks(webhooks):
    print(f"\n{Fore.GREEN}Available Webhooks:")
    for i, webhook in enumerate(webhooks, 1):
        short_webhook = webhook[:50] + "..." if len(webhook) > 50 else webhook
        print(f"{Fore.RED}[{Fore.MAGENTA}{i}{Fore.RED}] -> {Fore.GREEN}URL: {Fore.RED}{short_webhook}{Fore.RESET}")

async def send_message(session, webhook, message, message_id, queue, rate_limiter):
    try:
        await rate_limiter.should_send()
        
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        async with session.post(webhook, json={"content": message}, headers=headers, timeout=5) as response:
            if response.status == 429:
                retry_after = float(response.headers.get('Retry-After', 1))
                rate_limiter.update_stats(False)
                print(f"{Fore.RED}[!] {Fore.GREEN}Rate Limited : {Fore.RED}Message queued ({retry_after:.1f}s){Fore.RESET}")
                await queue.add_failed(message_id)
                return False

            elif response.status == 204:
                rate_limiter.update_stats(True)
                queue.sent += 1
                print(f"{Fore.RED}[+] {Fore.GREEN}Success      : {Fore.RED}Message sent{Fore.RESET}")
                return True

            else:
                rate_limiter.update_stats(False)
                print(f"{Fore.RED}[!] {Fore.GREEN}Failed       : {Fore.RED}Status {response.status}{Fore.RESET}")
                if response.status != 404:
                    await queue.add_failed(message_id)
                return False

    except Exception as e:
        print(f"{Fore.RED}[!] {Fore.GREEN}Error        : {Fore.RED}{str(e)}{Fore.RESET}")
        await queue.add_failed(message_id)
        return False

async def spam_webhook(webhook, message, count):
    connector = aiohttp.TCPConnector(limit=None, ttl_dns_cache=300)
    timeout = aiohttp.ClientTimeout(total=30)
    rate_limiter = RateLimiter()
    queue = MessageQueue(count)
    
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        message_ids = list(range(count))
        chunk_size = 4 
        
        while message_ids or not queue.failed_queue.empty():
            current_chunk = []
            
            
            while len(current_chunk) < chunk_size:
                if message_ids:
                    current_chunk.append(message_ids.pop(0))
                elif not queue.failed_queue.empty():
                    failed_id = await queue.failed_queue.get()
                    current_chunk.append(failed_id)
                else:
                    break
            
            if not current_chunk:
                break
                
            tasks = [
                asyncio.create_task(
                    send_message(session, webhook, message, msg_id, queue, rate_limiter)
                )
                for msg_id in current_chunk
            ]
            
            await asyncio.gather(*tasks)
            
            rate, eta, remaining = queue.get_stats()
            print(f"{Fore.YELLOW}Progress: {queue.sent}/{count} sent ({rate:.1f} msg/s | ETA: {format_time(eta)})")
            
        
            await asyncio.sleep(0.5)
            
        return queue.sent

async def main():
    webhooks_file_path = "input/discord-webhooks.txt"
    webhooks = extract_webhooks(webhooks_file_path)
    
    if not webhooks:
        print(f"{Fore.RED}[!] No webhooks found in /input/discord-webhooks.txt")
        return
    
    display_webhooks(webhooks)
    print(f"\n{Fore.YELLOW}Select webhook or type 'A' to use all...")
    choice = input(f"{Fore.RED}[+] {Fore.GREEN}Webhook >> {Fore.RED}").strip()
    
    if choice.lower() == 'a':
        selected_webhooks = webhooks
    elif choice.isdigit() and 1 <= int(choice) <= len(webhooks):
        selected_webhooks = [webhooks[int(choice) - 1]]
    else:
        print(f"{Fore.RED}[!] Invalid choice. Exiting...")
        return
    
    message = input(f"{Fore.RED}[+] {Fore.GREEN}Message >> {Fore.RED}").strip()
    count = input(f"{Fore.RED}[+] {Fore.GREEN}Count >> {Fore.RED}").strip()
    
    try:
        count = int(count)
        if count < 1:
            raise ValueError
    except ValueError:
        print(f"{Fore.RED}[!] Invalid count. Exiting...")
        return
    
    print(f"\n{Fore.YELLOW}Starting...")
    total_start_time = time.time()
    total_sent = 0
    
    try:
        for webhook in selected_webhooks:
            sent = await spam_webhook(webhook, message, count)
            total_sent += sent
            
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Operation interrupted by user")
    except Exception as e:
        print(f"\n{Fore.RED}[!] An error occurred: {str(e)}")
    finally:
        total_time = time.time() - total_start_time
        rate = total_sent / total_time if total_time > 0 else 0
        
        print(f"\n{Fore.RED}[+] {Fore.GREEN}Final Summary:")
        print(f"{Fore.RED}[+] {Fore.GREEN}Total Sent    : {Fore.RED}{total_sent}")
        print(f"{Fore.RED}[+] {Fore.GREEN}Time Elapsed  : {Fore.RED}{format_time(total_time)}")
        print(f"{Fore.RED}[+] {Fore.GREEN}Average Rate  : {Fore.RED}{rate:.1f} msg/s")
        print(f"{Fore.RED}[+] {Fore.GREEN}Webhooks Used : {Fore.RED}{len(selected_webhooks)}")

def run():
    asyncio.run(main())
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()