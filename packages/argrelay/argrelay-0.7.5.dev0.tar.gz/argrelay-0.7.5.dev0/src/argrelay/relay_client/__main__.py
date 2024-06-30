# Keep minimal import on start:
import sys

from argrelay.client_spec.ShellContext import ShellContext
from argrelay.enum_desc.CompType import CompType
from argrelay.misc_helper_common import get_config_path
from argrelay.misc_helper_common.ElapsedTime import ElapsedTime
from argrelay.runtime_data.ClientConfig import ClientConfig
from argrelay.runtime_data.ConnectionConfig import ConnectionConfig

ElapsedTime.measure("after_program_entry")


def main():
    ElapsedTime.measure("after_initial_imports")

    file_path = get_config_path("argrelay_client.json")
    client_config = load_client_config(file_path)
    ElapsedTime.measure("after_loading_client_config")

    shell_ctx = ShellContext.from_env(sys.argv)
    shell_ctx.print_debug()
    call_ctx = shell_ctx.create_call_context()

    # TODO: Init all client pipeline components via single logic - avoid splitting across files if reused.
    is_split_mode: bool = (
        # FS_14_59_14_06 pending requests: at the moment the process is split only to provide spinner:
        client_config.show_pending_spinner
        and
        shell_ctx.comp_type is not CompType.InvokeAction
    )

    pipe_end = None
    if is_split_mode:
        from argrelay.relay_client.proc_split import split_process
        (
            is_parent,
            child_pid,
            pipe_end,
        ) = split_process()

        if is_parent:
            pipe_dst_receiver = None
            from argrelay.client_pipeline.PipeDstReceiverAbstract import PipeDstReceiverAbstract
            from argrelay.enum_desc.ServerAction import ServerAction
            if (
                call_ctx.server_action is ServerAction.ProposeArgValues
                and
                client_config.optimize_completion_request
            ):
                from argrelay.client_pipeline.BytesHandlerTextProposeArgValuesRemoteOptimized import (
                    PipeDstReceiverTextProposeArgValuesRemoteOptimized,
                )
                pipe_dst_receiver = PipeDstReceiverAbstract(
                    PipeDstReceiverTextProposeArgValuesRemoteOptimized(),
                    child_pid,
                    pipe_end,
                    client_config,
                    shell_ctx,
                )
            else:
                from argrelay.client_pipeline.BytesHandlerJson import BytesHandlerJson
                from argrelay.relay_client.RemoteClientCommandFactory import RemoteClientCommandFactory
                pipe_dst_receiver = PipeDstReceiverAbstract(
                    BytesHandlerJson(
                        RemoteClientCommandFactory.select_response_handler(
                            call_ctx.server_action,
                        ),
                    ),
                    child_pid,
                    pipe_end,
                    client_config,
                    shell_ctx,
                )
            pipe_dst_receiver.receive_bytes()
            return

    from argrelay.relay_client.proc_worker import worker_main
    command_obj = worker_main(
        call_ctx,
        client_config,
        shell_ctx,
        pipe_end,
        is_split_mode,
    )
    return command_obj


def load_client_config(file_path):
    import json
    with open(file_path) as config_file:
        client_config_dict = json.load(config_file)
    client_config = client_config_dict_to_object(client_config_dict)
    return client_config


def client_config_dict_to_object(client_config_dict):
    """
    Optimized dict -> object conversion avoiding import of `*Schema` for performance:
    """
    client_config = ClientConfig(
        __comment__ = client_config_dict.get("use_local_requests", None),
        use_local_requests = client_config_dict.get("use_local_requests", False),
        optimize_completion_request = client_config_dict.get("optimize_completion_request", True),
        connection_config = ConnectionConfig(
            server_host_name = client_config_dict["connection_config"]["server_host_name"],
            server_port_number = client_config_dict["connection_config"]["server_port_number"],
        ),
        show_pending_spinner = client_config_dict.get("show_pending_spinner", True),
        spinless_sleep_sec = client_config_dict.get("spinless_sleep_sec", 0.0),
    )
    return client_config


if __name__ == "__main__":
    main()
