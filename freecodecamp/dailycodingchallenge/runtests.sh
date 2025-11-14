files=`ls -l | grep -oh "2025.*\.py" | tr '\n' ' \n' | tr -d '\n'`
echo $files
pytest $files