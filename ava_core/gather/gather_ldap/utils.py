import datetime
import re

group_model_schema = {
    'cn': 'cn',
    'distinguished_name': 'distinguishedName',
    'name': 'name',
    'object_category': 'objectCategory',
    'sam_account_name': 'sAMAccountName',
    'object_guid': 'objectGUID',
    'object_sid': 'objectSid',

}

group_model_schema_reversed = {value: key for key, value in group_model_schema.items()}


def group_model_field_to_ldap(self, fieldname):
    return group_model_schema.get(fieldname)


def ldap_field_to_group_model(self, fieldname):
    return group_model_schema_reversed.get(fieldname)


user_model_schema = {
    'dn': 'dn',
    'account_expires': 'accountExpires',
    'admin_count': 'adminCount',
    'bad_password_time': 'badPasswordTime',
    'bad_pwd_count': 'badPwdCount',
    'cn': 'cn',
    'description': 'description',
    'display_name': 'displayName',
    'distinguished_name': 'distinguishedName',
    'is_critical_system_object': 'isCriticalSystemObject',
    'last_logoff': 'lastLogoff',
    'last_logon': 'lastLogon',
    'last_logon_timestamp': 'lastLogonTimestamp',
    'logon_count': 'logonCount',
    # 'logon_hours': 'logonHours',
    'lockout_time': 'lockoutTime',
    'name': 'name',
    'object_guid': 'objectGUID',
    'object_sid': 'objectSid',
    'primary_group_id': 'primaryGroupID',
    'pwd_last_set': 'pwdLastSet',
    'sam_account_name': 'sAMAccountName',
    'sam_account_type': 'sAMAccountType',
    'usn_changed': 'uSNChanged',
    'usn_created': 'uSNCreated',
    'user_account_control': 'userAccountControl',
    'when_changed': 'whenChanged',
    'when_created': 'whenCreated',

}

user_model_schema_reversed = {value: key for key, value in user_model_schema.items()}


def user_model_field_to_ldap(self, fieldname):
    return user_model_schema.get(fieldname)


def ldap_field_to_user_model(self, fieldname):
    return user_model_schema_reversed.get(fieldname)


def convert_date_time(self, date_value):
    # LDAP date/times in FILETIME format use this as their epoch
    filetime_epoch = datetime.datetime(1601, 1, 1, 0, 0, 0)
    # Upper bound on valid FILETIME values.
    filetime_max = (datetime.datetime.max - filetime_epoch).total_seconds() * 1000000
    # Regular expression to check for valid FILETIME values.
    time_filetime = re.compile(r'^\d+$')
    # Regular expression to check for valid date/time string values.
    time_datestring = re.compile(r'^(?P<yr>\d{4})(?P<mon>0[1-9]|1[012])(?P<day>0[1-9]|[12][0-9]|3[01])'
                                 r'(?P<hr>[01][0-9]|2[0-3])(?P<min>[0-5][0-9])(?P<sec>[0-5][0-9])(?:\.\d{1,3})?Z$')

    # Check if the data is a Windows FILETIME value.
    match = time_filetime.match(date_value)
    if match:
        microseconds = int(date_value) / 10
        if microseconds > 0:
            if microseconds > filetime_max:
                return datetime.datetime.max
            delta = datetime.timedelta(microseconds=microseconds)
            return filetime_epoch + delta
        return None

    # Check if the data is a date string.
    match = time_datestring.match(date_value)
    if match:
        time_year = int(match.group('yr'))
        time_month = int(match.group('mon'))
        time_day = int(match.group('day'))
        time_hour = int(match.group('hr'))
        time_minute = int(match.group('min'))
        time_second = int(match.group('sec'))
        return datetime.datetime(time_year, time_month, time_day, time_hour, time_minute, time_second)

    # No value.
    return None


def clean_hex(self, val):
    s = ['\\%02X' % ord(x) for x in val]
    return ''.join(s)
