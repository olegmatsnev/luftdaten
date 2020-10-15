Luftdaten is an international crowdsourcing project to measure concentration of fine dust in ambient air. For details visit the project's website https://luftdaten.info/

This is a script that stores output from a fine dust sensor into a remote MySQL database.

To start using it, one has to populate `config.py` file with a link to output in `*.json` format and database credentials.

Crontab string to run the script every 3rd minute (no need to do that more often as stock firmware reads the sensor with just that frequency):

*/3 * * * * python3 <path to the script>/luftdaten_pub.py

To run it with a task scheduler on Windows, change the extension to `*.pyw` -- this will prevent a console window from popping up every time the script runs.
