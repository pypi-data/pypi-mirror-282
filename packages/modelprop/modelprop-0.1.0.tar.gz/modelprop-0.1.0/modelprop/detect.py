from time import asctime
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn import metrics
from statsmodels.stats.outliers_influence import variance_inflation_factor
import warnings
warnings.filterwarnings('ignore')



class ModelEval:

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_optimum_threshold(df, target,score):
        '''
        Given probability score and binary target, returns the optimum cut off point, where
        `true positive rate` is high and `false positive rate` is low.
        
        Parameters
        ---------------

        df: pandas.DataFrame, DataFrame that contains binary target values - 0 & 1 and prediction scores
        target : str, Name of the target column. Default = Target
        score: str, Name of the probability score column. Default = Score

        Returns
        ---------------
        float : returns ROC AUC
        pd.DataFrame: returns a new DataFrame that provides tpr, fpr and optimum threshold
        matplotlib.pyplot : returns a ROC curve with cut-off point
        matplotlib.pyplot : returns a Target Separability Plot with threshold
        
        '''
        fpr, tpr, thresholds = metrics.roc_curve(df[target], df[score])
        roc_auc  = metrics.auc(fpr, tpr)


        #################################################################################
        #The optimal cut off would be where tpr is high and fpr is low
        # tpr-(1-fpr) is zero or near to zero is the optimal cut off point
        #################################################################################

        i = np.arange(len(tpr))   #index for df
        roc = pd.DataFrame({
            'fpr' : pd.Series(fpr, index = i),
            'tpr' : pd.Series(tpr, index = i),
            '1-fpr' : pd.Series(1-fpr, index = i),
            'tf' : pd.Series(tpr - (1-fpr), index = i),
            'thresholds' : pd.Series(thresholds, index= i)
        })

        cutoff_df = roc.iloc[(roc.tf-0).abs().argsort()[:1]].reset_index(drop=True)

        # Plot tpr vs 1-fpr
        fig, ax = plt.subplots()
        plt.plot(roc['tpr'], label='tpr')
        plt.plot(roc['1-fpr'], color='red', label='1-fpr')
        plt.xlabel('1-False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristics')
        ax.set_xticklabels([])
        plt.legend()

        #plot tpr vs 1-fpr
        fig2, ax2 = plt.subplots()
        sns.kdeplot(x=df[df[target] == 0][score], label='0')
        sns.kdeplot(x=df[df[target] == 1][score], label='1')
        plt.axvline(x=cutoff_df['thresholds'].values[0],
                    label='thresh:{:.2f}'.format(cutoff_df['thresholds'].values[0]), color='red', ls='--')
        plt.title('Target Separability')
        plt.legend()

        return roc_auc, cutoff_df, ax, ax2


    @staticmethod
    def get_decile_score(df, target, score, qcut_duplicates='drop', req_dig=True):
        '''
        Given probability scores and binary target, returns decile scores and cumulative gain plot

        Parameters
        ------------

        df: pandas.DataFrame, Dataframe that contains binary target values - 0 & 1 and prediction scores
        target: str, Name of the target column. Default = Target
        score: str, Name of the probability score column. Default = Score

        Returns
        ------------
        pd.DataFrame: returns a new DataFrame that provides Deciles Scores
        matplotlib.pyplot: returns a cumulative gain plot object
        
        '''


        df['inv_score'] = 1 - df[score]

        df.sort_values(by='inv_score', ascending=False, ignore_index=True, inplace=True)

        df['DecileRank'] = pd.qcut(df['inv_score'], q=10, labels=False, duplicates=qcut_duplicates) + 1

        decile_performance = df.groupby('DecileRank')[target].agg(
            ['count','sum']).sort_values(by='DecileRank', ascending=True).reset_index()
        decile_performance['cumsum'] = np.cumsum(decile_performance['sum'])

        decile_performance['gain'] = decile_performance['cumsum']/decile_performance['sum'].sum() * 100

        if req_dig:
            ax = plt.figure(figsize=(12, 8))
            plt.title('Decile Score - Cumulative Gain Plot')
            sns.lineplot(
                x = decile_performance['DecileRank'], y=decile_performance['gain'], label='model')
            sns.lineplot(x=decile_performance['DecileRank'], 
                         y=decile_performance['DecileRank']*10, label='avg')

            return decile_performance, ax
        else:
            return decile_performance


    @staticmethod
    def get_classification_report(clf, X, y, thres=0.5):
        '''
        Given model, X and y provides classification report for the model
        
        Parameters
        ------------

        clf: sklearn model, trained classification model that has predict_proba available
        X: pandas.DataFrame or numpy array, DataFrame/array that acts as independent variables for the model
        y: pandas.Series or numpy 1D-array, Series/1D-array that acts as the dependent/target variable for the model
        thres: float, optional. The probability threshold to determine 0 or 1. Default is 0.5

        Returns
        -----------

        classification report: str, returns classification report
        
        '''
        x_train_proba = clf.predict_proba(X)[:, 1]
        x_train_pred = np.where(x_train_proba > thres, 1, 0)

        clf_report = metrics.classification_report(y, x_train_pred)

        return clf_report


    @staticmethod
    def get_d3_gain(y_actual, y_prob):
        '''
        Given ytrue and yproba returns and 3rd decile cumulative gain
        
        Parameters
        ----------
        y_actual: pandas.Series or numpy 1D-array, Binary valued Series/1D-array that is actual values
        y_prob: pandas.Series or numpy 1D-array, Series/1D-array that is the probability score of y_actual being 1

        Returns
        -------
        classificationr report: str, returns classification report
        '''

        test_result = pd.DataFrame(y_actual.copy(), columns=['Target'])
        test_result['Score'] = y_prob

        ds = ModelViz.get_decile_score(test_result, req_dig=False)

        return ds[ds['DecileRank']==3]['gain'].values[0]
    
    @staticmethod
    def calculate_vif(X):
        vif = pd.DataFrame()
        vif['variables'] = X.columns
        vif['VIF'] = [variance_inflation_factor (X.values, i) for i in range(X.shape[1])]
        return vif
    


    def cal_iv_num(df, feature, target):
        df = df.copy()
        print(f"Processing numerical feature: {feature}")
        lst = []
        df[feature] = df[feature].replace([np.inf, -np.inf], np.nan)
        df[feature] = df[feature].fillna(0)
        df[feature] = pd.to_numeric(df[feature], errors='coerce')
        
        # Split continuous variables into max 10 bins based on percentile
        df[feature + '_bin'] = pd.qcut(df[feature], q=10, duplicates='drop')
        for val in df[feature + '_bin'].unique():
            lst.append([
                feature,
                val,
                df[df[feature + '_bin'] == val].count()[feature],
                df[(df[feature + '_bin'] == val) & (df[target] == 0)].count()[feature],
                df[(df[feature + '_bin'] == val) & (df[target] == 1)].count()[feature]
            ])
        
        data = pd.DataFrame(lst, columns=['Variable', 'Value', 'All', 'Good', 'Bad'])
        data['Share'] = data['All'] / data['All'].sum()
        data['Bad Rate'] = data['Bad'] / data['All']
        data['Distribution Good'] = (data['All'] - data['Bad']) / (data['All'].sum() - data['Bad'].sum())
        data['Distribution Bad'] = data['Bad'] / data['Bad'].sum()
        data['WoE'] = np.log(data['Distribution Good'] / data['Distribution Bad'])
        data = data.replace({'WoE': {np.inf: 0, -np.inf: 0}})
        data['IV_bin'] = data['WoE'] * (data['Distribution Good'] - data['Distribution Bad'])
        data = data.sort_values(by=['Variable', 'Value'], ascending=[True, True])
        data.index = range(len(data.index))
        data['IV'] = data['IV_bin'].sum()
        
        return data

    def cal_iv_cat(df, feature, target):
        df = df.copy()
        print(f"Processing categorical feature: {feature}")
        lst = []
        
        # Ignore features having more than 100 unique values
        if df[feature].nunique() > 100:
            return pd.DataFrame()
        
        df[feature] = df[feature].fillna(0)
        df[feature + '_bin'] = df[feature]
        
        for val in df[feature + '_bin'].unique():
            lst.append([
                feature,
                val,
                df[df[feature + '_bin'] == val].count()[feature],
                df[(df[feature + '_bin'] == val) & (df[target] == 0)].count()[feature],
                df[(df[feature + '_bin'] == val) & (df[target] == 1)].count()[feature]
            ])
        
        data = pd.DataFrame(lst, columns=['Variable', 'Value', 'All', 'Good', 'Bad'])
        data['Share'] = data['All'] / data['All'].sum()
        data['Bad Rate'] = data['Bad'] / data['All']
        data['Distribution Good'] = (data['All'] - data['Bad']) / (data['All'].sum() - data['Bad'].sum())
        data['Distribution Bad'] = data['Bad'] / data['Bad'].sum()
        data['WoE'] = np.log(data['Distribution Good'] / data['Distribution Bad'])
        data = data.replace({'WoE': {np.inf: 0, -np.inf: 0}})
        data['IV_bin'] = data['WoE'] * (data['Distribution Good'] - data['Distribution Bad'])
        data = data.sort_values(by=['Variable', 'Value'], ascending=[True, True])
        data.index = range(len(data.index))
        data['IV'] = data['IV_bin'].sum()
        
        return data

    def get_information_value(df, cat_vars, target):
        data = pd.DataFrame()
        varlist = list(df.columns)
        
        for var in varlist:
            if var in cat_vars:
                data = data.append(cal_iv_cat(df, var, target), ignore_index=True)
            else:
                data = data.append(cal_iv_num(df, var, target), ignore_index=True)
        
        return data