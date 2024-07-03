from setuptools import find_packages, setup

with open("pyproject.toml", encoding="utf-8") as f:
    pyproject_data = f.read()

setup(
    name="pymft",
    version="0.1.4",
    description="Library for Midi Fighter Twister Interfacing in Python",
    long_description="""
        # pymft: Python Midi Fighter Twister Library

        This library provides a simple and easy-to-use interface for interacting with the [Midi Fighter Twister](https://djtechtools.com/product/midifighter-twister/) controller in Python. 

        The code in this library is inspired from the [Chromatik MidiFighterTwister library](https://github.com/heronarts/LX/blob/dev/src/main/java/heronarts/lx/midi/surface/MidiFighterTwister.java).

        ## Features

        - **Easy Configuration:** Define knob configurations using the `MidiFighterTwister` class. This library is trying to asbtract the complexity of the Midi Fighter Twister controller interface out of the client code.
        - **Knob Configuration:** Define knob settings (type, range, color, detent, movement, MIDI type, etc.) using the `KnobSettings` class.
        - **Easy Subscription:** Subscribe to knob changes using `mft.subscribe()`, which automatically applies the defined knob settings to the device.
        - **Efficient Reading:**  The library handles reading knob values in the background, allowing you to efficiently query changes using functions like `read_all_changed()`, `read_active_changed()`, `read_all()`, and `read_active()`.
        - **JSON Configuration:** Load knob configurations from JSON files, allowing you to define and manage settings easily.
        - **Value Change Callback:** Call a function when the value of a knob changes to avoid expensive while loops.

        Future developments include:
        - **Non-linear Mapping:** Support non-linear min-max mapping for knob values
        - **2-way Communication:** Send new knob values to the device to allow 2-way communication between the client code and the hardware
        - **Multiple MFT Devices:** Test with more than 1 MFT device and see if it works
        """,
    long_description_content_type='text/markdown',
    author="Sina Solaimanpour",
    author_email="sinas.cb@gmail.com",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=["python-rtmidi>=1.5.8", "typing>=3.7.4"],
    entry_points={
        "console_scripts": [
            "demo_main=pymft.main:run",
            "version=pymft.main:version",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
