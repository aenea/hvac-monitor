owfs -C -uall -m /mnt/1wire --allow_other
echo 1 > /mnt/1wire/EF.54A720150000/hub/branch.0
echo 1 > /mnt/1wire/EF.54A720150000/hub/branch.1

python /scripts/hvac-monitor.py