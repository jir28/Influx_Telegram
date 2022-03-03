
    query_api = client.query_api()
    query = ‘ from (bucket:"PythonExample") \
    | > range(start: -10m) \
    | > filter(fn: (r) = > r._measurement == "my_measurement") \
    | > filter(fn: (r) = > r.location == "Prague") \
    | > filter(fn: (r) = > r._field == "temperature" )‘