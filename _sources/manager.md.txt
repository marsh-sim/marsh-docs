# MARSH Manager

The `marsh-mgr` program is a graphical application that serves as the central node in the simulator architecture.

It is meant as a single tool to provide:

- Communicating data between simulator parts (nodes)
- Controlling the simulation execution and configuration
- Logging and replaying the simulation data

![diagram showing MARSH Manager as central element of the simulator](./simulator_variants_manager.svg)

## Usage

Start the application executable, either `marsh-mgr` or `marsh-mgr.exe`.
If other nodes are running on different computers, configure "manager address" to IP address of the computer running the manager.

## Contributing

Contributions to [documentation](./documentation.md) and code are welcome.
The repository is on GitHub as [marsh-sim/marsh-manager](https://github.com/marsh-sim/marsh-manager), contributions are expected as [Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to that repository.

## Licenses

The code for MARSH Manager is licensed under [GNU General Public License v3.0](https://github.com/marsh-sim/marsh-manager/blob/main/LICENSE.txt)

General application structure provided by [Qt Framework](https://www.qt.io/product) under terms of the [GNU Lesser General Public License (LGPL)](https://doc.qt.io/qt-6/lgpl.html)

Communication between components with [MAVLink](https://mavlink.io/en/) using generated code under [MIT License](https://github.com/mavlink/mavlink/blob/master/COPYING)
