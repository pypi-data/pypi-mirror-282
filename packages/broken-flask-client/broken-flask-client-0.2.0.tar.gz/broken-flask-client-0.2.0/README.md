# Broken Flask Backend

A flask app that is vulnerable to SQL Injection. It runs behind the [broken-flask](https://github.com/nvsecurity/broken-flask) API. The intent is to demonstrate a frontend API endpoint (broken-flask's `/api/v2/employees` endpoint) that is not inherently vulnerable on the frontend API to SQL Injection, but is vulnerable because it calls a secondary API.

It also exposes a thin Python client in PyPi that is used by the frontend API: https://pypi.org/project/broken-flask-client/.
