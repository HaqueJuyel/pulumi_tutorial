import pulumi
from pulumi_gcp import compute
import sys 
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'config')))
import variables

network=compute.Network(
    "pulumi-network",
    auto_create_subnetworks=True,
)
firelwall=compute.Firewall(
    "pulumi-firewall",
    network=network.id,
    allows=[
        {
            "protocol":"tcp",
            "ports":["22"],
        }
    ],
    source_ranges=["0.0.0.0/0"],
)

instance=compute.Instance(
    variables.INSTANCE_NAME,
    machine_type=variables.MACHINE_TYPE,
    zone=variables.ZONE,
    boot_disk=compute.InstanceBootDiskArgs(
        initialize_params=compute.InstanceBootDiskInitializeParamsArgs(
            image="projects/ubuntu-os-cloud/global/images/family/ubuntu-2004-lts",
        ),
    ),
    network_interfaces=[
        compute.InstanceNetworkInterfaceArgs(
            network=network.id,
            access_configs=[
                compute.InstanceNetworkInterfaceAccessConfigArgs()
            ],
        )
    ],
)
pulumi.export("Instance Name:::::",instance.name)
pulumi.export("Instance IP:::::::",instance.network_interfaces[0].access_configs[0].nat_ip)