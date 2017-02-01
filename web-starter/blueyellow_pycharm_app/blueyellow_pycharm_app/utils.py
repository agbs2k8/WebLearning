import hashlib
import os

__full_path = os.path.dirname(os.path.abspath(__file__))


def build_cache_id(relative_file_url: str):
    if not relative_file_url:
        return "ERROR_NO_FILE"

    fullname = os.path.abspath(os.path.join(
        __full_path, relative_file_url.lstrip('/')))

    if not os.path.exists(fullname):
        return "ERROR_MISSING_FILE"

    return __get_file_hash(fullname)


def __get_file_hash(filename):
    md5 = hashlib.md5()

    with open(filename, 'rb') as fim:
        data = fim.read()
        md5.update(data)

    return md5.hexdigest()