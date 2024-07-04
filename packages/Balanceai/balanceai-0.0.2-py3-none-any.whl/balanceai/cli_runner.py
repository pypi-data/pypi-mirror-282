import argparse


parser = argparse.ArgumentParser(prog='balanceai',
                                 description='BalanceAI Wrapper enables connection of AI models (API endpoints to AI models) to the BalanceAI blockchain. Wrapper is a Python utility (command-line tools and libraries) that wraps API calls from locally run model APIs, exposing them to BalanceAI users. It provides security by validating requests from authenticated users, checking authorization, and storing information about requests/responses on-chain and in the InterPlanetary File System (IPFS).',
                                 epilog='More information at: https://docs.balanceai.network/')


def handle_help(args):
    print("HELP")
    parser.print_help()


def handle_init(args):
    import balanceai.init.Init as Init
    Init.init(args.config)


def handle_validate(args):
    import balanceai.validate.Validate as Validate
    Validate.validate()


def handle_dev(args):
    import balanceai.wrapper.server as server
    server.run('dev', args.config)


def handle_run(args):
    import balanceai.wrapper.server as server
    server.run('prod', args.config)


def handle_docker(args):
    import balanceai.wrapper.docker.Docker as Docker
    Docker.docker()


def handle_zkml(args):
    import balanceai.zkml.Zkml as Zkml
    Zkml.run(args.x, args.y, args.z)


def handle_huggingface(args):
    import balanceai.huggingface.server as server
    server.run('dev', args.config)


def run():  # import sys
    # https://docs.python.org/3/library/argparse.html#argumentparser-objects
    subparsers = parser.add_subparsers(title='TODO subcommands',
                                       description='TODO valid subcommands',
                                       help='TODO sub-command help')

    parser_help = subparsers.add_parser('help', aliases=['h'], help='Help')
    parser_help.set_defaults(func=handle_help)

    parser_init = subparsers.add_parser('init', aliases=['i'],
                                        help='Initialize project structure, generate sample configuration.')
    parser_init.add_argument('--config', type=str, default='wrapper_config.json',
                            help='name of generated configuration file')
    parser_init.set_defaults(func=handle_init)

    parser_validate = subparsers.add_parser('validate', aliases=['v'], help='Validates configuration.')
    parser_validate.set_defaults(func=handle_validate)

    parser_dev = subparsers.add_parser('dev', aliases=['d'], help='Run system in DEV mode.')
    parser_dev.add_argument('--config', type=str, default='wrapper_config.json', help='path to configuration file')
    parser_dev.set_defaults(func=handle_dev)

    parser_run = subparsers.add_parser('run', aliases=['r'], help='Run system in PROD mode.')
    parser_run.add_argument('--config', type=str, default='wrapper_config.json', help='path to configuration file')
    parser_run.set_defaults(func=handle_run)

    parser_docker = subparsers.add_parser('docker', help='Generate Docker image (requires docker installed)')
    parser_docker.set_defaults(func=handle_docker)

    parser_zkml = subparsers.add_parser('zkml', aliases=['z'], help='TODO zkml help Lorem Ipsum')
    parser_zkml.add_argument('x', type=str, help='zkml x {val}')
    parser_zkml.add_argument('y', type=str, help='zkml y {val}')
    parser_zkml.add_argument('z', type=str, help='zkml z {val}')
    parser_zkml.set_defaults(func=handle_zkml)

    parser_huggingface = subparsers.add_parser('huggingface', aliases=['hf'], help='Running AI Model Node connected to Huggingface')
    parser_huggingface.add_argument('--config', type=str, default='wrapper_config.json', help='path to configuration file')
    parser_huggingface.set_defaults(func=handle_huggingface)

    args = parser.parse_args()

    if args.__contains__('func'):
        args.func(args)
    else:
        parser.print_usage()


if __name__ == '__main__':
    print("cli_runner __main__")
    run()
