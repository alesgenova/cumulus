from cumulus.celery import command
import ansible.playbook
from ansible import callbacks
import os


@command.task
def launch_cluster(cluster, profile, secret_key, girder_token, log_write_url):

    playbook_path = os.path.dirname(__file__) + "/../playbooks/default.yml"
    stats = callbacks.AggregateStats()

    extra_vars = {
        "girder_token": girder_token,
        "log_write_url": log_write_url,
        "cluster_region": profile['regionName'],
        "cluster_state": "running",
        "aws_access_key": profile['accessKeyId'],
        "aws_secret_key": secret_key
    }

    pb = ansible.playbook.PlayBook(
        playbook=playbook_path,
        inventory=ansible.inventory.Inventory(['localhost']),
        callbacks=callbacks.PlaybookCallbacks(verbose=1),
        runner_callbacks=callbacks.PlaybookRunnerCallbacks(stats, verbose=1),
        stats=stats,
        extra_vars=extra_vars
    )

    # Note:  can refer to callback.playbook.extra_vars  to get access
    # to girder_token after this point

    pb.run()


@command.task
def terminate_cluster(cluster, profile, secret_key,
                      girder_token, log_write_url):

    playbook_path = os.path.dirname(__file__) + "/../playbooks/default.yml"
    stats = callbacks.AggregateStats()

    extra_vars = {
        "girder_token": girder_token,
        "log_write_url": log_write_url,
        "cluster_region": profile['regionName'],
        "cluster_state": "absent",
        "aws_access_key": profile['accessKeyId'],
        "aws_secret_key": secret_key
    }

    pb = ansible.playbook.PlayBook(
        playbook=playbook_path,
        inventory=ansible.inventory.Inventory(['localhost']),
        callbacks=callbacks.PlaybookCallbacks(verbose=1),
        runner_callbacks=callbacks.PlaybookRunnerCallbacks(stats, verbose=1),
        stats=stats,
        extra_vars=extra_vars
    )

    # Note:  can refer to callback.playbook.extra_vars  to get access
    # to girder_token after this point

    pb.run()
