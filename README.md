This project is about predicting contribution to outlet sales, against each item that is sold, given mrp,store location, store size, item type and other features.

# Few points worth mentioning regarding directory structure:
- csv is placed under data/raw/
- Processed csv is places under data/processed after computation
- Notebook is present in notebooks folder
- bigmart_sales is a package which load all initial packages(__init__.py) and sets data file paths under config.py
  ++ Abstracts the messy paths in the main notebook to here, so that cleaner view can be provided
- scripts folder is a placeholder for future purposes
## How to run this?
  ++ start Anaconda prompt and go to this folder's parent location and type jupyter notebook
  ++ notebook starts with the parent folder as the base location and you can navigate to different projects from there


- I have used DecisionTreeRegressor and LinearRegression(with multiple variables)
	
---------------------------------------------------
New additions:
--------------------------------------------------
++Use KFolds instead of train_test_splits 

++write a OOPS style framework for running different ML regressor algo on the cleaned data and compare performance and choose the best ML model suited for this model

-------------------------------------------------- 
Exploratory data analysis
--------------------------------------------------
- There is one category Outlet_Establishment_Year, which actually has very a few values, is discrete also and hence should be categorical instead
	- I created one feature Outlet_age from Establishment year and deleted the former
- There are arund 3k entries in which either Item_Weight or Outlet_Size is missing
	- 1 frame without those, and will be referred by cleaned dataframe
	- 1 frame with these missing values handled by mean for Item_Weight and mode for Outlet_Size
- Few outliers in Item_Outlet_Sales , Item_Weight,Item_Visibility removed
- Zero values in Item_Visibilty : replaced with median

### Correlation
	- Cleaned dataframe has higher correlation of Item_MRP,Item_Weight to Item_Outlet_Sales, except Item_Visibiity
	- Original dataframe has lower as compared, except for Item_Visibilty which has higher corrleation wrt cleaned dataframe
### Categorical columns analysis
	- Outlet_Type
		- Cleaned dataframe has only 2 Outlet_Types, out of which Super Market Type 1 makes more significant contribution towards outlet sales than Super Market Type 2
		- Original dataframe states Super Market Type 3 contributing more, followed by Super Market Type 1 
		- Both datsets have Super Market Type 1 as the maximum occuring type for outlet_Type

	- Outlet_Identifier : Overall this is redundant column to keep
		- we can derive the same information from the Outet_Type these identifiers belongs to
		- Out027 makes the most sales, and it belongs to SuperMarket_Type3 which makes the most
		   - Grocery Stores have OUT010,OUT019
		   - Super Market Type 1 has OUT049, OUT013,OUT045,OUT017,OUT046,OUT035
		   - Super Market Type 2 has only OUT018
		   - Super Market Type 3 has only OUT027
	- Outlet_Size : Medium and High sized stores have more sales as compared to small ones
		- Grocery Stores,Super Market Type 1, Super Market Type 2 are having all 3 sizes small,medium and high and even the sale is ranging from 75 till 6k
		- Super Market Type 3 is only medium sized stores
	- Outlet_Location_Type : 
		- Tier-2 makes the most, followed by Tier 3
		- Tier-2 are small ones, tier-3 are both medium and high, so significant conclusion from just Outlet_Size alone
	- ** Outlet_age : Derived attribute from establishment year
		- Amlmost no correlation exists
	- *item_identifier : derived new identifier from the prefix of Item_Identifier
		- Item_Identifier has very less/insignificant effect on sales
	- Item_Fat_Content : cleaned the values to map to two categories Low fat and Regular
		- They have very less difference in sale contribution
	- ** Item_iden_Type : created a new column from Item_Type and Item_Identifier, since they seperately dont explain much when we build later on
		- Inside Food Item_Identifier, seafood, starchy_foods, snack foods have more sale contribution, irrespective of their sale quantity being less
		- Inside drinks, Hard drinks contribute more than soft_srinks
- ** means new features from old ones(feature engineering)  

   #### summary:
      - SuperMarket_Type3 (most sales contributor) is medium sized, followed by Type 1 which belongs to all 3 sizes
      - Further suggests that sales contribution has nothing to do with Outlet_dIdentifier
      - Outlet_Identifier is for sure redundant and will result in multi-collinearity issue and hence not to be included
      - as per Outlet_Size -  High and medium makes most
      - as per Outlet_Location_Type - Tier-2 makes most which are actually small sized stores, because medium ones are distrubited among different tiers(2 and 3)
      - Outlet_Location_Type when paired with Outlet_Type dictates the sales
	- eg. Tier 2 is making most overall from 2nd column bar graphs, but when Tier is combined with store type, Tier 3 with Super market Type 3 amkes the most
	- So both Outlet_Location_Type and Outlet_Type are important
      - Few items from Food and Non consumable category contribute more toward sale, as they are costlier

- Item_Outlet_Sales have a curvier rathan linear relation, linearregression wont do much good

-------------------------------------------------- 
Chi-square anlysis
--------------------------------------------------

- Original dataframe : Suggests to skip Outlet_Size
- cleaned dataframe : suggests to only accept Item_Weight and item_Iden_Type

-------------------------------------------------- 
Normalizations:
--------------------------------------------------
Normalization was done on 'Item_MRP','Item_Weight','Item_Visibility','Item_Outlet_Sales'

-------------------------------------------------- 
Model Tuning
--------------------------------------------------
Tuned RandomForestRegressor for n_estimator=500, max_features=16 for original

-------------------------------------------------- 
RESULT
--------------------------------------------------
- I have used DecisionTreeRegressor , LinearRegression and RandomForestRegressor
- original dataframeLinearRegression : performs better with average model score of 0.5459run over 5 KFolds, rmse : 0.157, accuracy : -66
- Cleaned dataframe :LinearRegression performs better with average model score of 0.46 run over 5 KFolds with original dataframe, rmse : 0.17, accuracy : 33
- The score is low as we have a curvier line representing the Item_Outlet_Sales
	- major contributer to more outlet sales is the mrp of the product which is sold
	- certain costly items like seafood, frozen foods , canned foods, breakfast food contribute more towards sale, despite the sales quantity being low
	- snack foods and Fruits/vegetables are the most sold food commodity, but the contribution is not as high as seafood/frozen foods/breakfast items/canned 
	- Drinks have overall less cost, so least contributor
		- Hard drinks contribute more
	- outlet location type or item_weight or Visibilty or outlet size have no or very less effect on sale contibution
	- results would be better if we can make the sales distribution follow a straighter line, may be remove the records contributing to higher curve or may be use more advanced model like xgboost(To be done)
	

