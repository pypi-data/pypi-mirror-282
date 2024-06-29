import warnings

from ...application_base import JupyterKernelsBaseApp


class KernelTerminateApp(JupyterKernelsBaseApp):
    """Kernel Terminate application."""

    description = """
      An application to terminate a Kernel.

      jupyter kernels terminate SERVER_NAME
    """

    def start(self):
        """Start the app."""
        if len(self.extra_args) > 1:  # pragma: no cover
            warnings.warn("Too many arguments were provided for kernel list.")
            self.print_help()
            self.exit(1)

        server_name = self.extra_args[0]

        self._fetch(
            "{}/api/jupyter/v1/kernel/{}".format(self.cloud_base_url, server_name),
            method="DELETE",
        )
        self.log.info(f"Kernel '{server_name}' deleted.")
