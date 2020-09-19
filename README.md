Luftdaten is an international crowdsourcing project to measure concentration of fine dust in ambient air. For details visit the project's website https://luftdaten.info/

This is a script that stores output from a fine dust sensor into a remote MySQL database.

To start using it, one has to populate `config.py` file with a link to output in `*.json` format and database credentials.

To run with a task scheduler on Windows, change the extension to `*.pyw` -- this will prevent a console window from popping up every time the script runs.
