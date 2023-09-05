import json
import os
# import word checker functions
from wordscanner.word_main import *
# import header checker functions
import subprocess
# import urls checker functions
from urlScanner.Test_model import *
import warnings
warnings.filterwarnings('ignore')
# import attachment checker functions
from attachmentScanner.analyze_attachment import *

class check:
    def __init__(self, f_name):
        self.f_name = f_name

    def check_header(self, headers):
        h_path = os.path.join(os.getcwd() + "\headerScanner", "heads.txt")
        with open(h_path, "w") as h:
            h.write(headers)

        directory = os.path.join(os.getcwd() + "\headerScanner")
        file_path = os.path.join(directory, "decode_spam_headers.py")
        subprocess.run(["python", file_path], cwd=directory)

        output_path = os.path.join(os.getcwd() + "\headerScanner", "output.json")
        f = open(output_path, "rb")
        output_json = json.load(f)
        header_spam = "spam" if "WARNING!" in json.dumps(output_json) else "not spam"

        h.close()
        os.remove(h_path)

        f.close()
        os.remove(output_path)

        return output_json, header_spam

    def check_word(self, words):
        word_checks_obj = WORDS(words)
        word_checks_obj_result = word_checks_obj.check_word()
        return word_checks_obj_result
    
    def check_urls(self, urls):
        return Test_model_analysis(urls)

    def check_attachment(self):
        name = self.f_name.split("\\")[-1]
        attachment_result, attachment_spam = [], []
        attachments_path = os.path.join(os.getcwd() , "temp" , name)
        for f_name in os.listdir(attachments_path):
            if not f_name.endswith(".py") and f_name != "__pycache__":
                f_path = os.path.join(os.getcwd() + "\\attachmentScanner" + "\\" + name, f_name)
                attachments_analyzer_obj = analyze_attachments(f_path)
                temp_res, temp_spam = attachments_analyzer_obj.results()
                
                attachment_result.append(temp_res)
                attachment_spam.append(temp_spam)
        
        return attachment_result, attachment_spam
