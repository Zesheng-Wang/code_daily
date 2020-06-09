import requests
import json
from pyecharts.charts import Map, Geo
from pyecharts import options as opts
from pyecharts.globals import GeoType, RenderType
import requests
import json

# 获取的腾讯疫情数据的URL
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
data = json.loads(requests.get(url=url).json()['data'])
china = data['areaTree'][0]['children']
date = data['lastUpdateTime']
print(date)
data = []
for i in range(len(china)):
    data.append([china[i]['name'], china[i]['total']['confirm']])
print(china)
confirm = []  # 确诊人数列表
dead = []  # 死亡人数列表
heal = []  # 治愈人数列表
# 读出来相应的数据存起来
for i in range(len(china)):
    confirm.append(china[i]['total']['confirm'])
for i in range(len(china)):
    dead.append(china[i]['total']['dead'])
for i in range(len(china)):
    heal.append(china[i]['total']['heal'])
# 求和
sum_confirm = str(sum(confirm))
sum_dead = str(sum(dead))
sum_heal = str(sum(heal))
print(data)
china_total = "确诊:" + sum_confirm + \
              " 死亡:" + sum_dead + \
              " 治愈:" + sum_heal + \
              " 更新日期:" + str(date)
geo = (
    Geo(init_opts=opts.InitOpts(width="100%", height="600px", bg_color="#404a59", page_title="全国疫情实时报告",
                                renderer=RenderType.SVG, theme="white"))  # 设置绘图尺寸，背景色，页面标题，绘制类型
        .add_schema(maptype="china", itemstyle_opts=opts.ItemStyleOpts(color="rgb(49,60,72)",
                                                                       border_color="rgb(0,0,0)"))  # 中国地图，地图区域颜色，区域边界颜色
        .add(series_name="geo", data_pair=data, type_=GeoType.EFFECT_SCATTER)  # 设置地图数据，动画方式为涟漪特效effect scatter
        .set_series_opts(  # 设置系列配置
        label_opts=opts.LabelOpts(is_show=False),  # 不显示Label
        effect_opts=opts.EffectOpts(scale=6))  # 设置涟漪特效缩放比例
        .set_global_opts(  # 设置全局系列配置
        visualmap_opts=opts.VisualMapOpts(min_=0, max_=100),  # 设置视觉映像配置，最大值为平均值
        title_opts=opts.TitleOpts(title="全国疫情地图", subtitle=china_total, pos_left="center", pos_top="10px",
                                  title_textstyle_opts=opts.TextStyleOpts(color="#fff")),
        # 设置标题，副标题，标题位置，文字颜色
        legend_opts=opts.LegendOpts(is_show=False),  # 不显示图例
    )
)
geo.render(path="./html/render.html")
