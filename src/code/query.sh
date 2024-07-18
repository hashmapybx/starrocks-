#!/bin/bash

# 要先获取iceberg catalog
sql_path="src/99sql"
out_path="src/output/result.log"

for file in $(ls -l "$sql_path" | awk '$9 ~ /sql/ {print $9}'| sort)
do
    #echo "文件路径 $sql_path/$file"
    echo -e "\n $file \n" > $out_path
    path="$sql_path/$file"
    sql_contents=$(<"$path")
    echo "$file"
    time mysql -h 'x.x.x.x' -u root -P 9030 -p'xxxxx' -e "set catalog iceberg_catalog; use tpcds_iceberg_parquet_100;${sql_contents}" >> $out_path
done


