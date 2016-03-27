#!/usr/bin/env python3
from multiprocessing import Process
from Chat import chat

chatProcess = Process(target=chat())
