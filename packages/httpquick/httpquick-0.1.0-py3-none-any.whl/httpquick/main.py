import argparse
import datetime
import glob
import json
import os
import re
import urllib.parse

import requests


class HttpQuick:
    """
    A HttpQuick that executes on the command line to make http requests.

    Write the command line in an http file.
    execute_http_file reads the file and sends the request.
    http file, Split text with "###".

    Specify the http file as an argument and optionally specify the path to the output folder.

    The received data is output as GET_[domain]_response to the output destination (the current directory if the output destination folder is not specified).
    The folder must exist.
    To append the time to the output file name, append "-d" to the argument.

    TOKEN can also be replaced.
    For example, http file as specify GET {{token}}/data, create *.env.json in the current directory and save it as {"token": "test"}. In this case, the file is interpreted as GET test/data. (If the extension is .env.json, it will be read).
    """

    def __init__(self):
        self.token_list = {}
        self.file_path = None

    def execute_http_file(self, argument):
        """
        Write the command in an http file.
        execute_http_file reads the file and sends the request.
        :param argument: command line argument
        :return: None
        """
        if argument.http_file is None:
            raise ValueError(f"-h, --help   show this help message and exit\n")
            return

        if not os.path.exists(self.get_directory_path(argument.http_file)):
            raise ValueError(
                f"file:{argument.http_file} is not found.\n please check file.\n"
            )

        try:
            self.file_path = argument.http_file
            self.set_env()
            requests_data = self.split_requests(self.file_path)

            for request in requests_data:

                # if len(content.replace("\n", "")) == 0:
                #     continue
                is_request, (method, url, headers, body) = self.parse_http_file(request)
                if not is_request:
                    continue
                response = self.execute_request(method, url, headers, body)
                print(f"info:StatusCode:{response.status_code}")
                # print("\n\n")
                # print(f"response:{response.text.splitlines()}")
                current_time = ""
                if argument.add_date:
                    current_time = "_" + datetime.datetime.now().strftime(
                        "%m%d%Y_%H%M%S"
                    )
                address = self.escape_invalid_filename_chars(url)
                filename = f"{method}_{address}{current_time}_response"
                if argument.output_path is None:
                    clt_path = self.get_directory_path(self.file_path)
                    output_path = os.path.join(clt_path, filename)
                else:
                    output_path = os.path.join(argument.output_path, filename)

                if os.path.exists(output_path):
                    mode = "a"  # Append mode if the file exists.
                else:
                    mode = "w"  # If the file does not exist, create a new file.

                with open(output_path, mode, encoding="utf-8") as f:
                    for key, value in response.headers.items():
                        f.write(f"{key}: {value}\n")
                    f.write("\n\n")
                    f.write(response.text)

        except Exception as e:
            raise ValueError(f"Error: {str(e)}\n")

    @staticmethod
    def get_directory_path(file_path):
        """
        If a file name is specified, it is assumed to be the current directory.
        not current directory file, for get absolute path
        :param file_path: file path
        :return: "./" or absolute path
        """
        if not os.path.isabs(file_path) and not os.path.dirname(file_path):
            return "./"

        abs_path = os.path.abspath(file_path)
        current_dir = os.getcwd()

        # Check if it is in the current directory
        if (
            abs_path == current_dir
            or os.path.commonpath([abs_path, current_dir]) == current_dir
        ):
            if abs_path == current_dir:
                return "./"
            relative_path = os.path.relpath(os.path.dirname(abs_path), current_dir)
            return "./" if relative_path == "." else relative_path
        else:
            return os.path.relpath(os.path.dirname(abs_path), current_dir)

    @staticmethod
    def escape_invalid_filename_chars(url):
        """
        escape invalid chars
        :param url: access url
        :return: escaped url
        """
        parsed_url = urllib.parse.urlparse(url)
        path = parsed_url.hostname
        escaped_url = urllib.parse.quote(path, safe="_")

        escaped_url = escaped_url.replace(".", "_")

        return escaped_url

    def set_env(self):
        """
        load Environment file, get tokens
        :return: None
        """
        path = self.get_directory_path(self.file_path)
        file_pattern = os.path.join(path, "*.env.json")
        self.load_environment_file(file_pattern)
        file_pattern = os.path.join(path, ".env.json")
        self.load_environment_file(file_pattern)
        if len(self.token_list) == 0:
            print("info:Environment files or token, could not be found.")

    def load_environment_file(self, file_pattern):
        """
        Use file_pattern to search all.
        :param file_pattern:Search conditions
        :return: None
        """
        env_json_files = glob.glob(file_pattern)
        for file_path in env_json_files:
            with open(file_path, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    self.find_properties(data)
                    print(f"info:loading file: {file_path}")
                except json.JSONDecodeError as e:
                    print(f"info:Error reading {file_path}: {e}")

    @staticmethod
    def execute_request(method, url, headers, body):
        """
        http requests
        :param method: GET|POST|PUT|DELETE|PATCH
        :param url: access url
        :param headers: send headers data
        :param body: send body data
        :return: response data
        """
        response = requests.request(method, url, headers=headers, data=body)
        return response

    @staticmethod
    def split_requests(file_path):
        """
        Split text with "###".
        :param file_path:
        :return:
        """
        with open(file_path, "r") as file:
            content = file.read()

        requests_data = re.split(r"###\s", content.strip())
        return requests_data

    def replace_placeholders(self, content: str):
        """
        token replace to data
        :param content: text
        :return: replaced txt
        """
        # if token list is empty, return
        if len(self.token_list) == 0:
            return content
        target = "{{"
        before = content.find(target) + len(target)

        target = "}}"
        after = content.find(target)
        token = content[before:after]
        if token in self.token_list:
            content = content.replace(f"{{{{{token}}}}}", self.token_list[token])
        elif after != -1:
            error_message = (
                f"[{token}] is not registered."
                f" Please check if Environment files (*.env.json) are properly set."
            )
            raise ValueError(error_message)

        return content

    def parse_http_file(self, content: str):
        """
        http file parser
        :param content: txt
        :return: http method, targets url, header data, body data
        """
        target = "\n"
        idx = content.find(target)
        if idx != -1 and idx == 0:
            content = content[idx:]
        if content.find("\n") == 0:
            content = content[1:]

        request_line = re.search(
            r"^(GET|POST|PUT|DELETE|PATCH)\s+(\S+)", content, re.MULTILINE
        )
        if not request_line:
            print(content)
            # raise ValueError("Invalid HTTP request format")
            return False, (None, None, None, None)

        method = request_line.group(1)
        url = request_line.group(2)
        url = self.replace_placeholders(url)
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        headers = {}
        body = None

        target = "\n\n"
        idx = content.find(target)
        line_headers = content[:idx]

        header_lines = re.findall(r"^(.*): (.*)$", line_headers, re.MULTILINE)
        for header in header_lines:
            headers[header[0]] = self.replace_placeholders(header[1])
            # no_headers = no_headers.replace(": ".join(header), "")

        line_body = "\n\n" + content[idx + len(target) :]
        body_match = re.search(r"\r?\n\r?\n(.+)", line_body, re.DOTALL)
        if body_match:
            body = body_match.group(1)

        return True, (method, url, headers, body)

    def find_properties(self, data):
        """
        Recursively traverses the dictionary and stores all properties and values in variables
        :param data:
        :return: None
        """
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    self.find_properties(value)
                else:
                    self.token_list[key] = value
        elif isinstance(data, list):
            for item in data:
                self.find_properties(item)


def main():
    parser = argparse.ArgumentParser(
        description="Send HTTP request and save the response"
    )

    parser.add_argument(
        "http_file",
        type=str,
        nargs="?",
        default=None,
        help="Enter the path to the HTTP request file",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        nargs="?",
        default=None,
        help="Enter the output file path (optional)",
    )
    parser.add_argument(
        "-d",
        "--add_date",
        action="store_true",
        help='Append "-d" if you want to append the time to the output file name. (optional)',
    )
    args = parser.parse_args()
    http_req = HttpQuick()
    http_req.execute_http_file(args)


# if __name__ == "__main__":
#     main()
