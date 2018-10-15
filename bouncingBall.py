import selenium
import re
import threading
import multiprocessing
import socket
import sys
import os
import requests
import queue
import json
import bs4
import threading


def bouncingBall(h, bounce, window):
    # your code

    n = 1
    # while True:
    #     h *= bounce
    #     if h >= window:
    #         n += 2
    #     else:
    #         break
    #
    # return n
    h * bounce**n <= window


if __name__ == "__main__":
    print(bouncingBall(3, 0.66, 1.5))