# Broker Report

## Alternative Data

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
- [开源金工 | 机构调研个股的潜在超额收益](https://mp.weixin.qq.com/s/ct3B77Pa_7ATgdXipli_dw)
  - 机构调研事前超额收益显著，事后超额收益有一定幅度下滑，即机构调研的多是已经上涨的股票
  - 将机构调研事件作为conditioner，考察月内被调研的个股股票池，构造以下因子的多空组合表现良好
    - 根据上市公司财报数据和分析师一致预期数据构建的业绩超预期因子 SUE
- [开源金工 | 高频股东数据的隐含信息量](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247488808&idx=1&sn=0f0bca8380fb56d6e2187e2587ba904f)
  - 低频股东数据：用季报股东数的变化量做因子
  - 高频股东数据：用深交所互动易(irm.cninfo.com.cn)上股东数问答结果对季报股东数数据进行补充，选取回答比较频繁的几百家股票做universe，高频股东变化量因子效果更好
- [ 开源金工 | 扎堆效应的识别：以股东户数变动为例](https://mp.weixin.qq.com/s/ouDcV77WFHawYgvjroyggg)
  - 股东变动数因子效果不错
  - 人均持股占比在时序上的变动 (PerCapitaRatioChange 因子) 比股东变动数因子更稳健
- [开源金工 | 投资者结构与因子收益](https://mp.weixin.qq.com/s/4maNQUaNNjIuBbavcqJ_Sw)
  - 投资者结构可以作为一个condi，量价因子和基本面因子在不同group投资者比例中的IC均单调
  - 基本面因子：单季度营收同比、单季度营业利润同比、单季度净利润环比、分析师预期（SUE）
- UBS | Can we trade on company visits in China?
  - company visits attracts investor attention and positive money flow
  - can trade on these events or take as interactor
  - Wind Institution's Field Research Dataset
- UBS | Collaborative Intelligence: How to combine human and machine insights to generate alpha?
  - On short horizon, analyst view generate significant excess returns while does not load systematically on any quant factors. Therefore, we can aggregate analyst short term insights with quant factors.
  - How to do: long the intersection of top names from both quant factors and analyst views, and short the intersection of the bottom names.
- UBS | A Definitive Approach to Crowding
  - Comprehensive crowding factor using
    - Prime brokerage position data: long/short
    - 13F regulatory filings: long
    - Stock loan data: short
    - UBS internal data: short
- UBS | Collaborative Intelligence: Can Crowding data Enhance Alpha?
  - Combining the crowding data in **UBS | A Definitive Approach to Crowding** with quant factors using the approach in **UBS | Collaborative Intelligence: How to combine human and machine insights to generate alpha?**.
  - **Question**: if a stock is long crowded, this info can enhance alpha if the quant signal is also long, meaning that we should bet more, this is confirmed using backtest. However, from a risk model perspective, shouldn't we sell if a stock is long crowded to avoid excess risk?
- ExtractAlpha | Transcripts Model
  - Transcript data: Earnings Call, Conference, Investor Meeting, etc. 
    - Model1: Word embedding -> BERT -> Sentence sentiment -> company sentiment score
    - Model2: Word embedding -> Bag of Words -> Machine Learning predict return

  -  The Model has non-trivial correlation to common risk factors, but alpha still remains after removing its factor exposures

- ExtractAlpha | EPS and Revenues Prediction
  - A combination of the following three parts

  - Experts: 
    - proprietary metrics of individual analyst ability
    - a simple measure for the age of the estimate provided by the analyst
    - analyst expertise can differ across different items – for example, some analysts are better at estimating Revenues and worse at estimating EPS

  - Trend:
    - The company’s time series of prior earnings and revenue surprises contains valuable information on how efficiently the firm has been able to beat expectations in the past
    - The experience of a firm’s competitors is also important, as earnings surprises in a particular industry tend to cluster in time

  - Management:
    - the presence of recent management guidance
    - the stock’s historical beats and misses relative to guidance
    - the timing of earnings announcements and whether they are later than anticipated (Companies which are late in announcing, or which announces on days with high news volume, or near weekends and holidays, tend to miss their numbers)
    - the expectation of an earnings loss
    - and the variance of estimates


## Factor

- 动量因子

  - [开源金工 | A股市场中如何构造动量因子？](https://mp.weixin.qq.com/s/vx9YWJ5-exUymp1w5Sb9qA) 
  - [开源金工 | 长端动量2.0：长期、低换手、多头显著的量价因子](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247547796&idx=1&sn=99898719dc33b997ed06f53ad1eaa785&chksm=ea313e02dd46b714298b28246acfa296a74de58203c8d02b65d6672b33891aa746996a41ff04&cur_album_id=1428197421624180736&scene=190#rd)
    - A股动量因子效果不好，因为存在比较显著的反转效应，传统改进方式：$$Ret_{t \, month} - Ret_{t-1 \, month} $$
    - 对动量因子按照振幅进行切割：高振幅区域存在反转效应，低振幅区域存在动量效应。
      - **切割指标：**振幅选用（最高价-最低价）/前收盘价的定义方式；
      - **切割对象：**个股alpha收益（股票日收益-市场日收益均值）。股票日收益受市场beta影响，在横截面对比时，若股票日收益对应时点一致，则市场beta不影响股票间相对排序，若股票日收益对应时点不一致，则两股票日收益时点重合度越低，市场beta对股票间相对排序影响越大；
      - **计算方式**：计算最近N日股票振幅，和每日idiosyncratic return，将振幅低的N/2交易日涨跌幅相加得到低振幅动量因子。
      - **中性化**: 将动量因子orthogonal 20日反转因子

## Fundamental

- [开源金工 | 业绩超预期 Plus 组合的构建](https://mp.weixin.qq.com/s/mpoPRS8l-ZO5agisePLJxA)

  - 披露时间最早的业绩预告未来超额收益表现最好，其次是业绩快报，公布时间最靠后的定期报告未来超额收益水平最低。

  - 超预期股票池：

    - 业绩超预期的判断标准为:上市公司发布的财报数据超过了最新一期券商分析师对该公司一致预期归母净利润的均值。
    - 业绩超预期的计算：以Q3为例

    ![](../notes/pic/EAR_SUP.png)

  - 超预期股票池内进一步区分的因子

    - **SUE 因子在超预期股票池内的分组表现较好，其适合用来对超预期标的进行进一步的区分。**

    $$
    S U E=\frac{R_t-E_t}{\left.\sigma\left(R_t-E_t\right)\right)}
    $$

    其中 $R_t$ 表示财报披露的净利润水平, $E_t$ 表示预期的净利闰水平, $\sigma\left(R_t-E_t\right)$ 表示 预测偏差的波动率水平。

    - 对于业绩超预期个股，市场的表现也呈现出不同的模式，一种是业绩公布后股价反应并不强烈，表明当前股价已经提前反映了业绩超预期表现，其可能的解释是市场中总有一些知情交易者在交易;另一种是业绩公布后的次日股价发生向上跳空，表明业绩超出市场预期尚未被市场完全定价。**我们选取公告日前后一个交易 **$$[T-1, T+1]$$ **的超额收益之和构建超预期收益因子 OER(Over Expectation Return)**
    - 报告发布后的下一个交易日股价是否出现跳空现象。一般而言，股价跳空幅度越大，表明个股业绩超预期幅度越高。
    - 理想反转因子 [开源金工 | 长端动量2.0：长期、低换手、多头显著的量价因子](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247547796&idx=1&sn=99898719dc33b997ed06f53ad1eaa785&chksm=ea313e02dd46b714298b28246acfa296a74de58203c8d02b65d6672b33891aa746996a41ff04&cur_album_id=1428197421624180736&scene=190#rd)
    - 大单残差因子 [开源金工 | 大单与小单资金流的alpha能力](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247499023&idx=1&sn=24dbad4491cbe6be1452b86848d829ab)

  - 改进超预期股票池

    - 分析师行为：若为真正超预期股票，当其发布财报后，分析师往往会上调盈利预期以匹配真实盈利。
    - 交易行为：利用跳空因子和超预期收益OER因子进行区分

  - 盈利预期调整因子：

    - 盈利预测调整横截面标准差，即分歧度

    ![](../notes/pic/FYR.png)

    - 分析师盈利预期上调往往能够获得更大超额收益，且上调的分层效果比下调的效果更好。下调分层效果较差的原因即:时效性更低，上调报告间隔的时间要小于下调。

    - FYR_DISP 的改进

      - 按照时效性对于分析师预期进行半衰期加权
      - 股价跟随性：对于盈利预期调整而言，往往会受到前期市场涨跌的影响，比如当某只股票处于强势的上涨趋势中，分析师更大概率会积极上调盈利预测。**对于跟随市场涨跌的盈利预期调整而言，我们认为其跟风效应强、创新性不足，对于这类预测，我们赋予更低权重。**而那些与市场走势不同的观点可能更有参考价值。
      - 预测准确度：分析师打分

    - 分析师羊群效应：我们参照用于刻画交易羊群效应的CSAD指标，则对于股票i，t时刻的分析师的羊群效应因子为
      $$
      C S A D_{-} F R_{i, t}=\frac{1}{m} \sum_{j=1}^m\left|f r_{i, j, t}-f r_{i, c o n, t}\right|
      $$
      使用本月CSAD与过去N月 CSAD 均值进行比较, 定义羊群效应变动因子
      $$
      \Delta C S A D_{-} F R_{i, t}=\left(C S A D_{-} F R_{i, t}-\frac{1}{N} \sum_{k=0}^{N-1} C S A D_{-} F R_{i, t-k}\right) /\left(\frac{1}{N} \sum_{k=0}^{N-1} C S A D_{-} F R_{i, t-k}\right)
      $$
      在盈利预期上调的样本池中，$$\Delta C S A D_{FR}$$ 呈现明显的正向选 股能力，而在盈利预期下调的样本池中，$$\Delta C S A D_{FR}$$呈现明显的负向选股能力。

## Linkage

- Fund 13F linkage

  - [开源金工 | 从基金持仓行为到股票关联网络](https://mp.weixin.qq.com/s/LToZyqOselgySavoxIvFIQ)

    - 数据范围：所有公募基金持仓，基金持仓数据选取基金季报披露的前十大持仓数据，将各季度所有公募基金权益持仓前十大股票汇总去重得到基金持仓股票池。
    - **关联度指标构建方式**：
      - 分别取A基金最新季报，取共同持有的股票a与股票b持仓市值数据，记作$$H_a$$、$$H_b$$；
      - 计算股票a过去20个交易日成交额均值 ，记作$$AMT_a$$，股票b记作$$AMT_b$$；
      - 计算$$H_a / AMT_a$$，作为股票a的机构拥挤度，记作$$I_a$$，股票b记作$$I_b$$；
      - 定义A基金共同持仓股票a与股票b的关联度指标为：$$J_{ab}=\min(I_a，I_b)$$；
      - 将所有共同持仓股票a与股票b的基金得到的关联度指标求和，得到股票a与股票b的关联度指标$$K_{ab}$$

    ![](../notes/pic/trans_20.png)

  - [开源金工 | 北向关联持仓中的Alpha](https://mp.weixin.qq.com/s/Y1I_Clyeg0G1DH5MexgThQ)

    - 类似的，可以用北上数据进行类似的关联度计算，可以使用市值替代20日成交额均值。如果网络过于稠密，可以通过设置threshold 或者取top N% linkage的方式稀疏化网络。

- [开源金工 | 从小单资金流行为到股票关联网络](https://mp.weixin.qq.com/s/mdXxUMeiTbJIrTvDyTIUPA)

  -  根据每日小单净流入/净流出数据，计算过去N交易日小单同向比例，构造关联度指标。
  - 优化：
    - 稀疏网络
    - 平滑处理
    - 考虑规模协同：N日daily flow vector的 cosine distance

## Machine Learning

- [华泰金工 | 人工智能系列之十二 | 人工智能选股之特征选择](https://mp.weixin.qq.com/s/p4VutHWsqKMk_65YPCWouw)

  - 单变量特征选择：有监督 可以根据FDR选择

- [华泰金工 | 人工智能系列之十三 | 人工智能选股之损失函数的改进](https://mp.weixin.qq.com/s/22rJ0xRGhGlIlSR3U0feLA)

  - 加权损失函数更加适合样本不均衡的分类问题
  - 广义损失函数能降低机器学习模型的换手率 (punish $$T+1$$ 期预测值和$$T$$ 期预测值的差)
  - XgBoost/LGBM 上自定义损失函数：定义梯度和hessian

- [华泰金工 | 人工智能系列之二十一 | 基于遗传规划的选股因子挖掘](https://mp.weixin.qq.com/s/KaGBU_adFl6VrqkG8GundA)

  - 遗传规划：公式的表示方式 - > 适应度定义 -> 公式的进化方法
  - gplearn改进：定义多种时间序列算子；对待挖掘因子进行传统风格因子中性化

- [华泰金工 | 人工智能系列之三十二 | AlphaNet：因子挖掘神经网络](https://mp.weixin.qq.com/s/NWghDHfqKPTzenDzxnMuGw)

  - 个股量价数据图片 -> 特征提取 时间序列“卷积”算子 -> pooling -> fully connected -> target

- [华泰金工 | 人工智能系列之三十七 | 舆情因子和 BERT 情感分类模型](https://mp.weixin.qq.com/s/TMRYqMnBr_be5ZhpDXvdvg)

  - 基于金融新闻的舆情因子：wind部分新闻数据是有标注正面负面的
  - BERT句头的 [CLS] 起始符 embedding 用于储存和分类有关的信息，在上面接小网络softmax 分类1/0，微调BERT
  - 用正面新闻数 - 负面新闻数/总数，再在window内做decay构造舆情因子

- [华泰金工 | 人工智能系列之四十一 | 基于 BERT 的分析师研报情感因子](https://mp.weixin.qq.com/s/brVT1tkfr3p_Ll3q4_81jw)

  - 研报评分因子：朝阳永续整理的研报评级 （卖出、减持、中性、增持、买入）
  - 研报数量因子
  - 研报情感因子：BERT + 微调 + 分类 + decay
  - 研报情感调整因子：分析师正面研报更多，给负面研报更大权重

- [华泰金工 | 人工智能系列之四十三 | 因子观点融入机器学习](https://mp.weixin.qq.com/s/cMLqAua01HLqLSQEkzwnjA)

  - 随机森林模型改进：修改XgBoost 使得可指定优先分裂的因子，前K层只用某类因子，这样使得最后训练得到的model更接近这类因子的风格。

  - 思考：前K层指定用interactor/conditioner

- [华泰金工 | 人工智能系列之五十一 | 文本 PEAD 选股策略](https://mp.weixin.qq.com/s/Jk9Mter9gyjU8yddc2Q-Kw)

  - 盈余后价格漂移效应(PEAD)：市场反应不足
  - 传统 SUE 因子基于公告财务数据来衡量 PEAD 效应并预测股票的异常收益
  - 本文使用的公告为业绩预告，相关文本为分析师点评业绩预告研报文本标题 和摘要
  - SUE.txt 使用纯文本，高频词构建标题和摘要词频向量，然后接XGBoost等模型进行预测，将模型预测的上涨和下跌类别的 log-odds 值之差，在进行指数衰减后，作为最终的 SUE.txt 因子。

- [华泰金工 | 人工智能系列之六十四 | 九坤Kaggle量化大赛有哪些启示？](https://mp.weixin.qq.com/s/VKLWLJMy6xg38oddvTO2pQ)

  - 特征工程引入均值因子对神经网络有效；

  - CCC损失优于MSE损失和IC损失；

    - IC loss: 不受量纲影响从而在模型间可比。缺点是非凸不保证收敛，可能导致训练不稳定。

    - MSE loss: 优点是易于计算和求导，具有凸性从而保证收敛，缺点是受数据量纲影响。

    - 一致性相关系数CCC loss:
      $$
      CCC = \frac{2 \sigma_{x y}}{M S E+2 \sigma_{x y}}
      $$

  - 时序交叉验证作用不明显；

  - 集成神经网络和决策树类模型提升较稳定

## Order Flow

- [开源金工 | 主动买卖因子的正确用法](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247486802&idx=1&sn=c60f0d7c790513358d7e8cc55d6673e2)

  - 改进主动买卖因子
  $$
    \mathrm{ACT}=\frac{\text { 主动买入金额 }-\text { 主动卖出金额 }}{\text { 主动买入金额 }+\text { 主动卖出金额 }}.
  $$
  
  - ACT因子切割：**大中单ACT因子，在高收益端呈现正向选股效应，小单ACT因子，在低收益端呈现负向选股效应。**
  
    - 取过去20交易日收益率最高的$$\lambda$$日的大中单ACT因子平均值，和过去20交易日收益率最低的$$\lambda$$日的小单ACT因子平均值。

- [开源金工 | 大单与小单资金流的alpha能力](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247499023&idx=1&sn=24dbad4491cbe6be1452b86848d829ab)

  - 成交额标准化衡量资金流入强度，净流入金额绝对值标准化表现最优，IR明显高于成交额标准化和“买入金额+卖出金额”标准化。

    ![](/Users/zizou/Zizou/Paper/reading-notes/notes/pic/order_sm.png)

  - 资金流强度和同时段的涨跌幅会存在一定相关性，为了剥离资金流强度因子中涨跌幅的影响，使用横截面回归，得到残差资金流强度因子$$\varepsilon_t$$，残差资金流强度因子$$\varepsilon_t$$表现显著优于资金流强度因子$$S_t$$。
    $$
    S_t=a+b * \operatorname{Ret} 20_t+\varepsilon_t.
    $$

  - 大单资金流强度因子具有正向alpha，可以将整体alpha切分为正向alpha和负向alpha两部分：正向alpha部分来自于大单的正向预见性；负向alpha部分：大单资金流强度因子的多头组合对应大单的净流入，伴随股票上涨，从而暴露反转因子，获得负向alpha。

  - 类似的，可以改进传统反转因子，得到残差反转因子。20日return与大单净流入正相关，而大单净流入强度更高的股票的上涨更有持续性，将这部分正向alpha剥离出去，可以使得20日return构造的反转因子的负向alpha部分更为纯粹。
    $$
    \operatorname{Ret} 20_t = a+b * S_t+\varepsilon_t.
    $$

  - 因子改进（[开源金工 | 大小单资金流alpha探究2.0：变量精筛与高频测算](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247550740&idx=1&sn=b6da8dfb0107c66ec284c3751ec61676)）：
    - 大单残差因子改进成 主动大中单残差rank+非主动大单强度rank
    - 小单残差因子改进成非主动小单残差

- [开源金工 | 新型因子：资金流动力学与散户羊群效应](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247535580&idx=1&sn=87841fc7d5f5c792e9f33b535f263df8)

  - 考虑flow的秩相关性 (spearman correlation)，用单股过去N日的X变量序列和Y变量序列的秩相关性作为signal
  - 超大单和小单的同步相关性 $$RankCorr(EL_t, S_t)$$有一定选股能力，但资金流同步相关性因子，是“伪动力学”因子，其底层alpha来源仍是资金流强度。
  - **散户的羊群效应因子：$$RankCorr(R_t, S_{t+1})$$ 即收益率与未来一日小单净流入序列的rankcorr，具有很强的负向alpha。**
  - 小单资金流错位因子 $$RankCorr(S_t, S_{t+1})$$ 也有不错的选股能力，但主要来自$$S_t, R_t$$的强相关性，该因子基本能被散户羊群效应因子解释。
  - 此外，一阶差分 $$RankCorr(\delta R_t, \delta S_{t+1})$$ 也有比较强的IC，（需要考虑跟羊群效应因子的相关性）。
  - 因子改进（[开源金工 | 大小单资金流alpha探究2.0：变量精筛与高频测算](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247550740&idx=1&sn=b6da8dfb0107c66ec284c3751ec61676)）：
    - 用日内收益率代替close-to-close衡量$$R_t$$
    - 用非主动小单净流入衡量$$S_t$$ （2017年后，A股机构拆单更细更频繁，主动小单净流入负向alpha消失）
    - 用开盘到10:00/10:30的非主动小单净流入代替全天非主动小单净流入

- [开源金工 | 大小单资金流alpha探究2.0：变量精筛与高频测算](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247550740&idx=1&sn=b6da8dfb0107c66ec284c3751ec61676)

  - 通过变量精筛和日内指标测算改进 资金流因子 （[开源金工 | 大单与小单资金流的alpha能力](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247499023&idx=1&sn=24dbad4491cbe6be1452b86848d829ab)）和散户羊群效应因子 （[开源金工 | 新型因子：资金流动力学与散户羊群效应](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247535580&idx=1&sn=87841fc7d5f5c792e9f33b535f263df8)）。具体见前两部分的补充。

- [开源金工 | 大小单重定标与资金流因子改进](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247544291&idx=1&sn=edd13ea12f84cc445a75f34d833cb079)

  - A股关于成交委托单金额的划分

    - 超大单：挂单金额大于100万元，定义为“机构”
    - 大单：挂单金额介于20万元至100万元之间，定义为“主力”
    - 中单：挂单金额介于4万元至20万元之间，定义为“大户”
    - 小单：挂单金额小于4万元，定义为“散户”

  - 上交所的逐笔数据并未包含委托信息，将在**深交所范围通过逐笔成交数据**重新划定大、小单资金的范围。基于**大单买入金额计算的资金流因子**（NI、NIR、NIPCT）表现较好。

    ![](/Users/zizou/Zizou/Paper/reading-notes/notes/pic/order_sm4.png)

  - 优化资金流因子，将大单/小单的买入卖出金额比作为代理变量衡量不平衡，
    $$
    IMB = \ln (B / S).
    $$
    每个交易日进行回归，取残差进行修正：
    $$
    \ln (B / S) = \alpha + \beta \times Ret + \varepsilon
    $$
    基于修正系数反算大单买入和大单卖出的比例关系
    $$
    \begin{array}{r}
    \hat{B}=\frac{e^{\varepsilon}}{1+e^{\varepsilon}} \times(B+S) \\
    \hat{S}=\frac{1}{1+e^{\varepsilon}} \times(B+S)
    \end{array}
    $$
    将修正后的因子记为NI_MOD、NIR_MOD和NIPCT_MOD。

  - 机构在大票上（中证300）交易更多，这些股票的大单划分阈值更高，小票上主力资金划分阈值明显偏低。由于小票的流动性不足，主力资金会把委托单拆得更细。

  - 通过逐笔交易数据进行测试，大单的划分阈值在2-10万元得到的NIR_MOD因子效果最好。实际中逐笔交易数据计算繁琐，考虑用传统定义中的中单+大单+超大单作为广义主力资金proxy。

  - 大额委托单的交易对手方主要以小额委托单为主，市场上的流动性主要由数量更多、报价更为频繁的小额委托单提供。

## Volatility

- [开源金工 | 振幅因子的隐藏结构](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247484599&idx=1&sn=f688f2d8adcabac3c41cbbb00b0a023b)

  - 按照股价维度将传统振幅因子（daily $$high/low - 1$$）切割为：高价态振幅因子和低价态振幅因子。

  - 将振幅加大视为多空博弈强烈的信号，进而视为该价格状态的不稳定性加大，这意味着该价格状态后续将难以维持。相比于低价态，高价态下的“振荡加大-状态跃迁”效应更为强烈。

  - 理想振幅因子：$$V_{high}(\lambda) - V_{low}(\lambda)$$, 具有比较好的负向选股能力，$$\lambda$$ 取20%效果较好。

    ![](/Users/zizou/Zizou/Paper/reading-notes/notes/pic/range_1.png)

## Smart Money

- UBS | Identifying fund managers' skills using peer cohort
  - Cluster fund managers based on return correlation
  - Identify fund manager skills by cohort alpha - idiosyncratic outperformance against cohort benchmark
  - construct portfolio using top fund managers from each group, to diversify style exposure

- UBS | Where is the onshore smart money positioned in China?
  - regress fund returns on sector returns to estimate sector exposure
  - obtain active position from sector exposure and benchmark weights
  - construct long-short based on that

- UBS | Who is the smart money in China?
  - Mutual funds: investors that clear and settle with custodians; 
  - Hedge funds: investors who prefer to settle their security holdings through their brokers 
  - among all Stock Connect Northbound investors, hedge fund investors are likely more skilled at capturing stock-specific returns
  - **built a composite trading signal based on hedge funds' positioning (active weights: investors' weights minus index weights) and trading (weekly change in active weights)**
  - hedge funds have brought greater information advantage in sectors with higher idiosyncratic risk (By regressing out sector and factor exposures from investor positions, we can extract idiosyncratic stock-specific views)
  - double sort traditional quant factors with composite hedge fund signals, yields better factors

- [开源金工 | 聪明钱因子模型的2.0版本](https://mp.weixin.qq.com/s?__biz=MzI1NTYxMjE1Mw==&mid=2247483960&idx=1&sn=ce495ee32c8b6a3ce3ae6887c9b39465)

  - 聪明钱因子如下，其中20%交易量的选取是因为A股机构历史交易量占比在10-20%之间

    ![](/Users/zizou/Zizou/Paper/reading-notes/notes/pic/smart_money1.jpeg)

  - 改进：

    - $$S_t = |R_t| / V_t^\beta$$, $$\beta = 0.1 \sim 0.5$$ 效果比较好
    - $$S_t = |R_t| / \ln V_t$$
    - $$S_t = Rank(|R_t|) + Rank(V_t)$$

- [兴业金工 | 如何提升机构仓位测算和宏观数据预测精准度？](https://mp.weixin.qq.com/s/pDqVdbiS1a0mZ9MJShqEgA)

  - 用机构每期收益率，以及行业指数收益率 计算机构在每个行业上的实时仓位

  - 传统方法：Lasso 回归

    ![](../notes/pic/position_lasso.png)

  - 卡尔曼滤波：将 仓位当做隐含变量，假设仓位和基金收益率的联合正态分布，得到仓位的后验分布

    ![](../notes/pic/position_kalman.png)


- [兴业金工 | 再论如何提升行业仓位测算精准度](https://mp.weixin.qq.com/s/TGlDvHlj2yFmLcj9MXN8Bg)
  - 问题：已有的行业指数未必能反应机构的正确持仓，尤其是对于偏好小市值风格的基金。针对这个问题，可以使用基金在各行业的历史持仓来构建该基金customized的行业指数，再在此基础上做Lasso回归或者卡尔曼滤波。

## Style Rotation

- UBS | Timing sector rotations in China from a Quant perspective
  - propose a comprehensive model to forecast sector rotations in China, three aspects of signals: 
    - fundamental drivers; smart-money positioning; news sentiment
  - Methodology: 
    1. give each stock a Fundamental Drivers score and sort the universe into
       deciles accordingly.
    2. calculate the sector weights within the top and bottom decile.
    3. subtract the weights from the top decile minus the bottom decile to arrive
       at implied sector weights.
    4. Repeat step 1 to 3 for Northbound Positioning and News Sentiment scores.
