import configparser

def config(file_name='dev_credentials.ini',section='dev-postgresql'):
        db = {}
        cp = configparser.ConfigParser()
        cp.read(file_name)
        if cp.has_section(section):
                items = cp.items(section)
                for item in items:
                        db[item[0]] = item[1]
        else :
                raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db