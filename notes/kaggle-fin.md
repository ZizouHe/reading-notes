# Kaggle

## Kaggle Summary

- [Learnings From the Typical Tabular Pipeline](https://www.kaggle.com/code/rhysie/learnings-from-the-typical-tabular-pipeline)

## Ubiquant Market Prediction

- [Ubiquant Market Prediction](kaggle.com/competitions/ubiquant-market-prediction)

### 1st Place Solution

- [Kaggle discussion](https://www.kaggle.com/competitions/ubiquant-market-prediction/discussion/338220)

- Models
  - LGBM, TabNet
  - ensemble method : Average of (LGBM x 5 Folds) + (TabNet x 5 Folds)

- Feature Engineering:

  - Raw 300 features

  - The added 100 is calculated in the following way: the average value at each time_id for the top 100 features by obtaining and sorting the corr. of 300 features and the target. 相当于加了100维market information

    ```python
    features = [f'f_{i}' for i in range(300)]
    
    corr = train_df[features[:] + ['target']].corr()['target'].reset_index()
    corr['target'] = abs(corr['target'])
    corr.sort_values('target', ascending = False, inplace = True)
    best_corr = corr.iloc[3:103, 0].to_list()
    
    time_id_mean_features = []
    for col in tqdm(best_corr):
       mapper = train_df.groupby(['time_id'])[col].mean().to_dict()
       train_df[f'time_id_{col}'] = train_df['time_id'].map(mapper)
       train_df[f'time_id_{col}'] = train_df[f'time_id_{col}'].astype(np.float16)
       time_id_mean_features.append(f'time_id_{col}')
    
    features += time_id_mean_features
    ```

- Cross Validation for Training : KFold, GroupKFold

  - GroupKFold：按照标签Y分组Kfold

- Cross Validation for FE and Parameter Tuning : PurgedGroupTimeSeries, TimeSerieseSplit

  - PurgedGroupTimeSeries: 
    - [金融里的交叉验证](https://zhuanlan.zhihu.com/p/350110799)
    - [Combinatorial Purged Cross-Validation](https://stats.stackexchange.com/questions/443159/what-is-combinatorial-purged-cross-validation-for-time-series-data)
    - Marcos Lopez de Prado's "Advances in Financial Machine Learning" book (p. 163 - p. 165).
    - e.g.，数据按照时间分成6份，每次选择其中2份作为test，剩下当做training。在training set上进行purging and embargoing 防止对测试集的数据泄露。这样可以得到 C(6,2)=15种training/test split 和每一天 15*0.4=6 次test evaluation。每天可以至少被验证6次，降低validation loss的variance。

### 3rd Place Solution

- [Kaggle discussion](https://www.kaggle.com/competitions/ubiquant-market-prediction/discussion/338561)
- Models
  - 6 layers transformer, max_seq_length=3500 investments，在股票维度进行attention，每一天当做一个record。
  - 直接把Pearson correlation当做loss
- Data Augmentation
  - random zero (feature level) + random mask(sequence level) 在transformer角度 like BERT
- No feature engineering, no fancy Kfold split, just take the last 200 days as validation

### 5th Place Solution

- [Kaggle discussion](https://www.kaggle.com/competitions/ubiquant-market-prediction/discussion/338400)
- Model
  - Simple NN model with four dense layers(optimizer=Adam, loss='mse', metrics=[rmse,wcorr])

- Feature Engineering
  - target log transformation, removed 127 target outliers rows
  - transform features with sklearn QuantileTransformer
    - Quantile transformer with uniform distribution: 就直接output quantile，[0,1] 和 n_quantiles
    - Quantile transformer with uniform distribution:
      - calculate empirical ranks, using `numpy.percentile`
      - modify the ranking through interpolation, using `numpy.interp`
      - map to a Normal distribution by inverting the CDF, using `scipy.stats.norm.ppf`

- Custom Cross Validation for Training with 20 folds and 10 purge time_id.

### 7th Place Solution

- [Kaggle discussion](https://www.kaggle.com/competitions/ubiquant-market-prediction/discussion/338293)

- Model
  - Simple LGBM, the 'extra_trees' pamameter is set to 'True'. This gives steady improvement when the number of trees goes large.
- Feature engineering
  - This is kind of my secret. The model takes in 900+ features, which are selected from an even larger feature pool.
  - As a control, in the second submission I have a similar model but only used the 300 original features. That one scored 0.112 which is not even in the medal range.
- Cross validation
  - Standard TimeSerieseSplit applies.

### 17th Place Solution

- [Kaggle discussion](https://www.kaggle.com/competitions/ubiquant-market-prediction/discussion/338239)



## Two Sigma Financial Modeling Challenge

- [Two Sigma Financial Modeling Challenge](https://www.kaggle.com/c/two-sigma-financial-modeling)

### 8th Place Solution

- [Kaggle discussion](https://www.kaggle.com/competitions/two-sigma-financial-modeling/discussion/29793)
- Model
  - XGBoost
- Feature Engineering
  - adding **first and second order differences**
  - some interaction terms
  - cross sectionally normalized forms of input features

### 13th Place Solution 

- [Kaggle discussion](https://www.kaggle.com/competitions/two-sigma-financial-modeling/discussion/29518)
- Model
  - Ridge A - Selected Features trained on SignedExp( y+1 ). Some cleaning on features and filter on target instances. **This is a target transformation. It helps decrease correlation with other models. Improving the blend.**
  - Ridge B - Selected features and some cleaning on features and filter on target instances.
  - XGB - Selected Features and tuned hyperparameters on "all" trainset.
- Cross validation
  - 2 folds: timestamp > 906 and timestamp <= 906
  - 5 kfolds
  - rolling fit for ts> 906



## Jane Street Market Prediction

- [Jane Street Market Prediction](https://www.kaggle.com/c/jane-street-market-prediction)

### 1st Place Solution

- [Kaggle discussion](https://www.kaggle.com/competitions/jane-street-market-prediction/discussion/224348)
- Feature Engineering
  - Transfer all resp targets (resp, resp_1, resp_2, resp_3, resp_4) to action for multi-label classification
  - Use the mean of the absolute values of all resp targets as sample weights for training so that the model can focus on capturing samples with large absolute resp.
- Model
  - **Use autoencoder to create new features, concatenating with the original features as the input** to the downstream MLP model
  - Add target information to autoencoder to force it to generate more relevant features
  - Add Gaussian noise layer before encoder for data augmentation and to prevent overfitting
  - Train the model with 3 different random seeds and take the average to reduce prediction variance
  - Use **Hyperopt** to find the optimal hyperparameter set, it improves the score a lot.
- Cross validation
  - 5-fold 31-gap **purged group time-series split**

### 39th Place Solution

- [Kaggle discussion](https://www.kaggle.com/competitions/jane-street-market-prediction/discussion/224029)
- Feature Engineering
  - There were a number of discussions about the meaning of `feature_0` (buy/sell, long/short?). I have no idea what the correct answer is – my hypothesis is that it is produced by a separate JS model that selects the trading opportunities. [技术指标之JS](https://zhuanlan.zhihu.com/p/411812379)
  - Binary feature representing part of the trading day (before/after lunch)
  - Number of trades suggested by JS algorithm earlier today (for the first part of the day) or after lunch (for the second part of the day) - the intuition here that together with 'clock' this feature could also represent a market condition (e.g. more trade opportunities = more volatility)
- Target Engineering
  - Treating this task as multi-label classification leads to better results compared to trying to predict just one label - `resp`.
  - Add the mean value of `resp`, `resp_1`, `resp_2` and `resp_3` as a separate target which did improve the CV score. This can be thought of as a proxy for the general direction of returns over the whole `resp` time horizon.
- Model
  - 3-layer MLP with batch normalization and dropout.

- Cross validation
  - GroupKFold



## G-Research Crypto Forecasting

- [G-Research Crypto Forecasting](https://www.kaggle.com/c/g-research-crypto-forecasting)
- [G-Research Crypto金牌方案解读](https://zhuanlan.zhihu.com/p/517402931)

### 2nd Place Solution

- [Kaggle discussion](https://www.kaggle.com/competitions/g-research-crypto-forecasting/discussion/323098)

- Feature engineering
  - Feature engineering was guided by feature importance. Focused further effort on developing features sets that already performed well (had high importance).
- Model
  - LightGBM GBDT regressor with squared loss
- Cross validation
  - Pay attention to CV variance. An easy way to see if your CV scores have too much variance is to look at a plot of CV score vs. a parameter you're tuning. A good plot will usually be smooth, with a knee and a plateau, or maybe a peak or a valley.

### 3rd Place Solution

- [Kaggle discussion](https://www.kaggle.com/competitions/g-research-crypto-forecasting/discussion/323703)
- Feature engineering
  - Only 'Close' is used.
  - For 'Close', two features are prepared for multiple lag periods: the log of the ratio of the current value to the average during the period, and the log of the ratio of the current value to the value a certain period ago. Also take the average for all currencies. In addition, the difference between each currency and the average of all currencies was also prepared as a feature.
- Model
  - Single model of LightGBM
- Cross validation
  - 7 fold EmbargoCV, which is adding gap between training and validation sets.

## 7th Place Solution

- [知乎回答](https://zhuanlan.zhihu.com/p/517402931)
- Feature Engineering
  - 都是原始数据，仅添加当日时间特征
- Model
  - 把交易数据转化为2d的数据，使用position embedding、transformer encoder和MLP构建模型。

### 13th Place Solution

- [Kaggle discussion](https://www.kaggle.com/competitions/g-research-crypto-forecasting/discussion/313386)
- Feature Engineering
  - 8 lagged features - a simple mixture of EMA's, historical returns and historical volatility over various lookback periods
  - These 8 features were averaged across timestamps to produce 8 more
  - It was also important to perform some kind on binning on the features, especially for training the LGBM model. The commonly used ```reduce_mem_usage``` function and some rounding functions seemed to provide a suitable amount of bins. I found binning to 500-1000 unique values worked well for any given continuous feature.
- Model
  - Ensembles of LGBM and Keras NN models.

### 14th Place Solution

- [知乎回答](https://zhuanlan.zhihu.com/p/517402931)
- Feature Engineering
  - 使用了大量的技术指标作为特征，例如布林带、RSI、ATR、log_return等。



## Optiver Realized Volatility Prediction

- [Optiver Realized Volatility Prediction](https://www.kaggle.com/competitions/optiver-realized-volatility-prediction/data)

### 1st Place Solution

- [Kaggle discussion](https://www.kaggle.com/c/optiver-realized-volatility-prediction/discussion/274970)

- [Optiver波动率预测金牌方案解读](https://zhuanlan.zhihu.com/p/473531503)

- Feature Engineering

  - By compressing the time-id x stock-id price matrix to one dimension using t-SNE, we can recover the order of the time-id with sufficient accuracy.
  - 基于time_id的KNN：使用knn算法找到相近的timeid，并把以下重要的特征重新聚集一遍；反映时间特征。
  - 基于stock_id的kmeans：使用corr+kmeans，找到相近的stockid，并把以下重要的特征重新聚集一遍；反映行业特征。

  | 特征名                                   | 解释                                        |
  | ---------------------------------------- | ------------------------------------------- |
  | stock_id                                 | 股票代码                                    |
  | log_return_realized_volatility           | 过去10min基于买一和卖一报价计算的实现波动率 |
  | log_return_realized_volatility_300       | 过去5min基于买一和卖一报价计算的实现波动率  |
  | trade_seconds_in_bucket_count_unique_300 | 过去5min发生的交易的时刻数                  |
  | price_spread_mean                        | 交易价差                                    |
  | trade_seconds_in_bucket_count_unique     | 过去10min发生的交易的时刻数                 |
  | price_spread_mean_300                    | 过去5min交易价差                            |
  | trade_log_return_realized_volatility     | 过去10min基于成交价计算的实现波动率         |
  | trade_log_return_realized_volatility_300 | 过去5min基于成交价计算的实现波动率          |
  | log_return2_realized_volatility          | 过去10min基于买二和卖二报价计算的实现波动率 |
  | log_return2_realized_volatility_300      | 过去5min基于买二和卖二报价计算的实现波动率  |
  | wap_balance_mean                         | 过去10min的成交均价价差                     |
  | wap_balance_mean_300                     | 过去5min的成交均价价差                      |
  | trade_size_sum                           | 过去10min的交易量                           |
  | trade_size_sum_300                       | 过去5min的交易量                            |
  | ask_spead_mean                           | 基于卖方报价的价差                          |
  | bid_spead_mean                           | 基于买方报价的价差                          |
  | bid_ask_spead_mean                       | 基于买方和卖方报价的价差                    |

- Model

  - Three simple blends for prediction: LightGBM, 1D-CNN, and MLP