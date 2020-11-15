import datetime
import os


class provnGenerator:
    def __init__(self):
        self.document = ''
        self.entities = list()
        self.activities = list()
        self.agents = list()

    def openDocument(self):
        self.document = "document"
        self.entities = list()
        self.activities = list()
        self.agents = list()

    def prefix(self, var, site):
        self.document += '\n  prefix {} <{}>'.format(var, site)

    def endDocument(self, filename='', path='./'):
        self.document += "\nendDocument"
        if filename:
            fullpath = os.path.join(path, filename)
        else:
            fullpath = os.path.join(path, str(datetime.datetime.now()).replace(' ', '_').replace('.', '_').replace(':','_') + '.' + 'proven.txt')
        try:
            file = open(fullpath, 'wb')
            file.write(self.document.encode('utf-8'))
            file.close()
            return True, self.document.encode('utf-8')
        except Exception as e:
            return False, e

    def entity(self, var, name, meta={}):
        if meta:
            meta_string = ', ' + self.metaConvert(meta)
        else:
            meta_string = ''
        self.document += '\n  entity({}:{}{})'.format(var, name, meta_string)
        self.entities.append((var,name))
        return var, name

    def activity(self, var, name, meta={}):
        self.document += '\n  activity({}:{}, -, -)'.format(var, name)
        self.activities.append((var, name))
        return (var, name)

    def agent(self, var, name, meta={}):
        if meta:
            meta_string = self.metaConvert(meta)
        else:
            meta_string = '-'
        self.document += '\n  agent({}:{}, {})'.format(var, name, meta_string)
        self.agents.append((var, name))
        return (var, name)

    def used(self, from_v, to_v, meta={}):
        from_var, from_name = from_v
        to_var, to_name = to_v
        self.document += '\n  used({}:{}, {}:{}, -)'.format(from_var, from_name, to_var, to_name)

    def wasGeneratedBy(self, from_v, to_v, meta={}):
        from_var, from_name = from_v
        to_var, to_name = to_v
        self.document += '\n  wasGeneratedBy({}:{}, {}:{}, -)'.format(from_var, from_name, to_var, to_name)

    def wasAssociatedWith(self, from_v, to_v, meta={}):
        from_var, from_name = from_v
        to_var, to_name = to_v
        self.document += '\n  wasAssociatedWith({}:{}, {}:{}, -)'.format(from_var, from_name, to_var, to_name)

    def wasInformedBy(self, from_v, to_v, meta={}):
        from_var, from_name = from_v
        to_var, to_name = to_v
        self.document += '\n  wasInformedBy({}:{}, {}:{})'.format(from_var, from_name, to_var, to_name)

    def metaConvert(self, meta={}):
        meta_string = '['
        begin_point = True
        for k, i in meta.items():
            if begin_point == False:
                meta_string += ', '
            begin_point = False
            if str(type(i)) == "<class 'str'>":

                meta_string += k + '=' + '"' + i + '"'
            else:
                meta_string += k + '=' + str(i)
        meta_string += ']'
        return meta_string
