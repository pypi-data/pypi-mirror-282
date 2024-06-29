import csv
import json
import os

try:
    import requests

    REQUESTS_IMPORTED = True
except ModuleNotFoundError:
    REQUESTS_IMPORTED = True


def get_last_id_in_csv_file(file_name, column="id"):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)

        # Iterate over each row in the CSV file
        for row in reader:
            # Assign the last row to the last_row variable
            last_row = row

        try:
            # Get the value you want from the last row by column name
            desired_value = last_row[column]

            return int(desired_value)
        except:
            return -1


def load_json_from_file(path):
    """
    Load json object from file.
    """
    with open(path, "r") as file:
        return json.load(file)


def write_json_to_file(path, data, indent: int = 4):
    """
    Write json object to file.
    """
    with open(path, "w") as file:
        json.dump(data, file, indent=indent)


class LyFile:
    def __init__(self, path: str = "LyFile/file.txt"):
        self._path = path

    def exists(self):
        return os.path.exists(self._path)

    def create(self):
        """
        Creates a blank file at path.
        """
        # Split path into directory and filename
        directory, _ = os.path.split(self._path)

        # If directory was included, create it if it doesn't exist
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        open(self._path, "w").close()  # Create file

    def append(self, text):
        """
        Appends text to file at path.
        """
        with open(self._path, "a") as file:
            file.write(f"{text}\n")

    def append_json(self, data: dict, indent: int = 4):
        """
        Appends json data to file at path.
        """
        with open(self._path, "a") as file:
            json.dump(data, file, indent=indent)
            file.write("\n")

    if REQUESTS_IMPORTED:

        def append_response(self, response: requests.Response, indent: int = 4):
            """
            Appends response object to file at path.
            """

            with open(self._path, "a") as file:
                # Try to get the JSON content
                try:
                    json_content = response.json()
                except ValueError:
                    json_content = ""  # If JSON decoding fails, set it to None or an empty dictionary

                try:
                    content = response.content.decode(
                        response.apparent_encoding or response.encoding
                    )
                except UnicodeDecodeError:
                    content = response.content.decode(
                        "latin1"
                    )  # Fallback to latin1 if UTF-8 and apparent_encoding fail

                # Create a dictionary from the response object
                data = {
                    "status_code": response.status_code,
                    "text": response.text,
                    "content": content,  # Decoding bytes to string
                    "json": json_content,
                    "headers": dict(response.headers),
                    "url": response.url,
                    "encoding": response.encoding,
                    "elapsed": response.elapsed.total_seconds(),  # Converting timedelta to seconds
                    "cookies": requests.utils.dict_from_cookiejar(response.cookies),
                    "history": [resp.url for resp in response.history],
                    "reason": response.reason,
                }

                json.dump(data, file, indent=indent)
                file.write("\n")
