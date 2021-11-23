import requests

res = requests.get('https://www.cscareers.dev/api/getSheetEntries?slug=2022-new-grad')   
res_intern = requests.get('https://www.cscareers.dev/api/getSheetEntries?slug=2022-summer-intern')   

# expected format: [{"company":{"friendlyName":"Applied Intuition","slug":"applied-intuition"},"applied":9,"rejected":0,"oa":0,"phone":0,"final":1,"offer":1}, ...]

res_json = res.json()
res_intern_json = res_intern.json()

res_json.sort(key=lambda x: x['offer'], reverse=True)
res_intern_json.sort(key=lambda x: x['offer'], reverse=True)

for r in res_json:
    print(r['company']['friendlyName'], r['offer'])

for r_intern in res_intern_json:
    print(r_intern['company']['friendlyName'], r_intern['offer'])