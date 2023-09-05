import pprint
# extract data from the email first
from ex_dt import *
# email checker and report generator
from check import *

# create required folders
from create_folders import *

import os
import shutil

# ---------{ LET'S CHECK OUR EMAIL }---------
def get_result(f_name):
    obj_ex_dt = ex_dt(f_name)
    obj_check = check(f_name)

    header_repo, header_res = obj_check.check_header(obj_ex_dt.get_header())
    word_res = obj_check.check_word(obj_ex_dt.get_words())
    url_res = ("No URLs Found 'or' All Not Working ", "No URLs Found 'or' All Not Working ") if len(obj_ex_dt.get_urls()) == 0 else obj_check.check_urls(obj_ex_dt.get_urls())
    #attachment_result, attachment_spam = obj_check.check_attachment() if len(obj_ex_dt.get_attachments()) != 0 else ['no attachment found in the email'], ['no attachment found in the email']

    if len(obj_ex_dt.get_attachments()) != 0:
        attachment_result, attachment_spam = obj_check.check_attachment()
    else:
        attachment_result, attachment_spam = ['no attachment found in the email'], ['no attachment found in the email']

    return {
        "header": {
            "json": header_repo,
            "flag": header_res
        },
        "word": {
            "flag": word_res
        },
        "url": {
            "json": url_res[0],
            "flag": url_res[1],
        },
        "attachments": {
            "json": attachment_result, 
            "flag": attachment_spam
        }
    }


create_samples_dir()
create_temp_folder()
create_benign_dir()
create_quarantine_folder()

# paths for created folders
g_path = os.getcwd()
b_path = os.path.join(g_path,'benign')
q_path = os.path.join(g_path, 'quarantine')

spam_f_path = os.path.join(os.getcwd() + "\samples")

"""

    this part of the code will be modified to make the user upload the file by himself
    using the upload button in GUI

    " until now this is a temp part of code ... "

"""
if len(os.listdir(spam_f_path)) == 0:
    print("No Files to Analysis...")
else:
    for f_name in os.listdir(spam_f_path):
        temp_path = os.path.join(g_path,'temp',f_name)
        f_name_path = os.path.join(spam_f_path, f_name)
        res = get_result(f_name_path)

        # move the analyzed file to its temp folder
        shutil.move(f_name_path,temp_path)

        """

        We are seeking (in this section) to also move the report 
        for each analyzed file to new destination in the benign folder "if the analyzed file is benign" or
        in the quarantine folder "if the analyzed file is spam or malicious" 
        
        """

        if res['header']['flag'] == 'spam' or res['url']['flag'] == 'phishing' or res['attachments']['flag'][0] != 'not spam' :
            shutil.move(temp_path, q_path) # move the file's temp folder to quarantine folder
        else:
            shutil.move(temp_path, b_path) # move the file's temp folder to benign folder
        
        print("header:", res['header']['flag'], " | word:", res['word']['flag'], " | url:", res['url']['flag'], " | attachment:", res['attachments']['flag'])


"""
res = get_result("spam/00116.29e39a0064e2714681726ac28ff3fdef")
print("header:", res['header']['flag'], " | word:", res['word']['flag'], " | url:", res['url']['flag'], " | attachment:", res['attachments']['flag'])
"""
