from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    html = """
    <h1>Hello world</h1>
    <p>Welcome to my site</p>
"""
    logger.info('index page access')
    return HttpResponse(html)


def about(request):
    html = """
    <h1>About me</h1>
    <p>This page about me</p>
"""
    logger.info('abour page access')
    return HttpResponse(html)

