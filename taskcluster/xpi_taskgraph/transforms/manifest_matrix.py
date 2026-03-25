from copy import deepcopy

from taskgraph.transforms.base import TransformSequence

from xpi_taskgraph.xpi_manifest import get_manifest

transforms = TransformSequence()

@transforms.add
def add_manifest_matrix(config, tasks):
    manifests = get_manifest()
    only_addon_types = None #config.get("only-for-addon-types")

    for task in tasks:
        from_manifests = task.pop("from-manifests")
        if not from_manifests:
            yield task
            continue

        for xpi_name in manifests:
            if only_addon_types and manifests[xpi_name]["addon-type"] not in only_addon_types:
                continue
            task.setdefault("matrix", {}).setdefault("xpi-name", []).append(xpi_name)
        yield task
