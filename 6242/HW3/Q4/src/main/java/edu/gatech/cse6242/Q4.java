package edu.gatech.cse6242;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;
import java.util.*;

public class Q4 {

  public static class MapperFirst
       extends Mapper<LongWritable, Text, Text, ArrayPrimitiveWritable> {

    public void map(LongWritable offset, Text value, Context context) 
    throws IOException, InterruptedException {

        StringTokenizer tok = new StringTokenizer(value.toString());

        Text col1 = new Text( tok.nextToken() );
        context.write( col1, new ArrayPrimitiveWritable(new int[]{1, 0}) );

        Text col2 = new Text( tok.nextToken() );        
        context.write( col2, new ArrayPrimitiveWritable(new int[]{0, 1}) );
    }

    private ArrayPrimitiveWritable toArray(int v1, int v2){     
        return new ArrayPrimitiveWritable( new int[]{v1, v2} );
    }
  }

  public static class ReducerFirst
       extends Reducer<Text, ArrayPrimitiveWritable, Text, Text> {
    public void reduce(Text key, Iterable<ArrayPrimitiveWritable> values, Context context) 
	throws IOException, InterruptedException {

	    Iterator<ArrayPrimitiveWritable> i = values.iterator();
	    int count = 0;
	    while ( i.hasNext() ){
	        int[] counts = (int[])i.next().get();
	        count += counts[0];
	        count -= counts[1];
	    }
	    context.write( new Text(Integer.toString(count)), key  );
	}
  }

  public static class MapperSecond
       extends Mapper<Object, Text, Text, IntWritable> {

    private final static IntWritable one = new IntWritable(1);
    // private Text nodeDiff = new Text();

    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
      	StringTokenizer itr = new StringTokenizer(value.toString());
      // while (itr.hasMoreTokens()) {
        Text nodeDiff = new Text(itr.nextToken());
        context.write(nodeDiff, one);
    }
  }

  public static class ReducerSecond
       extends Reducer<Text, IntWritable, Text, IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      result.set(sum);
      context.write(key, result);
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    conf.set("mapred.textoutputformat.separator", "");
    Job job1 = Job.getInstance(conf, "Q4");

    /* 1st map-reduce job */
    job1.setJarByClass(Q4.class);
    job1.setMapperClass(MapperFirst.class);
    job1.setReducerClass(ReducerFirst.class);
    job1.setMapOutputKeyClass(Text.class);
    job1.setMapOutputValueClass(ArrayPrimitiveWritable.class);
    job1.setOutputKeyClass(Text.class);
    job1.setOutputValueClass(Text.class);
    FileInputFormat.addInputPath(job1, new Path(args[0]));
    FileOutputFormat.setOutputPath(job1, new Path("int_out"));
    if (!job1.waitForCompletion(true)) {
    	System.exit(1);
    }

    Job job2 = Job.getInstance(conf, "Q4");

    /* 2nd map-reduce job */
    job2.setJarByClass(Q4.class);
    job2.setMapperClass(MapperSecond.class);
    job2.setReducerClass(ReducerSecond.class);
    job2.setMapOutputKeyClass(Text.class);
    job2.setMapOutputValueClass(IntWritable.class);
    job2.setOutputKeyClass(Text.class);
    job2.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job2, new Path("int_out"));
    FileOutputFormat.setOutputPath(job2, new Path(args[1]));
    System.exit(job2.waitForCompletion(true) ? 0 : 1);
  }
}
