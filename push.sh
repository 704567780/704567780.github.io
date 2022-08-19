python ./collect.py

sleep 1s
git add .

sleep 1s
git status

sleep 1s
echo "####### commit1 #######"
git commit -m "push"
echo "####### commit2 #######"

echo "####### push1 #######"
sleep 1s
git push origin master
echo "####### push2 #######"
