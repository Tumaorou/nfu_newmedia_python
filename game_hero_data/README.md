game_hero_data
英文项目名称game_hero_data，game hero指游戏中的英雄,data意思为”数据，资料”，就是指在《英雄联盟》这款游戏中英雄的相关资料。

# 简介 
网络游戏英雄联盟的英雄资料查询，输入方面用户可输入想查询英雄的名或称号（如“盖伦”和“德玛西亚之力”），输出方面则是该英雄的视频资料，被动技能以及其“Q、W、E、R”技能的描述、冷却时间、消耗法力值等方面的资料，共134个英雄的资料，数据来源于带玩|DaiWan游戏平台取得的json档。


## 输入：
用户输入英雄名，交互界面使用到HTML5之datalist标签，显示的是指标名称，其对映值为指标代码，所以用户可以用 指标代码 或 指标名称 的片段找所需要的指标。
## 输出：
用户得到输出结果为：英雄的技能、视频资料等6个方面的数据，详细见[
## 从输入到输出，本组作品使用了：

### 从输入到输出，除了flask模块，本组作品还使用了：
### 模块：
* [requests](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)
### 数据
* [data](https://github.com/Tumaorou/nfu_newmedia_python/tree/master/game_hero_data/data)
*  134个英雄，每个英雄输出一个json档
*  资料类型：字典包字典  
### API
* [带玩游戏平台](http://lolapi.games-cube.com/GetChampionDetail?champion_id={champion_id})

# Web APP动作描述
*以下按web 请求（web request） - web 响应 时序说明

後端伺服器启动：执行 pick_a_zb_meta.py 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

後端伺服器web 响应：pick_a_zb_meta.py 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版templates/entry.html及一个含指标代码及名称的字典（见代码 the_list_items = meta['cname']）产出的产生《英雄联盟英雄技能信息》的HTML页面

前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"text"，变数名称(name)为'user_zb'，使用了HTML5的datalist 定义在 list="zbs" 及 datalist标签，详见HTML模版templates/entry.html

前端浏览器web 请求：用户选取指标後按了提交钮「搞吧」，则产生新的web 请求，按照form元素中定义的method='POST' action='/pick_a_zb'，以POST为方法，动作为/pick_a_zb的web 请求

後端服务器收到用户web 请求，匹配到@app.route('/pick_a_zb', methods=['POST'])的函数 pick_a_zb()

pick_a_zb_meta.py 中 def pick_a_zb() 函数，把用户提交的数据，以flask 模块request.form['user_zb']	取到Web 请求中，HTML表单变数名称user_zb的值，存放在user_zb这Python变数下，再使用flask模块render_template 函数以templates/results.html模版为基础（输出），其中模版中the_zb的值，用user_zb这变数之值，其他4项值如此类推。

前端浏览器收到web 响应：模版中templates/results.html 的变数值正确的产生的话，前端浏览器会收到正确响应，看到指标的相关元数据。

## 作者成员：
见[_team_.tsv](_team_/_team_.tsv)
