import random
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import time
import telegram


def send_data_idb(totality_lit, time_s):
    bucket = "Raspi"
    org = "jirs28"
    token = "VksMePOqNhrLWmA29wyq7FTcHOKPO0eeMBYX0ILkwT2DgN6rWzmOeS8g8JVCX3wBgwu6py1ftSGLAYyt46A1Bg=="
    url = "https://us-east-1-1.aws.cloud2.influxdata.com"

    client = influxdb_client.InfluxDBClient(
        url=url,
        token=token,
        org=org
    )

    write_api = client.write_api(write_options=SYNCHRONOUS)
    p = influxdb_client.Point("Litros por baño").tag("Zone", "baño").field("Litros", totality_lit)
    ptime = influxdb_client.Point("Tiempo por baño").tag("Zone", "baño").field("Segundos", time_s)
    write_api.write(bucket=bucket, org=org, record=p)
    write_api.write(bucket=bucket, org=org, record=ptime)
    print("Data sended to influx")


if __name__ == '__main__':
    j = 1
    time.sleep(1)

    tot_lit = random.randint(10, 20)
    times_shower = random.randint(25, 30)
    send_data_idb(tot_lit, times_shower)

    totlit = 23
    timeshower = 25.4
    temp = 25.67

    api_key = '5225831499:AAH-0_bNem_7_fhM0exw1Mx_tWozVVjlU64'
    user_id = '@RgaderaBot'

    bot = telegram.Bot(token=api_key)
    bot.send_message(chat_id=user_id, text='USP-Python has started up!')
