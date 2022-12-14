#!/bin/bash

ownership() {
    # Fixes files ownership
    # source: https://github.com/BD2KGenomics/cgl-docker-lib/blob/master/mutect/runtime/wrapper.sh#L5
    user_id=$(stat -c '%u:%g' /app)
    chown -R ${user_id} /app
}

echo ''
echo '--------------------------'
echo 'Install missing packages'
echo '--------------------------'
echo ''
pip install -r ./requirements.txt

echo ''
echo '--------------------------'
echo 'Database migration'
echo '--------------------------'
echo ''

bash wait_for_db.sh

python manage.py makemigrations || exit 1
python manage.py migrate || exit 1

echo ''
echo '--------------------------'
echo 'Ownership fixes'
echo '--------------------------'
echo ''
ownership

echo ''
echo '-------------------------'
echo 'Run command'
echo $@
echo '-------------------------'
echo ''
python manage.py $@ || exit 1
