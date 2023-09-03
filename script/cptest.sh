#!/bin/bash

source ".venv/bin/activate"

relative_file=$1
contest_id=$(basename ${relative_file%/*})
task_id=$(basename ${relative_file} .py)

test_dir=test/${contest_id}/${task_id}
problem_name="$contest_id"_"$task_id"

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d ${test_dir} https://atcoder.jp/contests/${contest_id}/tasks/${problem_name//-/_}
fi

oj test -c "python3 src/${contest_id}/${task_id}.py" -d ${test_dir}
