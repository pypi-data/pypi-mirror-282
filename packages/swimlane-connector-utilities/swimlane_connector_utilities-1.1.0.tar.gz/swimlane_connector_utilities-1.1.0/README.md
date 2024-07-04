# swimlane-connector-utilities

This package contains utility functions to be used in Swimlane Connectors.

## Swimlane Attachments
This helper function is to create attachments easily, in Swimlane output format. You can either create a single attachment, with create_attachment
```python
from swimlane_connector_utilities import create_attachment

output = {
    "attachment_key1": create_attachment("myfile.txt", "this is a text file")
    "attachment_key2": create_attachment("myfile.exe", <byte data here>)
}
```
Or multiple attachments with SwimlaneAttachments
```python
from swimlane_connector_utilities import SwimlaneAttachments


swa = SwimlaneAttachments()


swa.add_attachment("myfile.txt", "this is a text file")
swa.add_attachment("myfile.exe", <byte data here>)


output = {
    "attachment_list": swa.get_attachments()
}
```

## Create Test Connection
Creating test connections can be repetitive, so a test connection that looks like this:
```python
from swimlane_connector_utilities import create_test_conn

# My Integration Auth, copied from __init__.py for example purposes
class MyIntegration(object):
    def __init__(self, context):
        # Do auth here
        pass

    def do_auth(self):
        pass


class SwMain(object):
    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            MyIntegration(self.context).do_auth()

            return {"successful": True}
        except Exception as e:
            return {"successful": False, "errorMessage": str(e)}
```
Can be easily turned into
```python
from swimlane_connector_utilities import create_test_conn

# My Integration Auth, copied from __init__.py for example purposes
class MyIntegration(object):
    def __init__(self, context):
        # Do auth here
        pass

    def do_auth(self):
        pass
        
SwMain = create_test_conn(MyIntegration, execute_func="do_auth")
```
Note that if you do authentication in __init__ you can exclude the execute_func param

## Parse Datetime

datetime inputs can be many different formats and often we want to accept a time relative 
to the current time, such as `10 minutes ago`.  To handle all datetime inputs, you can use
the function `parse_datetime`.  This function accepts all common datetime formats as well 
as the relative time format below, and returns a pendulum object.  An `InvalidInput` error
will be raised if it is not a valid datetime.

### Relative datetime format:
```
For the current time:
    now
Any other time:
    (+/-)(integer) (milliseconds|seconds|minutes|days|weeks|months|years)
    
examples:
    now
    -1 months
    +3 days
    -123 seconds
```

parse_datetime can be used to parse the input, then convert the pendulum object to the format the
api requires.
```python
from swimlane_connector_utilities import parse_datetime

data = {"time_1": "2020-02-02 10:10:10", "time_2": "-5 minutes", "text_field": "text"}
for field in ["time_1", "time_2"]:
    data[field] = parse_datetime(field, data[field]).to_iso8601_string()
```