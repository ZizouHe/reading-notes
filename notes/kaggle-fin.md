# Kaggle

## Ubiquant Market Prediction

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
- Feature engineer:
  - This is kind of my secret. The model takes in 900+ features, which are selected from an even larger feature pool.
  - As a control, in the second submission I have a similar model but only used the 300 original features. That one scored 0.112 which is not even in the medal range.
- Cross validation
  - Standard TimeSerieseSplit applies.

### 17th Place Solution

- [Kaggle discussion](https://www.kaggle.com/competitions/ubiquant-market-prediction/discussion/338239)