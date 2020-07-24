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

#### Results achieved by different approaches on German questions of QALD testbenchmark

<table>
  <thead>
  <tr>
    <th>QALD</th>
    <th colspan="2">3</th>
    <th colspan="2">4</th>
    <th colspan="2">5</th>
    <th colspan="2">6</th>
    <th colspan="2">7</th>
    <th colspan="2">9</th>
  </tr>
  <tr >
    <td>Questions</td>
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
    <td >0.87</td><td >1.00</td>
    <td >0.88</td><td >1.00</td>
    <td >0.93</td><td >1.00</td>
    <td >0.86</td><td >0.99</td>
    <td >0.90</td><td >1.00</td>
    <td >0.88</td><td >1.00</td>
  </tr>
  <tr>
	<td ><b>LangTag(C)</b></td>
    <td >0.80</td><td >1.00</td>
    <td >0.88</td><td >1.00</td>
    <td >0.93</td><td >1.00</td>
    <td >0.86</td><td >0.99</td>
    <td >0.90</td><td >1.00</td>
    <td >0.88</td><td >1.00</td>
  </tr>
  <tr>
	<td ><b>langdetect</b></td>
    <td >0.80</td><td >0.95</td>
    <td >0.80</td><td >0.92</td>
    <td >0.77</td><td >0.91</td>
    <td >0.71</td><td >0.88</td>
    <td >0.74</td><td >0.95</td>
    <td >0.81</td><td >0.94</td>
  </tr>
  <tr>
	<td ><b>Tika</b></td>
    <td >0.79</td><td >0.95</td>
    <td >0.78</td><td >0.92</td>
    <td >0.79</td><td >0.94</td>
    <td >0.71</td><td >0.88</td>
    <td >0.69</td><td >0.95</td>
    <td >0.81</td><td >0.94</td>
  </tr>
  <tr>
	<td ><b>openNLP</b></td>
    <td >0.42</td><td >0.88</td>
    <td >0.54</td><td >0.80</td>
    <td >0.59</td><td >0.81</td>
    <td >0.39</td><td >0.74</td>
    <td >0.48</td><td >0.79</td>
    <td >0.48</td><td >0.82</td>
  </tr>
  </tbody>
</table>

#### Results achieved by different approaches on French questions of QALD testbenchmark

<table>
  <thead>
  <tr>
    <th>QALD</th>
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
    <td >0.72</td><td >0.98</td>
    <td >0.72</td><td >1.00</td>
    <td >0.79</td><td >1.00</td>
    <td >0.74</td><td >0.99</td>
    <td >0.62</td><td >0.97</td>
    <td >0.66</td><td >0.99</td>
  </tr>
  <tr>
	<td ><b>LangTag(C)</b></td>
    <td >0.88</td><td >1.00</td>
    <td >0.84</td><td >1.00</td>
    <td >0.93</td><td >1.00</td>
    <td >0.78</td><td >0.99</td>
    <td >0.90</td><td >1.00</td>
    <td >0.80</td><td >0.99</td>
  </tr>
  <tr>
	<td ><b>langdetect</b></td>
    <td >0.61</td><td >0.90</td>
    <td >0.84</td><td >0.98</td>
    <td >0.86</td><td >0.96</td>
    <td >0.69</td><td >0.92</td>
    <td >0.88</td><td >1.00</td>
    <td >0.77</td><td >0.94</td>
  </tr>
  <tr>
	<td ><b>Tika</b></td>
    <td >0.61</td><td >0.89</td>
    <td >0.76</td><td >0.98</td>
    <td >0.79</td><td >0.93</td>
    <td >0.65</td><td >0.93</td>
    <td >0.79</td><td >1.00</td>
    <td >0.73</td><td >0.96</td>
  </tr>
  <tr>
	<td ><b>openNLP</b></td>
    <td >0.51</td><td >0.86</td>
    <td >0.62</td><td >0.90</td>
    <td >0.58</td><td >0.80</td>
    <td >0.59</td><td >0.82</td>
    <td >0.65</td><td >0.90</td>
    <td >0.62</td><td >0.82</td>
  </tr>
  </tbody>
