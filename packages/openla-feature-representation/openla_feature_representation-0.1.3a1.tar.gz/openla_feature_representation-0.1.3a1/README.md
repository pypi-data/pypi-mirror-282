# openla-feature-representation: generate features for EventStream data

## Introduction

openla-feature-representation is an open-source Python module that generates features from [OpenLA](https://limu.ait.kyushu-u.ac.jp/~openLA/) EventStream data, to make the data easier to use for ML.

## Installation

This module module is available on PyPI and it can be installed using `pip` as follows:

```sh
pip install openla-feature-representation
```

### Downloading the model

For the E2Vec class, you will need the `openla-feature-representation-fastText_1min.bin` model .
Feel free to dowload it from the [OpenLA models download site](https://limu.ait.kyushu-u.ac.jp/~openLA/models/).

## Usage of the E2Vec class

First, import the `openla_feature_representation` package with an arbitrary name, here `lafr`.

```py
import openla_feature_representation as lafr
```

### Initializing the class

This is the constructor:

```py
e2Vec = lafr.E2Vec(ftmodel_path, input_csv_dir_path, course_id)
```

- `ftmodel_path` is the path to a fastText language model trained for this task
- `input_csv_dir_path` is the path to a directory with the dataset (see below)
- `course_id` is a string to identify files for the course to analyze within the `info_dir` directory (e.g. `'A-2023'`)

After getting your own `e2Vec` object, all methods the class provides can be used on it.

### Generate sentences for the event log

The fastText model uses an artificial language to express event log entries as sentences. This is how you can generate them:

```py
sentences = e2Vec.generate_sentences(
    sentences_dir_path=sentences_dir_path,
    eventstream_file_path=eventstream_file_path,
    input_csv_dir_path=input_csv_dir_path,
    course_id=course_id,
)
```

If you need to select or filter a time span:

```py
sentences = e2Vec.generate_sentences(
    sentences_dir_path=sentence_path,
    use_timespan=True,
    start_minute=0,
    total_minutes=90,
    eventstream_file_path=eventstream_file_path,
    input_csv_dir_path=input_csv_dir_path,
    course_id=course_id,
)
```

- `sentences_dir_path` is the path to the directory where you want the sentence files to be written
- `eventstream_file_path` is the path to the event stream csv file
- `input_csv_dir_path` is the path to a directory with the dataset (see below)
- `course_id` is a string to identify files for the course to analyze within the `info_dir` directory
- `use_timespan` if `True`, the args below will be used to extract a timespan from the data (optional)
- `start_minute` is the minute in the data the sentence generation should start (optional)
- `total_minutes` is the number of minutes worth of sentences that should be generated (optional)

This function saves the sentences to a text file and returns a path to it.

### Vectorize the sentences

This function returns a pandas DataFrame with the vectors generated from the sentences.

```py
user_vectors = e2Vec.vectorize_sentences(sentences_file_path)
```

- `sentences_file_path` is the path to the sentence files generated in the previous step

### Concatenation

The class has a function to concatenate vectors by time (minutes) or weeks.

This will concatenate the vectors in 10-minute spans.

```py
vectors = e2Vec.concatenate_vectors(
    sentences_dir_path=sentences_dir_path,
    eventstream_file_path=eventstream_file_path,
    input_csv_dir_path=eduData,
    course_id=course_id,
    start_minute=0,
    total_minutes=10,
)
```

This will concatenate the vectors by the week or lesson.

```py
vectors = e2Vec.concatenate_vectors(
    sentences_dir_path=sentences_dir_path,
    eventstream_file_path=eventstream_file_path,
    input_csv_dir_path=eduData,
    course_id=course_id,
    by_weeks=True,
    start_minute=0,
)
```

- `sentences_dir_path` is the path to the sentence files generated in the previous step
- `eventstream_file_path` is the path to the event stream csv file
- `input_csv_dir_path` is the path to a directory with the dataset (see below)
- `course_id` is a string to identify files for the course to analyze within the `info_dir` directory
- `by_weeks` concatenates vectors by week if `True` (by time by default)
- `start_minute` is the minute in the data the sentence generation should start (optional)
- `total_minutes` is the number of minutes worth of sentences that should be generated each time (optional)

## Usage of the ALP class

ALP (Active Learner Point) is a set of metrics that take BookRoll (ebook) and Moodle activity per lecture into account: attendance, report submissions, course views, slide views, adding markers or memos, and other actions.

```py
from openla_feature_representation import Alp
alp = Alp(course_id="114")
```

- `course_id` is a string to identify files for the course to analyze within the `Dataset` directory

The `Alp` class constructor above makes three DataFrames available as properties of the returned `Alp` object:

- `features_df`: aggregated totals of how many times each user took any of the relevant actions for each lecture
- `alp_df`: the features above replaced by a number from 0 to 5 following the criteria below
- `alp_df_normalized`: same as above, only the 0 to 5 numbers are normalized between 0 and 1

### Criteria for the ALP 0-to-5 scale

| value | description                                               |
| ----- | --------------------------------------------------------- |
| `5`:  | Top 10%, or attending the lecture, or submitting a report |
| `4`:  | Top 20%                                                   |
| `3`:  | Top 30%, or being late to the lecture, or submitting late |
| `2`:  | Top 40%                                                   |
| `1`:  | Top 50%                                                   |
| `0`:  | Bottom 50%, or not attending, or not submitting           |

### Examples for the class's methods and instance variables

```py
alp.features_df       # These are the aggregated features
alp.alp_df            # These are the ALP 0-to-5 values
alp.alp_df_normalized # These are the normalized values

# The following will write CSV files for the relevant DataFrame
# Paths and filenames can be specified, but there are default
# filenames and the paths default to the present directory
alp.write_features_csv()
alp.write_alp_csv()
alp.write_alp_normalized_csv()
```

## Datasets for OpenLA

This module uses data in the same or a similar format as OpenLA. Please refer to the [OpenLA documentation](https://limu.ait.kyushu-u.ac.jp/~openLA/) for further information.

Datasets for the `Alp` class must be placed in the `"Dataset/"` directory relative to the Python script they are called from.
