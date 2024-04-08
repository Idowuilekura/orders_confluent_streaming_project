import os
def read_config():
  # reads the client configuration from client.properties
  # and returns it as a key-value map
  try:
    config = {}
    with open("client.properties") as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split('=', 1)
                config[parameter] = value.strip()
    return config
  except Exception:
    bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS')
    security_protocol = os.getenv('SECURITY_PROTOCOL')
    sasl_mechanisms = os.getenv('SASL_MECHANISMS')
    sasl_username = os.getenv('SASL_USERNAME')
    sasl_password = os.getenv('SASL_PASSWORD')
    session_timeout_ms = os.getenv('SESSION_TIMEOUT_MS')
    print(session_timeout_ms)
    if type(session_timeout_ms) == str:
        session_timeout_ms = int(session_timeout_ms)
    config = {'bootstrap.servers': bootstrap_servers, 'security.protocol': security_protocol, 
      'sasl.mechanisms': sasl_mechanisms, 'sasl.username': sasl_username, 'sasl.password': sasl_password,'session.timeout.ms': session_timeout_ms}
    return config