</table>

#### Results achieved by different approaches on Entity rdfs:labels

<table>
  <thead>
  <tr>
    <th>Approach</th>
    <th colspan="1">EN</th>
    <th colspan="1">DE</th>
    <th colspan="1">RU</th>
    <th colspan="1">IT</th>
    <th colspan="1">ES</th>
    <th colspan="1">FR</th>
    <th colspan="1">PT</th>
    <th colspan="2">AVG</th>
  </tr>
  <tr >
    <td>#Resources</td>
    <td >10,000</td>
    <td >10,000</td>
    <td >83</td>
    <td >243</td>
    <td >10,000</td>
    <td >782</td>
    <td >227</td>
    <td >Accuracy</td><td >Runtime(s)</td>
   </tr>
  </thead>>
  <tbody>
  <tr>
	<td ><b>LangTag(S)</b></td>
    <td >0.21</td>
    <td >0.91</td>
    <td >-</td>
    <td >0.25</td>
    <td >0.09</td>
    <td >0.34</td>
    <td >0.36</td>
    <td >0.36</td><td >0.00162</td>
  </tr>
  <tr>
	<td ><b>LangTag(C)</b></td>
    <td >0.26</td>
    <td >0.88</td>
    <td >0.12</td>
    <td >0.35</td>
    <td >0.15</td>
    <td >0.36</td>
    <td >0.44</td>
    <td >0.34</td><td >0.00186</td>
  </tr>
  <tr>
	<td ><b>langdetect</b></td>
    <td >0.40</td>
    <td >0.43</td>
    <td >0.57</td>
    <td >0.63</td>
    <td >0.31</td>
    <td >0.59</td>
    <td >0.43</td>
    <td >0.48</td><td >0.01761</td>
  </tr>
  <tr>
	<td ><b>Tika</b></td>
    <td >0.24</td>
    <td >0.39</td>
    <td >50</td>
    <td >0.68</td>
    <td >0.15</td>
    <td >0.59</td>
    <td >0.35</td>
    <td >0.41</td><td >0.41428</td>
  </tr>
  <tr>
    <td ><b>openNLP</b></td>
    <td >0.16</td>
    <td >0.18</td>
    <td >0.12</td>
    <td >0.30</td>
    <td >0.15</td>
    <td >0.33</td>
    <td >0.25</td>
    <td >0.21</td><td >0.01125</td>
  </tr>
  </tbody>
</table>


#### Results achieved by different approaches on Abstracts

<table>
  <thead>
  <tr>
    <th>Approach</th>
    <th colspan="1">EN</th>
    <th colspan="1">DE</th>
    <th colspan="1">RU</th>
    <th colspan="1">IT</th>
    <th colspan="1">ES</th>
    <th colspan="1">FR</th>
    <th colspan="2">AVG</th>
  </tr>
  <tr >
    <td>#Resources</td>
    <td >10,000</td>
    <td >10,000</td>
    <td >285</td>
    <td >10,000</td>
    <td >10,000</td>
    <td >10,000</td>
    <td >Accuracy</td><td >Runtime(s)</td>
   </tr>
  </thead>>
  <tbody>
  <tr>
	<td ><b>LangTag(S)</b></td>
    <td >0.96</td>
    <td >0.99</td>
    <td >-</td>
    <td >0.99</td>
    <td >0.99</td>
    <td >0.99</td>
    <td >0.98</td><td >0.00267</td>
  </tr>
  <tr>
	<td ><b>LangTag(C)</b></td>
    <td >0.96</td>
    <td >0.99</td>
    <td >0.86</td>
    <td >0.99</td>
    <td >0.99</td>
    <td >0.99</td>
    <td >0.96</td><td >0.00287</td>
  </tr>
  <tr>
	<td ><b>langdetect</b></td>
    <td >0.95</td>
    <td >0.99</td>
    <td >0.95</td>
    <td >0.99</td>
    <td >0.99</td>
    <td >0.99</td>
    <td >0.97</td><td >0.01657</td>
  </tr>
  <tr>
	<td ><b>Tika</b></td>
    <td >0.95</td>
    <td >0.99</td>
    <td >0.95</td>
    <td >0.99</td>
    <td >0.98</td>
    <td >0.98</td>
    <td >0.99</td>
    <td >0.97</td><td >0.43918</td>
  </tr>
  <tr>
    <td ><b>openNLP</b></td>
    <td >0.79</td>
    <td >0.81</td>
    <td >0.13</td>
    <td >0.76</td>
    <td >0.78</td>
    <td >0.71</td>
    <td >0.66</td><td >0.01427</td>
  </tr>
  </tbody>
