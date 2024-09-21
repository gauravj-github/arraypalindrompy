<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Longest Palindrome Finder</title>
</head>
<body>

<h1>Longest Palindrome Finder</h1>

<p>This Python script identifies the longest palindrome from a list of integers. A palindrome is a number that reads the same forwards and backwards. The script iterates through each number in the list, reverses it, and checks if the reversed number is present in the list. If a palindrome is found, it adds it to a new list and then determines the largest palindrome.</p>

<h2>How It Works</h2>

<p>The script works in two steps:</p>

<ol>
    <li>For each number in the list, it calculates the reverse of the number and checks if that reversed number is also present in the list.</li>
    <li>If a palindrome is found, it is added to a new list. The script then finds the largest palindrome in that list.</li>
</ol>

<h3>Code</h3>

<pre>
<code>
arr = [1, 232, 5545455, 909090, 161]
l = []

for i in arr:
    sum = 0
    s = i
    while s > 0:
        temp = s % 10
        sum = (sum * 10) + temp
        s = s // 10
    if sum in arr:
        l.append(sum)

print(l)

# Find the longest palindrome
m = l[0]
for j in range(1, len(l)):
    if m < l[j]:
        m = l[j]

print(m)
</code>
</pre>

<h3>Example</h3>

<p>For the input list:</p>

<pre>
<code>
arr = [1, 232, 5545455, 909090, 161]
</code>
</pre>

<p>The palindromes found will be:</p>

<pre>
<code>
[1, 232, 161]
</code>
</pre>

<p>The largest palindrome will be:</p>

<pre>
<code>
232
</code>
</pre>

<h3>Features</h3>

<ul>
    <li><strong>Simple and efficient</strong>: The script checks for palindromes by reversing each number and comparing it with the original list.</li>
    <li><strong>Finds the largest palindrome</strong>: After collecting all palindromes, the script outputs the largest one.</li>
</ul>

<h3>Usage</h3>

<ol>
    <li>Copy the provided code into a Python file (e.g., <code>palindrome_finder.py</code>).</li>
    <li>Modify the <code>arr</code> variable with your list of numbers.</li>
    <li>Run the script:</li>
</ol>

<pre>
<code>
python palindrome_finder.py
</code>
</pre>

<p>The script will print the list of palindromes found and the largest palindrome in the list.</p>
<h1>created by gaurav</h1>

</body>
</html>
