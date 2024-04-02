# Subset of Common Set

These messages are reproduced from the original documentation at [mavlink.io – MAVLink Common Message Set](https://mavlink.io/en/messages/common.html). This is **only a subset of the full list**, including only messages used in the MARSH project, to make the protocol less overwhelming.

Before designing a new message, first check the original documentation linked above. If you find a useful message in the common set, consider [editing](https://github.com/marsh-sim/marsh-sim.github.io/edit/main/docs/mavlink/common_subset.txt) the [list of identifiers](./common_subset.txt) used for generating this page.

## Conventions

Message [MANUAL_SETPOINT](#MANUAL_SETPOINT) is used for desired control positions (as displayed in [Lidia](https://pypi.org/project/lidia/)), so the values for all fields should be treated as normalized controls positions between -1 and 1 instead of rad/s.
It is not supported by ArduPilot at all, and only used for Rover in PX4, so no collisions are expected.

Message [RAW_RPM](#RAW_RPM) for helicopters should send rotor with index 0, and then engines in order.

<!-- markdownlint-disable -->
<!-- AUTO-GENERATED PART BELOW, DO NOT MODIFY BY HAND -->

## Definition list

Generated on 2024-04-02T17:46:25 from commit [192aaee](https://github.com/marsh-sim/mavlink/tree/192aaeebd3655fb3c663cb1ac07a89d5ab2cd209)

<ul>
 <li><a href="#enums">Enums</a><ul>
  <li><a href="#MAV_PARAM_TYPE">MAV_PARAM_TYPE</a></li>
  <li><a href="#MAV_SEVERITY">MAV_SEVERITY</a></li>
 </ul></li>
 <li><a href="#mav_commands">Mav Commands</a><ul>
 </ul></li>
 <li><a href="#messages">Messages</a><ul>
  <li><a href="#PARAM_REQUEST_READ">PARAM_REQUEST_READ</a></li>
  <li><a href="#PARAM_REQUEST_LIST">PARAM_REQUEST_LIST</a></li>
  <li><a href="#PARAM_VALUE">PARAM_VALUE</a></li>
  <li><a href="#PARAM_SET">PARAM_SET</a></li>
  <li><a href="#MANUAL_CONTROL">MANUAL_CONTROL</a></li>
  <li><a href="#MANUAL_SETPOINT">MANUAL_SETPOINT</a></li>
  <li><a href="#SIM_STATE">SIM_STATE</a></li>
  <li><a href="#STATUSTEXT">STATUSTEXT</a></li>
  <li><a href="#RAW_RPM">RAW_RPM</a></li>
 </ul></li>
</ul>
<html>
 <body>
  <p>
   <strong>MAVLink Include Files:</strong>
   <a href="https://mavlink.io/en/messages/standard.html">standard.xml</a>
  </p>
  <h2>MAVLink Protocol Version</h2>
  <p>The current MAVLink version is 2.3. The minor version numbers (after the dot) range from 1-255.</p>
  <p>This file has protocol dialect: 0.</p>
  <h2 id="enums">MAVLink Type Enumerations</h2>
  <h3 id="MAV_PARAM_TYPE">MAV_PARAM_TYPE</h3>
  <p>
   <a href="#enums">
    [Enum]
   </a>Specifies the datatype of a MAVLink parameter.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="MAV_PARAM_TYPE_UINT8">
     <td>1</td>
     <td>
      <a href="#MAV_PARAM_TYPE_UINT8">MAV_PARAM_TYPE_UINT8</a>
     </td>
     <td>8-bit unsigned integer</td>
    </tr>
    <tr id="MAV_PARAM_TYPE_INT8">
     <td>2</td>
     <td>
      <a href="#MAV_PARAM_TYPE_INT8">MAV_PARAM_TYPE_INT8</a>
     </td>
     <td>8-bit signed integer</td>
    </tr>
    <tr id="MAV_PARAM_TYPE_UINT16">
     <td>3</td>
     <td>
      <a href="#MAV_PARAM_TYPE_UINT16">MAV_PARAM_TYPE_UINT16</a>
     </td>
     <td>16-bit unsigned integer</td>
    </tr>
    <tr id="MAV_PARAM_TYPE_INT16">
     <td>4</td>
     <td>
      <a href="#MAV_PARAM_TYPE_INT16">MAV_PARAM_TYPE_INT16</a>
     </td>
     <td>16-bit signed integer</td>
    </tr>
    <tr id="MAV_PARAM_TYPE_UINT32">
     <td>5</td>
     <td>
      <a href="#MAV_PARAM_TYPE_UINT32">MAV_PARAM_TYPE_UINT32</a>
     </td>
     <td>32-bit unsigned integer</td>
    </tr>
    <tr id="MAV_PARAM_TYPE_INT32">
     <td>6</td>
     <td>
      <a href="#MAV_PARAM_TYPE_INT32">MAV_PARAM_TYPE_INT32</a>
     </td>
     <td>32-bit signed integer</td>
    </tr>
    <tr id="MAV_PARAM_TYPE_UINT64">
     <td>7</td>
     <td>
      <a href="#MAV_PARAM_TYPE_UINT64">MAV_PARAM_TYPE_UINT64</a>
     </td>
     <td>64-bit unsigned integer</td>
    </tr>
    <tr id="MAV_PARAM_TYPE_INT64">
     <td>8</td>
     <td>
      <a href="#MAV_PARAM_TYPE_INT64">MAV_PARAM_TYPE_INT64</a>
     </td>
     <td>64-bit signed integer</td>
    </tr>
    <tr id="MAV_PARAM_TYPE_REAL32">
     <td>9</td>
     <td>
      <a href="#MAV_PARAM_TYPE_REAL32">MAV_PARAM_TYPE_REAL32</a>
     </td>
     <td>32-bit floating-point</td>
    </tr>
    <tr id="MAV_PARAM_TYPE_REAL64">
     <td>10</td>
     <td>
      <a href="#MAV_PARAM_TYPE_REAL64">MAV_PARAM_TYPE_REAL64</a>
     </td>
     <td>64-bit floating-point</td>
    </tr>
   </tbody>
  </table>
  <h3 id="MAV_SEVERITY">MAV_SEVERITY</h3>
  <p>
   <a href="#enums">
    [Enum]
   </a>Indicates the severity level, generally used for status messages to indicate their relative urgency. Based on RFC-5424 using expanded definitions at: http://www.kiwisyslog.com/kb/info:-syslog-message-levels/.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="MAV_SEVERITY_EMERGENCY">
     <td>0</td>
     <td>
      <a href="#MAV_SEVERITY_EMERGENCY">MAV_SEVERITY_EMERGENCY</a>
     </td>
     <td>System is unusable. This is a "panic" condition.</td>
    </tr>
    <tr id="MAV_SEVERITY_ALERT">
     <td>1</td>
     <td>
      <a href="#MAV_SEVERITY_ALERT">MAV_SEVERITY_ALERT</a>
     </td>
     <td>Action should be taken immediately. Indicates error in non-critical systems.</td>
    </tr>
    <tr id="MAV_SEVERITY_CRITICAL">
     <td>2</td>
     <td>
      <a href="#MAV_SEVERITY_CRITICAL">MAV_SEVERITY_CRITICAL</a>
     </td>
     <td>Action must be taken immediately. Indicates failure in a primary system.</td>
    </tr>
    <tr id="MAV_SEVERITY_ERROR">
     <td>3</td>
     <td>
      <a href="#MAV_SEVERITY_ERROR">MAV_SEVERITY_ERROR</a>
     </td>
     <td>Indicates an error in secondary/redundant systems.</td>
    </tr>
    <tr id="MAV_SEVERITY_WARNING">
     <td>4</td>
     <td>
      <a href="#MAV_SEVERITY_WARNING">MAV_SEVERITY_WARNING</a>
     </td>
     <td>Indicates about a possible future error if this is not resolved within a given timeframe. Example would be a low battery warning.</td>
    </tr>
    <tr id="MAV_SEVERITY_NOTICE">
     <td>5</td>
     <td>
      <a href="#MAV_SEVERITY_NOTICE">MAV_SEVERITY_NOTICE</a>
     </td>
     <td>An unusual event has occurred, though not an error condition. This should be investigated for the root cause.</td>
    </tr>
    <tr id="MAV_SEVERITY_INFO">
     <td>6</td>
     <td>
      <a href="#MAV_SEVERITY_INFO">MAV_SEVERITY_INFO</a>
     </td>
     <td>Normal operational messages. Useful for logging. No action is required for these messages.</td>
    </tr>
    <tr id="MAV_SEVERITY_DEBUG">
     <td>7</td>
     <td>
      <a href="#MAV_SEVERITY_DEBUG">MAV_SEVERITY_DEBUG</a>
     </td>
     <td>Useful non-operational messages that can assist in debugging. These should not occur during normal operation.</td>
    </tr>
   </tbody>
  </table>
  <a id="MAV_CMD">
  </a>
  <h2 id="mav_commands">MAVLink Commands (<a href="#mav_commands">MAV_CMD</a>)</h2>
  <blockquote class="alert alert-info clearfix">
   <strong class="fa fa-2x fa-edit">
   </strong>
   <p>MAVLink commands (<a href="#mav_commands">MAV_CMD</a>) and messages are different! These commands define the values of up to 7 parameters that are packaged INSIDE specific messages used in the Mission Protocol and Command Protocol. Use commands for actions in missions or if you need acknowledgment and/or retry logic from a request. Otherwise use messages.</p>
  </blockquote>
  <p>Commands to be executed by the MAV. They can be executed on user request, or as part of a mission script. If the action is used in a mission, the parameter mapping to the waypoint/mission message is as follows: Param 1, Param 2, Param 3, Param 4, X: Param 5, Y:Param 6, Z:Param 7. This command list is similar what ARINC 424 is for commercial aircraft: A data format how to interpret waypoint/mission data. NaN and INT32_MAX may be used in float/integer params (respectively) to indicate optional/default values (e.g. to use the component's current yaw or latitude rather than a specific value). See https://mavlink.io/en/guide/xml_schema.html#MAV_CMD for information about the structure of the <a href="#mav_commands">MAV_CMD</a> entries</p>
  <h2 id="messages">MAVLink Messages</h2>
  <h3 id="PARAM_REQUEST_READ">PARAM_REQUEST_READ (<a href="#PARAM_REQUEST_READ">
    #20
   </a>
   )
  </h3>
  <p>
   <a href="#messages">
    [Message]
   </a>Request to read the onboard parameter with the param_id string id. Onboard parameters are stored as key[const char*] -&gt; value[float]. This allows to send a parameter to any other component (such as the GCS) without the need of previous knowledge of possible parameter names. Thus the same GCS can store different parameters for different autopilots. See also https://mavlink.io/en/services/parameter.html for a full documentation of QGroundControl and IMU code.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>target_system</td>
     <td>uint8_t</td>
     <td>System ID</td>
    </tr>
    <tr>
     <td>target_component</td>
     <td>uint8_t</td>
     <td>Component ID</td>
    </tr>
    <tr>
     <td>param_id</td>
     <td>char[16]</td>
     <td>Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string</td>
    </tr>
    <tr>
     <td>param_index</td>
     <td>int16_t</td>
     <td>Parameter index. Send -1 to use the param ID field as identifier (else the param id will be ignored)</td>
    </tr>
   </tbody>
  </table>
  <h3 id="PARAM_REQUEST_LIST">PARAM_REQUEST_LIST (<a href="#PARAM_REQUEST_LIST">
    #21
   </a>
   )
  </h3>
  <p>
   <a href="#messages">
    [Message]
   </a>Request all parameters of this component. After this request, all parameters are emitted. The parameter microservice is documented at https://mavlink.io/en/services/parameter.html</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>target_system</td>
     <td>uint8_t</td>
     <td>System ID</td>
    </tr>
    <tr>
     <td>target_component</td>
     <td>uint8_t</td>
     <td>Component ID</td>
    </tr>
   </tbody>
  </table>
  <h3 id="PARAM_VALUE">PARAM_VALUE (<a href="#PARAM_VALUE">
    #22
   </a>
   )
  </h3>
  <p>
   <a href="#messages">
    [Message]
   </a>Emit the value of a onboard parameter. The inclusion of param_count and param_index in the message allows the recipient to keep track of received parameters and allows him to re-request missing parameters after a loss or timeout. The parameter microservice is documented at https://mavlink.io/en/services/parameter.html</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Values</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>param_id</td>
     <td>char[16]</td>
     <td>
     </td>
     <td>Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string</td>
    </tr>
    <tr>
     <td>param_value</td>
     <td>float</td>
     <td>
     </td>
     <td>Onboard parameter value</td>
    </tr>
    <tr>
     <td>param_type</td>
     <td>uint8_t</td>
     <td>
      <a href="#MAV_PARAM_TYPE">MAV_PARAM_TYPE</a>
     </td>
     <td>Onboard parameter type.</td>
    </tr>
    <tr>
     <td>param_count</td>
     <td>uint16_t</td>
     <td>
     </td>
     <td>Total number of onboard parameters</td>
    </tr>
    <tr>
     <td>param_index</td>
     <td>uint16_t</td>
     <td>
     </td>
     <td>Index of this onboard parameter</td>
    </tr>
   </tbody>
  </table>
  <h3 id="PARAM_SET">PARAM_SET (<a href="#PARAM_SET">
    #23
   </a>
   )
  </h3>
  <p>
   <a href="#messages">
    [Message]
   </a>Set a parameter value (write new value to permanent storage).
        The receiving component should acknowledge the new parameter value by broadcasting a <a href="#PARAM_VALUE">PARAM_VALUE</a> message (broadcasting ensures that multiple GCS all have an up-to-date list of all parameters). If the sending GCS did not receive a <a href="#PARAM_VALUE">PARAM_VALUE</a> within its timeout time, it should re-send the <a href="#PARAM_SET">PARAM_SET</a> message. The parameter microservice is documented at https://mavlink.io/en/services/parameter.html.
        <a href="#PARAM_SET">PARAM_SET</a> may also be called within the context of a transaction (started with <a href="#MAV_CMD_PARAM_TRANSACTION">MAV_CMD_PARAM_TRANSACTION</a>). Within a transaction the receiving component should respond with <a href="#PARAM_ACK_TRANSACTION">PARAM_ACK_TRANSACTION</a> to the setter component (instead of broadcasting <a href="#PARAM_VALUE">PARAM_VALUE</a>), and <a href="#PARAM_SET">PARAM_SET</a> should be re-sent if this is ACK not received.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Values</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>target_system</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>System ID</td>
    </tr>
    <tr>
     <td>target_component</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Component ID</td>
    </tr>
    <tr>
     <td>param_id</td>
     <td>char[16]</td>
     <td>
     </td>
     <td>Onboard parameter id, terminated by NULL if the length is less than 16 human-readable chars and WITHOUT null termination (NULL) byte if the length is exactly 16 chars - applications have to provide 16+1 bytes storage if the ID is stored as string</td>
    </tr>
    <tr>
     <td>param_value</td>
     <td>float</td>
     <td>
     </td>
     <td>Onboard parameter value</td>
    </tr>
    <tr>
     <td>param_type</td>
     <td>uint8_t</td>
     <td>
      <a href="#MAV_PARAM_TYPE">MAV_PARAM_TYPE</a>
     </td>
     <td>Onboard parameter type.</td>
    </tr>
   </tbody>
  </table>
  <h3 id="MANUAL_CONTROL">MANUAL_CONTROL (<a href="#MANUAL_CONTROL">
    #69
   </a>
   )
  </h3>
  <p>
   <a href="#messages">
    [Message]
   </a>This message provides an API for manually controlling the vehicle using standard joystick axes nomenclature, along with a joystick-like input device. Unused axes can be disabled and buttons states are transmitted as individual on/off bits of a bitmask</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>target</td>
     <td>uint8_t</td>
     <td>The system to be controlled.</td>
    </tr>
    <tr>
     <td>x</td>
     <td>int16_t</td>
     <td>X-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to forward(1000)-backward(-1000) movement on a joystick and the pitch of a vehicle.</td>
    </tr>
    <tr>
     <td>y</td>
     <td>int16_t</td>
     <td>Y-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to left(-1000)-right(1000) movement on a joystick and the roll of a vehicle.</td>
    </tr>
    <tr>
     <td>z</td>
     <td>int16_t</td>
     <td>Z-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to a separate slider movement with maximum being 1000 and minimum being -1000 on a joystick and the thrust of a vehicle. Positive values are positive thrust, negative values are negative thrust.</td>
    </tr>
    <tr>
     <td>r</td>
     <td>int16_t</td>
     <td>R-axis, normalized to the range [-1000,1000]. A value of INT16_MAX indicates that this axis is invalid. Generally corresponds to a twisting of the joystick, with counter-clockwise being 1000 and clockwise being -1000, and the yaw of a vehicle.</td>
    </tr>
    <tr>
     <td>buttons</td>
     <td>uint16_t</td>
     <td>A bitfield corresponding to the joystick buttons' 0-15 current state, 1 for pressed, 0 for released. The lowest bit corresponds to Button 1.</td>
    </tr>
    <tr>
     <td style="color:blue;">buttons2<a href="#mav2_extension_field" title="MAVLink2 extension field">
       **
      </a>
     </td>
     <td>uint16_t</td>
     <td>A bitfield corresponding to the joystick buttons' 16-31 current state, 1 for pressed, 0 for released. The lowest bit corresponds to Button 16.</td>
    </tr>
    <tr>
     <td style="color:blue;">enabled_extensions<a href="#mav2_extension_field" title="MAVLink2 extension field">
       **
      </a>
     </td>
     <td>uint8_t</td>
     <td>Set bits to 1 to indicate which of the following extension fields contain valid data: bit 0: pitch, bit 1: roll, bit 2: aux1, bit 3: aux2, bit 4: aux3, bit 5: aux4, bit 6: aux5, bit 7: aux6</td>
    </tr>
    <tr>
     <td style="color:blue;">s<a href="#mav2_extension_field" title="MAVLink2 extension field">
       **
      </a>
     </td>
     <td>int16_t</td>
     <td>Pitch-only-axis, normalized to the range [-1000,1000]. Generally corresponds to pitch on vehicles with additional degrees of freedom. Valid if bit 0 of enabled_extensions field is set. Set to 0 if invalid.</td>
    </tr>
    <tr>
     <td style="color:blue;">t<a href="#mav2_extension_field" title="MAVLink2 extension field">
       **
      </a>
     </td>
     <td>int16_t</td>
     <td>Roll-only-axis, normalized to the range [-1000,1000]. Generally corresponds to roll on vehicles with additional degrees of freedom. Valid if bit 1 of enabled_extensions field is set. Set to 0 if invalid.</td>
    </tr>
    <tr>
     <td style="color:blue;">aux1<a href="#mav2_extension_field" title="MAVLink2 extension field">
       **
      </a>
     </td>
     <td>int16_t</td>
     <td>Aux continuous input field 1. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 2 of enabled_extensions field is set. 0 if bit 2 is unset.</td>
    </tr>
    <tr>
     <td style="color:blue;">aux2<a href="#mav2_extension_field" title="MAVLink2 extension field">
       **
      </a>
     </td>
     <td>int16_t</td>
     <td>Aux continuous input field 2. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 3 of enabled_extensions field is set. 0 if bit 3 is unset.</td>
    </tr>
    <tr>
     <td style="color:blue;">aux3<a href="#mav2_extension_field" title="MAVLink2 extension field">
       **
      </a>
     </td>
     <td>int16_t</td>
     <td>Aux continuous input field 3. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 4 of enabled_extensions field is set. 0 if bit 4 is unset.</td>
    </tr>
    <tr>
     <td style="color:blue;">aux4<a href="#mav2_extension_field" title="MAVLink2 extension field">
       **
      </a>
     </td>
     <td>int16_t</td>
     <td>Aux continuous input field 4. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 5 of enabled_extensions field is set. 0 if bit 5 is unset.</td>
    </tr>
    <tr>
     <td style="color:blue;">aux5<a href="#mav2_extension_field" title="MAVLink2 extension field">
       **
      </a>
     </td>
     <td>int16_t</td>
     <td>Aux continuous input field 5. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 6 of enabled_extensions field is set. 0 if bit 6 is unset.</td>
    </tr>
    <tr>
     <td style="color:blue;">aux6<a href="#mav2_extension_field" title="MAVLink2 extension field">
       **
      </a>
     </td>
     <td>int16_t</td>
     <td>Aux continuous input field 6. Normalized in the range [-1000,1000]. Purpose defined by recipient. Valid data if bit 7 of enabled_extensions field is set. 0 if bit 7 is unset.</td>
    </tr>
   </tbody>
  </table>
  <h3 id="MANUAL_SETPOINT">MANUAL_SETPOINT (<a href="#MANUAL_SETPOINT">
    #81
   </a>
   )
  </h3>
  <p>
   <a href="#messages">
    [Message]
   </a>Setpoint in roll, pitch, yaw and thrust from the operator</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>time_boot_ms</td>
     <td>uint32_t</td>
     <td>ms</td>
     <td>Timestamp (time since system boot).</td>
    </tr>
    <tr>
     <td>roll</td>
     <td>float</td>
     <td>rad/s</td>
     <td>Desired roll rate</td>
    </tr>
    <tr>
     <td>pitch</td>
     <td>float</td>
     <td>rad/s</td>
     <td>Desired pitch rate</td>
    </tr>
    <tr>
     <td>yaw</td>
     <td>float</td>
     <td>rad/s</td>
     <td>Desired yaw rate</td>
    </tr>
    <tr>
     <td>thrust</td>
     <td>float</td>
     <td>
     </td>
     <td>Collective thrust, normalized to 0 .. 1</td>
    </tr>
    <tr>
     <td>mode_switch</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Flight mode switch position, 0.. 255</td>
    </tr>
    <tr>
     <td>manual_override_switch</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Override mode switch position, 0.. 255</td>
    </tr>
   </tbody>
  </table>
  <h3 id="SIM_STATE">SIM_STATE (<a href="#SIM_STATE">
    #108
   </a>
   )
  </h3>
  <p>
   <a href="#messages">
    [Message]
   </a>Status of simulation environment, if used</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>q1</td>
     <td>float</td>
     <td>
     </td>
     <td>True attitude quaternion component 1, w (1 in null-rotation)</td>
    </tr>
    <tr>
     <td>q2</td>
     <td>float</td>
     <td>
     </td>
     <td>True attitude quaternion component 2, x (0 in null-rotation)</td>
    </tr>
    <tr>
     <td>q3</td>
     <td>float</td>
     <td>
     </td>
     <td>True attitude quaternion component 3, y (0 in null-rotation)</td>
    </tr>
    <tr>
     <td>q4</td>
     <td>float</td>
     <td>
     </td>
     <td>True attitude quaternion component 4, z (0 in null-rotation)</td>
    </tr>
    <tr>
     <td>roll</td>
     <td>float</td>
     <td>rad</td>
     <td>Attitude roll expressed as Euler angles, not recommended except for human-readable outputs</td>
    </tr>
    <tr>
     <td>pitch</td>
     <td>float</td>
     <td>rad</td>
     <td>Attitude pitch expressed as Euler angles, not recommended except for human-readable outputs</td>
    </tr>
    <tr>
     <td>yaw</td>
     <td>float</td>
     <td>rad</td>
     <td>Attitude yaw expressed as Euler angles, not recommended except for human-readable outputs</td>
    </tr>
    <tr>
     <td>xacc</td>
     <td>float</td>
     <td>m/s/s</td>
     <td>X acceleration</td>
    </tr>
    <tr>
     <td>yacc</td>
     <td>float</td>
     <td>m/s/s</td>
     <td>Y acceleration</td>
    </tr>
    <tr>
     <td>zacc</td>
     <td>float</td>
     <td>m/s/s</td>
     <td>Z acceleration</td>
    </tr>
    <tr>
     <td>xgyro</td>
     <td>float</td>
     <td>rad/s</td>
     <td>Angular speed around X axis</td>
    </tr>
    <tr>
     <td>ygyro</td>
     <td>float</td>
     <td>rad/s</td>
     <td>Angular speed around Y axis</td>
    </tr>
    <tr>
     <td>zgyro</td>
     <td>float</td>
     <td>rad/s</td>
     <td>Angular speed around Z axis</td>
    </tr>
    <tr>
     <td>lat</td>
     <td>float</td>
     <td>deg</td>
     <td>Latitude (lower precision). Both this and the lat_int field should be set.</td>
    </tr>
    <tr>
     <td>lon</td>
     <td>float</td>
     <td>deg</td>
     <td>Longitude (lower precision). Both this and the lon_int field should be set.</td>
    </tr>
    <tr>
     <td>alt</td>
     <td>float</td>
     <td>m</td>
     <td>Altitude</td>
    </tr>
    <tr>
     <td>std_dev_horz</td>
     <td>float</td>
     <td>
     </td>
     <td>Horizontal position standard deviation</td>
    </tr>
    <tr>
     <td>std_dev_vert</td>
     <td>float</td>
     <td>
     </td>
     <td>Vertical position standard deviation</td>
    </tr>
    <tr>
     <td>vn</td>
     <td>float</td>
     <td>m/s</td>
     <td>True velocity in north direction in earth-fixed NED frame</td>
    </tr>
    <tr>
     <td>ve</td>
     <td>float</td>
     <td>m/s</td>
     <td>True velocity in east direction in earth-fixed NED frame</td>
    </tr>
    <tr>
     <td>vd</td>
     <td>float</td>
     <td>m/s</td>
     <td>True velocity in down direction in earth-fixed NED frame</td>
    </tr>
    <tr>
     <td style="color:blue;">lat_int<a href="#mav2_extension_field" title="MAVLink2 extension field">
       **
      </a>
     </td>
     <td>int32_t</td>
     <td>degE7</td>
     <td>Latitude (higher precision). If 0, recipients should use the lat field value (otherwise this field is preferred).</td>
    </tr>
    <tr>
     <td style="color:blue;">lon_int<a href="#mav2_extension_field" title="MAVLink2 extension field">
       **
      </a>
     </td>
     <td>int32_t</td>
     <td>degE7</td>
     <td>Longitude (higher precision). If 0, recipients should use the lon field value (otherwise this field is preferred).</td>
    </tr>
   </tbody>
  </table>
  <h3 id="STATUSTEXT">STATUSTEXT (<a href="#STATUSTEXT">
    #253
   </a>
   )
  </h3>
  <p>
   <a href="#messages">
    [Message]
   </a>Status text message. These messages are printed in yellow in the COMM console of QGroundControl. WARNING: They consume quite some bandwidth, so use only for important status and error messages. If implemented wisely, these messages are buffered on the MCU and sent only at a limited rate (e.g. 10 Hz).</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Values</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>severity</td>
     <td>uint8_t</td>
     <td>
      <a href="#MAV_SEVERITY">MAV_SEVERITY</a>
     </td>
     <td>Severity of status. Relies on the definitions within RFC-5424.</td>
    </tr>
    <tr>
     <td>text</td>
     <td>char[50]</td>
     <td>
     </td>
     <td>Status text message, without null termination character</td>
    </tr>
    <tr>
     <td style="color:blue;">id<a href="#mav2_extension_field" title="MAVLink2 extension field">
       **
      </a>
     </td>
     <td>uint16_t</td>
     <td>
     </td>
     <td>Unique (opaque) identifier for this statustext message.  May be used to reassemble a logical long-statustext message from a sequence of chunks.  A value of zero indicates this is the only chunk in the sequence and the message can be emitted immediately.</td>
    </tr>
    <tr>
     <td style="color:blue;">chunk_seq<a href="#mav2_extension_field" title="MAVLink2 extension field">
       **
      </a>
     </td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>This chunk's sequence number; indexing is from zero.  Any null character in the text field is taken to mean this was the last chunk.</td>
    </tr>
   </tbody>
  </table>
  <h3 id="RAW_RPM">RAW_RPM (<a href="#RAW_RPM">
    #339
   </a>
   )
  </h3>
  <p>
   <a href="#messages">
    [Message]
   </a>
   <strong>
    (MAVLink 2)
   </strong>RPM sensor data message.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>index</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Index of this RPM sensor (0-indexed)</td>
    </tr>
    <tr>
     <td>frequency</td>
     <td>float</td>
     <td>rpm</td>
     <td>Indicated rate</td>
    </tr>
   </tbody>
  </table>
 </body>
</html>
