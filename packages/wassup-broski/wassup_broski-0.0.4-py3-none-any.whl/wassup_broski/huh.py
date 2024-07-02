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

haha_this_is_five = """
Creating the table:
create table if not exists movies( 
 id int, 
 name string, 
 genre string
) row format delimited fields terminated by ','; 

Loading the data into the table:
load data local inpath 'movies.csv' into table  movies;

a. To find the movie with the highest average rating.      
select movie_id, avg(rating) as avg_rating 
from ratings 
group by movie_id 
order by avg_rating desc 
limit 1;

b. Identify the most active users based on the number of ratings submitted.    
select user_id, count(*) as num_ratings 
from ratings 
group by user_id 
order by num_ratings desc 
limit 10;

c. Discover movies with the highest number of positive ratings. 
assuming a positive rating is 4 or 5: 
select movie_id, count(*) as positive_ratings 
from ratings 
where rating >= 4 
group by movie_id 
order by positive_ratings desc 
limit 10;
"""

bro_give_up_this_is_three = """
MyMaxMin.java:
import org.apache.hadoop.conf.Configuration; 
import org.apache.hadoop.io.IntWritable; 
import org.apache.hadoop.fs.Path; 
import org.apache.hadoop.io.Text; 
import org.apache.hadoop.mapreduce.Job; 
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat; 
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat; 
public class maxtemperature { 
 public static void main(String[] args) throws Exception { 
  Configuration conf = new Configuration(); 
 
  Job job = Job.getInstance(conf, "maxtemperature"); 
  job.setJarByClass(maxtemperature.class); 
  // TODO: specify a mapper 
  job.setMapperClass(MaxTempMapper.class); 
  // TODO: specify a reducer 
  job.setReducerClass(MaxTempReducer.class); 
  // TODO: specify output types 
  job.setOutputKeyClass(Text.class); 
  job.setOutputValueClass(IntWritable.class); 
  // TODO: specify input and output DIRECTORIES (not files) 
  FileInputFormat.setInputPaths(job, new Path(args[0])); 
  FileOutputFormat.setOutputPath(job, new Path(args[1])); 
  if (!job.waitForCompletion(true)) 
   return; 
 } 
} 

MaxTempReducer.java
import java.io.IOException; 
import org.apache.hadoop.io.Text; 
import org.apache.hadoop.io.IntWritable; 
import org.apache.hadoop.mapreduce.Reducer; 
public class MaxTempReducer extends Reducer<Text, IntWritable, Text, IntWritable>  
{ 
public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException  { 
  int maxvalue=Integer.MIN_VALUE; 
  for (IntWritable value : values)  
    { 
        maxvalue=Math.max(maxvalue, value.get()); 
    } 
    context.write(key, new IntWritable(maxvalue)); 
 } 
}

MaxTempMapper.java
import java.io.IOException; 
import org.apache.hadoop.io.LongWritable; 
import org.apache.hadoop.io.Text; 
import org.apache.hadoop.io.IntWritable; 
import org.apache.hadoop.mapreduce.Mapper; 
public class MaxTempMapper extends Mapper<LongWritable, Text, Text, IntWritable> { 
 
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException { 
        String line=value.toString(); 
        String year=line.substring(15,19); 
        int airtemp; 

        if(line.charAt(87)== '+') 
        { 
            airtemp=Integer.parseInt(line.substring(88,92)); 
        } 
        else 
        {
            airtemp=Integer.parseInt(line.substring(87,92)); 
        }

        String q=line.substring(92,93); 
        if(airtemp!=9999&&q.matches("[01459]")) 
        { 
            context.write(new Text(year),new IntWritable(airtemp));   
        } 
    }
}
"""

i_admire_2_be_like_you = """
WCDriver.java
import java.io.IOException; 
import org.apache.hadoop.conf.Configured; 
import org.apache.hadoop.fs.Path; 
import org.apache.hadoop.io.IntWritable; 
import org.apache.hadoop.io.Text; 
 
import org.apache.hadoop.mapred.FileInputFormat; 
import org.apache.hadoop.mapred.FileOutputFormat; 
import org.apache.hadoop.mapred.JobClient; 
import org.apache.hadoop.mapred.JobConf; 
import org.apache.hadoop.util.Tool; 
import org.apache.hadoop.util.ToolRunner; 
 
public class WCDriver extends Configured implements Tool  
{ 
 public int run(String args[]) throws IOException 
 { 
  if (args.length < 2) 
  { 
   System.out.println("Please give valid inputs"); 
   return -1; 
  } 
 
  JobConf conf = new JobConf(WCDriver.class); 
  FileInputFormat.setInputPaths(conf, new Path(args[0])); 
  FileOutputFormat.setOutputPath(conf, new Path(args[1])); 

  conf.setMapperClass(WCMapper.class); 
  conf.setReducerClass(WCReducer.class);

  conf.setMapOutputKeyClass(Text.class); 
  conf.setMapOutputValueClass(IntWritable.class);

  conf.setOutputKeyClass(Text.class); 
  conf.setOutputValueClass(IntWritable.class);

  JobClient.runJob(conf); 
  return 0; 
 }

 // Main Method 
 public static void main(String args[]) throws Exception 
 { 
  int exitCode = ToolRunner.run(new WCDriver(), args); 
  System.out.println(exitCode); 
 } 
}

WCMapper.java
import java.io.IOException; 
import org.apache.hadoop.io.IntWritable; 
import org.apache.hadoop.io.LongWritable; 
import org.apache.hadoop.io.Text; 
import org.apache.hadoop.mapred.MapReduceBase; 
import org.apache.hadoop.mapred.Mapper; 
import org.apache.hadoop.mapred.OutputCollector; 
import org.apache.hadoop.mapred.Reporter;

public class WCMapper extends MapReduceBase implements 
Mapper<LongWritable, Text, Text, IntWritable>  
{  
    // Map function 
    public void map(LongWritable key, Text value, OutputCollector<Text, IntWritable> output, Reporter rep) throws IOException 
    { 
        String line = value.toString(); 
        // Splitting the line on spaces 
        for (String word : line.split(" "))  
        { 
            if (word.length() > 0) 
            { 
                output.collect(new Text(word), new IntWritable(1)); 
            } 
        } 
    } 
}

WCReducer.java
import java.io.IOException; 
import java.util.Iterator; 
import org.apache.hadoop.io.IntWritable; 
import org.apache.hadoop.io.Text; 
 
import org.apache.hadoop.mapred.MapReduceBase; 
import org.apache.hadoop.mapred.OutputCollector; 
import org.apache.hadoop.mapred.Reducer; 
import org.apache.hadoop.mapred.Reporter; 
 
public class WCReducer extends MapReduceBase implements Reducer<Text, 
IntWritable, Text, IntWritable>  
{ 
    // Reduce function 
    public void reduce(Text key, Iterator<IntWritable> value,  OutputCollector<Text, IntWritable> output, Reporter rep) throws IOException 
    { 
        int count = 0; 
        // Counting the frequency of each words 
        while (value.hasNext())  
        { 
            IntWritable i = value.next(); 
            count += i.get(); 
        } 
        output.collect(key, new IntWritable(count)); 
    } 
} 
"""