class AvaCoreTestData(object):
    def get_data(self, name='standard'):
        data = getattr(self, name, None)
        return data

