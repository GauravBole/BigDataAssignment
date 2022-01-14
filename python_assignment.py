"""
List_remove_append
Description: Remove SPSS from input_list=['SAS', 'R', 'PYTHON', 'SPSS'] and add 'SPARK'
in its place.
"""
input_list=['SAS', 'R', 'PYTHON', 'SPSS']
if "SPSS" in input_list:
    input_list.remove("SPSS")
    input_list.append("SPARK")
print(input_list)

"""
String to List Conversion
Description: Convert a string input_str = 'I love Data Science & Python' to a list by
splitting it on '&'.
"""
input_str = 'I love Data Science & Python'
output_list = input_str.split("&")
print(output_list)


"""
List to String Conversion
Description: Convert a list ['Pythons syntax is easy to learn', 'Pythons syntax is very
clear'] to a string using "&".
"""
input_list =  ['Pythons syntax is easy to learn', 'Pythons syntax is very clear']
output_str = " & ".join(input_list)
print(output_str)

"""
Nested List
Description: Extract Python from a nested list
"""
input_list = [['SAS','R'],['Tableau','SQL'],['Python','Java']]
print(input_list[2][0])

"""
It's the time to disco
Description: t = ("disco", 12, 4.5)
What is the output of: t[0][2]
"""
t = ("disco", 12, 4.5)
t[0][2] # will return "s"

"""
String Palindrome
Description: Write a program to check whether a string is a palindrome or not. Print 1 if
the string is a palindrome and 0 otherwise.
"""

input_str = input("enter string to check Palindrome or not: ")
if (input_str == input_str[::-1]):
    print(1)
else:
    print(0)

"""
Reverse Words
Description: You will be given a sentence in the form of a string. You have to reverse the
order of the words in the sentence. Remember not to reverse the individual words, but
the order of words. Check the sample input-output for further clarification.
Input: A string, which will consist of a few spaces.
Output: The words in reverse order
# """
# input_str = "A string, which will consist of a few spaces."
input_str = input("input sentance to reverse : ")
all_words = input_str.split()
output_str = " ".join(reversed(all_words))
print(output_str)

"""
String Formatting
Description: Write a program that satisfies below examples
Input 1: caloRie ConsuMed
Output 1: calorie_consumed
Input 2: data science
Output 2: data_science
Input 3: datascience
Output 3: datascience
"""

# input1 = "caloRie ConsuMed" 
input_str = input("enter input str for formating:")
output_str = input_str.replace(" ", "_").lower()
print(output_str)


"""
Multiple Choice Questions
1. How will you extract "love" from the string S = "I love Python"? (More than one
option may be correct.).
a. S[2:5]
b. S[2:6]
c. S[3:7]
d. S[-11:-7]
e. S[-11:-8]

Ans: b, d

2. What will the output of 3 * 3 ** 3 be?
a. 9
b. 27
c. 81
d. 729

Ans: c

3. What will the output be of ((500//7) % 5) ** 3?
a. 1
b. 2.91
c. 71.42
d. 0
e. 8

Ans: a

4. If you have a tuple T = (3, 5, 7, 11), what will the output of T.append(9) be?
a. (3, 5, 7, 9, 11)
b. (9, 3, 5, 7, 11)
c. (3, 5, 7, 11, 9)
d. Error

Ans: d

5. What will the output of the following program be?
a. Vikas
b. Mahima
c. y
d. A

Ans: Invalid Question

6. What will the output of the following code be?
l = [32, 34, 12, 27, 33]
l.append([14, 19])
print(len(l))
a. 5
b. 6
c. 7
d. The code will throw an error

Ans: b

7. Which of the following statements is incorrect regarding sets in Python?
a. Sets do not contain duplicate elements
b. Sets are represented using curly braces {}
c. Sets are immutable
d. All of the above

Ans: c

8.What will the output be of the following code?
D = {1: ["Raj", 22], 2:["simran", 21], 3:["Rahul", 40]}
for val in D:
    print(val)
a. 1
2
3
b. ["Raj", 22]
["Simran", 21]
["Rahul", 40]
c. 1 ["Raj", 22]
2 ["Simran", 21]
3 ["Rahul", 40]
d. "Raj"
"Simran"
"Rahul"

Ans: a

9. What will the "comprehension equivalent" be for the following snippet of code?
for sentence in paragraph:
    for word in sentence.split():
        single_word_list.append(word)


a. word for sentence in paragraph for word in sentence.split()
b. [word for sentence in paragraph for word in sentence.split()]
c. word for word in sentence.split() for sentence in paragraph
d. [word for word in sentence.split() for sentence in paragraph]

Ans: b

10.What will be the output of this code?
print(list(range(10, 1, -1)))

a. [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
b. [9, 8, 7, 6, 5, 4, 3, 2]
c. [9, 8, 7, 6, 5, 4, 3, 2, 1]
d. [10, 9, 8, 7, 6, 5, 4, 3, 2]

Ans: d

"""
