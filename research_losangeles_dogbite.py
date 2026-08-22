import pplx_sdk
queries = [
  {"query":"Los Angeles County dangerous vicious dog hearing official"},
  {"query":"Los Angeles city dog leash law official"},
  {"query":"Los Angeles County animal care dog bites statistics annual report"},
  {"query":"Los Angeles County dog bite report animal care dangerous dog hearing"},
  {"query":"California dog bite statute 3342 legislature"},
  {"query":"Los Angeles Superior Court civil personal injury courthouse official"},
]
results = pplx_sdk.search.web_many(queries, limit_per_query=8)
for entry in results:
    print('\n###', entry.spec)
    if not entry.ok:
        print('ERROR', entry.error)
        continue
    for hit in entry.result:
        print(hit.title, '\n', hit.url, '\n', hit.snippet[:500], '\n')
