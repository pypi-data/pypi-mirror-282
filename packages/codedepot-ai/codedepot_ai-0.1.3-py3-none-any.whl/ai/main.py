import argparse

from ai.config import AIConfig
import ai.api as api


def parse_args():
    # Create the top-level parser
    parser = argparse.ArgumentParser(
        description="Command line tool for managing jobs, clusters, and providers.")
    parser.add_argument('--version', action='store_true',
                        help='Print the version of the tool')
    # Create subparsers for the main commands
    subparsers = parser.add_subparsers(dest='command', help='Main commands')

    # Subparser for the 'login' command
    login_parser = subparsers.add_parser('login', help='Log into the system')

    # Subparser for the 'job' command
    job_parser = subparsers.add_parser('job', help='Job operations')
    job_subparsers = job_parser.add_subparsers(
        dest='job_command', help='Job sub-commands')

    # Sub-commands under 'job'
    job_run_parser = job_subparsers.add_parser('run', help='Run a job')
    job_run_parser.add_argument(
        'cluster_name', help='Name of the cluster used to run the job.')
    job_subparsers.add_parser('list', help='List all jobs')
    job_stop_parser = job_subparsers.add_parser('stop', help='Stop a job')
    job_stop_parser.add_argument('name', help='Name of the job to stop')
    job_log_parser = job_subparsers.add_parser('log', help='Get the log of a job')
    job_log_parser.add_argument('name', help='Name of the job to get the log of')
    # Subparser for the 'cluster' command
    cluster_parser = subparsers.add_parser(
        'cluster', help='Cluster operations')
    cluster_subparsers = cluster_parser.add_subparsers(
        dest='cluster_command', help='Cluster sub-commands')

    # Sub-commands under 'cluster'
    cluster_create_parser = cluster_subparsers.add_parser(
        'create', help='Create a cluster')
    cluster_create_parser.add_argument(
        'spec', help='Filename of the cluster configuration')
    cluster_subparsers.add_parser('list', help='List all clusters')

    # Subparser for the 'provider' command
    provider_parser = subparsers.add_parser(
        'provider', help='Provider operations')
    provider_subparsers = provider_parser.add_subparsers(
        dest='provider_command', help='Provider sub-commands')

    # Sub-commands under 'provider'
    provider_create_parser = provider_subparsers.add_parser(
        'create', help='Create a provider')
    provider_create_parser.add_argument(
        'spec', help='Filename of the provider configuration')
    provider_subparsers.add_parser('list', help='List all providers')
    provider_subparsers.add_parser(
        'list_types', help='List available providers')

    # Subparser for the keys command
    key_parser = subparsers.add_parser('key', help='SshKey operations')
    key_subparsers = key_parser.add_subparsers(
        dest='key_command', help='SshKey sub-commands')
    key_create_parser = key_subparsers.add_parser('create', help='Create a new ssh key')
    key_create_parser.add_argument('name', help='Name of the key')
    key_create_parser.add_argument('path', help='Path to the private key file in the OpenSSH format')
    key_remove_parser = key_subparsers.add_parser('delete', help='Remove an ssh key')
    key_remove_parser.add_argument('name', help='Name of the key to remove')
    key_subparsers.add_parser('list', help='List all ssh keys')
    key_subparsers.add_parser('refresh_managed', help='Generate a new managed ssh key and register it with codedeot.ai')
    # Parse the arguments
    return parser.parse_args()



def main():
    args = parse_args()
    if args.version:
        print("0.1.3")
        return

    if args.command == 'login':
        AIConfig.create()
        return

    config = AIConfig.default()
    if not config:
        print("Please log in by running `ai login` first.")
        return

    if args.command == 'job':
        if args.job_command == 'run':
            api.start_job(config, args.cluster_name)
        elif args.job_command == 'list':
            api.list_jobs(config)
        elif args.job_command == 'stop':
            print(f"Stopping job {args.name}...")
            api.stop_job(config, args.name)
        elif args.job_command == 'log':
            print(f"Getting log for job {args.name}...")
            api.log(config, args.name)
    elif args.command == 'cluster':
        if args.cluster_command == 'create':
            print(f"Creating cluster from {args.spec}...")
            api.create_cluster(config, args.spec)
        elif args.cluster_command == 'list':
            api.list_clusters(config)
    elif args.command == 'provider':
        if args.provider_command == 'create':
            print(f"Creating provider from spec {args.spec}...")
            api.create_provider(config, args.spec)
        elif args.provider_command == 'list':
            api.list_providers(config)
        elif args.provider_command == 'list_types':
            api.list_provider_types(config)
    elif args.command == 'key':
        if args.key_command == 'create':
            api.create_ssh_key(config, args.name, args.path)
        elif args.key_command == 'delete':
            print(f"Deleting key {args.name}...")
            api.delete_ssh_key(config, args.name)
        elif args.key_command == 'list':
            api.list_ssh_keys(config)
        elif args.key_command == 'refresh_managed':
            api.refresh_managed_ssh_key(config)
if __name__ == "__main__":
    main()
