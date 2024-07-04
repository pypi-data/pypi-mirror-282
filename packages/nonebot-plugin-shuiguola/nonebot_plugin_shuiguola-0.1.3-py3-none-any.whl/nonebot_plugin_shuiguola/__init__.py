import nonebot
from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata
from nonebot import logger, on_command, on_message
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment, Event, GroupMessageEvent
from nonebot.rule import ToMeRule, KeywordsRule, Rule
from nonebot.message import handle_event
from nonebot.typing import T_State
import os

from . import database
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="shuiguola",
    description="水过了bot，正义查重姬",
    usage="""使用"统计"命令查看统计数据，使用？命令查看上次水图信息""",
    type="application",
    homepage="https://github.com/Souls-R/nonebot-plugin-shuiguola",
    config=Config,
    supported_adapters={"~onebot.v11"}
)

config = get_plugin_config(Config)

last_pic_info = ""
水过了path = os.path.join(os.path.dirname(__file__), 'shuiguole.jpg')
水烂了path = os.path.join(os.path.dirname(__file__), 'shuilanle.jpg')

def get_message_images(data: str):
    """
    获取消息中所有的 图片 的链接
    """
    try:
        img_list = []
        subTypelist = []
        filelist = []
        data = json.loads(data)
        for msg in data["message"]:
            if msg["type"] == "image":
                img_list.append(msg["data"]["url"])
                subTypelist.append(msg["data"]["subType"])
                filelist.append(msg["data"]["file"])
        return (img_list, filelist, subTypelist)
    except KeyError:
        return []

async def check_img(bot: Bot, event: Event, state: T_State) -> bool:
    img_list, filelist, subTypelist = get_message_images(event.json())
    state['img_list'] = img_list
    state['filelist'] = filelist
    state['subTypelist'] = subTypelist
    return len(img_list) != 0


PicsRecv = on_message(rule=check_img, priority=5)
@PicsRecv.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    global last_pic_info
    if isinstance(event, GroupMessageEvent):
        msg, count, date, subType = database.addPic(
            state['img_list'][0], state['filelist'][0], state['subTypelist'][0], str(event.group_id))
        logger.info(state)

        # 普通图片每次都嘲笑
        if msg == "old" and subType == '0':
            last_pic_info = "这张图上次水是在" + \
                date.strftime("%Y-%m-%d %H:%M:%S") + ", 被水过了"+str(count)+"次"
            if count <= 4:
                await PicsRecv.finish(MessageSegment.image('file:///'+水过了path))
            else:
                await PicsRecv.finish(MessageSegment.image('file:///'+水烂了path))
        # 表情包水5次发一颗小星星
        elif msg == "old" and subType == '1':
            if count % 5 == 0:
                last_pic_info = "这张表情包上次水是在" + \
                    date.strftime("%Y-%m-%d %H:%M:%S") + \
                    ", 被水过了"+str(count)+"次"
                await PicsRecv.finish("⭐"*int(count/5))


picstatus = on_command("统计", aliases={"图片统计"}, priority=2, block=True)
@picstatus.handle()
async def _(bot: Bot, event: MessageEvent):
    if isinstance(event, GroupMessageEvent):
        TopInfo = database.getTop(
            subType='0', group_id=str(event.group_id))
        msg = "图片统计数据：\n"
        for i in TopInfo:
            msg = msg+str(i["count"])+"次:"+MessageSegment.image(i["url"])+"\n"

        TopInfo = database.getTop(
            subType='1', group_id=str(event.group_id))
        msg = msg+"表情包统计数据：\n"
        for i in TopInfo:
            msg = msg+str(i["count"])+"次:"+MessageSegment.image(i["url"])+"\n"
        await picstatus.send(msg)


laststatus = on_message(rule=Rule(KeywordsRule("?", "？"), ToMeRule()), priority=2, block=True)
@laststatus.handle()
async def _(bot: Bot, event: MessageEvent):
    if(last_pic_info == ""):
        await laststatus.finish("没有水图记录")
    else:
        await laststatus.finish(message=last_pic_info)
