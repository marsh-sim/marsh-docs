# Node development

Every component of the simulator should be a separate node. The nodes have to publish a [HEARTBEAT](https://mavlink.io/en/messages/common.html#HEARTBEAT) message according to [Heartbeat/Connection Protocol](https://mavlink.io/en/services/heartbeat.html).

For any node-specific feature the workflow is as follows:

1. Check if there is already a relevant convention for a feature in [Microservices](https://mavlink.io/en/services/) section of Dev Guide
    - If nothing was found, search the [Common Message Set](https://mavlink.io/en/messages/common.html)
2. Read documentation for the service: e.g. [Parameter Protocol](https://mavlink.io/en/services/parameter.html)
3. Read documentation for specific messages: e.g. [SIM_STATE (#108)](https://mavlink.io/en/messages/common.html#SIM_STATE)
