# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from taskgraph.transforms.base import TransformSequence

from xpi_taskgraph.xpi_manifest import get_manifest

transforms = TransformSequence()

@transforms.add
def version_bump(config, tasks):
    for task in tasks:
        manifest = get_manifest()
        xpi_name = task["attributes"]["matrix"]["xpi-name"]
        xpi_manifest = manifest[xpi_name]
        if "version-bump" not in xpi_manifest:
            continue
        breakpoint()
        for action in task["worker"]["actions"]:
            if action.get("version-bump") is not None:
                action["version-bump"]["bump-files"] = [xpi_manifest["version-bump"]["path"]]
        yield task
