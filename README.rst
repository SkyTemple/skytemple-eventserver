|logo|

SkyTemple Eventserver
=====================

|build| |pypi-version| |pypi-downloads| |pypi-license| |pypi-pyversions| |discord|

.. |logo| image:: https://raw.githubusercontent.com/SkyTemple/skytemple/master/skytemple/data/icons/hicolor/256x256/apps/skytemple.png

.. |build| image:: https://img.shields.io/github/workflow/status/SkyTemple/skytemple-eventserver/Build,%20test%20and%20publish
    :target: https://pypi.org/project/skytemple-eventserver/
    :alt: Build Status

.. |pypi-version| image:: https://img.shields.io/pypi/v/skytemple-eventserver
    :target: https://pypi.org/project/skytemple-eventserver/
    :alt: Version

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/skytemple-eventserver
    :target: https://pypi.org/project/skytemple-eventserver/
    :alt: Downloads

.. |pypi-license| image:: https://img.shields.io/pypi/l/skytemple-eventserver
    :alt: License (GPLv3)

.. |pypi-pyversions| image:: https://img.shields.io/pypi/pyversions/skytemple-eventserver
    :alt: Supported Python versions

.. |discord| image:: https://img.shields.io/discord/710190644152369162?label=Discord
    :target: https://discord.gg/skytemple
    :alt: Discord

.. |kofi| image:: https://www.ko-fi.com/img/githubbutton_sm.svg
    :target: https://ko-fi.com/I2I81E5KH
    :alt: Ko-Fi

Websocket server that emits all of the events of SkyTemples event system via JSON to all connected clients.

Listens on port 45546.

All events are emitted using the following JSON object:

- ``event``: Name of the event
- ``args``: All positional arguments passed with the event (as an array).
- ``kwargs``: All keyword arguments passed with the event (as an object).

As of writing there is no documentation on which events exist yet, but if there is in the
future, you will find it in the main SkyTemple repository, most likely inside the "docs"
subdirectory.

|kofi|
