import os
import re # for regex stuff
from bs4 import BeautifulSoup # decode html
import email

class ex_dt:
    def __init__(self, file_n):
        # check if it's email format or not
        # if not file_n.endswith('.eml'):
        #     raise ValueError('File must be in .eml format')
        
        self.file_n = file_n
        self.eml_dt = open(self.file_n, "r", encoding='utf-8', errors='replace').read()

    def get_header(self):
        # get the headers
        headers = self.eml_dt.split("\n\n")[0]
        return headers

    def get_words(self):
        # we already have words :)
        # DONE -> words = eml_dt
        return self.eml_dt
    """
    def get_urls(self):
        urls = []

        with open(self.file_n, 'r') as eml_file:
            eml_message = email.message_from_file(eml_file)

            # Extract URLs from text part
            text_part = eml_message.get_payload()
            if isinstance(text_part, str):
                urls += re.findall(r'(https?://\S+)', text_part)

            # Extract URLs from HTML part
            html_part = None
            for part in eml_message.walk():
                if part.get_content_type() == 'text/html':
                    html_part = part.get_payload(decode=True).decode('ISO-8859-1')
                    break
            if html_part:
                soup = BeautifulSoup(html_part, 'html.parser')
                for link in soup.find_all('a'):
                    url = link.get('href')
                    if url:
                        urls.append(url)

        return urls
    """

    def get_urls(self):
        with open(self.file_n, 'r', encoding='utf-8', errors='replace') as eml_file:
            text_part = eml_file.read()

        if isinstance(text_part, str):
            #urls += re.findall(r'(https?://\S+)', text_part)
            urls =  re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text_part)

        return urls
             

    def get_attachments(self):
        name = self.file_n.split("\\")[-1]
        file_dir = os.path.join(os.getcwd() ,'temp'+"\\" + name)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        msg = email.message_from_string(self.eml_dt)
        attachments = []

        for part in msg.walk():
            if part.get_content_disposition() == 'attachment':
                filename = part.get_filename()
                if filename:
                    file_path = os.path.join(file_dir, filename)
                    with open(file_path, 'wb') as f:
                        f.write(part.get_payload(decode=True))
                    attachments.append(file_path)
        
        #if len(attachments) == 0:
        #    os.rmdir(file_dir)

        return attachments
