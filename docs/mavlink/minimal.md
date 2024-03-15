# Minimal Set

These are the messages which must be supported by any MAVLink system, reproduced from the original documentation at [mavlink.io – MAVLink Minimal Set](https://mavlink.io/en/messages/minimal.html).

The HEARTBEAT message is of special interest here, since it is used to communicate the node state to and from the [Manager](../manager/README.md) application.

Generally the nodes in the simulator system are expected to send MAV_AUTOPILOT_INVALID. When choosing a component id, first see if there is a more specific one in [MARSH_COMPONENT_ID](./marsh.md), otherwise use the standard values here.

<!-- markdownlint-disable -->
<!-- AUTO-GENERATED PART BELOW, DO NOT MODIFY BY HAND -->
