# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask, Blueprint, request, render_template, url_for, send_from_directory
import logging
import datetime
import requests
import urllib
import json
import uuid

from .forms import BankForm
from .utils import *

logger = logging.getLogger(__name__)
app = Flask(__name__, template_folder="templates", static_folder="statics")
#app.config.from_object("at.config")
app.secret_key = 'citibankfajdslkf'

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route("/", methods=['POST', 'GET'])
def index():
    form = BankForm()
    if form.luong.data not in ["yes", "no"]:
        form.luong.data = ''

    if not form.tabs.data:
        form.tabs.data = 1

    slbox_caoch = select_box_by_list(CAOCH, form.caoch.data, 'caoch', 'caoch', 'form-control styled', '',
                                      'Chọn mức lương hàng tháng của bạn')
    form.email.errors=[]
    form.phone.errors = []

    if request.method == 'POST':
        phone = form.phone.data
        url = "https://api.hubapi.com/contacts/v1/search/query?q=" + phone + "&hapikey=3f028fdd-3630-4098-a4aa-e93f123cf781"
        header = {'Content-Type': 'application/json'}
        res = requests.get(url=url, headers=header)
        res_json = res.json()
        total = res_json["total"]
        checkPhoneExist = None
        if (total > 0):
            contacts = res_json["contacts"]
            for contact in contacts:
                if (contact['properties']["phone"]["value"] == phone):
                    checkPhoneExist = True
                    break

        if checkPhoneExist is None:
            salary_method = "CASH_IN_HAND"
            if form.luong.data == "yes":
                salary_method = "BANK_TRANSFER"

            data = {
                "properties": [
                    {"property":"identifier", "value":str(uuid.uuid4())},
                    {"property":"firstname", "value":form.name.data},
                    {"property":"lastname", "value":""},
                    {"property":"email", "value":form.email.data},
                    {"property":"phone", "value":form.phone.data},
                    {"property":"hs_lead_status", "value":"NEW"},
                    {"property":"salary_payment_method", "value":salary_method},
                    {"property":"monthly_income_level", "value":int(form.caoch.data)},
                    {"property":"aff_source", "value":form.aff_source.data},
                    {"property":"aff_sid", "value":form.aff_sid.data},
                ]
            }

            url = "https://api.hubapi.com/contacts/v1/contact/?hapikey=3f028fdd-3630-4098-a4aa-e93f123cf781"
            header = {'Content-Type': 'application/json'}
            res=requests.post(url=url, data=json.dumps(data), headers=header)
            res_json = res.json()
            print res_json
            if "status" in res_json and res_json["status"] == "error":
                if "error" in res_json and res_json["error"] == "CONTACT_EXISTS":
                    form.email.errors.append(u"Email đã tồn tại")
                else:
                    form.email.errors.append("Invalid data!")
            else:
                return render_template('thankyou.html')
        else:
            form.phone.errors.append(u"Số điện thoại đã tồn tại")

    return render_template('index.html', form=form, slbox_caoch=slbox_caoch)
