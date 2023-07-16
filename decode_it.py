import json
raw = open('./your_posts_1.json', 'r').read()
parsed = json.loads(raw)

for nth in range(len(parsed)):
  #print(str(parsed[nth]).encode('latin1').decode('utf-8'))
  if 'data' in parsed[nth]:
    if len(parsed[nth]['data']) > 0:
      if 'post' in parsed[nth]['data'][0]:
        print(parsed[nth]['data'][0]['post'].encode('latin1').decode('utf-8'))
      else:
        print('Some other data in no. {}'.format(nth))
  print("----------")