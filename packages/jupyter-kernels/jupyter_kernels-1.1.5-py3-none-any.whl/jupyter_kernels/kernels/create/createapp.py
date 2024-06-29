import sys

from rich import print_json
from traitlets import Dict, Float, Unicode

from ...application_base import JupyterKernelsBaseApp, jupyter_kernels_aliases
from ..utils import display_kernels

create_alias = dict(jupyter_kernels_aliases)
create_alias["given-name"] = "KernelCreateApp.kernel_given_name"


class KernelCreateApp(JupyterKernelsBaseApp):
    """An application to create a kernel."""

    description = """
      An application to create the kernel.

      jupyter kernels create SPEC_ID [--given-name CUSTOM_NAME]
    """

    aliases = Dict(create_alias)

    kernel_given_name = Unicode(
        None, allow_none=True, config=True, help="Kernel custom name."
    )

    credits_limit = Float(
        None,
        allow_none=True,
        help="Maximal amount of credits that can be consumed by the kernels",
    )

    def start(self):
        """Start the app."""
        if len(self.extra_args) > 1:  # pragma: no cover
            self.log.warning("Too many arguments were provided for kernel create.")
            self.print_help()
            self.exit(1)
        environment_name = self.extra_args[0]
        body = {"kernel_type": "default"}
        if self.kernel_given_name:
            body["kernel_given_name"] = self.kernel_given_name

        if self.credits_limit is None:
            response = self._fetch(
                "{}/api/iam/v1/credits".format(self.cloud_base_url), method="GET"
            )
            raw = response.json()
            credits = raw["credits"]
            reservations = raw["reservations"]
            available = (
                credits["credits"]
                if credits.get("quota") is None
                else credits["quota"] - credits["credits"]
            )
            available -= sum(map(lambda r: r["credits"], reservations))
            self.credits_limit = max(0., available * 0.5)
            self.log.warning(
                "The kernel will be allowed to consumed half of your remaining credits; i.e. {:.2f}.".format(
                    self.credits_limit
                )
            )

        if self.credits_limit < sys.float_info.epsilon:
            self.log.warning("Credits reservation is not positive. Exiting…")
            self.exit(1)
        body["credits_limit"] = self.credits_limit

        response = self._fetch(
            "{}/api/jupyter/v1/environment/{}".format(
                self.cloud_base_url, environment_name
            ),
            method="POST",
            json=body,
        )
        raw = response.json()
        kernel = raw.get("kernel")
        if kernel:
            display_kernels([kernel])
        else:
            print_json(data=raw)
