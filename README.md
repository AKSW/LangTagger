# LangTagger
LangTagger is a Language Detector that uses a probabilistic model for language classification.
The LangTagger consists of two models, which are LangTag(S) the simple model and LangTag(C) the 
combined model. LangTag(S) is  trained using only QALD 7 training dataset. Therefore it supports
the languages English, Deutsch, French, Spanish, Brazilian Portuguese, Dutch, Hindi, Romanian 
and Persian. The LangTag(C) model is trained using all the QALD 3 to QALD 9 training datasets.
Therefore this model supports two more languages than the LangTag(S) model. They are Portuguese 
and Russian. 

## Benchmarks
To assess the efficiency of the different models and frameworks, we desgined threedifferent text length and domain 
benchmarks (1) Short, (2) Moderate and (3)Long.

Short: The short text benchmark uses the first10.000 entityrdfs:labelsofeach language returned 
by the DBpedia SPARQL endpoint if possible, excluding resources containing digits. It is designed
to measure the efficiency of the different approaches on identifying a label language. We used English,
German, Russian, Italian, Spanish, French and Portuguese language for the test. 

Moderate: The  moderate  text  benchmark  uses  all  questions  in  the  QuestionOver Linked Data 
(QALD) datasets in different forms, Keywords (K) and FullQuestions (F). It is designed to evaluate 
the efficiency of the different approaches in the Question and Answering (QA) domain. The efficiency 
of the models areassessed on detecting the language of a question containing a knowledge base resource.
The QALD test benchmark consists of following languages, 

* QALD 1 : English.
* QALD 2 : English.
* QALD 3 : English, German, French, Spanish, Italian and Dutch.
* QALD 4 : English, German, French, Spanish,  Italian, Dutch and Romanian.
* QALD 5 : English, German, French, Spanish, Italian, Dutch and Romanian.
* QALD 6 : English, German, French, Spanish, Italian, Dutch, Romanian and Persian.
* QALD 7: English, German, French, Spanish, Brazilian Portuguese, Italian, Dutch, Hindi, Romanian and Persian.
* QALD 8 : English
* QALD 9 : English, Deutsch, French, Spanish, Brazilian Portuguese, Italian, Dutch, Hindi, Romanian, Persian, Portuguese and Russian.

Long: The  long  text  benchmark  uses  thedbo:abstractsof  the  top 10.000resources returned by the 
DBpedia SPARQL endpoint–if possible. It is designedto evalute the efficiency of different language 
identification approaches on longresource texts. We used English,German, Russian, Italian, Spanish,
and French language for the test. 

## Evaluation

#### Results  achieved  by  different  approaches  on  all  languages  of  QALD  testbenchmark in Full (F) and Keyword (K) questions
<table>
  <thead>
  <tr>
    <th>QALD</th>
    <th colspan="1">1</th>
    <th colspan="1">2</th>
    <th colspan="2">3</th>
    <th colspan="2">4</th>
    <th colspan="2">5</th>
    <th colspan="2">6</th>
    <th colspan="2">7</th>
    <th colspan="2">8</th>
    <th colspan="2">9</th>
  </tr>
  <tr >
    <td>Questions</td>
    <td ><b>F</b></td>
    <td ><b>F</b></td>
    <td ><b>K</b></td><td ><b>F</b></td>
    <td ><b>K</b></td><td ><b>F</b></td>
    <td ><b>K</b></td><td ><b>F</b></td>
    <td ><b>K</b></td><td ><b>F</b></td>
    <td ><b>K</b></td><td ><b>F</b></td>
    <td ><b>K</b></td><td ><b>F</b></td>
    <td ><b>K</b></td><td ><b>F</b></td>
   </tr>
  </thead>>
  <tbody>
  <tr>
	<td ><b>LangTag(S)</b></td>
	<td >1.0</td>
    <td >1.0</td>
    <td >0.70</td><td >0.99</td>
    <td >0.77</td><td >0.99</td>
    <td >0.77</td><td >1.00</td>
    <td >0.76</td><td >0.99</td>
    <td >0.67</td><td >0.98</td>
    <td >0.48</td><td >1.00</td>
    <td >0.70</td><td >0.97</td>
  </tr>
  <tr>
	<td ><b>LangTag(C)</b></td>
	<td >1.0</td>
    <td >1.0</td>
    <td >0.86</td><td >0.99</td>
    <td >0.90</td><td >0.99</td>
    <td >0.92</td><td >1.00</td>
    <td >0.81</td><td >0.99</td>
    <td >0.93</td><td >1.00</td>
    <td >0.70</td><td >1.00</td>
    <td >0.84</td><td >0.97</td>
  </tr>
  <tr>
	<td ><b>langdetect</b></td>
	<td >0.96</td>
    <td >0.96</td>
    <td >0.65</td><td >0.93</td>
    <td >0.76</td><td >0.92</td>
    <td >0.72</td><td >0.92</td>
    <td >0.68</td><td >0.91</td>
    <td >0.76</td><td >0.95</td>
    <td >0.51</td><td >1.00</td>
    <td >0.65</td><td >0.82</td>
  </tr>
  <tr>
	<td ><b>Tika</b></td>
	<td >0.96</td>
    <td >0.93</td>
    <td >0.61</td><td >0.88</td>
    <td >0.70</td><td >0.90</td>
    <td >0.66</td><td >0.91</td>
    <td >0.63</td><td >0.89</td>
    <td >0.72</td><td >0.91</td>
    <td >0.56</td><td >0.97</td>
    <td >0.61</td><td >0.80</td>
  </tr>
  <tr>
	<td ><b>openNLP</b></td>
	<td >0.96</td>
    <td >0.97</td>
    <td >0.48</td><td >0.89</td>
    <td >0.62</td><td >0.89</td>
    <td >0.61</td><td >0.85</td>
    <td >0.48</td><td >0.75</td>
    <td >0.62</td><td >0.90</td>
    <td >0.39</td><td >0.95</td>
    <td >0.41</td><td >0.73</td>
  </tr>
  </tbody>
