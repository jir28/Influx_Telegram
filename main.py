import random
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import time
import requests



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





def send_alert(litros, time, tempe):
    requests.post('https://api.telegram.org/bot5225831499:AAH-0_bNem_7_fhM0exw1Mx_tWozVVjlU64/sendMessage',
                  data={'chat_id': '@RgaderaBot', 'text': ('Litros gastados: ' + str(litros))})
    requests.post('https://api.telegram.org/bot5225831499:AAH-0_bNem_7_fhM0exw1Mx_tWozVVjlU64/sendMessage',
                  data={'chat_id': '@RgaderaBot', 'text': ('Tiempo de baño: ' + str(time))})
    requests.post('https://api.telegram.org/bot5225831499:AAH-0_bNem_7_fhM0exw1Mx_tWozVVjlU64/sendMessage',
                  data={'chat_id': '@RgaderaBot', 'text': ('Temperatura promedio: ' + str(tempe))})
    print("Alerts sended")

def alertsTele(bot_message):
    bot_token = '5225831499:AAH-0_bNem_7_fhM0exw1Mx_tWozVVjlU64'
    bot_chatid = '@RgaderaBot'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatid + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()



if __name__ == '__main__':
    j = 1
    time.sleep(1)

    tot_lit = random.randint(10, 20)
    times_shower = random.randint(25, 30)
    send_data_idb(tot_lit, times_shower)

    totlit = 23
    timeshower = 25.4
    temp = 25.67
    tests = alertsTele("Testing telegram bot")
    print(tests)
    #send_alert(totlit, timeshower, temp)
