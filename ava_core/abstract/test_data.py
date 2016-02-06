class AvaCoreTestData(object):
    def get_data(self, name='standard'):
        data = getattr(self, name, None)
        if not data:
            raise Exception('Data <{}> not found.'.format(name))
        return data

    # def get_data_with_owner(self, owner, name='standard'):
    #     data = getattr(self, name, None)
    #
    #     # Check that data with given name exists.
    #     # True - Attempt to set the owner field.
    #     # False - Raise exception.
    #     if data:
    #         # Check that the data contains the owner field.
    #         # True - Set owner field to passed owner.
    #         if 'owner' in data or 'suggested_by' in data:
    #             # Check that owner is valid.
    #             # True - Set owner field to passed owner.
    #             # False - Return none.
    #             if owner:
    #                 data['owner'] = owner['id']
    #             else:
    #                 raise Exception('Cannot give owner as None to model when owner is requested.')
    #     else:
    #         raise Exception('Data <{}> not found in <AvaCoreTestData>.'.format(name))
    #
    #     return data