</table>

#### Results achieved by different approaches on English questions of QALD testbenchmark.

<table>
  <thead>
  <tr>
    <th>QALD</th>
    <th colspan="1">1</th>
    <th colspan="1">2</th>
    <th colspan="2">3</th>
    <th colspan="2">4</th>
    <th colspan="2">5</th>
    <th colspan="2">6</th>
    <th colspan="2">7</th>
    <th colspan="2">8</th>
    <th colspan="2">9</th>
  </tr>
  <tr >
    <td>Questions</td>
    <td ><b>F</b></td>
    <td ><b>F</b></td>
    <td ><b>K</b></td><td ><b>F</b></td>
    <td ><b>K</b></td><td ><b>F</b></td>
    <td ><b>K</b></td><td ><b>F</b></td>
    <td ><b>K</b></td><td ><b>F</b></td>
    <td ><b>K</b></td><td ><b>F</b></td>
    <td ><b>K</b></td><td ><b>F</b></td>
    <td ><b>K</b></td><td ><b>F</b></td>
   </tr>
  </thead>>
  <tbody>
  <tr>
	<td ><b>LangTag(S)</b></td>
	<td >1.00</td>
    <td >1.00</td>
    <td >0.69</td><td >1.00</td>
    <td >0.80</td><td >1.00</td>
    <td >0.77</td><td >1.00</td>
    <td >0.80</td><td >1.00</td>
    <td >0.60</td><td >1.00</td>
    <td >0.48</td><td >1.00</td>
    <td >0.72</td><td >1.00</td>
  </tr>
  <tr>
	<td ><b>LangTag(C)</b></td>
	<td >1.0</td>
    <td >1.0</td>
    <td >0.87</td><td >1.00</td>
    <td >0.98</td><td >1.00</td>
    <td >0.93</td><td >1.00</td>
    <td >0.83</td><td >1.00</td>
    <td >0.93</td><td >1.00</td>
    <td >0.70</td><td >1.00</td>
    <td >0.87</td><td >1.00</td>
  </tr>
  <tr>
	<td ><b>langdetect</b></td>
	<td >0.96</td>
    <td >0.96</td>
    <td >0.53</td><td >0.96</td>
    <td >0.68</td><td >0.94</td>
    <td >0.67</td><td >0.94</td>
    <td >0.70</td><td >0.95</td>
    <td >0.65</td><td >0.93</td>
    <td >0.51</td><td >1.00</td>
    <td >0.68</td><td >0.92</td>
  </tr>
  <tr>
	<td ><b>Tika</b></td>
	<td >0.96</td>
    <td >0.93</td>
    <td >0.51</td><td >0.97</td>
    <td >0.68</td><td >0.92</td>
    <td >0.61</td><td >0.91</td>
    <td >0.65</td><td >0.94</td>
    <td >0.67</td><td >0.96</td>
    <td >0.56</td><td >0.95</td>
    <td >0.64</td><td >0.93</td>
  </tr>
  <tr>
	<td ><b>openNLP</b></td>
	<td >0.96</td>
    <td >0.97</td>
    <td >0.52</td><td >0.97</td>
    <td >0.70</td><td >0.92</td>
    <td >0.67</td><td >0.91</td>
    <td >0.63</td><td >0.94</td>
    <td >0.62</td><td >0.96</td>
    <td >0.39</td><td >0.95</td>
    <td >0.58</td><td >0.93</td>
  </tr>
  </tbody>
</table>


