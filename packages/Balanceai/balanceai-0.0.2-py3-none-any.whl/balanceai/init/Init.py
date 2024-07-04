import json
import os


def init(config_filename):
    print(f"Initializing configuration: [{config_filename}]")

    config_template = ({
        "wrapper": {

            "bai": {
                "port": 9000,
                "debug": True
            },
            "chain": {
                "url": {
                    "auth": "http://127.0.0.1:9200/chain/authorize",
                    "update_usage": "http://127.0.0.1:9200/chain/updateModelUsageInfo"
                }
            },
            "ai": {
                "url": {
                    "model": "http://127.0.0.1:9300/ai/"
                }
            },
            "ipfs": {
                "url": {
                    "transaction": "http://127.0.0.1:9100/ipfs/transaction"
                }
            }
        },
        "huggingface": {
            "api_token": "",
            "model_id":"",
            "model_context":""
        }
    })

    try:
        if os.path.exists(config_filename):
            print(f'[ERROR] File already exists, please remove or rename [{config_filename}]')
        else:
            with open(config_filename, 'w', encoding='utf-8') as f:
                json.dump(config_template, f, ensure_ascii=False, indent=4)
            print(f"Initialized configuration file: [{config_filename}]")

    except OSError as e:
        print('Error when initializing configuration:', e)
        return None


