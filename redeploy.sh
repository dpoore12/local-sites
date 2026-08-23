#!/bin/bash
# Publish the staged sites plus the hostname router. Run with the Cloudflare credential.
set -e
cd "$(dirname "$0")"
A=a3bf1a13d93899d8408b9d1ea94df078
( cd router && /home/user/node_modules/.bin/wrangler pages functions build functions \
    --outfile=../data/_worker.bundle --build-output-directory=../.stage )
curl -s -X POST "https://api.cloudflare.com/client/v4/accounts/$A/pages/projects/local-sites/deployments" \
  --form-string "manifest=$(cat data/manifest.json)" \
  --form-string "branch=main" \
  -F "_worker.bundle=@data/_worker.bundle" \
| python3 -c "import json,sys;d=json.load(sys.stdin);print('deployed:',(d.get('result') or {}).get('url') or d.get('errors'))"
