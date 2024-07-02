import re
import json
from _ctypes import PyObj_FromPtr


__version__ = '0.1'


class NoIndent(object):
    """value wrapper"""
    def __init__(self, value):
        self.value = value


class PrettyEncoder(json.JSONEncoder):
    FORMAT_SPEC = "@@{}@@"
    regex = re.compile(FORMAT_SPEC.format(r'(\d+)'))

    def __init__(self, **kwargs):
        # save copy of any keyword argument values needed for use here
        self.__sort_keys = kwargs.get('sort_keys', None)
        super(PrettyEncoder, self).__init__(**kwargs)

    def default(self, obj):
        return self.FORMAT_SPEC.format(id(obj)) if isinstance(obj, NoIndent) else super().default(obj)

    def encode(self, obj):
        json_repr = super().encode(obj)  # Default JSON
        # Create a dictionary for replacements
        replacements = {}

        def replacement(match):
            idx = int(match.group(1))
            if idx not in replacements:
                no_indent = PyObj_FromPtr(idx)
                json_obj_repr = json.dumps(no_indent.value, sort_keys=self.__sort_keys)
                replacements[idx] = json_obj_repr
            return replacements[idx]

        # Use re to perform the replacement with a callback function
        pattern = re.compile(r'"{}"'.format(self.FORMAT_SPEC.format(r'(\d+)')))
        json_repr = pattern.sub(replacement, json_repr)

        return json_repr


def dumps(contents, indent=2):
    json_data = json.dumps(contents, cls=PrettyEncoder, ensure_ascii=False, sort_keys=False, indent=indent)
    return json_data


def write_json(contents, json_save_path, indent=2):
    with open(json_save_path, 'w', encoding='utf8') as fw:
        json_data = dumps(contents, indent)
        fw.write(json_data)


def sample():
    samples = {
        "name": "John",
        "age": 30,
        "pets": [
            {
                "name": "Fluffy",
                "type": "cat",
                "toys": [
                    [1, 2, 3],
                    [2, 3, 4]
                ]
            },
            {
                "name": "Fido",
                "type": "dog",
                "toys": [
                    "bone",
                    "frisbee"
                ]
            }
        ]
    }

    pretty_samples = {
        "name": "John",
        "age": 30,
        "pets": [
            {
                "name": "Fluffy",
                "type": "cat",
                "toys": NoIndent([
                    [1, 2, 3],
                    [2, 3, 4]
                ])
            },
            {
                "name": "Fido",
                "type": "dog",
                "toys": NoIndent([
                    "bone",
                    "frisbee"
                ])
            }
        ]
    }

    samples = json.dumps(samples, ensure_ascii=False, sort_keys=False, indent=2)
    pretty_samples = dumps(pretty_samples, indent=2)

    return samples, pretty_samples
