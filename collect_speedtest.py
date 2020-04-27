import pandas as pd
from pandas import DataFrame
import subprocess
from datetime import datetime
from pathlib import Path

def run_speedtest():
    """
    Runs speedtest via speedtest-cli (https://github.com/sivel/speedtest-cli) and collects results
    in readable csv
    :return:
    """
    # Results of speedtest-cli collected in the block below
    result = subprocess.run(['speedtest-cli', '--simple'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    output = result.split('\n')
    raw_download = output[1]
    raw_upload = output[2]
    split_download = raw_download.split(' ')
    split_upload = raw_upload.split(' ')
    download = split_download[1]
    upload = split_upload[1]

    # creates dataframe for current speedtest run
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    speedtest_output = pd.DataFrame([[current_time, raw_download, download, raw_upload, upload]],
                      columns=['time_checked', 'raw_download', 'download', 'raw_upload', 'upload'])

    return speedtest_output


def data_handler(df):
    """
    Either saves down first entry of speedtest-cli output
    :param df:
    :return:
    """
    history_path = 'data/speedtest.csv'
    csv_ouptut = Path(history_path)
    if csv_ouptut.is_file():
        speedtest_history = pd.read_csv(history_path)
        concat_speedtest = pd.concat([speedtest_history, df])
        concat_speedtest.to_csv(history_path, index=False)
    else:
        df.to_csv(history_path, index=False)


if __name__ == '__main__':
    speedtest_output = run_speedtest()
    data_handler(speedtest_output)






