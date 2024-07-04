## Installation

Run 
```pip install llm-similarity-checker```

This module includes three classes:

1. **AnalysisMatcher**
2. **NumericMatcher**
3. **AltairGraphComparer**

### AnalysisMatcher

This class performs sentence comparison using state-of-the-art transformer models in natural language processing (NLP). Leveraging the Hugging Face transformers library, it tokenizes input sentences, extracts embeddings using a pre-trained model, and calculates similarity scores between sentences.

Example:
```python
from similarity_checker import AnalysisMatcher

reference = "Based on the visualization 'Sale Price vs. Unit Profit' and 'Bulk Price vs. Bulk Profit', it appears that there's a positive correlation between price and profit for both individual unit sales and bulk sales."

sentence1 = "Both pricing strategies do not have positive linear relationship with their respective revenues."
sentence2 = "Both pricing strategies have positive linear relationship with their respective revenues."

# Initialize the AnalysisMatcher
matcher = AnalysisMatcher()

# Perform matches for answer_query1
match1 = matcher.match(reference, sentence1)
match2 = matcher.match(reference, sentence2)

# Print results
print("Match results for sentence1:")
print(match1)

print("\nMatch results for sentence2:")
print(match2)
```

Output:
```bash
Match results for sentence1:
(0.24839641153812408, False)

Match results for sentence2:
(0.6842396259307861, True)
```


### NumericMatcher

This class focuses on extracting numerical values from strings and comparing them against target values. It uses regular expressions to locate and normalize numeric values from input strings, handling variations like comma separators.

Example:
```python
sentence = "The top 5 most preferred car brands in the UAE, based on the average proportion across cities, are:\n\n| brand         | avg_proportion   |\n|:--------------|:-----------------|\n| Nissan        | 0.159158         |\n| Toyota        | 0.0978399        |\n| Mercedes-Benz | 0.0843513        |\n| Honda         | 0.0776763        |\n| BMW           | 0.056902         |"

target1 = 0.159
target2 = 0

matcher = NumericMatcher()

print(matcher.match(sentence, target1))
print(matcher.match(sentence, target2))
```

### AltairGraphComparer

This class compares two Altair graphs to determine their similarity.

Example:
```python
chart1 = "{\"config\": {\"view\": {\"continuousWidth\": 400, \"continuousHeight\": 300}}, \"data\": {\"name\": \"data-679d61f96919a9b00678a3858e27aa15\"}, \"mark\": \"bar\", \"encoding\": {\"tooltip\": [{\"field\": \"month\", \"type\": \"nominal\"}, {\"field\": \"booking_duration\", \"type\": \"quantitative\"}], \"x\": {\"axis\": {\"labelAngle\": -45, \"title\": \"Month\"}, \"field\": \"month\", \"sort\": null, \"type\": \"nominal\"}, \"y\": {\"field\": \"booking_duration\", \"title\": \"Average Booking Duration (Days)\", \"type\": \"quantitative\"}}, \"selection\": {\"selector001\": {\"type\": \"interval\", \"bind\": \"scales\", \"encodings\": [\"x\", \"y\"]}}, \"title\": \"Average Booking Duration by Month\", \"$schema\": \"https://vega.github.io/schema/vega-lite/v4.17.0.json\", \"datasets\": {\"data-679d61f96919a9b00678a3858e27aa15\": [{\"month\": \"January\", \"booking_duration\": -778.581308411215, \"month_order\": 0}]}}"

chart2 = "{\"config\": {\"view\": {\"continuousWidth\": 400, \"continuousHeight\": 300}}, \"data\": {\"name\": \"data-71fd4bd6411150f723ef9e15bf55c9ea\"}, \"mark\": \"bar\", \"encoding\": {\"tooltip\": [{\"field\": \"month\", \"type\": \"nominal\"}, {\"field\": \"booking_duration\", \"type\": \"quantitative\"}], \"x\": {\"axis\": {\"labelAngle\": -45, \"title\": \"Month\"}, \"field\": \"month\", \"sort\": null, \"type\": \"nominal\"}, \"y\": {\"field\": \"booking_duration\", \"title\": \"Average Booking Duration (Days)\", \"type\": \"quantitative\"}}, \"selection\": {\"selector001\": {\"type\": \"interval\", \"bind\": \"scales\", \"encodings\": [\"x\", \"y\"]}}, \"title\": \"Average Booking Duration by Month\", \"$schema\": \"https://vega.github.io/schema/vega-lite/v4.17.0.json\", \"datasets\": {\"data-71fd4bd6411150f723ef9e15bf55c9ea\": [{\"month\": \"January\", \"booking_duration\": 1.8288770053475936, \"month_order\": 0}]}}"

matcher = AltairGraphComparer()
matcher.match(chart1, chart2)
```