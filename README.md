# Word-Sense-Disambiguation
Computational Linguistics-2 project

We understand that words have different meanings
based on the context of its usage in the sentence. If
we talk about human languages, then they are
ambiguous too because many words can be
interpreted in multiple ways depending upon the
context of their occurrence.<br/>
Therefore, WSD becomes a very crucial component
in MT systems. If the sense of a word is not
correctly identified, the translation can become
jarring. It was basically a task for us to identify the
correct meaning of a word in the given context. As a
basic semantic understanding at the lexical level,
WSD is a fundamental problem in NLP.<br/>
Determining which “sense” of a word is activated by
the use of the word in a particular context, which
can be a phrase, a sentence or a paragraph. So,
WSD is basically a task of finding the correct sense
of the words and automatically assigning its correct
sense to the words which may be polysemous in
some cases. We can easily find out the correct
meaning of a word in context, but for machines it’s a
difficult task.

```
import pyiwn
```

- for Lesk_hindi.py
```
python3 Lesk_hindi.py word "sentence"
```
for example बाल in "कीटनाशक का छिड़काव न करने से अनाज की बालों में कीड़े लग गए हैं"
```
python3 Lesk_hindi.py बाल "कीटनाशक का छिड़काव न करने से अनाज की बालों में कीड़े लग गए हैं"
```
consider result as output


- for english lesk_english.py
```
python3 Lesk_english.py word "sentence"
```
for example
cricket in "he plays cricket"
```
python3 Lesk_hindi.py cricket "he plays cricket"
```
consider result as output

- for english lesk_algorithm.py
input your sentence in line no. 16 of code and run python file.
```
python3 lesk_english.py
```
