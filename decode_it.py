import json
raw = open('./your_posts_1.json', 'r').read()
parsed = json.loads(raw)

# Iterate through all entries
for nth in range(len(parsed)):
  print('entry {}'.format(nth))
  # If data exists?
  if 'data' in parsed[nth]:
    # For every data entry (list)
    for i in range(len(parsed[nth]['data'])):
      # Every entry in the data entry list (繞口令ㄟ)
      for tag in parsed[nth]['data'][i]:
        print('tag: {}'.format(tag))
        # 如果是個字串那當作臉書版壞掉兩倍寬UTF-8處理
        if type(parsed[nth]['data'][i][tag]) == str:
          print(parsed[nth]['data'][i][tag].encode('latin1').decode('utf-8'))
        else:
          print(parsed[nth]['data'][i][tag])
  print("----------")