</table>

#### Average runtime in seconds(s) different approaches on on QALD test bench-marks.


<table>
  <thead>
  <tr>
    <th>QALD</th>
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
    <td >0.0003</td><td >0.0003</td>
    <td >0.0006</td><td >0.0003</td>
    <td >0.0006</td><td >0.0003</td>
    <td >0.0002</td><td >0.0002</td>
    <td >0.0019</td><td >0.0004</td>
    <td >0.0041</td><td >0.0014</td>
    <td >0.0001</td><td >0.0002</td>
  </tr>
  <tr>
	<td ><b>LangTag(C)</b></td>
    <td >0.0018</td><td >0.0012</td>
    <td >0.0026</td><td >0.0021</td>
    <td >0.0029</td><td >0.0022</td>
    <td >0.0017</td><td >0.0011</td>
    <td >0.0036</td><td >0.0031</td>
    <td >0.0131</td><td >0.0120</td>
    <td >0.0017</td><td >0.0012</td>
  </tr>
  <tr>
	<td ><b>langdetect</b></td>
    <td >0.0087</td><td >0.0063</td>
    <td >0.0079</td><td >0.0042</td>
    <td >0.0072</td><td >0.0057</td>
    <td >0.0078</td><td >0.0054</td>
    <td >0.0082</td><td >0.0041</td>
    <td >0.0092</td><td >0.0021</td>
    <td >0.0075</td><td >0.0116</td>
  </tr>
  <tr>
	<td ><b>Tika</b></td>
    <td >1.5677</td><td >1.4068</td>
    <td >1.4021</td><td >1.4009</td>
    <td >1.6072</td><td >1.3928</td>
    <td >1.5981</td><td >1.3978</td>
    <td >1.4379</td><td >1.3955</td>
    <td >1.4213</td><td >1.3778</td>
    <td >1.9081</td><td >1.4836</td>
  </tr>
  <tr>
	<td ><b>openNLP</b></td>
    <td >0.0027</td><td >0.0011</td>
    <td >0.0036</td><td >0.0039</td>
    <td >0.0035</td><td >0.0030</td>
    <td >0.0023</td><td >0.0011</td>
    <td >0.0058</td><td >0.0062</td>
    <td >0.0032</td><td >0.0026</td>
    <td >0.0012</td><td >0.0014</td>
  </tr>
  </tbody>
</table>


#### model  size  in  Megabytes  (MB)  andKilobytes (KB) achieved by different approaches on QALD test benchmarks.

<table>
  <thead>
  <tr>
    <th>Approach</th>
    <th colspan="1">Model Size</th>
    <th colspan="1">#Languages</th>
  </tr>
  </thead>>
  <tbody>
  <tr>
	<td ><b>LangTag(S)</b></td>
    <td >8.2 KB</td>
    <td >10</td>
  </tr>
  <tr>
	<td ><b>LangTag(C)</b></td>
    <td >9.7 KB</td>
    <td >12</td>
  </tr>
  <tr>
	<td ><b>langdetect</b></td>
    <td >981.5 KB</td>
    <td >55</td>
  </tr>
  <tr>
	<td ><b>Tika</b></td>
    <td >74.9 MB</td>
    <td >18</td>
  </tr>
  <tr>
    <td ><b>openNLP</b></td>
    <td >10.6 MB</td>
    <td >103</td>
  </tr>
  </tbody>
</table>
