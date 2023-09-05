import os
general_path = os.getcwd()
def create_samples_dir():
    sample_path = os.path.join(general_path,'samples')
    exist_samples = os.path.exists(sample_path)
    if not exist_samples:
        os.mkdir(sample_path)
    else:
        pass

def create_benign_dir():
    benign_path = os.path.join(general_path,'benign')
    exist_benign = os.path.exists(benign_path)
    if not exist_benign:
        os.mkdir(benign_path)
    else:
        pass

def create_quarantine_folder():
    qaurantine_path = os.path.join(general_path,'quarantine')
    exist_quarantine = os.path.exists(qaurantine_path)
    if not exist_quarantine:
        os.mkdir(qaurantine_path)
    else:
        pass

def create_temp_folder():
    temp_path = os.path.join(general_path,'temp')
    exist_temp = os.path.exists(temp_path)
    if not exist_temp:
        os.mkdir(temp_path)
    else:
        pass

create_samples_dir()
create_benign_dir()
create_quarantine_folder()
create_temp_folder()