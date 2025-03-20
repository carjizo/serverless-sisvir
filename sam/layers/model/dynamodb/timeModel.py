import logging
import os
import pytz
import uuid
from datetime import datetime, date

from pynamodb.models import Model
from pynamodb.attributes import (
    ListAttribute, UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute, BooleanAttribute, MapAttribute
)
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection, LocalSecondaryIndex

logging.basicConfig()
log = logging.getLogger("pynamodb")
log.setLevel(logging.DEBUG)
log.propagate = True

REGION = os.environ['AWS_DEFAULT_REGION']
APP = os.environ['application']
STAGE = os.environ['stage']

class ConvertAttr(object):
    def myconverter(o):
        if isinstance(o, date):
            return o.__str__()
        elif isinstance(o, datetime):
            return o.__str__()
        elif isinstance(o, MapAttribute):
            return o.attribute_values
        
    def to_dict(self):
        rval = {}
        for key in self.attribute_values:
            rval[key] = self.__getattribute__(key)
        return rval

class UserEntity(Model,ConvertAttr):
    class Meta:
        table_name = f"{APP}-{STAGE}-users"
        region = REGION
        read_capacity_units = 1
        write_capacity_units = 1

    identityNumber = UnicodeAttribute(hash_key=True,  default='')
    fullName = UnicodeAttribute(default='')
    idMac = UnicodeAttribute(default='')
    active = BooleanAttribute(default=False)