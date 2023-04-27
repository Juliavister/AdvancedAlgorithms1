# AdvancedAlgorithms1
Group project 1 from the course Advanced Algorithms

* Part One 
	
	A) "Mom bought me a new computer"

	Implement the following pattern matching algorithms: Brute-force, Sunday, KMP, FSM, Rabin-Karp, Gusfield Z.
	Compare their running times using chapters of a book, with a small (few words or a sentence) and a large pattern (a paragraph).
	Your report should contain some description of the algorithms and, most importantly, your findings.
	Include a graph showing the relation of RT against the text length.
	(This implies that you have to use several different lengths, which are placed on the x-axis of a graph.)
	The results should be reproducible.

	B) "Wacky Races"

	Prove empirically that there can be situations in which
		- Binary Sunday (the first algorithms covered in class) is at least twice as fast as Gusfield Z.
		- KMP is at least twice as fast as Rabin-Karp.
		- Rabin-Karp is at least twice as fast as Sunday
	It means that you should present a specific P and a specific T for which this happens.
	T should be at least 100kB long. The results should be reproducible.

** Part Two 

	"What was that char again?"

	Implement the Brute-force and Sunday algorithms so that they accept wildcards ? and *.
	Your implementation should produce a Boolean value of a match found or not.
	The wildcards and \ itself can be escaped with a backslash.
	Explain your extensions to the algorithms in your report.


*** Part three 

	"Jewish-style carp"

	Devise a version of Rabin-Karp algorithm which will check if for a given
	picture* M by N large its top-right K by K corner is duplicated somewhere in the picture.
	Your algorithm should replace slow modulo prime operations with faster bitwise mask &'s.
	!!!! Do make sure that the RT is at most linear in the number of pixels in the text !!!

	* Here, picture is a two-dimensional array of arbitrary items.
