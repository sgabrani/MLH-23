cat apache_access | awk '{ print $9 }' | sort | uniq -c
