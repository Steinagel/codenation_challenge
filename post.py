# Sent through insomnia
import http.client

conn = http.client.HTTPSConnection("api.codenation.dev")

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"answer\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

headers = { 'content-type': "multipart/form-data; boundary=---011000010111000001101001" }

conn.request("POST", "/v1/challenge/dev-ps/submit-solution?token=2318ff2032de236e61faa160f2b982cdc3f109a7", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))