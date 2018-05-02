# RAD (Rapid Autonomous Defense) - A PAL security initiative
Stateful, automatic and minimal security system for one's dorm or interstellar military installation.

## Overview

The system employs cameras and other sensors to assess the state of its
surroundings and then employs any integrated systems to handle and respond to evolving threats.

## State Awareness

Consumes a pollable JPEG feed and identifies anomalous events and distinct states be it the owner's presence or a thief's intrusion.

## Setup

Open the `config.json` file for editing and add a link to a web accessible
pollable video frame feed. You can then run `python3 feed.py` and it will begin
detecting motion and printing to the console relevant info.

## Contribution

Please feel free to open an issue or PR if you've found a bug. If you're looking to implement a feature, please open an issue before creating a PR so I can review it and make sure it's something that should be added.

## License

This project is under the [WTFPL](http://www.wtfpl.net/) license
