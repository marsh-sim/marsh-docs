# Subset of Common Set

These messages are reproduced from the original documentation at [mavlink.io – MAVLink Common Message Set](https://mavlink.io/en/messages/common.html). This is **only a subset of the full list**, including only messages used in the MARSH project, to make the protocol less overwhelming.

Before designing a new message, first check the original documentation linked above. If you find a useful message in the common set, consider [editing](https://github.com/marsh-sim/marsh-sim.github.io/edit/main/docs/mavlink/common_subset.txt) the [list of identifiers](./common_subset.txt) used for generating this page.

<!-- markdownlint-disable -->
<!-- AUTO-GENERATED PART BELOW, DO NOT MODIFY BY HAND -->

---

Generated on 2024-03-15T01:36:59 from commit [a272aa9](https://github.com/marsh-sim/mavlink/tree/a272aa9a26f9607a8c0115fde948ffe2d2505a38)

<html>
 <body>
  <p>
   <strong>MAVLink Include Files:</strong>
   <a href="standard.md">standard.xml</a>
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
 </body>
</html>
