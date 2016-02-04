class AvaCoreTestData(object):
    @staticmethod
    def get_data(self, name='standard'):
        data = getattr(self, name, None)
        return data

