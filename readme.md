# USDA DATA Profile

## Contents

- [USDA DATA Profile](#usda-data-profile)
  - [Contents](#contents)
  - [Introduction](#introduction)
  - [Accessing the data](#accessing-the-data)
  - [Map foods](#map-foods)
    - [List foods](#list-foods)
    - [Get a specific food](#get-a-specific-food)
  - [Examples](#examples)
    - [Foundation Foods](#foundation-foods)
    - [Experimental Foods](#experimental-foods)
    - [SR Legacy](#sr-legacy)
    - [Food and Nutrient Database for Dietary Studies 2019-2020 (FNDDS 2019-2020)](#food-and-nutrient-database-for-dietary-studies-2019-2020-fndds-2019-2020)
    - [The USDA Global Branded Food Products Database (Branded Foods)](#the-usda-global-branded-food-products-database-branded-foods)


## Introduction
The [USDA Food Central database](https://fdc.nal.usda.gov/about-us.html) was established to document the nutritional information in food sold and distributed in the USA. 

> Provides a broad snapshot in time of the nutrients and other components found in a wide variety of foods and food products.

It combines five separate data sources:
1. Foundation Foods
1. Experimental Foods
1. SR Legacy
1. Food and Nutrient Database for Dietary Studies 2019-2020 (FNDDS 2019-2020)
1. USDA Global Branded Food Products Database (Branded Foods)

[Wikipedia](https://en.wikipedia.org/wiki/USDA_National_Nutrient_Database) provides a good overview of the data set. The USDA website states the users of this data as:

> Can be used by, and has benefits for, a variety of users, including researchers, policy makers, academicians and educators, nutrition and health professionals, product developers, and others.


## Accessing the data
https://fdc.nal.usda.gov/api-guide.html


```python
import os
import sys
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath('__file__'))))

from src.utils.connect import DatabaseModelsClass
from src.get_data import GetData
usda = GetData()
```

## Map foods
All foods in the USDA database will have to be mapped by paging through the `/foods/list' API to obtain the fdcId of each food.

### List foods
Use of the `/v1/foods/list' call to page through all foods in the database. A query parameter can be given to distinguish between one of the five data types.

Fields in `list'

```python
list = usda.get_food_list()
```

    2353623 | A Low-Starch and High-Fiber Diet Intervention Impacts the Microbial Community of Raw Bovine Milk | Experimental | 2022-10-28
    2341752 | Abalone | Survey (FNDDS) | 2022-10-28
    167782 | Abiyuch, raw | SR Legacy | 2019-04-01
    171687 | Acerola juice, raw | SR Legacy | 2019-04-01
    171686 | Acerola, (west indian cherry), raw | SR Legacy | 2019-04-01
    

### Get a specific food
Use of the `/v1/food/{fdcId}' call get details about a specific food in the database.

## Examples
### Foundation Foods
Foundation Foods includes values derived from analyses for food components, including nutrients on a diverse range of foods and ingredients as well as extensive underlying metadata. These metadata include the number of samples, sampling location, date of collection, analytical approaches used, and if appropriate, agricultural information such as genotype and production practices. The enhanced depth and transparency of Foundation Foods data can provide valuable insights into the many factors that influence variability in nutrient and food component profiles. The goal of Foundation Foods will be to, over time, expand the number of basic foods and ingredients and their underlying data.


```python
list = usda.get_food_list("Foundation")
```

    2262074 | Almond butter, creamy | Foundation | 2022-04-28
    2257045 | Almond milk, unsweetened, plain, refrigerated | Foundation | 2022-04-28
    1999631 | Almond milk, unsweetened, plain, shelf stable | Foundation | 2021-10-28
    2003590 | Apple juice, with added vitamin C, from concentrate, shelf stable | Foundation | 2021-10-28
    1750340 | Apples, fuji, with skin, raw | Foundation | 2020-10-30
    


```python
data = usda.get_food_fdcid('1750340')
```

    fdcId: LONG RESPONSE...
    description: Apples, fuji, with skin, raw
    publicationDate: 10/30/2020
    foodNutrients: LONG RESPONSE...
    dataType: Foundation
    foodClass: FinalFood
    scientificName: Malus domestica
    inputFoods: LONG RESPONSE...
    foodComponents: LONG RESPONSE...
    foodAttributes: LONG RESPONSE...
    nutrientConversionFactors: LONG RESPONSE...
    ndbNumber: LONG RESPONSE...
    isHistoricalReference: LONG RESPONSE...
    foodCategory: LONG RESPONSE...
    

### Experimental Foods
Experimental Foods contains foods produced, acquired, or studied under unique conditions, such as alternative management systems, experimental genotypes, or research/analytical protocols. The foods in this data type may not be commercially available to the public or the data may expand information about the specific food. Experimental Foods are for research purposes and may not be appropriate as a reference for the consumer or for diet planning. Experimental Foods data may also be available through links to relevant agricultural research data sources, such as the AgCROS. The data in Experimental Foods may include (or link to) variables such as genetics, environmental inputs and outputs, supply chains, economic considerations, and nutrition research. These data will allow users to examine a range of factors used that may affect the profiles of food components, including nutrients and resulting dietary intakes as well as the sustainability of agricultural and dietary food systems.


```python
list = usda.get_food_list("Experimental")
```

    2353623 | A Low-Starch and High-Fiber Diet Intervention Impacts the Microbial Community of Raw Bovine Milk | Experimental | 2022-10-28
    2516771 | Amino Acid Digestibility of Extruded Chickpea and Yellow Pea Protein is High and Comparable in Moderately Stunted South Indian Children with Use of a Dual Stable Isotope Tracer Method | Experimental | 2023-04-20
    1999623 | Associations of polymorphisms in the promoter I of bovine acetyl-CoA carboxylase-a gene with beef fatty acid composition | Experimental | 2021-10-28
    1750335 | AtPDS overexpression in tomato: exposing unique patterns of carotenoid self‐regulation and an alternative strategy for the enhancement of fruit carotenoid content | Experimental | 2021-04-23
    2516768 | Bioaccessibility and intestinal cell uptake of carotenoids and chlorophylls differ in powdered spinach by the ingredient form as measured using in vitro gastrointestinal digestion and anaerobic fecal fermentation models | Experimental | 2023-04-20
    


```python
data = usda.get_food_fdcid('2516768')
```

    fdcId: LONG RESPONSE...
    description: Bioaccessibility and intestinal cell uptake of carotenoids and chlorophylls differ in powdered spinach by the ingredient form as measured using in vitro gastrointestinal digestion and anaerobic fecal fermentation models
    publicationDate: 4/20/2023
    dataType: Experimental
    foodClass: Experimental
    abstract: Scientific journal extract..
    title: Bioaccessibility and intestinal cell uptake of carotenoids and chlorophylls differ in powdered spinach by the ingredient form as measured using in vitro gastrointestinal digestion and anaerobic fecal fermentation models
    doiNumber: https://doi.org/10.1039/d2fo00051b
    doiUrl: https://doi.org/10.1039/d2fo00051b
    studyDesign: Scientific journal extract..
    results: Scientific journal extract..
    authors: LONG RESPONSE...
    affiliations: LONG RESPONSE...
    

### SR Legacy
SR Legacy has been the primary food composition data type in the United States for decades. It provides a comprehensive list of values for food components, including nutrients derived from analyses, imputations, and the published literature. This data type has provided the values for most other public and private food composition databases and has supported a wide range of public policy initiatives, research studies, and diet planning and education activities. SR Legacy, released in April 2018, is the final release of this data type and will not be updated. For more recent data, users should search other data types in FoodData Central.


```python
list = usda.get_food_list("SR Legacy")
```

    167782 | Abiyuch, raw | SR Legacy | 2019-04-01
    171687 | Acerola juice, raw | SR Legacy | 2019-04-01
    171686 | Acerola, (west indian cherry), raw | SR Legacy | 2019-04-01
    168061 | Acorn stew (Apache) | SR Legacy | 2019-04-01
    168992 | Agave, cooked (Southwest) | SR Legacy | 2019-04-01
    


```python
data = usda.get_food_fdcid('168992')
```

    fdcId: LONG RESPONSE...
    description: Agave, cooked (Southwest)
    publicationDate: 4/1/2019
    foodNutrients: LONG RESPONSE...
    dataType: SR Legacy
    foodClass: FinalFood
    foodComponents: LONG RESPONSE...
    foodAttributes: LONG RESPONSE...
    nutrientConversionFactors: LONG RESPONSE...
    inputFoods: LONG RESPONSE...
    ndbNumber: LONG RESPONSE...
    isHistoricalReference: LONG RESPONSE...
    foodCategory: LONG RESPONSE...
    

### Food and Nutrient Database for Dietary Studies 2019-2020 (FNDDS 2019-2020)
Food and Nutrient Database for Dietary Studies 2019-2020 (FNDDS 2019-2020) provides nutrient and food component values for the foods and beverages reported in What We Eat in America, the dietary intake component of the National Health and Nutrition Examination Survey (NHANES). FNDDS data releases correspond to the NHANES two-year data cycles. FNDDS data facilitate analyses of dietary intakes reported in NHANES as well as many other dietary research studies.


```python
list = usda.get_food_list("Survey (FNDDS)")
```

    2341752 | Abalone | Survey (FNDDS) | 2022-10-28
    2344293 | Adobo, with noodles | Survey (FNDDS) | 2022-10-28
    2344443 | Adobo, with rice | Survey (FNDDS) | 2022-10-28
    2345842 | Agave liquid sweetener | Survey (FNDDS) | 2022-10-28
    2346197 | Alcoholic malt beverage | Survey (FNDDS) | 2022-10-28
    


```python
data = usda.get_food_fdcid('2346197')
```

    foodClass: Survey
    description: Alcoholic malt beverage
    foodNutrients: LONG RESPONSE...
    foodAttributes: LONG RESPONSE...
    foodCode: 93106100
    startDate: 1/1/2019
    endDate: 12/31/2020
    wweiaFoodCategory: LONG RESPONSE...
    dataType: Survey (FNDDS)
    fdcId: LONG RESPONSE...
    foodPortions: LONG RESPONSE...
    publicationDate: 10/28/2022
    inputFoods: LONG RESPONSE...
    

### The USDA Global Branded Food Products Database (Branded Foods)
The USDA Global Branded Food Products Database (Branded Foods), formerly hosted on the USDA Food Composition Databases website, are data from a public-private partnership whose goal is to enhance the open sharing of nutrient data that appear on branded and private label foods and are provided by the food industry.


```python
list = usda.get_food_list("Branded")
```

    2533357 |  ALL NATURAL GLUTEN FREE CHICKEN NUGGETS | Branded | 2023-04-27
    1861692 |  BERRY NUT BLEND BREAKFAST IN THE GO!  | Branded | 2021-07-29
    2527760 |  CHEDDAR & SOUR CREAM FLAVORED POTATO CHIPS | Branded | 2023-04-27
    2216356 |  CHOCOLATE CAKE HOOPIE PIES,  CHOCOLATE CAKE | Branded | 2022-01-06
    1909487 |  COCONUT WATER BARS, MANGO | Branded | 2021-07-29
    


```python
data = usda.get_food_fdcid('1861692')
```

    discontinuedDate: 
    foodComponents: LONG RESPONSE...
    foodAttributes: LONG RESPONSE...
    foodPortions: LONG RESPONSE...
    fdcId: LONG RESPONSE...
    description:  BERRY NUT BLEND BREAKFAST IN THE GO! 
    publicationDate: 7/29/2021
    foodNutrients: LONG RESPONSE...
    dataType: Branded
    foodClass: Branded
    modifiedDate: 9/8/2018
    availableDate: 9/8/2018
    brandOwner: Snyder's-Lance, Inc.
    brandName: EMERALD
    dataSource: LI
    brandedFoodCategory: Popcorn, Peanuts, Seeds & Related Snacks
    gtinUpc: 010300064220
    ingredients: VANILLA GRANOLA (ROLLED OATS, BROWN SUGAR, WHEAT FLAKES, WHOLE OAT FLOUR, CANOLA OIL, CORN SYRUP, RICE FLOUR, ARTIFICIAL FLAVOR, SALT, MIXED TOCOPHEROLS [TO PRESERVE FRESHNESS], RICE EXTRACT, DISTILLED MONOGLYCERIDES, BARLEY MALT EXTRACT), COCKTAIL PEANUTS (PEANUTS, PEANUT AND/OR COTTONSEED OIL, SALT), YOGURT FLAVORED RAISINS (YOGURT COATING [SUGAR, PARTIALLY HYDROGENATED PALM KERNEL OIL, CALCIUM CARBONATE, YOGURT POWDER {CULTURED WHEY PROTEIN CONCENTRATE, CULTURED SKIM MILK, AND YOGURT CULTURE}, ARTIFICIAL COLOR, SOY LECITHIN {AN EMULSIFIER}, NATURAL FLAVOR], RAISINS, SUNFLOWER OIL, CORN SYRUP, MODIFIED STARCH, COCONUT OIL, CONFECTIONER'S GLAZE), INFUSED DRIED CRANBERRIES (SLICED CRANBERRIES, SUGAR, GLYCERIN, SUNFLOWER OIL), GLAZED WALNUTS (WALNUTS, SUGAR, CORN SYRUP, SESAME SEEDS, SALT, CANOLA OIL, NATURAL FLAVORS, SOY LECITHIN [AN EMULISIFIER], CITRIC ACID), INFUSED DRIED BLUEBERRY FLAVORED CRANBERRIES (SLICED CRANBERRIES, SUGAR, BLUEBERRY JUICE, SUNFLOWER OIL, NATURAL BLUEBERRY FLAVOR, MALIC ACID), DUSTED WITH: MALTODEXTRIN, MANNITOL, MODIFIED CELLULOSE.
    marketCountry: United States
    servingSize: LONG RESPONSE...
    servingSizeUnit: g
    packageWeight: 212.5 g/7.5 oz
    foodUpdateLog: LONG RESPONSE...
    labelNutrients: LONG RESPONSE...
    
