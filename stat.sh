if [ -f stat.txt ]; then
    rm stat.txt;
fi

echo "=== 0 ===" >> stat.txt
git log --after="$1-1-1" --before="$1-1-31" --no-merges --stat | grep insertion >> stat.txt
echo "=== 1 ===" >> stat.txt
git log --after="$1-2-1" --before="$1-2-28" --no-merges --stat | grep insertion >> stat.txt
echo "=== 2 ===" >> stat.txt
git log --after="$1-3-1" --before="$1-3-31" --no-merges --stat | grep insertion >> stat.txt
echo "=== 3 ===" >> stat.txt
git log --after="$1-4-1" --before="$1-4-30" --no-merges --stat | grep insertion >> stat.txt
echo "=== 4 ===" >> stat.txt
git log --after="$1-5-1" --before="$1-5-31" --no-merges --stat | grep insertion >> stat.txt
echo "=== 5 ===" >> stat.txt
git log --after="$1-6-1" --before="$1-6-30" --no-merges --stat | grep insertion >> stat.txt
echo "=== 6 ===" >> stat.txt
git log --after="$1-7-1" --before="$1-7-31" --no-merges --stat | grep insertion >> stat.txt
echo "=== 7 ===" >> stat.txt
git log --after="$1-8-1" --before="$1-8-31" --no-merges --stat | grep insertion >> stat.txt
echo "=== 8 ===" >> stat.txt
git log --after="$1-9-1" --before="$1-9-30" --no-merges --stat | grep insertion >> stat.txt
echo "=== 9 ===" >> stat.txt
git log --after="$1-10-1" --before="$1-10-31" --no-merges --stat | grep insertion >> stat.txt
echo "=== 10 ===" >> stat.txt
git log --after="$1-11-1" --before="$1-11-30" --no-merges --stat | grep insertion >> stat.txt
echo "=== 11 ===" >> stat.txt
git log --after="$1-12-1" --before="$1-12-31" --no-merges --stat | grep insertion >> stat.txt
echo "=== 12 ===" >> stat.txt
