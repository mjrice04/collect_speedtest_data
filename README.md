# SpeedTest CLI Data Collection
Runs *speedtest-cli* from <https://github.com/sivel/speedtest-cli> and collects the results in a csv.

You can schedule the job with crontab to have it continously run the job.

Run `crontab -e` to create or edit your existing crontab

Example: `30 * * * * python collect_speedtest.py` to run every 30 minutes 
