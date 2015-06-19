#!/usr/bin/python





def get_users(self) {
    page_token = None
    params = {'customer': 'my_customer'}
    all_users = []
    while True:
      try:
        if page_token:
         params['pageToken'] = page_token
        current_page = directory_service.users().list(**params).execute()

        all_users.extend(current_page['users'])
        page_token = current_page.get('nextPageToken')
        if not page_token:
         break

      except errors.HttpError as error:
        print 'An error occurred: %s' % error
        break

    return all_users
}


def get_groups(self) {
    page_token = None
    params = {'customer': 'my_customer'}
    all_groups = []
    while True:
      try:
        if page_token:
          params['pageToken'] = page_token
        current_page = directory_service.groups().list(**params).execute()

        all_groups.extend(current_page['groups'])
        page_token = current_page.get('nextPageToken')
        if not page_token:
          break

      except errors.HttpError as error:
        print 'An error occurred: %s' % error
        break

    return all_groups
}




def get_user_groups(self): {
    page_token = None
    params = {}
    user_groups ={}

    for user in all_users:
        user_groups[user['primaryEmail']] = []

        while True:
            try:
                if page_token:
                    params['pageToken'] = page_token

                params['userKey'] = user['id']
                current_page = directory_service.groups().list(**params).execute()
                curr_groups = []

                if 'groups' in current_page:
                    curr_groups.extend(current_page['groups'])
                    #print current_page['groups']

                page_token = current_page.get('nextPageToken')
                if not page_token:
                    user_groups[user['primaryEmail']] = curr_groups
                    break

            except errors.HttpError as error:
                print 'An error occurred: %s' % error
                break

    return user_groups
}


def get_group_members(self) {
    page_token = None
    params = {}
    group_members = {}
    for group in all_groups:
      group_members[group['id']] = []

      while True:
        try:
          if page_token:
            params['pageToken'] = page_token

          params['groupKey'] = group['id']
          current_page = directory_service.members().list(**params).execute()
          curr_members = []

          print current_page

          if 'members' in current_page:
            curr_members.extend(current_page['members'])

          page_token = current_page.get('nextPageToken')
          if not page_token:
            group_members[group['name']] = curr_members
            break

        except errors.HttpError as error:
          print 'An error occurred: %s' % error
          break

    return group_members
}

def to_string(self, dictionary):
    for key, value in dictionary:
        print key
        for item in value:
            print item






