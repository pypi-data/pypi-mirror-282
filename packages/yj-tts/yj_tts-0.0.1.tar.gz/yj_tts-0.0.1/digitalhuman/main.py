# -*-coding:utf-8-*-
"""
工程入口

"""
import base64
import json
import os
import queue
import subprocess
import threading
from typing import Optional

import requests
import uvicorn
from fastapi import FastAPI, Header
from starlette.requests import Request
from starlette.responses import JSONResponse

import ttsHuman
from config.env_config import config, opt
from entity.digitalHumanParam import DigitalHumanParam, DigitalHumanRealParam
from scheduleJob import scheduler
from utils.common import md5_encryption, get_parent_path
from utils.mysqlhelp import MysqlHelp

app = FastAPI()


# 自定义中间件处理 OPTIONS 请求
@app.middleware("http")
async def options_middleware(request: Request, call_next):
    if request.method == "OPTIONS":
        # 返回允许的 HTTP 方法和其他相关头部信息
        headers = {
            "Access-Control-Allow-Origin": config.cors_allowOrigins,
            "Access-Control-Allow-Methods": config.cors_allowMethods,
            "Access-Control-Allow-Headers": config.cors_allowHeaders
        }
        # encoded_list = [item.encode('utf-8') for item in headers]
        return JSONResponse(content=None, status_code=200, headers=headers)
    # 如果不是 OPTIONS 请求，则继续处理请求
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = config.cors_allowOrigins
    response.headers["Access-Control-Allow-Methods"] = config.cors_allowMethods
    response.headers["Access-Control-Allow-Headers"] = config.cors_allowHeaders
    return response


args = ['-o', '', '-f', 'json', '', '-r', 'phonetic']
mysqlHelper = MysqlHelp.getInstance()
tts = ttsHuman.HumanTTS(config.DATA_PATH)
q = queue.Queue(10)


if __name__ == '__main__':
    scheduler.start()
    uvicorn.run("main:app", host='0.0.0.0', port=config.port, reload=True)
    scheduler.shutdown()




# =====================================
# 权限校验
# =====================================
def valid_permission(access_token):
    if access_token is None or access_token != config.ACCESS_TOKEN:
        return False
    return True


# =====================================
# 离线文本转语音生成和口型文件生成
# =====================================
@app.post("/pushSpeechMsg")
async def pushSpeechMsg(params: DigitalHumanParam, access_token: Optional[str] = Header(None)):
    if not valid_permission(access_token):
        return {"errorCode": "00001", "message": "没有访问该接口的权限"}
    print('收到的参数：', params)
    q.put(params)
    return {"errorCode": "00000", "message": "success"}


# =====================================
# 实时语音生成-暂时废弃
# =====================================
@app.post("/generateLipAndWavFile1")
async def generateLipAndWavFile(params: DigitalHumanRealParam):
    print('收到的参数：', params)
    file_name = md5_encryption(params.msg)
    # 生成音频文件
    save_file = tts.generate_speech(params.msg, params.voiceName, file_name)
    print(save_file)
    parent_path = get_parent_path(save_file)
    save_json_file = parent_path + file_name + ".json"
    save_wave_file = parent_path + file_name + ".wav"
    generate_lip_json(save_json_file, save_wave_file)
    with open(save_json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    maveUrl = upload(save_wave_file)
    return {"errorCode": "00000", "data": {"videoUrl": maveUrl, "jsonObj": data}}


# =====================================
# 实时语音生成
# =====================================
@app.post("/generateLipAndWavFile")
async def generateLipAndWavFile(params: DigitalHumanRealParam):
    print('收到的参数：', params)
    if params.id is not None:
        result = get_digital_human_by_sql(params.id)
        if result is not None:
            return {"errorCode": "00000", "data": {"videoUrl": result[0], "jsonObj": result[1]}}
    file_name = md5_encryption(params.msg)
    # 生成音频文件
    save_file = tts.generate_speech(params.msg, params.voiceName, file_name)
    print(save_file)
    parent_path = get_parent_path(save_file)
    save_json_file = parent_path + file_name + ".json"
    save_wave_file = parent_path + file_name + ".wav"
    generate_lip_json(save_json_file, save_wave_file)
    with open(save_json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    with open(save_wave_file, 'rb') as file:
        audio_base64 = base64.b64encode(file.read()).decode('utf-8')
    return {"errorCode": "00000", "data": {"audioBase64": audio_base64, "jsonObj": data}}


# 文本生成音频与口型,并更新入库
def generate_human(params: DigitalHumanParam):
    try:
        file_name = md5_encryption(params.msg)
        # 生成音频文件
        save_file = tts.generate_speech(params.msg, params.voiceName, file_name)
        print(save_file)
        parent_path = get_parent_path(save_file)
        generate_lip_json_to_sql(parent_path, file_name, params.id)
    except Exception as ex:
        print("语音生成或嘴唇生成发生异常,", ex.args)
        sql = 'update tb_rasa_digital_human set status = %s,fail_reason = %s where id = %s'
        values = [2, str(ex), params.id]
        mysqlHelper.update(sql, values)
    pass


# 生成口型文件
def generate_lip_json(saveJsonFile, saveWaveFile):
    # 如果文件已经存在，直接返回
    if os.path.exists(saveJsonFile):
        return saveJsonFile
    args[1] = saveJsonFile
    args[4] = saveWaveFile
    print("参数：", args)
    print(opt.rhubarbPath)
    subprocess.call([opt.rhubarbPath] + args)


pass


# 生成口型文件并上传到nginx,更新入库
def generate_lip_json_to_sql(parent_path, file_name, id):
    save_json_file = parent_path + file_name + ".json"
    save_wave_file = parent_path + file_name + ".wav"
    generate_lip_json(save_json_file, save_wave_file)
    success = 1
    mave_url = upload(save_wave_file)
    if len(mave_url) == 0:
        success = 2
    print(f'是都成功：', success)
    with open(save_json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    print(data)
    # 如果存在一个失败，则本次生成失败，都成功则需要将数据库中值置为成功
    sql = 'update tb_rasa_digital_human set video_url = %s,json_obj = %s,status = %s where id = %s'
    values = [mave_url, json.dumps(data), success, id]
    mysqlHelper.update(sql, values)


pass


# 最后进行文件上传到nginx
def upload(file_path):
    print(config.BASE_URL + "upload-api/upload")

    with open(file_path, 'rb') as file:
        response = requests.post(config.BASE_URL + "upload-api/upload", files={'file': file},
                                 params={'domainId': 1, 'dir': "video"},
                                 headers={'access-token': config.ACCESS_TOKEN})
    # 输出返回信息
    print(response.text)
    resp_obj = json.loads(response.text)
    if "00000" == resp_obj['errorCode']:
        return resp_obj['data']
    else:
        return ""


# =====================================
# 查询数据库关联信息
# =====================================
def get_digital_human_by_sql(id):
    sql = 'select video_url,json_obj,status,relation_id from tb_rasa_digital_human where relation_id = %s limit 1'
    result = mysqlHelper.selectone(sql, [id])
    if result is None:
        return None
    else:
        if result[2] == 1:
            # 如果是已经生成语音直接返回
            return result
        else:
            return None
    pass


def worker():
    while True:
        if q.empty():
            continue
        item = q.get(block=True, timeout=3)
        generate_human(item)
        q.task_done()


# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()
