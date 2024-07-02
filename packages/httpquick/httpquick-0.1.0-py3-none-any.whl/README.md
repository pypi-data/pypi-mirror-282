# EN
A HttpQuick that executes on the command line to make http requests.

I am not responsible for any damages whatsoever. Please use at your own risk.

Write the command line in an http file.
execute_http_file reads the file and sends the request.
Reads the http file, splitting the text with "###" to recognize it as a separate command.

Specify the http file as an argument and optionally specify the path to the output folder.

The received data is output as GET_[domain]_response to the output destination (the current directory if the output destination folder is not specified).
The folder must exist.
To append the time to the output file name, append "-d" to the argument.

TOKEN can also be replaced.
For example, http file as specify GET {{token}}/data, create *.env.json in the current directory and save it as {"token": "test"}. In this case, the file is interpreted as GET test/data. (If the extension is .env.json, it will be read).

how to use

file:test.http
GET {{access_url}}/user/userlist/json
###
GET {{access_url}}/user/data
Name: Alice
Data: {{data_type}}

file:.env.json
{
    "access_url": "localhost"
    "data_type": "Age"
}

console
HttpQuick test.http

{{token name}} will be read from .env.json and repressed and interpreted.
# JP
HttpQuickはコマンドラインで実行してhttpリクエストを行うツール。

いかなる損害についても、私は責任を負いません。自己責任でご利用ください。

コマンドラインを http ファイルに記述する。
execute_http_fileはファイルを読み込んでリクエストを送信する。
httpファイルを読み込む、"###"でテキストを分割することで別のコマンドと認識する。

引数にhttpファイルを指定し、オプションで出力フォルダのパスを指定する。

受信したデータはGET_[domain]_responseとして出力先（出力先フォルダが指定されていない場合はカレントディレクトリ）に出力される。
フォルダが存在する必要があります。
出力ファイル名に時刻を付加するには、引数に"-d "を付加する。

TOKENを置き換えることもできる。
例えば、httpファイルにGET {{token}}/dataと用意し、カレントディレクトリに*.env.jsonを作成して{"token"： 「test"}として保存します。この場合、ファイルはGET test/dataとして解釈されます。(拡張子が.env.jsonの場合に読み込まれます）。

使用方法

ファイル:test.http
GET {{access_url}}/user/userlist/json
###
GET {{access_url}}/user/data
Name: Alice
Data: {{data_type}}



ファイル:.env.json
{
    "access_url": "localhost"
    "data_type": "Age"
}



コンソール上
HttpQuick test.http

{{トークン名}}としておくと、.env.jsonから読み込んでリプレスして解釈します。