import json
import shutil
import tempfile

class File:
    def __init__(self, enc_key, content):
        self._enc_key = enc_key
        self._content = content.decode()
      
    
    def make_physical(self):
        self._dirpath = tempfile.mkdtemp()
        self._file_name = tempfile.mkstemp(dir=self._dirpath)

        with open(self._file_name, 'wt') as f:
            f.write(self._content)

        return self._file_name


    def add_record(self, site, uname, passwd):
        """Return: updated content"""
        content_list = json.loads(self._content)

        if (content_list == None):
            content_list = []

        content_list.append({
            'site': site,
            'uname': uname,
            'passwd': passwd
            })

        self._content = json.dumps(content_list)

        return self._content


        
    def get_records(self):
        """Return: List of Dictories containing recored"""
        return self._content

    def delete_physical(self):
        shutil.rmtree(self._dirpath)
        return
