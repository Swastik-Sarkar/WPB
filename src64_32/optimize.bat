@Echo OFF
echo "===================="
echo "|        WBP       |"
echo "===================="
timeout /T 3 /NOBREAK
echo "Running Task1..."
sfc /scannow <null
echo "Task1 Finished."
start poweredt
