# balance-ai-wrapper

## Requirements

* python 12

## setup venv

```shell
python3.12 -m venv venv
source venv/bin/activate
python
> Python 3.12.2 (...)
which python
> (...)venv/bin/python

pip install -r requirements.txt
```

## Run all locally from sources

```shell
export PYTHONPATH=$PYTHONPATH:src
OR 
export PYTHONPATH=src

python src/balanceai/cli_runner.py init
# update generated config file
python src/balanceai/cli_runner.py dev


```

## Other commands
```shell
python src/balanceai/cli_runner.py zkml
python src/balanceai/cli_runner.py help
python src/balanceai/cli_runner.py init --config my-ai-model-wrapper-config.json
python src/balanceai/cli_runner.py dev --config my-ai-model-wrapper-config.json
```


## Start mocked services
```shell
python mock/chain-app.py
python mock/ipfs-app.py
python mock/ai-app.py
```

# bai wrapper - sample call
```shell
curl --location 'http://127.0.0.1:9000/baiwrapper/aimodel' \
--header 'Content-Type: application/json' \
--data '{
    "caller_address": "CALLER_ADDR_5CSRVkQYi8P25Jidzhp9t1qzmnhEuTQim8L",
    "id": "request_id_guid_gen_by_client_4364977e-c1b0-4e85-bb35-53538fab0909",
    "model_id": "MODEL_ID_47djsnv9483ghj9idsv",
    "encryption_key": "PUB_ENC_KEY_TO_IPFS_rzyw8Hwb7KkZQGxnMgWm2EXb1zh6DmRKX22",
    "transparency": {
        "request_store": true,
        "response_store": false,
        "encrypt": true
    },
    "request": {
        "model_api_request": {
          "x": 45,
          "y": 123.45
        }
    },
    "signature": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
}'


# AI model
curl http://127.0.0.1:9300/ai
curl http://127.0.0.1:9300/ai/model333 -d {}

# IPFS
curl http://127.0.0.1:9100/ipfs
curl --location 'http://127.0.0.1:9100/ipfs/transaction' \
--header 'Content-Type: application/json' \
--data '{
    "model": 222,
    "timestamp": "2012-04-23T18:25:43.511Z",
    "request": {
        "p1": 2
    },
    "response": {
        "r1": "response data"
    }
}'

# CHAIN
curl http://127.0.0.1:9200/chain

curl --location 'http://127.0.0.1:9200/chain/updateModelUsageInfo' \
--header 'Content-Type: application/json' \
--data '{
    "model_address": "0123123123",
    "usage_info": "encrypted_usage"
}'
```

## Build module 

```shell
python3 -m build
```

## install & run module
```shell
mkdir balanceai
cd balanceai
python3.12 -m venv venv
source venv/bin/activate
pip install ../../dist/balanceai-0.0.2.tar.gz

balanceai init
balanceai dev
```

## Args & Parse

```shell
balanceai dev
balanceai zkml
balanceai help

```
