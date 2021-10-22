import requests
import time
import json
import pandas

count = 0
tic = time.perf_counter()

query = """query {
    characters {
    results {
      name
      status
      species
      type
      gender
    }
  }
}"""

while count < 200:
    req = requests.post('https://rickandmortyapi.com/graphql/', json={'query': query})
    print(req.status_code)
    res = json.loads(req.text)
    characters = res['data']['characters']['results']
    df = pandas.DataFrame(characters)
    print(df)
    count = count + 1

toc = time.perf_counter()
print(f"temps: {toc - tic:0.4f} seconds")
