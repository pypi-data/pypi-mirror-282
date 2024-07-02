this_is_the_sixth_program = """
# pip install pyspark

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MovieRatingsAnalysis").getOrCreate()

# Load the datasets
movies_df = spark.read.csv("/Users/amithpradhaan/Desktop/ml-latest-small/movies.csv", 
header=True, inferSchema=True)

ratings_df = spark.read.csv("/Users/amithpradhaan/Desktop/ml-latest-small/ratings.csv", 
header=True, inferSchema=True)

# Create the RDDs
movies_rdd = movies_df.rdd 
ratings_rdd = ratings_df.rdd

# Find the Movie with the Lowest Average Rating Using RDD.

# Compute average ratings
avg_ratings_rdd = ratings_rdd.map(lambda x: (x['movieId'], (x['rating'], 1)))\
.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))\
.mapValues(lambda x: x[0] / x[1])

# Find the movie with the lowest average rating 
lowest_avg_rating = avg_ratings_rdd.sortBy(lambda x: x[1]).first() 
print(f"Movie with the lowest average rating: {lowest_avg_rating}")

# Identify Users Who Have Rated the Most Movies.

# Compute number of ratings per user 
user_ratings_count = ratings_rdd.map(lambda x: (x['userId'], 1))\
.reduceByKey(lambda x, y: x + y)\
.sortBy(lambda x: x[1], ascending=False)\
 
# Get top users 
top_users = user_ratings_count.take(10) 
print(f"Top users by number of ratings: {top_users}")

# Explore the Distribution of Ratings Over Time.

from pyspark.sql.functions import from_unixtime, year, month 

# Convert timestamp to date and extract year and month 
ratings_df = ratings_df.withColumn("year", year(from_unixtime(ratings_df['timestamp'])))\
.withColumn("month", month(from_unixtime(ratings_df['timestamp']))) 

# Group by year and month to get rating counts 
ratings_over_time = ratings_df.groupBy("year", "month").count().orderBy("year", "month") 
 
# Show distribution 
ratings_over_time.show()

# Find the Highest-Rated Movies with a Minimum Number of Ratings. 

# Set a minimum number of ratings, ex: 100. 
# Compute average ratings and count ratings per movie 
movie_ratings_stats = ratings_rdd.map(lambda x: (x['movieId'], (x['rating'], 1)))\
    .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))\
    .mapValues(lambda x: (x[0] / x[1], x[1]))  

# (avg_rating, count) 
# Filter movies with a minimum number of ratings 
min_ratings = 100 
qualified_movies = movie_ratings_stats.filter(lambda x: x[1][1] >= min_ratings)
 
# Find the highest-rated movies 
highest_rated_movies = qualified_movies.sortBy(lambda x: x[1][0], ascending=False).take(10) 
print(f"Highest-rated movies with at least {min_ratings} ratings: {highest_rated_movies}") 
"""

lo_vade_this_is_seven = """
from pyspark.sql import SparkSession 
spark=SparkSession.builder.appName('housing_price_model').getOrCreate() 

#create spark dataframe of input csv file 
df=spark.read.csv('/content/drive/MyDrive/cruise_ship_info.csv',inferSchema=True,header=True) 
df.show(10) 
#prints structure of dataframe along with datatype 
df.printSchema() 

#In our predictive model, below are the columns 
df.columns 

from pyspark.ml.feature import StringIndexer 
indexer=StringIndexer(inputCol='Cruise_line',outputCol='cruise_cat') 
indexed=indexer.fit(df).transform(df) 
#above code will convert string to numeric feature and create a new dataframe 
#new dataframe contains a new feature 'cruise_cat' and can be used further 
#feature cruise_cat is now vectorized and can be used to fed to model 
for item in indexed.head(5): 
    print(item) 
    print('\n')
    
from pyspark.ml.linalg import Vectors 
from pyspark.ml.feature import VectorAssembler 

#creating vectors from features 
#Apache MLlib takes input if vector form 
assembler=VectorAssembler(inputCols=['Age', 
 'Tonnage', 
 'passengers', 
 'length', 
 'cabins', 
 'passenger_density', 
 'cruise_cat'],outputCol='features') 

output=assembler.transform(indexed) 
output.select('features','crew').show(5) 

#final data consist of features and label which is crew. 
final_data=output.select('features','crew') 

#splitting data into train and test 
train_data,test_data=final_data.randomSplit([0.7,0.3]) 
train_data.describe().show() 
test_data.describe().show() 

#import LinearRegression library 
from pyspark.ml.regression import LinearRegression 

#creating an object of class LinearRegression 
#object takes features and label as input arguments 

ship_lr=LinearRegression(featuresCol='features',labelCol='crew') 
#pass train_data to train model 

trained_ship_model=ship_lr.fit(train_data) 

#evaluating model trained for Rsquared error 
ship_results=trained_ship_model.evaluate(train_data) 
print('Rsquared Error :',ship_results.r2) 

#testing Model on unlabeled data 
#create unlabeled data from test_data 
unlabeled_data=test_data.select('features') 
 
unlabeled_data.show(5) 
predictions=trained_ship_model.transform(unlabeled_data) 
predictions.show()
"""