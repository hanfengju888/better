from flask import Blueprint, session
from flask import jsonify
from flask import request
from flask import render_template
from app.utils.SingletonDecorator import permission

from app.middleware.HttpClient import Request

req = Blueprint("request",__name__,url_prefix="/request")

@req.route("/http",methods=['POST'])
@permission()
def http_request(user_info):
    data = request.get_json()
    method = data.get("method")
    if not method:
        return jsonify(dict(code=101,msg="请求方式不能为空"))
    url = data.get("url")
    if not url:
        return jsonify(dict(code=101,msg="请求地址不能为空"))
    body = data.get("body")
    headers = data.get("headers")
    r = Request(url,data=body,headers=headers)
    response = r.request(method)

    if response.get("status"):
        print("通过。。。")
        return jsonify(dict(code=0,data=response,msg="操作成功"))
    return jsonify(dict(code=110,data=response,msg=response.get("msg")))

@req.route("/http_ui",methods=["GET"])
def http_ui():
    sign = request.args.get('sign')
    session["sign"] = sign

    return render_template("http/http.html")

@req.route("/send_http",methods=["POST"])
@permission()
def send_http(user_info):
    method = request.form["method"]
    url = request.form["url"]
    payload = request.form["payload"]
    # headers = {"Content-Type":"application/json"}
    headers = None

    r = Request(url, data=payload, headers=headers)
    response = r.request(method)

    if not response.get("status"):
        print("未通过。。。")
        return jsonify(dict(code=110, data=response, msg=response.get("msg")))
    return render_template("http/http.html",url=url,payload=payload,response=response)