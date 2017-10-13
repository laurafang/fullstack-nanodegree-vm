#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect,jsonify, url_for,\
     flash, jsonify, flash, make_response
import random
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catalog, Item, User
from flask import session as login_session
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from functools import wraps
import requests

app = Flask(__name__)

def login():
def display_login():
def connect():
def create_user():
def get_user_info():
def get_user_ID():
def cata_item_json():
def item_json():
def show_catalogs():
def new_catalog():
def edit_catalog():
def del_catalog():
def show_items():
def new_item():
def edit_item():
def del_item():


if __name__ == '__main__':
    
