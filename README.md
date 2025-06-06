# TV Show Language Distribution Analysis with Hadoop Streaming

This project analyzes TV show distribution by language using Hadoop Streaming with Python scripts (Mapper and Reducer). The dataset is `TMDB_tv_dataset_v3.csv`, stored in HDFS.

source: https://www.kaggle.com/datasets/asaniczka/full-tmdb-tv-shows-dataset-2023-150k-shows

---

## Prerequisites

✅ Hadoop installed and configured on your Azure VM
✅ NameNode and DataNode running
✅ HDFS accessible at `hdfs://localhost:9000/`
✅ `mapper.py` and `reducer.py` available on the VM under `/home/hadoop/mapreduce-scripts/`

---

## How to Run

### 1. SSH into the VM

```bash
ssh username@_ip_
```

---

### 2. Restart Hadoop Services

```bash
stop-yarn.sh
stop-dfs.sh
start-dfs.sh
start-yarn.sh
```

---

### 3. Remove Existing Output Directory

If the output directory exists from a previous run, delete it:

```bash
hdfs rm -r hdfs://localhost:9000/dataset/lang_output
```

---

### 4. Run the Hadoop Streaming Job

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input hdfs://localhost:9000/dataset/TMDB_tv_dataset_v3.csv \
  -output hdfs://localhost:9000/dataset/lang_output \
  -mapper /home/hadoop/mapreduce-scripts/mapper.py \
  -reducer /home/hadoop/mapreduce-scripts/reducer.py
```

---

### 5. View the Results

```bash
hdfs cat hdfs://localhost:9000/dataset/lang_output/part-00000
```

---

## Notes

* Make sure the CSV file is uploaded to HDFS at `/dataset/TMDB_tv_dataset_v3.csv` before running the job.
* The Mapper emits language codes as keys and counts as values.
* The Reducer aggregates counts and calculates percentages.
* Always delete the output directory before re-running the job to avoid conflicts.

---

## Example Output

```
aa      1       0.00%
ab      13      0.01%
af      88      0.05%
am      48      0.03%
ar      2638    1.56%
as      5       0.00%
...  
```

---


