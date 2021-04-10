import json
import shutil
import tempfile

class File:
    def __init__(self, enc_key, content):
        self._enc_key = enc_key
        self._content = content.decode()
      
    def content_to_list(self):
        return json.loads(self._content)

    def update_content(self, records):
        self._content = json.dumps(records)
        return self._content
    
    def make_physical(self):
        self._dirpath = tempfile.mkdtemp()
        self._file_name = tempfile.mkstemp(dir=self._dirpath)

        with open(self._file_name, 'wt') as f:
            f.write(self._content)

        return self._file_name


    def add_record(self, site, uname, passwd):
        """Return: updated content"""
        content_list = self.content_to_list()

        if (content_list == None):
            content_list = []

        content_list.append({
            'site': site,
            'uname': uname,
            'passwd': passwd
            })

        return self.update_content(content_list)


    def delete_record(self, site):
        records = self.content_to_list()

        site_record = self.get_site_record(site)

        records.remove(site_record)

        self.update_content(records)

        return self._content


    def get_site_record(self, site):
        content_list = self.content_to_list()

        for record in content_list:
            if(site.lower() == record['site'].lower()):
                return record


    def delete_physical(self):
        shutil.rmtree(self._dirpath)
        return
