class {project_name}TestData(object):
    @staticmethod
    def get_data(self, name='standard'):
        data = getattr(self, name, None)
        return data
