# Broker Report

## Order Flow

- [开源金工 | 量化私募行为的蛛丝马迹：龙虎榜营业部的新视角](https://mp.weixin.qq.com/s/OZINfbw0R7swg0RYkjxHmw)

  - 通过筛选量化私募进入前十大流通股东的个股，并与季末对应有龙虎榜股票的营业部买入情况进行匹配。识别量化私募席位营业部。
  - 量化私募营业部异常净流入（出）具有正（负）向超额收益

- [开源金工 | 识别假外资：内地营业部与北上经纪商的共振](https://mp.weixin.qq.com/s/M7wcZGd_1Esn9pg8z26Csg)

  - 北上经纪商托管数据+龙虎榜数据，识别北上券商和内地已经识别出的量化私募营业部的共振行为，识别假外资

- [开源金工 | 机构行为alpha的细分结构：龙虎榜、机构调研、大宗交易](https://mp.weixin.qq.com/s/ct3B77Pa_7ATgdXipli_dw)

  - 龙虎榜机构专用席位细分：单向上榜为不换手机构专用，双向上榜为换手机构专用

  - 不换手机构专用的alpha更强，不换手机构专用事件超额收益随净流入金额单调变化

  - 在不换手机构专用净流入样本中，随着机构持仓占比提升，超额收益逐渐增加。

  - 机构专用买卖席位数量衡量机构买卖强度，机构专用买卖数量能够很好的衡量机构买卖强度。

    

## Event

- [开源金工 | 机构调研个股的潜在超额收益](https://mp.weixin.qq.com/s/ct3B77Pa_7ATgdXipli_dw)

## Machine Learning

- [华泰金工 | 人工智能系列之二十一 | 基于遗传规划的选股因子挖掘](https://mp.weixin.qq.com/s/KaGBU_adFl6VrqkG8GundA)
  - 遗传规划：公式的表示方式 - > 适应度定义 -> 公式的进化方法
  - gplearn改进：定义多种时间序列算子；对待挖掘因子进行传统风格因子中性化

- [华泰金工 | 人工智能系列之三十二 | AlphaNet：因子挖掘神经网络](https://mp.weixin.qq.com/s/NWghDHfqKPTzenDzxnMuGw)
  - 个股量价数据图片 -> 特征提取 时间序列“卷积”算子 -> pooling -> fully connected -> target

