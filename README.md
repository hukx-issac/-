# -
基于共现欢乐颂人物关系提取

实体间的共现是一种基于统计的信息提取。
关系紧密的人物往往会在文本中多段内同时出现，可以通过识别文本中已确定的实体（人名），计算不同实体共同出现的次数和比率。
当比率大于某一阈值，我们认为两个实体间存在某种联系。
这个小程序使用python编写代码实现对《欢乐颂》人物关系的提取，最终利用Gephi软件对提取的人物关系绘制人物关系图。
文中所使用的人物列表和情节均来自《欢乐颂》百度百科 
http://baike.baidu.com/link?url=C-1jriqVHYgjYVotP0-KvxDmakR5CCS5en8LOgULtnDirYnoJKnfIceRRXp2aKnluwTOV-lHPD6ez4NBR4uNlEHog97miAUh-COoadrxEdWEY9puVOu1NwDSyMKKD7zi
