git config --global user.name "Star"
git config --global user.email "i@ssstttar.com"
# git config --global user.signingkey 7288DB9F
git add README.md
# git commit -S -m 'Update at $(date +%Y-%m-%d)'
git commit -m 'Update at '$(date +%Y-%m-%d)
git push