# MARSH Dialect

This page documents all extensions to MAVLink that were required for the simulator.

The definitions are in the [marsh.xml file](https://github.com/marsh-sim/mavlink/blob/dialect/message_definitions/v1.0/marsh.xml) on the [`dialect` branch](https://github.com/marsh-sim/mavlink/tree/dialect) in our fork of main [MAVLink repository](https://github.com/mavlink/mavlink).
All other projects need to generate and appropriate libraries, following the [mavlink.io – Generating MAVLink Libraries](https://mavlink.io/en/getting_started/generate_libraries.html) documentation.

When in need of a definition for a given functionality which is not covered here, first consult the Common Message Set, both [our subset](./common.md) and [full list](https://mavlink.io/en/messages/common.html). If a new definition is actually needed, follow the original guide on [how to define MAVLink Messages & Enums](https://mavlink.io/en/guide/define_xml_element.html)

<!-- markdownlint-disable -->
<!-- AUTO-GENERATED PART BELOW, DO NOT MODIFY BY HAND -->

---

Generated on 2024-03-15T17:53:42 from commit [a272aa9](https://github.com/marsh-sim/mavlink/tree/a272aa9a26f9607a8c0115fde948ffe2d2505a38)

<h2 id="definition_list">Definition list</h2>
<ul>
 <li><a href="#enums">Enums</a><ul>
  <li><a href="#MARSH_COMPONENT">MARSH_COMPONENT</a></li>
 </ul></li>
 <li><a href="#mav_commands">Mav Commands</a><ul>
 </ul></li>
 <li><a href="#messages">Messages</a><ul>
 </ul></li>
</ul>
<html>
 <body>
  <p>
   <strong>MAVLink Include Files:</strong>
   <a href="https://mavlink.io/en/messages/common.html">common.xml</a>
  </p>
  <h2>MAVLink Protocol Version</h2>
  <p>The current MAVLink version is 2.1. The minor version numbers (after the dot) range from 1-255.</p>
  <p>This file has protocol dialect: 2.</p>
  <h2 id="enums">MAVLink Type Enumerations</h2>
  <h3 id="MARSH_COMPONENT">MARSH_COMPONENT</h3>
  <p>
   <a href="#enums">
    [Enum]
   </a>Component ids (values) for different nodes of the simulator network (flight model, controls, visualisation etc.). Components will always receive messages from the Manager relevant for their ID. Only the first component in a network with a given system ID and component ID will have its messages forwarded by the Manager, all other ones will only be treated as output (will be shadowed). This enum is a redefinition of MAV_COMP_ID_USER# messages from <a href="#MAV_COMPONENT">MAV_COMPONENT</a> documented at https://mavlink.io/en/messages/common.html#MAV_COMPONENT</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="MARSH_COMP_ID_MANAGER">
     <td>25</td>
     <td>
      <a href="#MARSH_COMP_ID_MANAGER">MARSH_COMP_ID_MANAGER</a>
     </td>
     <td>The simulation manager responsible for routing packets between different nodes. Typically MARSH Manager, see https://marsh-sim.github.io/manager.html</td>
    </tr>
    <tr id="MARSH_COMP_ID_FLIGHT_MODEL">
     <td>26</td>
     <td>
      <a href="#MARSH_COMP_ID_FLIGHT_MODEL">MARSH_COMP_ID_FLIGHT_MODEL</a>
     </td>
     <td>Component simulating flight dynamics of the aircraft.</td>
    </tr>
    <tr id="MARSH_COMP_ID_CONTROLS">
     <td>27</td>
     <td>
      <a href="#MARSH_COMP_ID_CONTROLS">MARSH_COMP_ID_CONTROLS</a>
     </td>
     <td>Component providing pilot control inputs.</td>
    </tr>
    <tr id="MARSH_COMP_ID_VISUALISATION">
     <td>28</td>
     <td>
      <a href="#MARSH_COMP_ID_VISUALISATION">MARSH_COMP_ID_VISUALISATION</a>
     </td>
     <td>Component showing the visual situation to the pilot.</td>
    </tr>
    <tr id="MARSH_COMP_ID_INSTRUMENTS">
     <td>29</td>
     <td>
      <a href="#MARSH_COMP_ID_INSTRUMENTS">MARSH_COMP_ID_INSTRUMENTS</a>
     </td>
     <td>Component implementing pilot instrument panel.</td>
    </tr>
    <tr id="MARSH_COMP_ID_MOVING_PLATFORM">
     <td>30</td>
     <td>
      <a href="#MARSH_COMP_ID_MOVING_PLATFORM">MARSH_COMP_ID_MOVING_PLATFORM</a>
     </td>
     <td>Component that moves the entire cockpit for motion cueing.</td>
    </tr>
    <tr id="MARSH_COMP_ID_GSEAT">
     <td>31</td>
     <td>
      <a href="#MARSH_COMP_ID_GSEAT">MARSH_COMP_ID_GSEAT</a>
     </td>
     <td>Component for in-seat motion cueing.</td>
    </tr>
    <tr id="MARSH_COMP_ID_EYE_TRACKER">
     <td>32</td>
     <td>
      <a href="#MARSH_COMP_ID_EYE_TRACKER">MARSH_COMP_ID_EYE_TRACKER</a>
     </td>
     <td>Component providing gaze data of pilot eyes.</td>
    </tr>
    <tr id="MARSH_COMP_ID_CONTROL_LOADING">
     <td>33</td>
     <td>
      <a href="#MARSH_COMP_ID_CONTROL_LOADING">MARSH_COMP_ID_CONTROL_LOADING</a>
     </td>
     <td>Component measuring and actuating forces on pilot control inputs.</td>
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
  <h2 id="messages">MAVLink Messages</h2>
 </body>
</html>
